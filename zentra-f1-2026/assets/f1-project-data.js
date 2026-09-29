/* f1-project-data.js — Fasa 1 fixtures for the Zentra Project (developer) side.
   Same rules: synthetic only, impossible personal values, every record sumber:"SINTETIK". */
window.F1 = window.F1 || {};

F1.STAGES = [
  {k:1, id:"pending",   label:"Pending",           who:["Agent"],                 desc:"Lead converted into a booking draft. Unit is held for 7 days."},
  {k:2, id:"confirmed", label:"Waiting confirmation", who:["Agent","Developer"],  desc:"Developer verifies the unit, price and rebate, then confirms the hold."},
  {k:3, id:"loan",      label:"Loan processing",   who:["Agent","Developer","Bank"], desc:"Bank receives the file, runs the valuation and issues the offer letter."},
  {k:4, id:"signed_lo", label:"Signed LO",         who:["Agent","Developer","Bank"], desc:"Offer letter accepted and signed by the buyer."},
  {k:5, id:"legal",     label:"Legal processing",  who:["Agent","Developer","Lawyer"], desc:"Lawyer prepares the SPA or the deed of assignment."},
  {k:6, id:"signed_spa",label:"Signed SPA",        who:["Agent","Developer","Lawyer"], desc:"SPA executed and stamped; the file is complete."},
  {k:7, id:"completed", label:"Completed",         who:["Agent","Developer"],     desc:"Balance settled, unit handed over, commission released to the payout run."}
];

F1.PROJECTS = [
  {id:"PRJ-01", name:"Aster Heights Residences", developer:"Pemaju Aster Sdn Bhd", location:"Bangi, Selangor",
   type:"Serviced residence", tenure:"Freehold", blocks:2, units_total:420, sold:212, reserved:36,
   price_min:398000, price_max:742000, apdl:"APDL 2026/0412", completion:"Q4 2028", phase:"Phase 1", sumber:"SINTETIK"},
  {id:"PRJ-02", name:"Laman Nadi Terrace", developer:"Nadi Land Sdn Bhd", location:"Semenyih, Selangor",
   type:"Terrace houses", tenure:"Leasehold 99", blocks:3, units_total:186, sold:131, reserved:22,
   price_min:598000, price_max:886000, apdl:"APDL 2025/1188", completion:"Q2 2027", phase:"Phase 2", sumber:"SINTETIK"},
  {id:"PRJ-03", name:"Vista Commercial Centre", developer:"Vista Hartanah Sdn Bhd", location:"Seremban, N. Sembilan",
   type:"Shop offices", tenure:"Freehold", blocks:1, units_total:64, sold:29, reserved:9,
   price_min:880000, price_max:1680000, apdl:"APDL 2026/0733", completion:"Q1 2028", phase:"Phase 1", sumber:"SINTETIK"}
];

F1.UNITS = [
  {id:"U-01-08-03", project:"PRJ-01", block:"A", level:8, type:"Type A (3R2B)", built_up:950,  price:512000, status:"booked",  booking:"BK-2609-014", sumber:"SINTETIK"},
  {id:"U-01-08-05", project:"PRJ-01", block:"A", level:8, type:"Type A (3R2B)", built_up:950,  price:516000, status:"available", booking:null, sumber:"SINTETIK"},
  {id:"U-01-12-02", project:"PRJ-01", block:"A", level:12, type:"Type B (4R2B)", built_up:1180, price:638000, status:"reserved", booking:"BK-2609-016", sumber:"SINTETIK"},
  {id:"U-01-15-01", project:"PRJ-01", block:"A", level:15, type:"Type B (4R2B)", built_up:1180, price:645000, status:"available", booking:null, sumber:"SINTETIK"},
  {id:"U-01-06-09", project:"PRJ-01", block:"B", level:6,  type:"Type C (2R2B)", built_up:760,  price:432000, status:"available", booking:null, sumber:"SINTETIK"},
  {id:"U-01-09-11", project:"PRJ-01", block:"B", level:9,  type:"Type C (2R2B)", built_up:760,  price:438000, status:"sold", booking:"BK-2608-091", sumber:"SINTETIK"},
  {id:"U-02-22-07", project:"PRJ-02", block:"C", level:0,  type:"Terrace 22x75", built_up:1650, price:738000, status:"booked",  booking:"BK-2609-015", sumber:"SINTETIK"},
  {id:"U-02-22-09", project:"PRJ-02", block:"C", level:0,  type:"Terrace 22x75", built_up:1650, price:745000, status:"available", booking:null, sumber:"SINTETIK"},
  {id:"U-02-20-14", project:"PRJ-02", block:"C", level:0,  type:"Terrace 20x70", built_up:1400, price:672000, status:"sold", booking:"BK-2608-077", sumber:"SINTETIK"},
  {id:"U-02-20-16", project:"PRJ-02", block:"D", level:0,  type:"Terrace 20x70", built_up:1400, price:678000, status:"reserved", booking:"BK-2609-013", sumber:"SINTETIK"},
  {id:"U-02-22-21", project:"PRJ-02", block:"D", level:0,  type:"Terrace 22x75", built_up:1650, price:752000, status:"available", booking:null, sumber:"SINTETIK"},
  {id:"U-03-G-05",  project:"PRJ-03", block:"G", level:0,  type:"Shop lot 22x70", built_up:1540, price:980000, status:"available", booking:null, sumber:"SINTETIK"},
  {id:"U-03-G-12",  project:"PRJ-03", block:"G", level:0,  type:"Shop lot 22x70", built_up:1540, price:995000, status:"reserved", booking:"BK-2609-017", sumber:"SINTETIK"},
  {id:"U-03-G-20",  project:"PRJ-03", block:"G", level:0,  type:"Shop lot 24x80", built_up:1920, price:1420000, status:"available", booking:null, sumber:"SINTETIK"}
];

F1.BOOKINGS = [
  {id:"BK-2609-017", project:"PRJ-03", unit:"U-03-G-12", lead:"LR-2609-038", buyer:"Kavitha Ramasamy",
   agent:"ZR-AG-0103", price:995000, rebate:"3% + free legal fees", stage:5, booked:"2026-09-25",
   bank:"Maybank (offer issued)", lawyer:"M/s Razak & Co", signed_lo:"2026-09-27", updated:"2026-09-29 08:40", sumber:"SINTETIK"},
  {id:"BK-2609-016", project:"PRJ-01", unit:"U-01-12-02", lead:"LR-2609-031", buyer:"Ahmad Zaki Bin Idris",
   agent:"ZR-AG-0104", price:638000, rebate:"2%", stage:4, booked:"2026-09-24",
   bank:"CIMB (offer accepted)", lawyer:"pending appointment", signed_lo:"2026-09-28", updated:"2026-09-29 07:50", sumber:"SINTETIK"},
  {id:"BK-2609-015", project:"PRJ-02", unit:"U-02-22-07", lead:"LR-2609-034", buyer:"Farah Diyana Binti Yusof",
   agent:"ZR-AG-0102", price:738000, rebate:"3%", stage:3, booked:"2026-09-26",
   bank:"RHB (valuation booked)", lawyer:"M/s Tan & Partners", signed_lo:null, updated:"2026-09-28 19:10", sumber:"SINTETIK"},
  {id:"BK-2609-014", project:"PRJ-01", unit:"U-01-08-03", lead:"LR-2609-039", buyer:"Muhammad Faiz Bin Aziz",
   agent:"ZR-AG-0102", price:512000, rebate:"1.5%", stage:2, booked:"2026-09-28",
   bank:"not submitted", lawyer:"not appointed", signed_lo:null, updated:"2026-09-29 09:15", sumber:"SINTETIK"},
  {id:"BK-2609-013", project:"PRJ-02", unit:"U-02-20-16", lead:"LR-2609-030", buyer:"Chong Mei Yee",
   agent:"ZR-AG-0105", price:678000, rebate:"2%", stage:1, booked:"2026-09-29",
   bank:"not submitted", lawyer:"not appointed", signed_lo:null, updated:"2026-09-29 08:10", sumber:"SINTETIK"},
  {id:"BK-2608-091", project:"PRJ-01", unit:"U-01-09-11", lead:"LR-2608-302", buyer:"Lee Chin Hong",
   agent:"ZR-AG-0101", price:438000, rebate:"2%", stage:7, booked:"2026-08-14",
   bank:"Public Bank (disbursed)", lawyer:"M/s Wong & Co", signed_lo:"2026-08-22", updated:"2026-09-20 16:00", sumber:"SINTETIK"}
];

F1.CAMPAIGNS = [
  {id:"CP-2609-01", name:"Aster Heights · weekend viewing drive", channel:"Facebook", sent:1840, replies:96, leads:41, bookings:3, spend:1200, status:"running", sumber:"SINTETIK"},
  {id:"CP-2609-02", name:"Laman Nadi · phase 2 rebate blast",     channel:"WhatsApp", sent:920,  replies:131, leads:52, bookings:6, spend:0, status:"running", sumber:"SINTETIK"},
  {id:"CP-2608-07", name:"Vista shops · investor list",           channel:"Email",    sent:410,  replies:38,  leads:14, bookings:1, spend:0, status:"ended", sumber:"SINTETIK"},
  {id:"CP-2609-03", name:"Raya open house follow-up",             channel:"WhatsApp", sent:0,    replies:0,   leads:0, bookings:0, spend:0, status:"draft", sumber:"SINTETIK"}
];
