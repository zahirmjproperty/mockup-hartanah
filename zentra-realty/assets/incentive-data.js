/* ============================================================================
   assets/incentive-data.js — single source of truth for the incentive,
   campaign-target and recognition module (ZENTRA Realty).

   EVERY VALUE BELOW IS SAMPLE DATA (mock-up). No real agent, buyer or
   transaction is represented here. UI language: EN(US).

   This file is the one place that defines a campaign. Any screen that shows
   incentives reads from here — never hard-code a target in a page.
   ========================================================================= */
window.INS = (function () {
  'use strict';

  /* ---------------- 1. Campaigns ---------------- */
  const CAMPAIGNS = [
    {
      id: 'CMP-2026-01', name: '2026 Incentive Trip — Kuala Lumpur',
      kind: 'Trip', target: 6000000, metric: 'Group sales value (RM)',
      window: '1 Jan 2026 – 31 Dec 2026', reward: '5D4N, 2 pax',
      audience: 'Whole agency', open: '2026-01-01', close: '2026-12-31'
    },
    {
      id: 'CMP-2026-02', name: '2026 Incentive Trip — Other Regions',
      kind: 'Trip', target: 6000000, metric: 'Group sales value (RM)',
      window: '1 Jan 2026 – 31 Dec 2026', reward: '4D3N, 2 pax',
      audience: 'Whole agency', open: '2026-01-01', close: '2026-12-31'
    },
    {
      id: 'CMP-2026-03', name: '2026 Dream Car Campaign',
      kind: 'Asset', target: 6000000, metric: 'Personal sales value (RM)',
      window: '1 Jan 2026 – 31 Dec 2026', reward: 'Car lease contribution',
      audience: 'Negotiator and above', open: '2026-01-01', close: '2026-12-31'
    },
    {
      id: 'CMP-2026-04', name: '2026 Home Bonus Campaign',
      kind: 'Cash', target: 12000000, metric: 'Personal sales value (RM)',
      window: '1 Jan 2026 – 31 Dec 2026', reward: 'Bonus on net fee',
      audience: 'Negotiator and above', open: '2026-01-01', close: '2026-12-31'
    },
    {
      id: 'CMP-2026-05', name: '2026 World Club Campaign',
      kind: 'Recognition', target: 12000000, metric: 'Personal sales value (RM)',
      window: '1 Jan 2026 – 31 Dec 2026', reward: 'Club status + gala seat',
      audience: 'Negotiator and above', open: '2026-01-01', close: '2026-12-31'
    },
    {
      id: 'CMP-2026-06', name: 'Project Launch Push — Q4 2026',
      kind: 'Cash', target: 3000000, metric: 'Booked project sales value (RM)',
      window: '1 Oct 2026 – 31 Dec 2026', reward: 'Extra 0.25% on booked units',
      audience: 'Whole agency', open: '2026-10-01', close: '2026-12-31'
    }
  ];

  /* ---------------- 2. Eligibility gate ----------------
     A participant can only be paid a campaign when all four are satisfied.
     Conditions carry an id so the UI can show exactly what is missing. */
  const CONDITIONS = [
    { id: 'C1', text: 'Valid REN/REA licence for the whole campaign period', hard: true },
    { id: 'C2', text: 'No open disciplinary case', hard: true },
    { id: 'C3', text: 'AMLA compliance training completed for the current year', hard: true },
    { id: 'C4', text: 'Minimum 6 months active service', hard: true }
  ];

  /* ---------------- 3. Participation (SAMPLE figures) ----------------
     agent_id is a stand-in seat code, not a real registration number.
     Names are reused from the names already used elsewhere in this mock-up so
     the same seat never shows two identities. */
  const SEATS = {
    'SEAT-01': 'Zahiruddin M.J.',
    'SEAT-02': 'Fadilah Yusof',
    'SEAT-03': 'Hafiz Rahman',
    'SEAT-04': 'Nurul Izzah binti Kamal',
    'SEAT-05': 'New agent seat',
    'SEAT-06': 'Aina Zulkifli'
  };
  function seatName(id) { return SEATS[id] || id; }

  /* sales value achieved inside each campaign window.
     Deliberately includes a seat that EXCEEDS its target while failing a
     compliance condition, so the gate (Held vs Qualified) is always visible. */
  const PROGRESS = [
    { campaign: 'CMP-2026-01', seat: 'SEAT-01', value: 4780000, units: 0 },
    { campaign: 'CMP-2026-01', seat: 'SEAT-02', value: 3120000, units: 0 },
    { campaign: 'CMP-2026-01', seat: 'SEAT-03', value: 5960000, units: 0 },
    { campaign: 'CMP-2026-01', seat: 'SEAT-04', value: 1240000, units: 0 },
    /* SEAT-02 clears the 6.0m target in campaign 2 but fails C3 (AMLA) */
    { campaign: 'CMP-2026-02', seat: 'SEAT-01', value: 4780000, units: 0 },
    { campaign: 'CMP-2026-02', seat: 'SEAT-02', value: 6240000, units: 0 },
    { campaign: 'CMP-2026-02', seat: 'SEAT-03', value: 5960000, units: 0 },
    /* SEAT-01 clears the 12.0m home-bonus target cleanly */
    { campaign: 'CMP-2026-04', seat: 'SEAT-01', value: 12350000, units: 0 },
    { campaign: 'CMP-2026-04', seat: 'SEAT-04', value: 1240000, units: 0 },
    /* SEAT-06 clears the 12.0m club target cleanly */
    { campaign: 'CMP-2026-05', seat: 'SEAT-01', value: 4780000, units: 0 },
    { campaign: 'CMP-2026-05', seat: 'SEAT-06', value: 12480000, units: 0 },
    /* campaign 6 counts booked units, not value — SEAT-05 fails C4 (service) */
    { campaign: 'CMP-2026-06', seat: 'SEAT-01', value: 1140000, units: 2 },
    { campaign: 'CMP-2026-06', seat: 'SEAT-02', value: 1710000, units: 3 },
    { campaign: 'CMP-2026-06', seat: 'SEAT-05', value: 2280000, units: 4 },
    { campaign: 'CMP-2026-06', seat: 'SEAT-06', value: 2280000, units: 4 }
  ];

  /* condition checks per seat */
  const COMPLIANCE = [
    { seat: 'SEAT-01', C1: true,  C2: true,  C3: true,  C4: true },
    { seat: 'SEAT-02', C1: true,  C2: true,  C3: false, C4: true },
    { seat: 'SEAT-03', C1: false, C2: true,  C3: true,  C4: true },
    { seat: 'SEAT-04', C1: true,  C2: false, C3: true,  C4: true },
    { seat: 'SEAT-05', C1: true,  C2: true,  C3: true,  C4: false },
    { seat: 'SEAT-06', C1: true,  C2: true,  C3: true,  C4: true }
  ];

  function campaign(id) {
    return CAMPAIGNS.filter(function (c) { return c.id === id; })[0] || null;
  }
  function participants(id) {
    return PROGRESS.filter(function (p) { return p.campaign === id; });
  }
  function compliance(seat) {
    return COMPLIANCE.filter(function (c) { return c.seat === seat; })[0] || null;
  }
  /* which conditions a seat still fails */
  function missing(seat) {
    const c = compliance(seat);
    if (!c) return [];
    return CONDITIONS.filter(function (k) { return !c[k.id]; })
                     .map(function (k) { return k.id; });
  }
  function qualifies(seat) { return missing(seat).length === 0; }

  /* progress of one seat in one campaign, as a percentage of target */
  function progress(campaignId, seat) {
    const c = campaign(campaignId);
    const p = PROGRESS.filter(function (x) {
      return x.campaign === campaignId && x.seat === seat; })[0];
    if (!c || !p) return 0;
    return Math.min(100, Math.round((p.value / c.target) * 1000) / 10);
  }

  /* 0 = nothing, 1 = target met, 2 = target met but held back (compliance) */
  function state(campaignId, seat) {
    const c = campaign(campaignId);
    const p = PROGRESS.filter(function (x) {
      return x.campaign === campaignId && x.seat === seat; })[0];
    if (!c || !p || p.value < c.target) return 0;
    return qualifies(seat) ? 1 : 2;
  }

  /* ranking of a whole campaign: qualifiers first, then by value */
  function board(campaignId) {
    return participants(campaignId)
      .map(function (p) {
        const c = campaign(campaignId);
        return {
          seat: p.seat, name: seatName(p.seat),
          value: p.value, units: p.units,
          pct: progress(campaignId, p.seat),
          state: state(campaignId, p.seat),
          missing: missing(p.seat),
          reward: c ? c.reward : ''
        };
      })
      .sort(function (a, b) {
        if (b.state !== a.state) return b.state - a.state;
        return b.value - a.value;
      });
  }

  /* agency-wide roll-up for the header cards */
  function summary() {
    const totalTarget = CAMPAIGNS.reduce(function (a, c) { return a + c.target; }, 0);
    const achieved = CAMPAIGNS.reduce(function (a, c) {
      return a + participants(c.id).reduce(function (x, p) { return x + p.value; }, 0);
    }, 0);
    let qualified = 0, held = 0;
    const seen = {};
    CAMPAIGNS.forEach(function (c) {
      participants(c.id).forEach(function (p) {
        const s = state(c.id, p.seat);
        if (s === 1) qualified++;
        if (s === 2) held++;
        seen[p.seat] = 1;
      });
    });
    return {
      campaigns: CAMPAIGNS.length,
      seats: Object.keys(seen).length,
      target: totalTarget,
      achieved: achieved,
      qualified: qualified,
      held: held,
      pct: totalTarget ? Math.round((achieved / totalTarget) * 1000) / 10 : 0
    };
  }

  function money(n) {
    return 'RM ' + Number(n || 0).toLocaleString('en-US');
  }
  function millions(n) {
    return (Number(n || 0) / 1000000).toFixed(1) + 'm';
  }

  return {
    CAMPAIGNS: CAMPAIGNS, CONDITIONS: CONDITIONS, PROGRESS: PROGRESS,
    COMPLIANCE: COMPLIANCE, SEATS: SEATS, seatName: seatName,
    campaign: campaign, participants: participants, compliance: compliance,
    missing: missing, qualifies: qualifies, progress: progress,
    state: state, board: board, summary: summary,
    money: money, millions: millions
  };
})();
