"""Train lasso model on returns."""
import json
import pandas as pd
from sklearn.linear_model import LassoCV
from sklearn.model_selection import TimeSeriesSplit
from .utils import load_returns, make_design_matrix


if __name__ == "__main__":
    data = load_returns()
    features, target = make_design_matrix(data)
    split = TimeSeriesSplit(n_splits=5)
    model = LassoCV(cv=split, alphas=[0.0001, 0.001, 0.01, 0.1, 1], max_iter=10000)
    model.fit(features, target)
    weights = pd.Series(model.coef_, index=features.columns)
    with open('latest_weights.json', 'w') as fh:
        json.dump(weights.to_dict(), fh, indent=2)
