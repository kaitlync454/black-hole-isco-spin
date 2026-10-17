"""
Compare ISCO radii for black holes of different masses
at the same dimensionless spin.
"""

from ISCO import calculate_isco, gravitational_radius


def main():
    spin = 0.9
    masses_solar = [10, 1_000_000, 1_000_000_000]

    isco_rg = calculate_isco(spin)

    print("ISCO Mass Comparison")
    print("--------------------")
    print(f"Dimensionless spin: {spin:.2f}")
    print(f"ISCO radius: {isco_rg:.4f} GM/c^2")
    print()

    for mass in masses_solar:
        rg_m = gravitational_radius(mass)
        isco_km = isco_rg * rg_m / 1000

        print(f"Black hole mass: {mass:,} solar masses")
        print(f"ISCO radius: {isco_km:,.3f} km")
        print()


if __name__ == "__main__":
    main()