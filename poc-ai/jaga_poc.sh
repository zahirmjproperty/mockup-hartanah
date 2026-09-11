#!/usr/bin/env bash
# Jaga POC "Tanya Ali": pastikan pelayan AI + terowong hidup; jika URL terowong
# berubah, kemas kini assets/ali-chat.js dan push ke repo mock-up.
# Guna: bash poc-ai/jaga_poc.sh   (stdout kosong = semua sihat)
DIR="$(cd "$(dirname "$0")" && pwd)"
ROOT="$(cd "$DIR/.." && pwd)"
LOG=/tmp/ali-poc-tunnel.log
URLF="$DIR/url_semasa.txt"

sihat_server() { curl -s -m 8 http://127.0.0.1:8795/health | grep -q '"ok": true'; }
url_terowong() { grep -oE "https://[a-z0-9-]+\.trycloudflare\.com" "$LOG" 2>/dev/null | tail -1; }
sihat_terowong() { # cuba 3x, timeout panjang (elak mula semula tak perlu)
  [ -z "$1" ] && return 1
  for i in 1 2 3; do
    curl -s -m 25 "$1/health" | grep -q '"ok": true' && return 0
    sleep 4
  done
  return 1
}

U="$(url_terowong)"
if sihat_server && sihat_terowong "$U"; then
  echo "$U" > "$URLF"; exit 0
fi

echo "[jaga_poc] memulakan semula pelayan/terowong $(date '+%F %T')"
bash "$DIR/start_poc.sh" >/tmp/ali-poc-start.log 2>&1 || { echo "[jaga_poc] GAGAL mula"; exit 1; }
NEW="$(url_terowong)"
[ -z "$NEW" ] && { echo "[jaga_poc] tiada URL"; exit 1; }
OLD="$(cat "$URLF" 2>/dev/null)"
if [ "$NEW" != "$OLD" ]; then
  cp /dev/null "$LOG.old" 2>/dev/null || true
  cd "$ROOT" || exit 1
  if git diff --quiet -- assets/ali-chat.js; then :; else
    set -a; . /home/ubuntu/.hermes/.env; set +a
    git add assets/ali-chat.js
    git -c user.name="Zahir" -c user.email="zahir@zahirproperty.my" commit -q -m "POC Ali: URL terowong dikemas kini ($NEW)"
    git push -q "https://x-access-token:$GITHUB_TOKEN@github.com/zahirmjproperty/mockup-hartanah.git" main \
      && echo "[jaga_poc] push OK → $NEW" || echo "[jaga_poc] push GAGAL"
  fi
fi
echo "$NEW" > "$URLF"
