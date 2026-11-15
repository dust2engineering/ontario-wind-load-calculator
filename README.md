# Ontario Wind Load Data Calculator (SB-1)

Hourly wind pressures q (1-in-10 and 1-in-50) for GTA and Ontario municipalities from OBC Supplementary Standard SB-1 Table 2, with a simplified velocity-pressure calculation using designer-supplied factors.

**Live web tool:** https://dust2engineering.github.io/ontario-wind-load-calculator/web/

## How it works

- Pick the municipality and return period; q is read from the SB-1 row (snow Ss/Sr from the same row shown for reference).
- Optionally multiply by your own Iw, Ce and Cg×Cp from OBC 4.1.7 for a simplified pressure p — the factors are inputs, not built-in design values.
- Toronto is four SB-1 district rows; Hamilton's q is one value across its four zones.

## Data in this repository

- `wind-data.json` — SB-1 Table 2 rows for 13 GTA/Ontario locations (Ss, Sr, q 1/10, q 1/50), transcribed from the 2024 Compendium SB-1 on ontario.ca, checked 2026-11-15.
- `wind_load.py` — command-line lookup using the same JSON.

## Command line

```bash
python3 wind_load.py "Toronto (City Hall)" 50 0.9 1.0 1.0
```

## Worked examples

- [toronto-1in50.md](examples/toronto-1in50.md)
- [barrie-vs-toronto.md](examples/barrie-vs-toronto.md)

## Scope and limits

Preliminary design aid only. It does not replace the current Ontario Building Code, the Canadian Electrical Code or CSA B149.1, or the judgement of the designer of record. Verify all values against the Code in force for your project before submitting drawings for permit.

## About

Maintained by **Dust 2 Engineering Inc.** (Mississauga, Ontario) — building permit drawings
(architectural, HVAC, plumbing, sprinkler, electrical) for restaurants and small commercial
projects across the Greater Toronto Area, stamped by an Ontario P.Eng. Flat rate $3,500–$5,000.

Category: Structural. More free Ontario code tools: see the full index at
https://github.com/dust2engineering
