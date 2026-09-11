#!/usr/bin/env python3
# Tangkap skrin POC chat guna Chrome headless + CDP (venv hermes: ada websocket-client).
# Guna: ~/.hermes/hermes-agent/venv/bin/python tangkap_skrin.py <url> <out.png> [w] [h] ["soalan"]
import base64, json, os, subprocess, sys, tempfile, time, urllib.request, shutil
import websocket

URL = sys.argv[1]
OUT = sys.argv[2]
W = int(sys.argv[3]) if len(sys.argv) > 3 else 1280
H = int(sys.argv[4]) if len(sys.argv) > 4 else 860
ASK = sys.argv[5] if len(sys.argv) > 5 else None
MOBILE = W < 640

profile = tempfile.mkdtemp(prefix="shot-")
port = 9333
proc = subprocess.Popen(["google-chrome", "--headless=new", f"--remote-debugging-port={port}",
                         f"--user-data-dir={profile}", "--no-first-run", "--no-default-browser-check",
                         "--hide-scrollbars", "--disable-gpu", "--remote-allow-origins=*",
                         f"--window-size={W},{H}", "about:blank"],
                        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
wsurl = None
for _ in range(80):
    try:
        tabs = json.loads(urllib.request.urlopen(f"http://127.0.0.1:{port}/json/list", timeout=2).read())
        pages = [t for t in tabs if t.get("type") == "page"]
        if pages:
            wsurl = pages[0]["webSocketDebuggerUrl"]
            break
    except Exception:
        time.sleep(0.5)
if not wsurl:
    print("chrome gagal mula")
    sys.exit(1)

ws = websocket.create_connection(wsurl, timeout=60, suppress_origin=True)
mid = 0


def cdp(method, params=None, timeout=60):
    global mid
    mid += 1
    ws.settimeout(timeout)
    ws.send(json.dumps({"id": mid, "method": method, "params": params or {}}))
    while True:
        m = json.loads(ws.recv())
        if m.get("id") == mid:
            if "error" in m:
                raise RuntimeError(m["error"])
            return m.get("result", {})


cdp("Page.enable")
cdp("Emulation.setDeviceMetricsOverride",
    {"width": W, "height": H, "deviceScaleFactor": 2 if MOBILE else 1, "mobile": MOBILE})
cdp("Page.navigate", {"url": URL})
time.sleep(7)
if ASK:
    cdp("Runtime.evaluate", {"expression": "document.querySelector('.ali-btn')&&document.querySelector('.ali-btn').click()"})
    time.sleep(1)
    cdp("Runtime.evaluate", {"expression":
        "(()=>{var i=document.querySelector('#aliQ');if(i){i.value=" + json.dumps(ASK) +
        ";document.querySelector('#aliSend').click();}return 1})()"})
    time.sleep(18)
r = cdp("Page.captureScreenshot", {"format": "png"}, timeout=90)
open(OUT, "wb").write(base64.b64decode(r["data"]))
print("siap", OUT, os.path.getsize(OUT))
ws.close()
proc.terminate()
shutil.rmtree(profile, ignore_errors=True)
