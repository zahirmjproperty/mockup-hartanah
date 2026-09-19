#!/usr/bin/env node
/*
 * bina_data_realty.js — jana assets/realty-listings.js untuk Zentra Realty
 * DARIPADA satu sumber: zentra-push/assets/push-data.js
 *
 * Sebab: satu rekod hidup dalam dua sistem. Kalau data disalin dengan tangan,
 * kedua-dua sistem akan bercanggah. Penjana ini memastikan ia sama.
 * Termasuk versi rekod + kesegaran penghantaran, supaya aliran edit/push semula
 * di sisi agensi mengira daripada nombor yang sama.
 *
 * Guna: node bina_data_realty.js
 */
const fs = require('fs');
const path = require('path');

const SRC = '/home/ubuntu/zentra-push/assets/push-data.js';
const OUT = '/home/ubuntu/mockup-hartanah/zentra-realty/assets/realty-listings.js';

global.window = {};
require(SRC);
const Z = global.window.ZP;

const CH = {};
Z.CHANNELS.forEach(c => { CH[c.id] = c; });

const rec = l => ({
  id: l.id,
  src: l.src,
  entry: l.entry,
  title: l.title,
  type: l.type,
  location: l.location,
  price: l.price,
  agent: l.agent,
  status: l.status,
  images: l.images,
  realty: l.realty,
  channels: l.channels,
  v: l.v,
  stale: Z.staleOf(l),
  where: l.location + ', ' + (l.type || ''),
  live: Object.values(l.channels).filter(c => c[0] === 'live' || c[0] === 'native').length,
  placed: Object.keys(l.channels).length,
  hero: Z.HERO[l.id] || ''
});

const upd = {};
Z.CHANNELS.forEach(c => { upd[c.id] = Z.UPD_MODE(c.id); });

const out = {
  ZR_LISTINGS: Z.LISTINGS.map(rec),
  ZR_HISTORY: Z.HISTORY,
  ZR_EVIDENCE: Z.EVIDENCE,
  ZR_STATUS_LABEL: Z.STATUS_LABEL,
  ZR_STATUS_CLS: Z.STATUS_CLS,
  ZR_STATUS_ORDER: Z.STATUS_ORDER,
  ZR_UPD_MODE: upd,
  ZR_UPD_LABEL: Z.UPD_LABEL,
  ZR_UPD_NOTE: Z.UPD_NOTE,
  ZR_AGENTS: Z.SEATS.map(s => ({
    name: s.name, role: s.role, cert: s.cert, firm: s.firm,
    realtyId: s.realty ? s.realty.id : '', realtyLevel: s.realty ? s.realty.level : '',
    pushLinked: !!(s.realty && s.realty.linked)
  })),
  ZR_CHANNELS: Z.CHANNELS.map(c => ({id: c.id, name: c.name, group: c.group, tier: c.tier, gate: c.gate || ''}))
};

const body = '/* DIJANA oleh bina_data_realty.js daripada zentra-push/assets/push-data.js.\n' +
  '   JANGAN edit dengan tangan — jalankan penjana semula. */\n' +
  'window.ZR = ' + JSON.stringify(out, null, 1) + ';\n' +
  'window.ZR.stLabel = v => window.ZR.ZR_STATUS_LABEL[v] || v;\n' +
  'window.ZR.stCls = v => window.ZR.ZR_STATUS_CLS[v] || "st-draft";\n' +
  'window.ZR.historyOf = id => window.ZR.ZR_HISTORY[id] || [];\n' +
  'window.ZR.byId = id => window.ZR.ZR_LISTINGS.find(l => l.id === id) || window.ZR.ZR_LISTINGS[0];\n' +
  'window.ZR.updMode = id => window.ZR.ZR_UPD_MODE[id] || "assist";\n' +
  'window.ZR.isStale = (l, ch) => (l.stale || []).indexOf(ch) > -1;\n';

fs.mkdirSync(path.dirname(OUT), {recursive: true});
fs.writeFileSync(OUT, body);

console.log('ditulis: ' + OUT + ' (' + body.length + ' bait)');
console.log('listing: ' + out.ZR_LISTINGS.length +
  ' | sejarah: ' + Object.keys(out.ZR_HISTORY).length +
  ' | agen: ' + out.ZR_AGENTS.length +
  ' | saluran: ' + out.ZR_CHANNELS.length);
out.ZR_LISTINGS.forEach(l => console.log('  ' + l.id.padEnd(9) + 'v' + String(l.v).padEnd(3) +
  l.status.padEnd(9) + (l.live + '/' + l.placed).padEnd(6) + 'lapuk: ' + (l.stale.join(',') || '-') +
  '   ' + l.agent));
