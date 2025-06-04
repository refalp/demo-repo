"""Calculate futures positions from model weights."""
import json
import pandas as pd
from .config import CONTRACT_MULTIPLIER


EXPOSURE_PER_FEU = 5000  # USD value of 1 FEU


if __name__ == "__main__":
    with open('latest_weights.json') as fh:
        weights = pd.Series(json.load(fh))

    contracts = {}
    for sym, w in weights.items():
        multiplier = CONTRACT_MULTIPLIER.get(sym, 1)
        contracts[sym] = round(w * EXPOSURE_PER_FEU / multiplier, 2)

    print("Contract sizes:", contracts)
