#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""fasa0_fix.py — Fasa 0: betulkan isu K1-K8 dalam mock-up Zentra Hub.
Setiap penggantian DISAHKAN (assert) — gagal keras jika teks tidak dijumpai."""
import io, os, sys

D = "/home/ubuntu/mockup-hartanah/agency-system"
log = []

def edit(fn, old, new, label):
    p = os.path.join(D, fn)
    s = io.open(p, encoding="utf-8").read()
    if old not in s:
        print("GAGAL: teks tidak dijumpai dalam %s [%s]" % (fn, label))
        print("  cari: %r" % old[:120])
        sys.exit(1)
    if s.count(old) != 1:
        print("GAGAL: teks tidak unik (%d kali) dalam %s [%s]" % (s.count(old), fn, label))
        sys.exit(1)
    s = s.replace(old, new)
    io.open(p, "w", encoding="utf-8").write(s)
    log.append((fn, label))
    print("OK  %-16s %s" % (fn, label))

# ---------------------------------------------------------------- K1: GL berasingan
edit("assets/levels.js",
     "window.ZTH_LEVEL_NOTE =",
     """/* GL — kod akaun mesti berasingan: komisen (dihadkan) vs ganjaran agensi. */
window.ZTH_GL = {commission:'602-100', marketingBonus:'602-150', leaderOverride:'602-200', agencyResidual:'602-900'};

/* Versi kadar (K8) — kadar dikunci pada versi yang berkuat kuasa semasa perjanjian ditandatangani. */
window.ZTH_RATE_VERSION = {v:'v1.0', effective:'2026-01-01'};

/* Peraturan keras (K4/K5/K6/K7) yang dibaca oleh semua skrin. */
window.ZTH_RULES = {
  referrerRecordOnly: true,
  overrideFollowsManagementUpline: true,
  externalReferrerNoPayout: true,
  maxOverrideLevels: 2,
  rounding: 'Setiap split dibundarkan ke sen; beza sen diserap oleh baki agensi supaya jumlah pemegang bayaran tepat.',
  dualRepresentation: 'Wakil dua pihak (pembeli & penjual) memerlukan kelulusan bertulis + persetujuan klien + split fi berasingan.',
  clawbackLedger: 'Clawback dibuka sebagai lejar berasingan per ejen; jika ejen keluar, baki clawback kekal sebagai hutang yang boleh ditolak daripada apa-apa bayaran kelak.'
};

window.ZTH_LEVEL_NOTE =""",
     "K1/K8 levels.js: GL + versi kadar + peraturan")

# K1 — claims.html: caption bercanggah ("one account code")
edit("claims.html",
     "Two documents, one account code, two names: only RM407.41 is declared as <b>commission</b>;",
     "Two documents, <b>two separate account codes</b>, two names: only RM407.41 is declared as <b>commission</b> (A/C 602-100);",
     "K1 claims.html: caption GL dibetulkan")

# K1 — index.html: ayat "Both post to the agency's marketing account code"
edit("index.html",
     "Both post to the agency's marketing account code.",
     "They post to <b>separate</b> account codes &mdash; the capped commission to 602-100, the Marketing Bonus to 602-150 &mdash; so a regulator can see which line was capped and which was funded by the agency.",
     "K1 index.html: ayat kod akaun")

# K1 — team.html: "same account code as the commission voucher"
edit("team.html",
     "Override comes out of the <b>agency share</b> and is labeled <b>Marketing Bonus</b> (same account code as the commission voucher).",
     "Override comes out of the <b>agency share</b>, is labeled <b>Marketing Bonus</b>, and posts to its <b>own</b> account code (602-150) &mdash; never merged into the declared commission line (602-100).",
     "K1 team.html: kod akaun override")

# ---------------------------------------------------------------- K7: pembundaran (jumlah mesti tepat)
edit("index.html", "Marketing Bonus (leader) &mdash; RM152.79", "Marketing Bonus (leader) &mdash; RM152.78",
     "K7 index.html: RM152.79 -> 152.78 (sen)")
edit("index.html",
     '<tr><td>Marketing Bonus — leader override</td><td class="num">RM152.79</td><td class="num">15.0%</td></tr>',
     '<tr><td>Marketing Bonus — leader override</td><td class="num">RM152.78</td><td class="num">15.0%</td></tr>\n          <tr class="total"><td>Reconciles to the professional fee</td><td class="num">RM1,018.52</td><td class="num">100.0%</td></tr>',
     "K7 index.html: jumlah rekonsiliasi 100%")
edit("index.html",
     '<p class="small muted" style="margin-bottom:0">Two separate documents are produced: the <b>commission voucher</b> (never above 40%) and the <b>Marketing Bonus voucher</b>.',
     '<p class="small muted" style="margin:0">Rounding: RM407.41 + RM458.33 + RM152.78 = <b>RM1,018.52 exactly</b>. Any odd sen is absorbed by the agency residual, never silently folded into a payee line.</p>\n        <p class="small muted" style="margin-bottom:0">Two separate documents are produced: the <b>commission voucher</b> (never above 40%) and the <b>Marketing Bonus voucher</b>.',
     "K7 index.html: nota pembundaran")

# ---------------------------------------------------------------- K4: referrer vs upline pengurusan
edit("team.html",
     '<span class="num">1</span> Referral chain (upline → downline)',
     '<span class="num">1</span> Management upline (who supervises whom) — referral record shown separately',
     "K4 team.html: tajuk rantai")
edit("team.html",
     '<span class="tag ref">referrer: Hamdan Hussin (external)</span>',
     '<span class="tag ref">introduced by: Hamdan Hussin (external) &middot; record only, not a payee &middot; no REN/PEA &rarr; RM0 override</span>',
     "K4 team.html: referrer luar = rekod sahaja")
edit("team.html",
     "Her referrer chain: Faizal Omar (L4 · 75%) → Nadia Rahman (L6 · 90%, override capped at 10%).",
     "The chain that pays is her <b>management upline</b> (who supervises her, not who introduced her): Faizal Omar (L4 · 75%) &rarr; Nadia Rahman (L6 · 90%, override capped at 10%). A referrer who is not her leader is kept as a record and is paid <b>RM0</b>.",
     "K4 team.html: contoh guna upline")
edit("team.html",
     "<li><b>Cap + clawback:</b>",
     "<li><b>Referrer ≠ leader:</b> the referral record (who introduced whom) carries <b>no payment right</b>. Override runs on the management upline only, and only to registered, active agents (Act 242).</li>\n          <li><b>Rate versioning:</b> rates are locked to the version in force when the agreement was signed (v1.0, effective 01 Jan 2026). A ladder change applies to new agreements only &mdash; it never rewrites what an existing agent already signed.</li>\n          <li><b>Cap + clawback:</b>",
     "K4/K8 team.html: peraturan referrer + versi kadar")

# K2: tahap kelayakan team.html tidak padan levels.js/hierarchy.html
edit("team.html",
     "Levels are earned on <b>production</b>: L1 RM100k · L2 RM250k · L3 RM500k · L4 RM1.5m · L5 RM2.5m · L6 RM3.5m (closed gross sales, rolling 12 months).",
     "Levels are earned on <b>production</b> (closed production, rolling 12 months) — exactly as in the ladder: L1 REN tag + onboarding &middot; L2 RM600k &middot; L3 RM1.5m &middot; L4 RM2.5m + 2 mentored agents &middot; L5 RM3.5m + 3 producing agents &middot; L6 RM6m + 2 team leaders.",
     "K2 team.html: tahap kelayakan padan levels.js")

# K4: index.html kad & tree
edit("index.html",
     "The referrer chain the override engine walks — personal vs group sales.",
     "The management upline the override engine walks — personal vs group sales. (The referral record is kept separately and carries no payment right.)",
     "K4 index.html: kad team")
edit("index.html",
     "The referrer chain the reward engine walks — sorted by chain or by production.",
     "The management upline the reward engine walks — sorted by chain or by production.",
     "K4 index.html: kad tree")

# K4: modules.html
edit("modules.html",
     "Team &amp; referrers page + override engine walks the chain",
     "Team page (management upline) + override engine walks the upline chain",
     "K4 modules.html: baris My Team")
edit("modules.html", "<li>Referrer tree + titles</li>", "<li>Upline tree + titles (referral record kept separate)</li>",
     "K4 modules.html: senarai ciri")

# K4: f4.html
edit("f4.html",
     "Group sales include the agents below them (referrer chain). Documents and commission follow the same chain &mdash; one payout point, the agency.",
     "Group sales include the agents below them on the <b>management upline</b> (the only chain that pays). Documents and commission follow the same chain &mdash; one payout point, the agency. The referral record (who introduced whom) is stored separately and gives no payment right.",
     "K4 f4.html: nota rantai")
edit("f4.html", "'6 agents &middot; total sales value (referrer chain)'",
     "'6 agents &middot; total sales value (management upline)'", "K4 f4.html: label KPI")

# K4: tree.html
edit("tree.html", '<button class="btn ghost" id="modeRef">Referrer chain</button>',
     '<button class="btn ghost" id="modeRef">Management upline</button>', "K4 tree.html: label butang")
edit("tree.html",
     "<span class=\"small muted\" id=\"modeNote\" style=\"margin-left:auto\">Viewing: referrer chain (who introduced whom)</span>",
     "<span class=\"small muted\" id=\"modeNote\" style=\"margin-left:auto\">Viewing: management upline (who supervises whom — the only chain that pays)</span>",
     "K4 tree.html: nota mod")
edit("tree.html", ": 'Viewing: referrer chain (who introduced whom)';",
     ": 'Viewing: management upline (who supervises whom — the only chain that pays)';", "K4 tree.html: nota mod (JS)")
edit("tree.html", "${x.ref?` &nbsp;·&nbsp; introduced by ${byId(x.ref).name.split(' ')[0]}`:' &nbsp;·&nbsp; agency owner'}",
     "${x.ref?` &nbsp;·&nbsp; upline: ${byId(x.ref).name.split(' ')[0]}`:' &nbsp;·&nbsp; agency owner'}",
     "K4 tree.html: label upline pada nod")
edit("tree.html", "const N = [\n",
     "/* ref = management upline (who supervises). The referral record (who introduced) is a\n   separate field: it carries NO payment right and never walks the override engine. */\nconst N = [\n",
     "K4 tree.html: komen model data")
edit("tree.html",
     "<li><span class=\"ok\">&#10003;</span><div><b>Rank is production-based.</b>",
     "<li><span class=\"ok\">&#10003;</span><div><b>Referrer &ne; leader.</b> Whoever introduced an agent is a record, not a payee. Override follows the management upline only.</div></li>\n          <li><span class=\"ok\">&#10003;</span><div><b>Rank is production-based.</b>",
     "K4 tree.html: baris merah referrer")
edit("tree.html",
     "<h2 class=\"sec\"><span class=\"num\">2</span> How a completed sale walks the chain</h2>",
     """<div class="card" style="margin-top:14px">
      <div class="h3" style="margin:0 0 6px">Referral record &mdash; kept, but never paid</div>
      <table class="tbl">
        <tr><th>Person</th><th>Introduced by</th><th>Registration</th><th class="num">Override rights</th></tr>
        <tr><td>Zahiruddin bin Mat Jailaini <span class="small muted">(Agency Head)</span></td><td>Hamdan Hussin <span class="small muted">(external)</span></td><td><span class="pill red">no REN/PEA</span></td><td class="num">RM0 &mdash; record only</td></tr>
      </table>
      <p class="small muted" style="margin:10px 0 0">This is the case that decides whether the whole structure is safe: a founder introduced by an unregistered outsider. The introduction stays on file; the engine pays nothing to it, because <b>Act 242</b> allows fee sharing only with registered agents.</p>
    </div>

    <h2 class="sec"><span class="num">2</span> How a completed sale walks the chain</h2>""",
     "K4 tree.html: kad rekod referrer")
edit("tree.html",
     "<tr><td>Team leader</td><td>the leader who trained and supervises</td><td class=\"num\">14.5&ndash;15% from the agency share</td></tr>",
     "<tr><td>Team leader</td><td>the leader who supervises (management upline)</td><td class=\"num\">15% of team fees from the agency share &middot; L6 cap 10%</td></tr>",
     "K3/K4 tree.html: lajur leader")

# ---------------------------------------------------------------- K8: nota versi kadar (hierarchy)
edit("hierarchy.html",
     "Leader override is drawn from the <b>agency share</b> and paid as Marketing Bonus. An agent can never be paid more than their level, and the agency never pays more than 100% of a professional fee.",
     "Leader override is drawn from the <b>agency share</b> and paid as Marketing Bonus (A/C 602-150 for the agent's reward, 602-200 for the leader's override &mdash; never merged with the declared commission 602-100). An agent can never be paid more than their level, and the agency never pays more than 100% of a professional fee.<br><b>Rate versioning:</b> this ladder is <b>v1.0, effective 01 Jan 2026</b>. An agent keeps the rates in force when their agreement was signed; a ladder change applies to new agreements only. Every change is versioned with a date and written to the audit log.",
     "K8 hierarchy.html: versi kadar + GL")

# ---------------------------------------------------------------- K6: lejar clawback ejen keluar
edit("payouts.html",
     "<p class=\"foot-note\">Zentra Hub prototype &middot; Payout runs",
     """<div class="card" style="margin-top:14px">
      <div class="h3" style="margin:0 0 6px">Open clawback ledger (including departed agents)</div>
      <table class="tbl">
        <tr><th>Agent</th><th>Status</th><th>Deal</th><th class="num">Clawback (RM)</th><th>Recovery route</th></tr>
        <tr><td>Ameer Haziq <span class="small muted">(AG-004)</span></td><td><span class="pill warn">resigned</span></td><td class="mono">DS-LOCR-160437</td><td class="num">458.33</td><td>Held against final voucher; balance becomes a recorded debt owed to the agency</td></tr>
        <tr><td>J. Lim <span class="small muted">(AG-005)</span></td><td><span class="pill amber">payout hold</span></td><td class="mono">DS-LOCS-161250</td><td class="num">1,200.00</td><td>Deducted from the next run once the release gate clears</td></tr>
      </table>
      <p class="small muted" style="margin:10px 0 0">A clawback never disappears because an agent leaves. It moves to a separate ledger, stays tied to the transaction that caused it, and follows the agent until it is settled &mdash; that record is what makes the payout numbers defensible.</p>
    </div>

    <p class="foot-note">Zentra Hub prototype &middot; Payout runs""",
     "K6 payouts.html: lejar clawback")

# ---------------------------------------------------------------- K5: wakil dua pihak
edit("compliance.html",
     '<option value="recruit">Add a reward for recruiting an agent</option>',
     '<option value="recruit">Add a reward for recruiting an agent</option>\n        <option value="extref">Pay an override to an external introducer (no REN/PEA)</option>\n        <option value="dualrep">Let one negotiator represent buyer and seller on the same deal</option>',
     "K5 compliance.html: pilihan baharu")
edit("compliance.html",
     "    recruit:['BLOCKED',",
     """    extref:['BLOCKED','The introducer holds no REN/PEA registration and is not part of the management upline. <b>Act 242</b> allows a professional fee to be shared only with a registered estate agent or negotiator, so the engine pays RM0 here. The introduction stays on file as a record — that is the difference between an agency and a recruitment scheme.'],
    dualrep:['CONDITIONAL','Two-side representation is not refused outright, but it is never silent: it needs written pre-approval by the agency head, client consent recorded on both letters, and a separately agreed fee split. Without that approval the engine refuses to pay one negotiator both sides of the same deal.'],
    recruit:['BLOCKED',""",
     "K5 compliance.html: peraturan extref + dualrep")

# K7 — nota pembundaran pada enjin (agency.js)
edit("assets/agency.js",
     "    /* payout schedule */",
     """    /* rounding note (K7): payee lines are exact to the sen; odd sen goes to the agency residual */
    (function () {
      var sum = r.comm + r.mbAgent + r.leaderAmt + r.agencyResidual;
      var el = document.getElementById("roundNote");
      if (el) el.textContent = "Reconciles: " + money(r.comm) + " + " + money(r.mbAgent) + " + " + money(r.leaderAmt) +
        " + " + money(r.agencyResidual) + " = " + money(sum) + " (fee " + money(r.fee) + ")";
    })();

    /* payout schedule */""",
     "K7 agency.js: nota rekonsiliasi")
edit("commission.html",
     '<h2 class="sec"><span class="num">2</span> Engine checks</h2>',
     '<p class="small mono" id="roundNote" style="margin:8px 0 0">&mdash;</p>\n\n    <h2 class="sec"><span class="num">2</span> Engine checks</h2>',
     "K7 commission.html: elemen roundNote")

print("\n%d pembetulan selesai." % len(log))
