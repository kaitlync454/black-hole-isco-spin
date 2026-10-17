
"""
Kerr Black Hole ISCO Calculator

Calculate the innermost stable circular orbit (ISCO)
for an idealized rotating Kerr black hole.
"""

import math

# Physical constants (SI units)
G = 6.67430e-11       # Gravitational constant (m^3 kg^-1 s^-2)
C = 299792458         # Speed of light (m/s)
SOLAR_MASS = 1.98847e30  # Solar mass (kg)


def calculate_isco(spin):
    """
    Calculate the Kerr ISCO radius in units of GM/c^2.

    Parameters:
        spin (float): Dimensionless spin, from -1 to 1.
                      Positive = prograde equatorial orbit.
                      Negative = retrograde equatorial orbit.

    Returns:
        float: Dimensionless ISCO radius in units of GM/c^2.

    Raises:
        ValueError: If spin is nonnumeric, nonfinite, or outside [-1, 1].
    """
    try:
        spin = float(spin)
    except (TypeError, ValueError, OverflowError):
        raise ValueError("Spin must be a finite number between -1 and 1.")

    if not math.isfinite(spin) or not -1.0 <= spin <= 1.0:
        raise ValueError("Spin must be a finite number between -1 and 1.")

    # Schwarzschild limit: nonrotating black hole.
    if spin == 0.0:
        return 6.0

    z1 = 1 + (1 - spin**2)**(1 / 3) * (
        (1 + abs(spin))**(1 / 3)
        + (1 - abs(spin))**(1 / 3)
    )

    z2 = math.sqrt(3 * spin**2 + z1**2)

    correction = math.sqrt(
        (3 - z1) * (3 + z1 + 2 * z2)
    )

    isco_radius = 3 + z2 - math.copysign(correction, spin)

    return isco_radius


def gravitational_radius(mass_solar):
    """
    Calculate the gravitational radius GM/c^2 in meters.

    Parameters:
        mass_solar (float): Black hole mass in solar masses.

    Returns:
        float: Gravitational radius in meters.

    Raises:
        ValueError: If mass is nonnumeric, nonfinite, nonpositive,
                    or too large for a finite result.
    """
    try:
        mass_solar = float(mass_solar)
    except (TypeError, ValueError, OverflowError):
        raise ValueError("Black hole mass must be positive and finite.")

    if not math.isfinite(mass_solar) or mass_solar <= 0:
        raise ValueError("Black hole mass must be positive and finite.")

    mass_kg = mass_solar * SOLAR_MASS

    radius = G * mass_kg / C**2

    if not math.isfinite(radius):
        raise ValueError("Black hole mass is too large to calculate safely.")

    return radius


def main():
    """Run example ISCO calculations."""

    print("\nKerr ISCO Example Calculations")
    print("------------------------------")

    test_spins = [-1.0, -0.5, 0.0, 0.5, 0.9, 0.998, 1.0]

    for test_spin in test_spins:
        radius = calculate_isco(test_spin)
        print(
            f"Spin: {test_spin:>6.3f} | "
            f"ISCO: {radius:.4f} GM/c^2"
        )

    mass_solar = 10.0
    spin = 0.9

    isco_rg = calculate_isco(spin)
    rg_m = gravitational_radius(mass_solar)
    isco_km = isco_rg * rg_m / 1000

    print("\nExample Physical Radius")
    print("-----------------------")
    print(f"Black hole mass: {mass_solar:.2f} solar masses")
    print(f"Dimensionless spin: {spin:.2f}")
    print(f"Gravitational radius: {rg_m / 1000:.3f} km")
    print(f"ISCO radius: {isco_rg:.4f} gravitational radii")
    print(f"ISCO radius: {isco_km:.3f} km")


if __name__ == "__main__":
    main()
