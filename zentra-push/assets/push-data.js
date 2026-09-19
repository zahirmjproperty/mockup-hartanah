/* push-data.js — data contoh Zentra Push. Semua angka ilustrasi mockup. */
window.ZP = {};

/* ---------- KITARAN HAYAT SALURAN ---------- */
window.ZP.STATES = ['draft','mapped','queued','submitted','live','renewal','dead'];

window.ZP.STATE_LABEL = {
  draft:'Draft', mapped:'Mapped', queued:'Queued', submitted:'Submitted',
  live:'Live', renewal:'Needs renewal', dead:'Taken down'
};

/* ---------- TAHAP KEUPAYAAN ---------- */
window.ZP.TIER = {
  AUTO:   {label:'Auto',    cls:'t-auto',   txt:'Fully automatic - sanctioned channel'},
  ASSIST: {label:'Assist',  cls:'t-assist', txt:'Prefill only - a human presses Submit'},
  NATIVE: {label:'Native',  cls:'t-native', txt:'Switch it on inside the portal itself'},
  MANUAL: {label:'Manual',  cls:'t-manual', txt:'Content pack only - no automation available'}
};

/* ---------- SALURAN (disahkan terhadap AUP/ToS portal, Sep 2026) ---------- */
window.ZP.CHANNELS = [
  {id:'zentrarealty', name:'Zentra Realty', group:'Owned', tier:'AUTO', gate:'realty',
   api:'Zentra Realty internal API', apistate:'owned', tos:'clear',
   tosnote:'Our own network, so no third-party terms apply. Gated: only available when the listing agent holds a linked Zentra Realty account.',
   cost:'RM0', reach:'Zentra Realty agent network', href:'#'},

  {id:'site-zmp', name:'zahirmjproperty.com + mrtanah.com', group:'Owned',
   tier:'AUTO', api:'Git deploy + sitemap', apistate:'owned', tos:'clear',
   tosnote:'Wholly ours. No third-party terms apply.',
   cost:'RM0', reach:'Organic + Google Indexing API', href:'#'},

  {id:'dotproperty', name:'Dot Property Malaysia', group:'Aggregator network',
   tier:'AUTO', api:'XML feed (Proppit)', apistate:'feed', tos:'clear',
   tosnote:'Free unlimited listings. Feed ingest is the intended integration path.',
   cost:'RM0', reach:'MY + 10 regional portals', href:'https://www.dotproperty.com.my/upload-your-property'},

  {id:'trovit', name:'Trovit', group:'Aggregator network',
   tier:'AUTO', api:'XML feed', apistate:'feed', tos:'clear',
   tosnote:'Aggregator. Accepts agency feeds; no listing-form automation needed.',
   cost:'RM0', reach:'Metasearch, MY + global', href:'#'},

  {id:'mitula', name:'Mitula', group:'Aggregator network',
   tier:'AUTO', api:'XML feed', apistate:'feed', tos:'clear',
   tosnote:'Aggregator. Same feed family as Trovit (Lifull Connect group).',
   cost:'RM0', reach:'Metasearch, MY + global', href:'#'},

  {id:'nestoria', name:'Nestoria', group:'Aggregator network',
   tier:'AUTO', api:'XML feed', apistate:'feed', tos:'clear',
   tosnote:'Aggregator. Feed-driven.',
   cost:'RM0', reach:'Metasearch', href:'#'},

  {id:'fbpage', name:'Facebook Page', group:'Social',
   tier:'AUTO', api:'Graph API (page feed)', apistate:'yes', tos:'clear',
   tosnote:'Official Meta API for Pages. Page publishing remains supported.',
   cost:'RM0', reach:'Followers + paid boost', href:'https://developers.facebook.com/docs/pages-api'},

  {id:'telegram', name:'Telegram channels', group:'Social',
   tier:'AUTO', api:'Bot API sendMessage', apistate:'yes', tos:'clear',
   tosnote:'Official bot API. Bot must be an admin of the channel or group.',
   cost:'RM0', reach:'Subscribers', href:'https://core.telegram.org/bots/api'},

  {id:'gbp', name:'Google Business Profile', group:'Search',
   tier:'AUTO', api:'GBP API localPosts', apistate:'yes', tos:'clear',
   tosnote:'Official Google API. Posts are capped at 1,500 characters and expire after 7 days.',
   cost:'RM0', reach:'Local pack, Maps', href:'https://developers.google.com/my-business'},

  {id:'propguru', name:'PropertyGuru', group:'Major portal',
   tier:'ASSIST', api:'None published for agents', apistate:'no', tos:'blocked',
   tosnote:'AUP bans third-party automation; the "Policy on Porting Listings" (29 Aug 2026) states their systems actively detect and block third-party access, and that bots cannot be granted access on request.',
   cost:'Agent package + Universal Credits', reach:'~2.0-2.4M visits/mo', href:'https://www.propertyguru.com.my/'},

  {id:'iproperty', name:'iProperty.com.my', group:'Major portal',
   tier:'NATIVE', api:'Via AgentNet cross-listing', apistate:'native', tos:'blocked',
   tosnote:'Same group as PropertyGuru. AUP cl. 5.1.24 bans automation software and bots. Cross-listing from AgentNet is the sanctioned route.',
   cost:'Dual concurrent listing (package)', reach:'~0.9-1.5M visits/mo', href:'https://www.iproperty.com.my/'},

  {id:'edgeprop', name:'EdgeProp.my', group:'Major portal',
   tier:'ASSIST', api:'None published', apistate:'no', tos:'caution',
   tosnote:'No public posting API. The portal itself ships a listing-sync browser plugin in SG - evidence they tolerate assistive tooling, but nothing is published for MY.',
   cost:'PRO Agent RM3.15/day', reach:'~340-520K visits/mo', href:'https://www.edgeprop.my/pro-agents'},

  {id:'mudah', name:'Mudah.my (Property)', group:'Major portal',
   tier:'ASSIST', api:'None published', apistate:'no', tos:'caution',
   tosnote:'ToS bans scraping, framing and spidering without written consent, and assigns listing copyright to Mudah. The PRO Niaga dashboard does support drafting then publishing, which an assistant can prefill.',
   cost:'PRO Niaga free; Mudah Credits for premium', reach:'~0.9M visits/mo, 18K+ agents', href:'https://www.mudah.my/about/pro-niaga-guide/'},

  {id:'carousell', name:'Carousell MY', group:'Major portal',
   tier:'NATIVE', api:'Via Mudah dual listing', apistate:'native', tos:'caution',
   tosnote:'Mudah "Dual Platform Listing" auto-publishes property ads to Carousell for Advance/Elite storefronts. No separate feed needed.',
   cost:'CarouBiz (where applicable)', reach:'Consumer marketplace', href:'#'},

  {id:'fbmarket', name:'Facebook Marketplace', group:'Social',
   tier:'MANUAL', api:'Partner API = EU countries only', apistate:'no', tos:'blocked',
   tosnote:'The Marketplace Partner item API country enum contains European countries only, and Meta policy bans business sellers from Marketplace. Not automatable in MY.',
   cost:'n/a', reach:'Very large, but policy-fenced', href:'#'},

  {id:'fbgroups', name:'Facebook Groups', group:'Social',
   tier:'MANUAL', api:'Groups API removed 22 Apr 2024', apistate:'no', tos:'blocked',
   tosnote:'publish_to_groups and groups_access_member_info were deprecated in Graph v19 and removed from all versions on 22 April 2024. Group app install by admins was removed too.',
   cost:'n/a', reach:'Category communities', href:'#'},

  {id:'whatsapp', name:'WhatsApp (groups & broadcast)', group:'Social',
   tier:'MANUAL', api:'Cloud API has no group support', apistate:'no', tos:'caution',
   tosnote:'WABA cannot post to groups or channels. Broadcast lists cap at 256 recipients who must have saved the number, and are manual. Cloud API suits opt-in 1:1 template messages only.',
   cost:'Cloud API per-conversation (optional)', reach:'Direct network', href:'#'},

  {id:'community', name:'PropSocial / iBilik / other portals', group:'Long tail',
   tier:'MANUAL', api:'None found', apistate:'no', tos:'caution',
   tosnote:'No public agent APIs located. Treated as content-pack targets until verified otherwise.',
   cost:'Varies', reach:'Niche / rental', href:'#'}
];

/* ---------- SISTEM BERKAITAN: ZENTRA REALTY ---------- */
window.ZP.REALTY = {
  name:'Zentra Realty',
  tag:'Owned system',
  what:'The agency platform for the Zentra Realty network. An agent who already holds a Zentra Realty account can mirror each listing there at the same time.',
  rule:'Enter a listing once. If the agent holds a Zentra Realty account, the record is created in both systems and the two stay linked. If there is no account, the listing lives in Zentra Push only - and can be linked later without re-typing anything.'
};

/* ---------- KERUSI EJEN (dengan status pautan Zentra Realty) ---------- */
window.ZP.SEATS = [
  {name:'Zahiruddin M.J.', firm:'IQI Realty Sdn Bhd', role:'Principal', cert:'PEA 2684',
   cap:6, used:4, live:9, state:'ok',  realty:{linked:true,  id:'ZR-AG-0142', level:'Principal'}},
  {name:'Fadilah Yusof',   firm:'IQI Realty Sdn Bhd', role:'Negotiator', cert:'PEA 2313',
   cap:4, used:4, live:5, state:'cap', realty:{linked:true,  id:'ZR-AG-0231', level:'Negotiator'}},
  {name:'New agent seat',  firm:'IQI Realty Sdn Bhd', role:'Negotiator', cert:'pending',
   cap:4, used:0, live:0, state:'idle', realty:{linked:false, id:'', level:''}}
];

/* sesi semasa - boleh ditukar pada halaman "New listing" untuk melihat kedua-dua keadaan */
window.ZP.ACTOR = 'Zahiruddin M.J.';

window.ZP.seat       = n => window.ZP.SEATS.find(s => s.name === (n || window.ZP.ACTOR)) || window.ZP.SEATS[0];
window.ZP.realtyLinked = n => !!(window.ZP.seat(n).realty || {}).linked;
window.ZP.realtyId   = n => (window.ZP.seat(n).realty || {}).id || '';
/* saluran yang layak untuk kerusi ini (gate 'realty' hanya bila akaun berpaut) */
window.ZP.channelsFor = n => window.ZP.CHANNELS.filter(c => !c.gate || window.ZP.realtyLinked(n));

/* ---------- RINGKASAN KEUPAYAAN (dikira selepas saluran ditapis) ---------- */
window.ZP.COUNTS_FOR = (function(){
  const cache = {};
  return function(n){
    const k = n || window.ZP.ACTOR;
    if (cache[k]) return cache[k];
    const c = {AUTO:0, ASSIST:0, NATIVE:0, MANUAL:0};
    window.ZP.channelsFor(k).forEach(x => c[x.tier]++);
    return (cache[k] = c);
  };
})();

window.ZP.COUNTS = (function(){
  const c = {AUTO:0, ASSIST:0, NATIVE:0, MANUAL:0};
  window.ZP.CHANNELS.forEach(x => c[x.tier]++);
  return c;
})();

/* ---------- LISTING (rekod kanonik) ---------- */
window.ZP.LISTINGS = [
  {id:'MT-0001', src:'Notion - Listing Mr Tanah', entry:'Zentra Push form', title:'Tanah Janda Baik (Sungai)', type:'Land',
   location:'Janda Baik, Pahang', price:3500000, agent:'Zahiruddin M.J.', status:'active', images:14,
   realty:{mirrored:true, id:'ZR-L-0917'},
   channels:{'zentrarealty':['live','zentrarealty.com/listing/zr-l-0917'], 'site-zmp':['live','/tanah-janda-baik'],
             dotproperty:['live','dotproperty.com.my/ads/mt-0001'], trovit:['live','trovit.my/ads/mt-0001'],
             mitula:['live','mitula.my/ads/mt-0001'], propguru:['queued',''], mudah:['assist','']}},

  {id:'ZMP-0142', src:'Notion - Listing ZMP', entry:'Notion sync', title:'Residensi Avalon, Cybersouth', type:'Condo',
   location:'Dengkil, Selangor', price:485000, agent:'Fadilah Yusof', status:'active', images:22,
   realty:{mirrored:true, id:'ZR-L-0902'},
   channels:{'zentrarealty':['live','zentrarealty.com/listing/zr-l-0902'], 'site-zmp':['live','/residensi-avalon'],
             dotproperty:['live',''], trovit:['live',''], iproperty:['native',''], mudah:['assist',''], carousell:['native','']}},

  {id:'MT-0044', src:'Notion - Listing Mr Tanah', entry:'Notion sync', title:'Kebun Kelapa Sawit, Kuala Pilah', type:'Agriculture',
   location:'Kuala Pilah, N.Sembilan', price:1250000, agent:'Zahiruddin M.J.', status:'active', images:9,
   realty:{mirrored:true, id:'ZR-L-0888'},
   channels:{'zentrarealty':['live','zentrarealty.com/listing/zr-l-0888'], 'site-zmp':['live',''],
             dotproperty:['submitted',''], fbpage:['live',''], telegram:['live',''], gbp:['live','']}},

  {id:'ZMP-0193', src:'Notion - Listing ZMP', entry:'Notion sync', title:'Senna Presint 12, Putrajaya', type:'Terrace',
   location:'Putrajaya', price:1080000, agent:'Fadilah Yusof', status:'active', images:18,
   realty:{mirrored:true, id:'ZR-L-0871'},
   channels:{'zentrarealty':['submitted',''], 'site-zmp':['live',''], propguru:['submitted',''],
             iproperty:['native',''], edgeprop:['queued',''], mudah:['assist','']}},

  {id:'MT-0061', src:'Notion - Listing Mr Tanah', entry:'Notion sync', title:'Bungalow Lot, Seremban 2', type:'Bungalow',
   location:'Seremban, N.Sembilan', price:890000, agent:'Zahiruddin M.J.', status:'renewal', images:11,
   realty:{mirrored:true, id:'ZR-L-0850'},
   channels:{'zentrarealty':['renewal',''], 'site-zmp':['renewal',''], mudah:['renewal',''], dotproperty:['renewal','']}},

  {id:'ZMP-0207', src:'Zentra Push', entry:'Zentra Push form', title:'Terra Residences, Bangi', type:'Condominium',
   location:'Bandar Baru Bangi, Selangor', price:520000, agent:'New agent seat', status:'draft', images:16,
   realty:{mirrored:false, id:''},
   channels:{}}
];

/* ---------- JEJAK BUKTI (evidence trail) ---------- */
window.ZP.EVIDENCE = [
  {ts:'2026-09-19 09:14', listing:'MT-0001', ch:'propguru',    action:'Queued for assist session',
   detail:'Human submit required (AUP). Prefilled 24 of 24 fields.', who:'Ali (agent)', cost:'1 PG credit'},
  {ts:'2026-09-19 09:06', listing:'MT-0001', ch:'zentrarealty', action:'Mirrored to Zentra Realty',
   detail:'Account ZR-AG-0142 linked. Record created as ZR-L-0917; read back: OK.', who:'Zentra Push (auto)', cost:'RM0'},
  {ts:'2026-09-19 08:52', listing:'ZMP-0193', ch:'iproperty',  action:'Cross-listed',
   detail:'AgentNet cross-listing duplicated the PropertyGuru record. Read back: OK.', who:'Ali (agent)', cost:'0'},
  {ts:'2026-09-19 08:40', listing:'MT-0044', ch:'dotproperty', action:'Feed submitted',
   detail:'Record written to feed XML v1.2. Awaiting ingest (24h SLA).', who:'Zentra Push (auto)', cost:'RM0'},
  {ts:'2026-09-19 08:39', listing:'MT-0044', ch:'telegram',    action:'Posted to 3 channels',
   detail:'Bot API sendMessage returned message_id 4417, 4418, 4419.', who:'Zentra Push (auto)', cost:'RM0'},
  {ts:'2026-09-19 08:12', listing:'ZMP-0142', ch:'mudah',      action:'Assist draft created',
   detail:'Draft saved in PRO Niaga. Agent pressed Publish manually.', who:'Fadilah Y.', cost:'2 Mudah Credits'},
  {ts:'2026-09-19 07:58', listing:'ZMP-0207', ch:'zentrarealty', action:'Option withheld',
   detail:'Listing agent holds no Zentra Realty account. Record kept in Zentra Push; can be linked later.', who:'Zentra Push (auto)', cost:'-'},
  {ts:'2026-09-18 21:03', listing:'MT-0061', ch:'mudah',       action:'Renewal flagged',
   detail:'7 days to expiry. Assist session scheduled.', who:'Zentra Push (auto)', cost:'-'},
  {ts:'2026-09-18 17:44', listing:'MT-0044', ch:'fbpage',      action:'Page post published',
   detail:'Graph API returned post id 122094... Read back: live.', who:'Zentra Push (auto)', cost:'RM0'},
  {ts:'2026-09-18 11:20', listing:'MT-0001', ch:'ipush-style', action:'BLOCKED by guard',
   detail:'Credential-based portal automation refused: PropertyGuru AUP prohibits it.', who:'Compliance guard', cost:'-'}
];

/* ---------- PENJAGA PEMATUHAN (compliance guard) ---------- */
window.ZP.RULES = [
  {id:'G1', rule:'Never automate a channel whose terms prohibit automation',
   rationale:'PropertyGuru AUP and iProperty AUP cl. 5.1.24 both ban third-party automation software.',
   effect:'Auto routes for these channels are disabled in code, not by policy memo.'},
  {id:'G2', rule:'Never store agent portal passwords',
   rationale:'Mudah assigns listing copyright and restricts automated access; holding credentials multiplies breach surface under PDPA.',
   effect:'Assist mode runs in the agent\'s own logged-in browser session. No secret ever reaches the server.'},
  {id:'G3', rule:'A human presses Submit on ASSIST channels',
   rationale:'Keeps the action attributable to the licensed agent and outside the definition of a bot.',
   effect:'Prefill + open tab; the ledger only marks "submitted" after the agent confirms.'},
  {id:'G4', rule:'No scraping of any portal to build listings',
   rationale:'Mudah ToS bans spidering; PropertyGuru prohibits content extraction and reposting.',
   effect:'Canonical records come from our own database or our own intake form only.'},
  {id:'G5', rule:'Every push leaves evidence',
   rationale:'A successful API call is not a successful task - portals silently reject listings.',
   effect:'Each channel write requires a read-back URL plus timestamp before status becomes Live.'},
  {id:'G6', rule:'Agent identity block is injected per channel',
   rationale:'Registered firm and agent numbers must appear on advertising; portals also forbid contact details inside listing bodies.',
   effect:'Identity goes into profile and mandated fields, never the description text.'},
  {id:'G7', rule:'A gated channel stays hidden until its gate is satisfied',
   rationale:'Zentra Realty mirroring needs an account on that system. Offering the switch without one would only produce a failed write.',
   effect:'The Zentra Realty channel is filtered out of every channel picker until the agent\'s account is linked.'}
];

/* ---------- KPI ---------- */
window.ZP.KPI = {
  listings: 6, live: 17, queued: 3, assist: 4, renewal: 3, auto: 9, mirrored: 5
};
