import pandas as pd
import numpy as np
from sklearn.linear_model import Lasso
from sklearn.model_selection import TimeSeriesSplit
from sklearn.metrics import mean_squared_error


def load_series(path):
    """Load a single time series CSV with columns Date, Price."""
    df = pd.read_csv(path, parse_dates=[0])
    df.columns = ['Date', 'Price']
    df = df.sort_values('Date')
    df.set_index('Date', inplace=True)
    return df


def compute_returns(df, freq='W'):
    """Resample to the given frequency and compute log returns."""
    resampled = df['Price'].resample(freq).last().ffill()
    returns = np.log(resampled).diff().dropna()
    return returns


def prepare_dataset(paths, freq='W'):
    """Load all series and assemble a DataFrame of returns."""
    series = {}
    for name, path in paths.items():
        df = load_series(path)
        series[name] = compute_returns(df, freq)
    data = pd.DataFrame(series).dropna()
    target = data.pop('FBX')
    return data, target


def fit_lasso(X, y, alpha=0.1):
    """Fit a Lasso regression with time-series cross validation."""
    tscv = TimeSeriesSplit(n_splits=5)
    best_model = None
    best_score = np.inf
    for train_idx, test_idx in tscv.split(X):
        model = Lasso(alpha=alpha)
        model.fit(X.iloc[train_idx], y.iloc[train_idx])
        preds = model.predict(X.iloc[test_idx])
        score = mean_squared_error(y.iloc[test_idx], preds)
        if score < best_score:
            best_score = score
            best_model = model
    return best_model


def main():
    paths = {
        'FBX': 'data/FBX.csv',
        'Brent': 'data/Brent.csv',
        'BDI': 'data/BDI.csv',
        'SP500': 'data/SP500.csv',
        'Copper': 'data/Copper.csv',
        'LSFO': 'data/LSFO.csv',
    }
    X, y = prepare_dataset(paths)
    model = fit_lasso(X, y)
    print('Hedge ratios:')
    for name, coef in zip(X.columns, model.coef_):
        print(f'{name}: {coef:.4f}')

if __name__ == '__main__':
    main()
