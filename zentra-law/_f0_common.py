# _f0_common.py — Zentra Law F0 mock-up: helpers + shell (theme identical to Zentra Hub)
from datetime import date

PROTO_DATE = date(2026, 9, 17)

def money(x, dp=2):
    s = f"{x:,.{dp}f}"
    return "RM" + s

def sro_scale(value):
    """Solicitors' Remuneration Order 2023, First Schedule Table A (sale & transfer / loan docs)."""
    v = float(value); fee = 0.0
    if v <= 0: return 0.0
    first = min(v, 500_000) * 0.0125
    fee += first
    if v > 500_000:
        fee += (min(v, 7_500_000) - 500_000) * 0.01
    # above RM7.5m: negotiable, not exceeding 1% (shown separately on the page)
    return max(fee, 500.0) if v > 0 else 0.0

def subsidiary_instrument(full_scale_fee):
    """Stamp Act 1949 s.4(3) subsidiary instruments: 10% of full scale fee, min RM500, max RM2,000."""
    return min(max(full_scale_fee * 0.10, 500.0), 2000.0)

def stamp_duty_mot(value):
    """Malaysia MOT stamp duty (citizen/PR), 2026: 1% first 100k, 2% next 400k, 3% next 500k, 4% above 1m."""
    v = float(value); d = 0.0
    d += min(v, 100_000) * 0.01
    if v > 100_000: d += (min(v, 500_000) - 100_000) * 0.02
    if v > 500_000: d += (min(v, 1_000_000) - 500_000) * 0.03
    if v > 1_000_000: d += (v - 1_000_000) * 0.04
    return d

def stamp_duty_loan(amount):
    """Loan / financing agreement: 0.5% of the amount secured."""
    return float(amount) * 0.005

def fmt_date(d):
    return d.strftime("%d %b %Y")

def days_left(target):
    return (target - PROTO_DATE).days

def tail(title, extra=""):
    return f"""    <p class="foot-note">Zentra Law prototype &middot; Zentra Property Group &middot; English (US) UI &middot; sample data only<br>
{title}. No real client, file or money is represented here. Compliance notes are design intent and remain subject to legal review.</p>
{extra}"""

SHELL = """<!DOCTYPE html>
<html lang="en-US">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>{title} | Zentra Law</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/law.css">
</head>
<body data-page="{page}">
<div class="shell">
  <aside class="side" id="znav"></aside>
  <main class="main">
{body}
  </main>
</div>
<script src="assets/law.js"></script>
<script src="assets/law-nav.js"></script>
</body>
</html>
"""

def top(title, sub, badge="PROTOTYPE &middot; SAMPLE DATA", pill="gold"):
    return f"""    <div class="top">
      <div>
        <h1>{title}</h1>
        <p>{sub}</p>
      </div>
      <span class="badge-demo">{badge}</span>
    </div>
"""

def h2(num, text):
    return f'    <h2 class="sec"><span class="num">{num}</span> {text}</h2>\n'

def note(text, kind="", icon=""):
    cls = "note" + (" " + kind if kind else "")
    return f'    <div class="{cls}">{text}</div>\n'
