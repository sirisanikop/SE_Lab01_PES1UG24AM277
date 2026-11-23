"""Lab 6 - Branch coverage tests for elevator_dispatch.py.

Goal: make every decision (if / for / or) take BOTH its True and False outcome
(>= 90% branch coverage). Builds on the code-coverage tests, then adds the
branches that line coverage alone missed in pick_elevator (38->40, 40->36)
plus boundary values.

Run:
    coverage run --branch -m pytest BranchCoverageTest_elevator_dispatch.py
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


# ---------------------------------------------------------------------------
# Branch-coverage additions
# ---------------------------------------------------------------------------
def test_pick_idle_car_skips_penalty():
    # `if not is_idle` -> False branch (38->40): idle car gets no +5 penalty.
    assert pick_elevator([("A", 3, True)], 3) == "A"


def test_pick_keeps_earlier_better_car():
    # `if best is None or gap < best_gap` -> False branch (40->36):
    # second car is farther, so best is NOT replaced.
    assert pick_elevator([("A", 1, True), ("B", 9, True)], 2) == "A"


def test_pick_replaces_with_closer_car():
    # Second car is closer -> best IS replaced (True via `gap < best_gap`).
    assert pick_elevator([("A", 9, True), ("B", 3, True)], 2) == "B"


def test_pick_idle_far_car_beats_busy_near_car():
    # Busy penalty changes the decision: busy A gap 1+5=6, idle B gap 4.
    assert pick_elevator([("A", 3, False), ("B", 6, True)], 2) == "B"


def test_pick_tie_keeps_first_car():
    # Equal gaps -> `gap < best_gap` is False, first car wins.
    assert pick_elevator([("A", 1, True), ("B", 3, True)], 2) == "A"


def test_pick_no_cars_returns_none():
    # Loop body never runs (for-loop exits immediately).
    assert pick_elevator([], 5) is None


def test_overload_boundary_exactly_630_is_not_overload():
    # `load_kg > 630` False at the boundary value.
    assert door_action(630, False, False) == "close"


def test_overload_boundary_631_is_overload():
    assert door_action(631, False, False) == "overload"


def test_emergency_has_priority_over_overload_and_block():
    assert door_action(900, True, True) == "hold_open"


def test_overload_has_priority_over_blocked():
    assert door_action(900, True, False) == "overload"


def test_request_on_current_floor_is_ignored():
    # Floor equal to current is neither above nor below.
    assert next_direction(4, "up", [4]) == "idle"


def test_unknown_direction_treated_as_idle():
    assert next_direction(4, "sideways", [2, 8]) == "up"


def test_up_prefers_above_even_when_below_exists():
    assert next_direction(4, "up", [1, 8]) == "up"


def test_down_prefers_below_even_when_above_exists():
    assert next_direction(4, "down", [1, 8]) == "down"
