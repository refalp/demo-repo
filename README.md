# Demo

This repository provides a minimal skeleton for building a synthetic hedge on the Freightos Baltic Index (FBX) as described in the roadmap.

## Structure

```
fbx_hedge/
    config.py          # symbols and constants
    run_daily_etl.py   # placeholder nightly ETL
    utils.py           # helpers for loading and preparing data
    fit_model.py       # LassoCV model training
    size_positions.py  # compute contract quantities
    monitor.py         # simple monitoring loop
```

The scripts are intentionally lightweight and focus on illustrating the workflow, not production readiness.
