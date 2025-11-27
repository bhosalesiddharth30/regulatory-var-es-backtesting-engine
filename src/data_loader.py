import pandas as pd


def load_returns_csv(path: str) -> pd.Series:
    """
    Loads 'date,return' CSV and returns daily returns as a Series.
    """
    df = pd.read_csv(path, parse_dates=["date"])
    df = df.set_index("date").sort_index()
    return df["return"]
