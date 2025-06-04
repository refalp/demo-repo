"""Utility helpers."""
import pandas as pd
from pathlib import Path
from .config import SYM

RAW_DATA_DIR = Path('data/raw')


def load_returns():
    frames = {}
    for sym in SYM:
        f = RAW_DATA_DIR / f"{sym}.parquet"
        if f.exists():
            df = pd.read_parquet(f)
            frames[sym] = df['close'].pct_change().rename(sym)
    return pd.concat(frames.values(), axis=1)


def make_design_matrix(data):
    target = data['FBX']
    features = data.drop(columns=['FBX'])
    return features.fillna(0), target.fillna(0)
