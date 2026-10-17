
"""
Tests for the Kerr black hole ISCO project.

Run with:
    python test_ISCO.py
"""

import math
from ISCO import calculate_isco, gravitational_radius


def test_schwarzschild_limit():
    """A nonrotating black hole has an ISCO of 6 GM/c^2."""
    assert math.isclose(calculate_isco(0.0), 6.0)


def test_extremal_spin_limits():
    """Check the prograde and retrograde extremal limits."""
    assert math.isclose(calculate_isco(1.0), 1.0)
    assert math.isclose(calculate_isco(-1.0), 9.0)


def test_reference_values():
    """Compare against established Kerr ISCO benchmark values."""
    reference_values = {
        -0.9: 8.717352,
        -0.5: 7.554585,
         0.5: 4.233003,
         0.9: 2.320883,
         0.998: 1.236971,
    }

    for spin, expected in reference_values.items():
        actual = calculate_isco(spin)
        assert math.isclose(
            actual, expected, rel_tol=1e-5
        ), f"Spin {spin}: expected {expected}, got {actual}"


def test_isco_decreases_with_prograde_spin():
    """ISCO radius should decrease as spin increases."""
    spins = [-0.9, -0.5, 0.0, 0.5, 0.9, 0.998]
    radii = [calculate_isco(spin) for spin in spins]

    for earlier, later in zip(radii, radii[1:]):
        assert earlier > later, (
            "ISCO radius should decrease as spin increases."
        )


def test_invalid_spin():
    """Spins outside [-1, 1] should raise ValueError."""
    for spin in (-1.1, 1.1):
        try:
            calculate_isco(spin)
        except ValueError:
            continue
        raise AssertionError(
            f"Invalid spin {spin} should raise ValueError"
        )


def test_invalid_mass():
    """Zero or negative masses should raise ValueError."""
    for mass in (0, -10):
        try:
            gravitational_radius(mass)
        except ValueError:
            continue
        raise AssertionError(
            f"Invalid mass {mass} should raise ValueError"
        )


def test_gravitational_radius_scales_with_mass():
    """Doubling mass should double the gravitational radius."""
    radius_10 = gravitational_radius(10)
    radius_20 = gravitational_radius(20)

    assert math.isclose(radius_20, 2 * radius_10, rel_tol=1e-12)


def test_gravitational_radius_is_positive():
    """A valid positive mass should produce a positive radius."""
    assert gravitational_radius(10) > 0


def run_all_tests():
    test_schwarzschild_limit()
    test_extremal_spin_limits()
    test_reference_values()
    test_isco_decreases_with_prograde_spin()
    test_invalid_spin()
    test_invalid_mass()
    test_gravitational_radius_scales_with_mass()
    test_gravitational_radius_is_positive()

    print("All ISCO tests passed!")


if __name__ == "__main__":
    run_all_tests()
