#!/usr/bin/env bash
# (LAPUK sejak 2026-09-12) POC dahulu memulakan pelayan sendiri + terowong.
# Produksi kini = systemd ali-ai.service (127.0.0.1:8795) di belakang Caddy.
# Skrip ini TIDAK lagi memulakan pelayan (dulu ia boleh MEMBUNUH servis produksi
# kerana pkill -f "poc-ai/server.py"). Kini ia hanya memastikan servis hidup.
# Pratonton: guna /home/ubuntu/ali-preview/mula_pratonton.sh
set -u
if curl -s -m 10 http://127.0.0.1:8795/health | grep -q '"ok": true'; then
  echo "Servis produksi sihat (127.0.0.1:8795). Tiada tindakan."
  exit 0
fi
echo "Servis tidak sihat — mula semula melalui systemd (bukan nohup)."
sudo systemctl restart ali-ai.service
sleep 6
curl -s -m 15 https://api.zahirmjproperty.com/health | grep -q '"ok": true' \
  && echo "pulih OK" || { echo "MASIH GAGAL"; exit 1; }
