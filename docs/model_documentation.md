# Model Documentation – Historical VaR (99%)

## 1. Model Purpose & Scope

This model estimates the 1-day Value-at-Risk (VaR) at the 99% confidence level for a synthetic trading portfolio.  
It is used purely for educational and prototyping purposes to demonstrate:

- Daily VaR estimation using historical simulation
- Regulatory-style backtesting based on exceptions
- High-level Basel traffic-light style classification

## 2. Input Data

- **Data type:** Daily PnL or simple returns
- **File format:** CSV with columns `date` (YYYY-MM-DD) and `return`
- **Frequency:** Business days
- **Data source:** Synthetic data generated for this project

The model assumes the input data has already been cleaned for missing values and obvious outliers.

## 3. Methodology

### 3.1 VaR Definition

For a given confidence level α (here 99%), the 1-day VaR is defined as the loss threshold that will not be exceeded with probability α under normal market conditions.

Mathematically, VaR is the negative of the (1 − α) quantile of the return distribution:

\[
\text{VaR}_{\alpha} = - Q_{1-\alpha}(\text{returns})
\]

### 3.2 Historical Simulation

1. Take a rolling window of the last _N_ trading days (default: 250).
2. Compute the empirical (1 − α) quantile of these returns.
3. Multiply by −1 to express the result as a loss threshold.
4. Shift the estimate forward by one day to obtain a 1-day-ahead VaR forecast.

### 3.3 Backtesting

For each day where a VaR estimate is available:

- Compare the **actual return** with **−VaR**.
- An **exception** (or violation) occurs when:

\[
\text{return}_t < -\text{VaR}_t
\]

The backtest records:

- Total number of exceptions
- Exception indicator series (0/1)

### 3.4 Kupiec Proportion-of-Failures (POF) Test

The Kupiec POF test checks whether the observed exception frequency is consistent with the expected frequency (1 − α).

- Null hypothesis: The model has the correct unconditional coverage.
- Test statistic: Likelihood ratio based on a binomial model.
- Higher values of the LR statistic indicate worse fit.

This implementation reports the LR statistic only (no p-value), as the project is intended as a lightweight prototype.

### 3.5 Basel Traffic-Light Classification (Simplified)

Based on the number of exceptions over ~250 observations:

- **Green:** 0–4 exceptions  
- **Yellow:** 5–9 exceptions  
- **Red:** 10+ exceptions  

This mapping is inspired by the Basel framework but simplified for demonstration.

## 4. Outputs

The engine produces:

1. **Time series plot** of daily returns vs 99% historical VaR.  
2. **Exception count** and **Kupiec LR statistic**.  
3. A markdown **Basel-style backtesting report** saved as:

`reports/basel_backtest_report.md`

The report includes confidence level, number of exceptions, LR statistic, and the traffic-light category.

## 5. Model Monitoring & Governance

Although this is a small prototype, the following governance concepts are illustrated:

- Clear definition of model purpose and assumptions
- Transparent input data specification
- Reproducible backtesting logic
- Simple traffic-light style performance categorisation
- Generated documentation and reports for review

## 6. Limitations

- Single portfolio, single risk factor, synthetic data only
- Only historical simulation VaR is implemented in the demo
- No explicit modelling of fat tails, volatility clustering, or liquidity effects
- Kupiec test is implemented without full p-value reporting
- This code is **not** intended for production use in any financial institution

## 7. Disclaimer

This project is an educational prototype created to demonstrate core ideas in traded-risk model development, backtesting, and documentation.  
It must **not** be used directly for production risk management, regulatory reporting, or trading decisions.
