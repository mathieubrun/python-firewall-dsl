from dataclasses import asdict
from glob import glob
from importlib import import_module
from pathlib import Path

import shared.firewalls

for f in glob("./**/rules.py", recursive=True):
    parts = list(Path(f).parts)
    parts[-1] = parts[-1].strip(".py")
    import_module(".".join(parts))

for fw in shared.firewalls.fw:
    print(f"---- rules for {fw.name} ----")
    for r in fw.rules:
        print(f"rule {r.name}")
        print("  sources")
        for s in r.sources:
            print(f"  - {s}")
        print("  destinations")
        for d in r.destinations:
            print(f"  - {d}")
        print("  services")
        for s in r.services:
            print(f"  - {s}")
    print(f"dependencies :")
    for d in fw.dependencies():
        print(f"- {str(d)}")