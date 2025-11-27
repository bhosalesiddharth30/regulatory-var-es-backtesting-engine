import numpy as np
import pandas as pd
from scipy.stats import chi2


def generate_var_series(returns: pd.Series, alpha: float, var_fn, window: int = 250, **kwargs):
    """
    Rolls a 1-day-ahead VaR estimate using a sliding window.
    """
    var_values = []
    dates = []

    for i in range(window, len(returns)):
        window_data = returns.iloc[i-window:i]
        var_t = var_fn(window_data, alpha=alpha, **kwargs)
        var_values.append(var_t)
        dates.append(returns.index[i])

    return pd.Series(var_values, index=dates)


def count_exceptions(returns: pd.Series, var_series: pd.Series):
    """
    Exception = return < -VaR
    (Since VaR is a loss threshold)
    """
    aligned_returns = returns.loc[var_series.index]
    exceptions = (aligned_returns < -var_series).astype(int)
    return exceptions.sum(), exceptions


def kupiec_pof_test(exceptions: pd.Series, alpha: float):
    """
    Kupiec Proportion of Failures (POF) test.
    Tests if exception rate matches expected rate (1 - alpha).
    """
    n = len(exceptions)
    x = exceptions.sum()

    # Expected exception probability = 1 - alpha
    p0 = 1 - alpha
    phat = x / n if n > 0 else 0

    if phat == 0 or phat == 1:
        return 0.0  # edge case: LR goes to zero

    lr_stat = -2 * (
        (n - x) * np.log((1 - p0) / (1 - phat)) +
        x * np.log(p0 / phat)
    )
    return lr_stat


def basel_traffic_light(num_exceptions: int):
    """
    Simplified Basel Traffic-Light Zones
    Green: 0–4
    Yellow: 5–9
    Red: 10+
    """
    if num_exceptions <= 4:
        return "Green"
    elif num_exceptions <= 9:
        return "Yellow"
    else:
        return "Red"
