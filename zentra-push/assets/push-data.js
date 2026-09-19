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
   location:'Dengkil, Selangor', price:485000, agent:'Fadilah Yusof', status:'offer', images:22,
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

  {id:'ZMP-0118', src:'Notion - Listing ZMP', entry:'Notion sync', title:'Serviced Apartment, Cyberjaya', type:'Serviced apartment',
   location:'Cyberjaya, Selangor', price:712000, agent:'Fadilah Yusof', status:'sold', images:20,
   realty:{mirrored:true, id:'ZR-L-0802'},
   channels:{'zentrarealty':['live',''], 'site-zmp':['live',''], dotproperty:['live',''], mudah:['live',''], fbpage:['live',''], telegram:['live','']}},

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

/* ---------- KITARAN HAYAT LISTING (status perniagaan) ---------- */
window.ZP.STATUS_LABEL = {
  draft:   'Draft',
  active:  'Live',
  offer:   'Under offer',
  sold:    'Sold',
  renewal: 'Renewal due',
  withdrawn:'Withdrawn'
};
window.ZP.STATUS_CLS = {
  draft:'st-draft', active:'st-live', offer:'st-submitted',
  sold:'st-native', renewal:'st-renewal', withdrawn:'st-dead'
};
window.ZP.STATUS_ORDER = ['active', 'offer', 'renewal', 'draft', 'sold', 'withdrawn'];
window.ZP.stLabel = v => window.ZP.STATUS_LABEL[v] || v;
window.ZP.stCls  = v => window.ZP.STATUS_CLS[v] || 'st-draft';

/* ---------- SEJARAH PER-LISTING ---------- */
/* setiap peristiwa: ts, kind, what, detail, who
   kind: created | hero | channel | status | price | doc | note */
window.ZP.HISTORY = {
  'MT-0001': [
    {ts:'2026-09-19 09:14', kind:'channel', what:'PropertyGuru queued for an assist session',
     detail:'Human submit required by the AUP. 24 of 24 fields prefilled; no password stored.', who:'Ali (agent)', cost:'1 PG credit'},
    {ts:'2026-09-19 09:06', kind:'channel', what:'Mirrored to Zentra Realty',
     detail:'Account ZR-AG-0142 linked. Record created as ZR-L-0917; read back OK.', who:'Auto', cost:'RM0'},
    {ts:'2026-09-19 08:58', kind:'channel', what:'Published to Mitula via feed',
     detail:'Feed XML v1.2 accepted. Read-back confirms the ad is live.', who:'Auto', cost:'RM0'},
    {ts:'2026-09-18 11:20', kind:'note', what:'Blocked by the compliance guard',
     detail:'A credential-based portal automation request was refused: PropertyGuru AUP prohibits it.', who:'Compliance guard', cost:'-'},
    {ts:'2026-09-17 16:31', kind:'hero', what:'Hero image changed',
     detail:'Hero set to MT-0001-foto-3.jpg (the river view). 14 images attached.', who:'Zahiruddin M.J.', cost:'-'},
    {ts:'2026-09-17 16:02', kind:'price', what:'Asking price revised',
     detail:'RM3,600,000 -> RM3,500,000 after the owner review.', who:'Zahiruddin M.J.', cost:'-'},
    {ts:'2026-09-16 10:07', kind:'created', what:'Listing created',
     detail:'Entered through the Zentra Push intake form. Land, 2.824 acres, freehold, Malay reserve.', who:'Zahiruddin M.J.', cost:'-'}
  ],
  'ZMP-0142': [
    {ts:'2026-09-19 07:12', kind:'status', what:'Marked as under offer',
     detail:'Booking form received; deposit in the client account. Adverts stay live until the SPA is signed.', who:'Fadilah Y.', cost:'-'},
    {ts:'2026-09-18 15:40', kind:'doc', what:'Booking form filed',
     detail:'Signed booking form stored with the listing record.', who:'Fadilah Y.', cost:'-'},
    {ts:'2026-09-18 08:12', kind:'channel', what:'Mudah draft published by hand',
     detail:'Draft saved in PRO Niaga; the agent pressed Publish in their own session. 2 Mudah Credits.', who:'Fadilah Y.', cost:'2 Mudah Credits'},
    {ts:'2026-09-17 19:22', kind:'channel', what:'Carousell received the record',
     detail:'Mudah dual-platform listing carried it across automatically once the store tier allowed it.', who:'Auto', cost:'RM0'},
    {ts:'2026-09-17 19:20', kind:'channel', what:'Mudah published',
     detail:'Advance store. Mudah applied its own watermark as required.', who:'Auto', cost:'RM0'},
    {ts:'2026-09-15 11:03', kind:'hero', what:'Hero image changed',
     detail:'Hero set to ZMP-0142-foto-2.jpg. 22 images attached.', who:'Fadilah Y.', cost:'-'},
    {ts:'2026-09-15 10:31', kind:'created', what:'Listing created',
     detail:'Imported from Notion, then reviewed. Condominium, 1,050 sqft, freehold.', who:'Fadilah Y.', cost:'-'}
  ],
  'MT-0044': [
    {ts:'2026-09-19 08:40', kind:'channel', what:'Sent to Dot Property and the aggregator feed',
     detail:'Record written to feed XML v1.2. Ingest SLA is 24 hours.', who:'Auto', cost:'RM0'},
    {ts:'2026-09-19 08:39', kind:'channel', what:'Posted to 3 Telegram channels',
     detail:'Bot API sendMessage returned message ids 4417, 4418 and 4419.', who:'Auto', cost:'RM0'},
    {ts:'2026-09-18 17:44', kind:'channel', what:'Facebook Page post published',
     detail:'Graph API returned post id 122094... Read back: live.', who:'Auto', cost:'RM0'},
    {ts:'2026-09-18 09:15', kind:'note', what:'Plan image withheld',
     detail:'The survey plan was kept private per the house image rule; 9 publishable photos remain.', who:'Compliance guard', cost:'-'},
    {ts:'2026-09-14 14:22', kind:'created', what:'Listing created',
     detail:'Imported from Notion. Oil palm smallholding, 6.2 acres, leasehold.', who:'Zahiruddin M.J.', cost:'-'}
  ],
  'ZMP-0193': [
    {ts:'2026-09-19 08:52', kind:'channel', what:'iProperty cross-listed',
     detail:'AgentNet cross-listing duplicated the PropertyGuru record; no third-party tooling involved. Read back OK.', who:'Ali (agent)', cost:'0'},
    {ts:'2026-09-18 16:10', kind:'channel', what:'PropertyGuru submitted',
     detail:'Pay-per-post submission; record read back on the portal.', who:'Ali (agent)', cost:'1 PG credit'},
    {ts:'2026-09-18 16:05', kind:'channel', what:'EdgeProp queued',
     detail:'Prefill ready for the agent to submit inside EdgeProp.', who:'Auto', cost:'-'},
    {ts:'2026-09-16 12:48', kind:'hero', what:'Hero image changed',
     detail:'Hero set to ZMP-0193-foto-1.jpg. 18 images attached.', who:'Fadilah Y.', cost:'-'},
    {ts:'2026-09-16 09:30', kind:'created', what:'Listing created',
     detail:'Imported from Notion. Terrace house, 1,650 sqft, leasehold.', who:'Fadilah Y.', cost:'-'}
  ],
  'MT-0061': [
    {ts:'2026-09-18 21:03', kind:'channel', what:'Renewal flagged on 4 channels',
     detail:'7 days to expiry on the Mudah advert. An assist session is scheduled.', who:'Auto', cost:'-'},
    {ts:'2026-09-18 21:01', kind:'status', what:'Ads moved to renewal due',
     detail:'The portal adverts lapsed; the listing itself is still available.', who:'Auto', cost:'-'},
    {ts:'2026-09-10 10:12', kind:'channel', what:'Published to 4 channels',
     detail:'Site, Dot Property, Mudah and the Realty mirror.', who:'Auto', cost:'RM0'},
    {ts:'2026-09-10 09:50', kind:'created', what:'Listing created',
     detail:'Imported from Notion. Bungalow lot, 5,200 sqft, freehold.', who:'Zahiruddin M.J.', cost:'-'}
  ],
  'ZMP-0118': [
    {ts:'2026-09-19 09:02', kind:'status', what:'Marked as sold',
     detail:'SPA signed and stamped. Adverts withdrawn from every channel within the hour.', who:'Fadilah Y.', cost:'-'},
    {ts:'2026-09-19 09:00', kind:'channel', what:'Adverts withdrawn everywhere',
     detail:'8 placements taken down; the ledger keeps the history for the commission file.', who:'Auto', cost:'-'},
    {ts:'2026-08-30 14:20', kind:'status', what:'Marked as under offer',
     detail:'Offer accepted at RM712,000, subject to loan.', who:'Fadilah Y.', cost:'-'},
    {ts:'2026-08-22 09:05', kind:'created', what:'Listing created',
     detail:'Imported from Notion. Serviced apartment, 1,020 sqft, freehold.', who:'Fadilah Y.', cost:'-'}
  ],
  'ZMP-0207': [
    {ts:'2026-09-19 07:58', kind:'note', what:'Zentra Realty mirror withheld',
     detail:'The listing agent holds no Zentra Realty account, so the record stays in Zentra Push. A later link backfills it.', who:'Auto', cost:'-'},
    {ts:'2026-09-19 07:55', kind:'hero', what:'16 images attached',
     detail:'Hero set to ZMP-0207-foto-1.jpg.', who:'New agent seat', cost:'-'},
    {ts:'2026-09-19 07:52', kind:'created', what:'Draft started',
     detail:'Entered through the Zentra Push intake form; not yet published to any channel.', who:'New agent seat', cost:'-'}
  ]
};

window.ZP.historyOf = id => window.ZP.HISTORY[id] || [];

/* ---------- GAMBAR HERO PER-LISTING ---------- */
window.ZP.HERO = {
 "MT-0001": "https://lh3.googleusercontent.com/d/11R_E-xft6V3NGf05YGqKEgTed8Z7WAJK=w1000",
 "ZMP-0142": "https://lh3.googleusercontent.com/d/1zp1PvWqO8Zk0EG0p_Z7JhDEBjA4WDOqP=w1000",
 "MT-0044": "https://lh3.googleusercontent.com/d/1yfMejiuoq41PPZeN_QWmxrnzojmdLynF=w1000",
 "ZMP-0193": "https://lh3.googleusercontent.com/d/1r64Zuz8ufxZPsR4jb1D2djHR4Fl52_KF=w1000",
 "MT-0061": "https://lh3.googleusercontent.com/d/1PpBgYOv9ay3iwsxVtflZOs6_rdSRCMth=w1000",
 "ZMP-0118": "https://lh3.googleusercontent.com/d/1dNIrxwl8_jPI1Y8N8FCIP1NN4WYnEjAf=w1000",
 "ZMP-0207": "https://lh3.googleusercontent.com/d/126BKiOOOmvUCoQy8t4VsTOv7l_RWBU4M=w1000"
};
