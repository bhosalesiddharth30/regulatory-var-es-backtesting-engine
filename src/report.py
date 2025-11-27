import os


def generate_text_report(model_name: str,
                         alpha: float,
                         num_exceptions: int,
                         kupiec_lr: float,
                         traffic_light: str,
                         output_path: str = "reports/basel_backtest_report.md"):
    """
    Creates a Basel-style markdown risk report.
    """

    os.makedirs("reports", exist_ok=True)

    content = f"""# Basel Backtesting Report – {model_name}

**Confidence Level:** {alpha:.2%}  
**Number of Exceptions:** {num_exceptions}  
**Kupiec LR Statistic:** {kupiec_lr:.4f}  
**Basel Traffic-Light Category:** **{traffic_light}**

---

## Interpretation

- The Basel traffic-light classification provides a high-level indication of model quality.
- **Green** = acceptable VaR calibration  
- **Yellow** = model may require closer monitoring  
- **Red** = potentially underestimates risk  
- Kupiec test evaluates whether exception frequency matches expected levels.
"""

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)
