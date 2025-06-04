import pytest
from vol.cli import main

def test_main_requires_csv_arg(capsys):
    """
    Calling main() without --csv should exit with code 2
    and print an error about the missing --csv argument.
    """
    with pytest.raises(SystemExit) as exc:
        main()

    # argparse uses exit code 2 for “missing required arguments”
    assert exc.value.code == 2

    # Check stderr for the “the following arguments are required: --csv” message
    captured = capsys.readouterr()
    assert "the following arguments are required: --csv" in captured.err