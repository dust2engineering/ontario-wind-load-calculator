#!/usr/bin/env python3
"""SB-1 wind climate data + simplified velocity pressure.
Usage: python3 wind_load.py "CITY" RETURN_PERIOD(10|50) [Ce] [CgCp] [Iw]
p = Iw x q x Ce x (CgCp). Lookup + arithmetic aid only — not a full
OBC 4.1.7 wind design. Cities: see wind-data.json.
"""
import json, os, sys

DATA = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "wind-data.json")))

def main():
    if len(sys.argv) < 3:
        print(__doc__); print("Cities:", ", ".join(DATA["cities"])); return
    city, rp = sys.argv[1], sys.argv[2]
    c = DATA["cities"][city]
    q = c["q_1in10_kPa"] if rp == "10" else c["q_1in50_kPa"]
    print(f"{city}: Ss {c['Ss_kPa']} kPa, Sr {c['Sr_kPa']} kPa, q(1/{rp}) = {q} kPa")
    if len(sys.argv) >= 6:
        ce, cgcp, iw = float(sys.argv[3]), float(sys.argv[4]), float(sys.argv[5])
        print(f"Simplified pressure p = {iw} x {q} x {ce} x {cgcp} = {iw * q * ce * cgcp:.3f} kPa")

if __name__ == "__main__":
    main()
