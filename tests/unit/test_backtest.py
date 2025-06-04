import pytest
from vol.backtest.rv_engine import run_simple_backtest

def test_run_simple_backtest_returns_dict_with_pnl():
    """
    run_simple_backtest() should return a dict containing the key "pnl"
    and its value should be a float (for now, 0.0).
    """
    result = run_simple_backtest()
    # 1) It must be a dictionary
    assert isinstance(result, dict)
    # 2) It must contain the "pnl" key
    assert "pnl" in result
    # 3) The value for "pnl" should be a float (we expect 0.0)
    assert isinstance(result["pnl"], float)
    assert result["pnl"] == 0.0

@pytest.mark.parametrize("override", [None, 5.0, -1.23])
def test_run_simple_backtest_always_returns_zero(override):
    """
    Even if someone mistakenly passes args (shouldn’t matter),
    run_simple_backtest still returns {"pnl": 0.0}.
    This tests that extra args don’t accidentally break it.
    """
    # The function signature doesn’t accept args, so override is unused.
    result = run_simple_backtest()
    assert result == {"pnl": 0.0}
