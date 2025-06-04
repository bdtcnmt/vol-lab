import pytest
from vol.models.svi import svi_total_variance

def test_svi_total_variance_base_case():
    """
    If params={"a": 0.1}, k=0.0, t=any value, then svi_total_variance should return 0.1.
    """
    result = svi_total_variance(k=0.0, t=0.5, params={"a": 0.1})
    assert abs(result - 0.1) < 1e-8

def test_svi_total_variance_with_k_squared():
    """
    If params={"a": 0.0}, k=2.0, then result should be 2^2 = 4.0.
    """
    result = svi_total_variance(k=2.0, t=1.0, params={"a": 0.0})
    assert abs(result - 4.0) < 1e-8

def test_svi_total_variance_missing_key_defaults_zero():
    """
    If params does not contain "a", default to a=0.0. For k=1.5, result=1.5^2=2.25.
    """
    result = svi_total_variance(k=1.5, t=0.2, params={})
    assert abs(result - 2.25) < 1e-8

@pytest.mark.parametrize("k,t,params,expected", [
    (0.0, 0.0, {"a": 0.2}, 0.2),
    (1.0, 0.5, {"a": 0.3}, 1.0 + 0.3),
    (-1.0, 0.1, {"a": 0.5}, 1.0 + 0.5),
])
def test_svi_parametrized(k, t, params, expected):
    assert abs(svi_total_variance(k=k, t=t, params=params) - expected) < 1e-8