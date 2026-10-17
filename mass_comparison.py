
"""
Compare physical ISCO radii for black holes of different masses
at a fixed dimensionless spin.

Run with:
    python mass_comparison.py
"""

import matplotlib.pyplot as plt
import numpy as np

from ISCO import calculate_isco, gravitational_radius


def main():
    """Calculate, compare, and plot physical ISCO radii."""

    spin = 0.9

    # Representative stellar-mass, intermediate-mass, and
    # supermassive black holes.
    masses_solar = np.array([10, 1_000_000, 1_000_000_000])

    # Dimensionless ISCO radius, measured in units of GM/c^2.
    isco_rg = calculate_isco(spin)

    # Convert gravitational radii from meters to kilometers.
    rg_km = np.array([
        gravitational_radius(float(mass)) / 1000
        for mass in masses_solar
    ])

    isco_km = isco_rg * rg_km

    print("ISCO Mass Comparison")
    print("--------------------")
    print(f"Dimensionless spin: {spin:.2f}")
    print(f"ISCO radius: {isco_rg:.4f} GM/c^2")
    print()

    for mass, radius in zip(masses_solar, isco_km):
        print(f"Black hole mass: {mass:,.0f} solar masses")
        print(f"ISCO radius: {radius:,.3f} km")
        print()

    # Plot the relationship over a continuous mass range.
    mass_range = np.logspace(1, 9, 300)

    isco_radius_range_km = np.array([
        isco_rg * gravitational_radius(float(mass)) / 1000
        for mass in mass_range
    ])

    fig, ax = plt.subplots(figsize=(9, 6))

    ax.loglog(
        mass_range,
        isco_radius_range_km,
        linewidth=2,
        label=f"ISCO, spin = {spin:.1f}"
    )

    ax.scatter(
        masses_solar,
        isco_km,
        s=55,
        zorder=3,
        label="Example black holes"
    )

    ax.set_xlabel("Black hole mass (solar masses)")
    ax.set_ylabel("Physical ISCO radius (km)")
    ax.set_title("Physical ISCO Radius vs. Black Hole Mass")

    ax.grid(True, which="both", alpha=0.25)
    ax.legend(frameon=False)
    fig.tight_layout()

    fig.savefig(
        "isco_vs_mass.png",
        dpi=300,
        bbox_inches="tight"
    )

    print("Graph saved as isco_vs_mass.png")

    plt.show()


if __name__ == "__main__":
    main()
