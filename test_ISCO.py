
"""
Tests for the ISCO Black Hole Project.

Run with:
    python test_isco.py
"""

import math
from ISCO import calculate_isco, gravitational_radius


def test_schwarzschild_limit():
    """A nonrotating black hole has an ISCO of 6 gravitational radii."""
    assert math.isclose(calculate_isco(0.0), 6.0)


def test_maximum_prograde_spin():
    """The extremal prograde limit is 1 gravitational radius."""
    assert math.isclose(calculate_isco(1.0), 1.0)


def test_maximum_retrograde_spin():
    """The extremal retrograde limit is 9 gravitational radii."""
    assert math.isclose(calculate_isco(-1.0), 9.0)


def test_intermediate_spin():
    """Check a known intermediate-spin result."""
    assert math.isclose(
        calculate_isco(0.9), 2.320883,
        rel_tol=1e-5
    )


def test_invalid_spin():
    """Spin outside the allowed range should raise ValueError."""
    try:
        calculate_isco(1.1)
    except ValueError:
        pass
    else:
        raise AssertionError("Invalid spin should raise ValueError")


def test_invalid_mass():
    """Zero or negative black hole mass should raise ValueError."""
    for mass in (0, -10):
        try:
            gravitational_radius(mass)
        except ValueError:
            continue
        raise AssertionError("Invalid mass should raise ValueError")


def run_all_tests():
    """Run all tests and report success."""
    test_schwarzschild_limit()
    test_maximum_prograde_spin()
    test_maximum_retrograde_spin()
    test_intermediate_spin()
    test_invalid_spin()
    test_invalid_mass()

    print("All ISCO tests passed!")


if __name__ == "__main__":
    run_all_tests()
