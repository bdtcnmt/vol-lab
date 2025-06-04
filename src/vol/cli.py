import sys
import argparse
import pandas as pd

from vol.io.pull_opra import load_opra_csv
from vol.models.svi import svi_total_variance
from vol.backtest.rv_engine import run_simple_backtest

def main():
    parser = argparse.ArgumentParser(
        description="vol-project demo: load CSV, compute dummy SVI, run backtest stub"
    )
    parser.add_argument(
        "--csv",
        type=str,
        required=True,
        help="Path to a sample OPRA-style CSV (strike,mid,iv columns)"
    )
    args = parser.parse_args()

    csv_path = args.csv
    print(f"Loading CSV from {csv_path} ...")
    try:
        df = load_opra_csv(csv_path)
    except FileNotFoundError as e:
        print(f"ERROR: {e}")
        sys.exit(1)

    nrows = len(df)
    print(f"✅ Loaded {nrows} row(s) from {csv_path}")

    # For now, just take the first row.
    row0 = df.iloc[0]
    k = float(row0["strike"])   # treat strike column as log-moneyness
    observed_iv = float(row0["iv"])

    # Use a dummy time‐to‐expiry t=0.10 (i.e. 0.10 years) and a={"a": observed_iv}
    t = 0.10
    params = {"a": observed_iv}
    total_var = svi_total_variance(k=k, t=t, params=params)
    print(f"Computed dummy SVI total variance = {total_var:.2f} for k={k:.2f}, t={t:.2f}, a={observed_iv:.2f}")

    # Now call the backtest stub
    result = run_simple_backtest()
    pnl = result.get("pnl", None)
    print(f"Backtest stub returned P&L = {pnl}")

    sys.exit(0)

if __name__ == "__main__":
    main()