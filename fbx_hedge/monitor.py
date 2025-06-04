"""Simple tracking error monitor."""
import json
import time

import pandas as pd


LIVE_ERROR_THRESHOLD = 0.02


def fetch_live_fbx_estimate():
    return 0.0


def fetch_live_futures_returns():
    return pd.Series()


if __name__ == "__main__":
    with open('latest_weights.json') as fh:
        weights = pd.Series(json.load(fh))

    while True:
        live_r_fbx = fetch_live_fbx_estimate()
        live_r_futs = fetch_live_futures_returns()
        synth_ret = (live_r_futs * weights).sum()
        error = live_r_fbx - synth_ret
        if abs(error) > LIVE_ERROR_THRESHOLD:
            print('Hedge offside – investigate')
        time.sleep(60)
