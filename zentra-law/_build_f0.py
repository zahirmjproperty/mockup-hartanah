#!/usr/bin/env python3
"""_build_f0.py — bina semua halaman HTML Zentra Law F0 (mock-up boleh klik).
Jalankan:  cd /home/ubuntu/mockup-hartanah/zentra-law && python3 _build_f0.py
Sumber halaman hidup dalam _f0_a.py / _f0_b.py / _f0_c.py / _f0_d.py (satu sumber kebenaran).
"""
import os, re, sys
from _f0_common import SHELL, top
from _f0_a import PAGES_A, rows_matters, rows_checklist, MATTERS
from _f0_b import PAGES_B, rows_docs
from _f0_c import PAGES_C
from _f0_d import PAGES_D, board_html, rows_stages, rows_versions, rows_nego, rows_sla, rows_instr, rows_playbook
from _f0_e import PAGES_E, rows_tlib, rows_fields, rows_clauses, rows_redline

OUT = os.path.dirname(os.path.abspath(__file__))

SUB = {
    "index.html": "A law firm's day in one screen: files in flight, dates that cannot slip, money held for clients, and bills to raise.",
    "matters.html": "Every file the firm is carrying, with its stage, its lawyer and how far it has run.",
    "matter.html": "One conveyancing file, from the first search to the last stamped instrument.",
    "checklist.html": "What a file needs, who owes it, and what may never be signed electronically.",
    "documents.html": "Precedents, generated documents, and the correct signing method for each one.",
    "drafting.html": "Fourteen stages from instruction to stamped agreement, with the version trail, the negotiation log and the client's instructions.",
    "generator.html": "Pick an approved template, let the matter fill the form, let the rules block what is wrong, and generate a draft that nobody may release without a partner.",
    "signing.html": "Signing sessions in wet ink, and the envelopes that can be signed electronically.",
    "deadlines.html": "The 3+1 month clock, stamping within 30 days, CKHT within 60 days, and state consent.",
    "fees.html": "Scale fees under the Solicitors' Remuneration Order 2023, stamp duty bands, and the 25% ceiling.",
    "billing.html": "One bill that carries the scale fee, the disbursements, the tax and the e-invoice status.",
    "client-account.html": "The ledger, the reconciliation and the pack the firm's accountant signs.",
    "portal.html": "What the client sees: where the file is, what to sign, what to pay.",
    "admin.html": "Users, roles, the subscription, data residency, and the AI switch.",
    "compliance.html": "No referral payments, a discount and waiver log, publicity approvals, and the checks the law requires.",
    "audit.html": "An append-only record of who did what, sealed so a gap shows.",
    "roadmap.html": "Conveyancing first, then four more practice areas on the same core.",
    "guide.html": "Eighteen screens, ten questions, four product decisions.",
}
TITLE = {
    "index.html": "Overview", "matters.html": "Matters", "matter.html": "Matter detail",
    "checklist.html": "Document checklist", "documents.html": "Documents and signing",
    "drafting.html": "Drafting and vetting", "generator.html": "Agreement generator",
    "signing.html": "Signing room", "deadlines.html": "Statutory clock", "fees.html": "Fee engine",
    "billing.html": "Billing", "client-account.html": "Client account", "portal.html": "Client portal",
    "admin.html": "Firm admin", "compliance.html": "Compliance guard", "audit.html": "Audit trail",
    "roadmap.html": "Roadmap", "guide.html": "Review guide",
}

TOKENS = {
    "@@MATTER_ROWS@@": rows_matters,
    "@@CHECKLIST_ROWS@@": rows_checklist,
    "@@DOC_ROWS@@": rows_docs,
    "@@BOARD@@": board_html,
    "@@STAGE_ROWS@@": rows_stages,
    "@@VERSION_ROWS@@": rows_versions,
    "@@NEGO_ROWS@@": rows_nego,
    "@@SLA_ROWS@@": rows_sla,
    "@@INSTR_ROWS@@": rows_instr,
    "@@PLAYBOOK_ROWS@@": rows_playbook,
    "@@TLIB_ROWS@@": rows_tlib,
    "@@FIELD_ROWS@@": rows_fields,
    "@@CLAUSE_ROWS@@": rows_clauses,
    "@@REDLINE_ROWS@@": rows_redline,
}

def render(page):
    f = page["f"]
    body = page["body"]
    body = body.replace("@@TOP@@", top(TITLE[f], SUB[f]))
    for token, fn in TOKENS.items():
        if token in body:
            body = body.replace(token, fn())
    left = re.findall(r"@@[A-Z_]+@@", body)
    if left:
        raise SystemExit("Token belum diganti pada " + f + ": " + ", ".join(sorted(set(left))))
    return SHELL.format(title=TITLE[f], page=f.replace(".html", ""), body=body)

def main():
    pages = PAGES_A + PAGES_B + PAGES_C + PAGES_D + PAGES_E
    seen = set()
    for p in pages:
        if p["f"] in seen:
            raise SystemExit("Halaman bertindih: " + p["f"])
        seen.add(p["f"])
    total = 0
    for p in pages:
        html = render(p)
        path = os.path.join(OUT, p["f"])
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(html)
        total += len(html)
        print("  %-22s %6d bytes" % (p["f"], len(html)))
    print("HALAMAN: %d | JUMLAH: %d bytes" % (len(pages), total))
    missing = [k for k in SUB if k not in seen]
    if missing:
        print("AMARAN halaman dirancang belum wujud:", missing)

if __name__ == "__main__":
    main()
