import numpy as np
import pandas as pd
from scipy.stats import norm


def historical_var(returns: pd.Series, alpha: float = 0.99) -> float:
    """
    Historical simulation VaR.
    VaR is defined as the negative quantile at (1 - alpha).
    """
    return -np.quantile(returns, 1 - alpha)


def variance_covariance_var(returns: pd.Series, alpha: float = 0.99) -> float:
    """
    Parametric VaR using the variance-covariance (normal) method.
    VaR = -(μ + z * σ)
    """
    mu = returns.mean()
    sigma = returns.std(ddof=1)
    z = norm.ppf(alpha)
    return -(mu + z * sigma)


def monte_carlo_var(returns: pd.Series, alpha: float = 0.99, n_sims: int = 10000) -> float:
    """
    Monte Carlo VaR assuming normally-distributed returns.
    """
    mu = returns.mean()
    sigma = returns.std(ddof=1)
    sims = np.random.normal(mu, sigma, n_sims)
    return -np.quantile(sims, 1 - alpha)
