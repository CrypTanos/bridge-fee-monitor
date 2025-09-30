import json
import pathlib
import random
import sys
from datetime import datetime, timezone

BRIDGES = ["Across", "Hop", "Meson", "Orbiter"]
ASSETS = ["USDC", "ETH"]
ROUTE = "Base→Ethereum L1"

def mock_fee_ppm():
    # "parts per million" (0.01% = 100 ppm). Просто плейсхолдери.
    return random.randint(30, 450)  # 0.003%..0.045% як приклад

def mock_eta_min():
    return random.randint(2, 25)

def build_snapshot():
    now = datetime.now(timezone.utc)
    payload = {
        "ts": now.isoformat(timespec="seconds"),
        "route": ROUTE,
        "bridges": {}
    }
    for b in BRIDGES:
        payload["bridges"][b] = {}
        for a in ASSETS:
            payload["bridges"][b][a] = {
                "fee_ppm": mock_fee_ppm(),      # плейсхолдер до реальних API
                "eta_min": mock_eta_min()
            }
    return payload

def write_snapshot(data):
    dt = datetime.now(timezone.utc)
    folder = pathlib.Path("data") / dt.strftime("%Y-%m-%d")
    folder.mkdir(parents=True, exist_ok=True)
    path = folder / f"{dt.strftime('%H%M%S')}.json"  # унікальне ім'я з секундами
    path.write_text(json.dumps(data, indent=2))
    return path

if __name__ == "__main__":
    out = write_snapshot(build_snapshot())
    print(f"[update.py] wrote file: {out}")
    sys.exit(0)
