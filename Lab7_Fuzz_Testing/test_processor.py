"""
Hypothesis Property-Based Fuzz Tests (Generic test_processor.py)
Lab 7: Fuzzing for Input Validation Bugs
Student: Siri Sanikop (PES1UG24AM277)
"""
from hypothesis import given, strategies as st
try:
    from elevator_dispatch import parse_request, total_travel, load_percent
except ImportError:
    from processor import parse_request, total_travel, load_percent


@given(st.text() | st.none())
def test_parse_request_no_crash(s):
    """
    Fuzz test parse_request with arbitrary strings and None.
    Property invariant: parse_request must never crash or raise an unhandled exception.
    """
    try:
        parse_request(s)
    except Exception as e:
        assert False, f"parse_request crashed with: {e}"


@given(st.text() | st.none())
def test_total_travel_no_crash(s):
    """
    Fuzz test total_travel with arbitrary strings and None.
    Property invariant: total_travel must never crash or raise an unhandled exception.
    """
    try:
        total_travel(s)
    except Exception as e:
        assert False, f"total_travel crashed with: {e}"


@given(st.text() | st.none())
def test_load_percent_no_crash(s):
    """
    Fuzz test load_percent with arbitrary strings and None.
    Property invariant: load_percent must never crash or raise an unhandled exception.
    """
    try:
        load_percent(s)
    except Exception as e:
        assert False, f"load_percent crashed with: {e}"
