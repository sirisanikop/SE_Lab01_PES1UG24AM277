"""Lab 6 - Code (line/statement) coverage tests for elevator_dispatch.py.

Goal: execute every statement of the module at least once (>= 90% line coverage).
Each test targets one specific `return` / statement that the starter tests missed.

Run:
    coverage run -m pytest CodeCoverageTest_elevator_dispatch.py
    coverage report -m
"""
from elevator_dispatch import next_direction, door_action, pick_elevator


# ---------------------------------------------------------------------------
# Starter tests (from the given test file)
# ---------------------------------------------------------------------------
def test_emergency_holds_doors():
    assert door_action(100, False, True) == "hold_open"


def test_idle_with_no_requests():
    assert next_direction(3, "idle", []) == "idle"


# ---------------------------------------------------------------------------
# next_direction - every return statement
# ---------------------------------------------------------------------------
def test_up_with_requests_above_keeps_going_up():
    assert next_direction(3, "up", [5, 7]) == "up"


def test_up_with_only_requests_below_turns_down():
    assert next_direction(5, "up", [1, 2]) == "down"


def test_up_with_no_requests_goes_idle():
    assert next_direction(5, "up", []) == "idle"


def test_down_with_requests_below_keeps_going_down():
    assert next_direction(6, "down", [2]) == "down"


def test_down_with_only_requests_above_turns_up():
    assert next_direction(2, "down", [8]) == "up"


def test_down_with_no_requests_goes_idle():
    assert next_direction(4, "down", []) == "idle"


def test_idle_with_request_above_goes_up():
    assert next_direction(0, "idle", [3]) == "up"


def test_idle_with_request_below_goes_down():
    assert next_direction(9, "idle", [1]) == "down"


# ---------------------------------------------------------------------------
# door_action - every return statement
# ---------------------------------------------------------------------------
def test_overload_when_load_exceeds_limit():
    assert door_action(700, False, False) == "overload"


def test_reopen_when_doorway_blocked():
    assert door_action(200, True, False) == "reopen"


def test_close_when_everything_normal():
    assert door_action(200, False, False) == "close"


# ---------------------------------------------------------------------------
# pick_elevator - executes loop body, busy-car penalty and best update
# ---------------------------------------------------------------------------
def test_pick_busy_car_executes_penalty():
    # Single busy car: runs `gap += 5` and the `best = name` update.
    assert pick_elevator([("A", 2, False)], 4) == "A"
