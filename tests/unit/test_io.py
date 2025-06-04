import pandas as pd
import pytest
from vol.io.pull_opra import load_opra_csv

def test_load_opra_csv_success(tmp_path):
    """
    Create a tiny CSV in a temporary directory and ensure
    load_opra_csv returns a DataFrame with correct shape.
    """
    # 1) Define CSV content with a header row and one data row.
    csv_content = "strike,mid,iv\n100,2.5,0.20\n"

    # 2) Write it to a file under tmp_path / "sample.csv"
    file_path = tmp_path / "sample.csv"
    file_path.write_text(csv_content)

    # 3) Call load_opra_csv on that path
    df = load_opra_csv(str(file_path))

    # 4) Assertions: It must be a DataFrame with exactly 1 row and 3 columns
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (1, 3)
    # Check column names match the header
    assert list(df.columns) == ["strike", "mid", "iv"]
    # Check the values were read correctly
    assert df.loc[0, "strike"] == 100
    assert abs(df.loc[0, "iv"] - 0.20) < 1e-8

def test_load_opra_csv_file_not_found():
    """
    If the path doesn’t exist, load_opra_csv should raise FileNotFoundError.
    """
    with pytest.raises(FileNotFoundError):
        load_opra_csv("/this/path/does/not/exist.csv")
