"""Simplified ETL for price data."""
import pandas as pd
from pathlib import Path
from .config import SYM

RAW_DATA_DIR = Path('data/raw')
RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)


def download(symbol_code):
    """Placeholder for data download."""
    # In production, call API or load file
    return pd.DataFrame()


def store_parquet(sym, df):
    """Store DataFrame to Parquet."""
    out = RAW_DATA_DIR / f"{sym}.parquet"
    df.to_parquet(out)


if __name__ == "__main__":
    for sym, code in SYM.items():
        raw = download(code)
        store_parquet(sym, raw)
