
"""
ISCO Black Hole Project
Calculate the innermost stable circular orbit (ISCO)
for a rotating Kerr black hole.
"""

import math

# Physical constants (SI units)
G = 6.67430e-11
C = 299792458
SOLAR_MASS = 1.98847e30


def calculate_isco(spin):
    """
    Calculate the Kerr ISCO radius in gravitational-radius units.

    Parameters:
        spin (float): Dimensionless black hole spin, from -1 to 1.
                      Positive = prograde orbit.
                      Negative = retrograde orbit.

    Returns:
        float: ISCO radius in units of GM/c^2.
    """

    if not -1.0 <= spin <= 1.0:
        raise ValueError("Spin must be between -1 and 1.")

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
    """

    if not math.isfinite(mass_solar) or mass_solar <= 0:
        raise ValueError("Black hole mass must be positive and finite.")

    mass_kg = mass_solar * SOLAR_MASS

    radius = G * mass_kg / C**2

    return radius


def main():
    """Run an example ISCO calculation."""

    print("\nISCO Validation")
    print("---------")

    test_spins = [-1.0, -0.5, 0.0, 0.5, 0.9, 0.998, 1.0]

    for test_spin in test_spins:
        radius = calculate_isco(test_spin)
        print(f"Spin: {test_spin:>6.3f} | ISCO: {radius:.4f} GM/c^2")

    mass_solar = 10.0
    spin = 0.9

    isco_rg = calculate_isco(spin)
    rg_m = gravitational_radius(mass_solar)

    isco_km = isco_rg * rg_m / 1000

    print("Kerr Black Hole ISCO Calculator")
    print("--------------------------------")
    print(f"Black hole mass: {mass_solar:.2f} solar masses")
    print(f"Dimensionless spin: {spin:.2f}")
    print(f"Gravitational radius: {rg_m / 1000:.3f} km")
    print(f"ISCO radius: {isco_rg:.4f} gravitational radii")
    print(f"ISCO radius: {isco_km:.3f} km")


if __name__ == "__main__":
    main()

