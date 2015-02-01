"""Tests for being able to generate weird and wonderful floating point
numbers."""

from hypothesis import given, assume
from tests.common.utils import fails
import math


@fails
@given(float)
def test_inversion_is_imperfect(x):
    assume(x != 0.0)
    y = 1.0 / x
    assert x * y == 1.0


@given(float)
def test_negation_is_self_inverse(x):
    assume(not math.isnan(x))
    y = -x
    assert -y == x


@fails
@given(float)
def test_is_not_nan(x):
    assert not math.isnan(x)


@fails
@given(float)
def test_is_not_positive_infinite(x):
    assume(x > 0)
    assert not math.isinf(x)


@fails
@given(float)
def test_is_not_negative_infinite(x):
    assume(x < 0)
    assert not math.isinf(x)


@fails
@given(float)
def test_is_int(x):
    assume(not (math.isinf(x) or math.isnan(x)))
    assert x == int(x)


@fails
@given(float)
def test_is_not_int(x):
    assume(not (math.isinf(x) or math.isnan(x)))
    assert x != int(x)


@fails
@given(float)
def test_is_in_exact_int_range(x):
    assume(not (math.isinf(x) or math.isnan(x)))
    assert x + 1 != x


@fails
@given(float)
def test_can_generate_really_small_floats(x):
    assume(x > 0)
    assert x > 1e-200
