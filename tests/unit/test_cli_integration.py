import sys
import pandas as pd
import pytest
from pathlib import Path
from vol.cli import main

def test_cli_flow(tmp_path, capsys):
    """
    1) Write a tiny CSV under tmp_path
    2) Call main() with ['--csv', <path_to_csv>]
    3) Capture output and assert that key strings appear
    """
    # 1) Write sample CSV
    csv_content = "strike,mid,iv\n0.00,2.5,0.20\n"
    csv_file = tmp_path / "test.csv"
    csv_file.write_text(csv_content)

    # 2) Temporarily override sys.argv
    sys_argv_backup = sys.argv[:]
    sys.argv = ["vol-cli", "--csv", str(csv_file)]

    # 3) Run main()
    try:
        with pytest.raises(SystemExit) as e_info:
            main()   # main() will call sys.exit(0)
        assert e_info.value.code == 0
    finally:
        sys.argv = sys_argv_backup

    # 4) Capture stdout
    captured = capsys.readouterr().out
    assert "Loading CSV from" in captured
    assert "✅ Loaded 1 row" in captured
    assert "Computed dummy SVI total variance" in captured
    assert "Backtest stub returned P&L = 0.0" in captured