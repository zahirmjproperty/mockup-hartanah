#!/usr/bin/env bash
# Mula POC "Tanya Ali": pelayan AI + terowong awam, kemudian kunci URL ke widget.
# Guna: bash poc-ai/start_poc.sh   (kemudian push mock-up supaya URL baharu terpakai)
set -e
DIR="$(cd "$(dirname "$0")" && pwd)"
LOG=/tmp/ali-poc-tunnel.log
pkill -f "poc-ai/server.py" 2>/dev/null || true
pkill -f "cloudflared tunnel --url http://127.0.0.1:8795" 2>/dev/null || true
sleep 1
nohup python3 "$DIR/server.py" >/tmp/ali-poc-server.log 2>&1 &
sleep 2
nohup cloudflared tunnel --url http://127.0.0.1:8795 --no-autoupdate >"$LOG" 2>&1 &
for i in $(seq 1 30); do
  URL=$(grep -oE "https://[a-z0-9-]+\.trycloudflare\.com" "$LOG" | head -1 || true)
  [ -n "$URL" ] && break
  sleep 2
done
[ -z "$URL" ] && { echo "GAGAL dapat URL terowong"; exit 1; }
echo "URL: $URL"
python3 - "$URL" <<'PY'
import re, sys
url = sys.argv[1].rstrip('/') + '/chat'
p = '/home/ubuntu/mockup-hartanah/assets/ali-chat.js'
s = open(p).read()
s = re.sub(r'var ALI_API = window\.ALI_API \|\| "[^"]*"',
           f'var ALI_API = window.ALI_API || "{url}"', s)
open(p, 'w').write(s)
print('ali-chat.js ->', url)
PY
echo "Selesai. Ingat: push repo mockup-hartanah supaya URL baharu diterbitkan."
