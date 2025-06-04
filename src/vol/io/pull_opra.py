import pandas as pd
from pathlib import Path

def load_opra_csv(path: str) -> pd.DataFrame:
    """
    Minimal stub that loads an OPRA-format CSV from disk.
    For now, it calls pd.read_csv and returns the DataFrame.
    In future, replace or augment this to handle:
      - Column renaming (e.g., 'Strike' → 'strike')
      - Datetime parsing
      - Sorting/filtering
      - Corporate‐action adjustments
    """
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"No such file: {path}")
    return pd.read_csv(p)
