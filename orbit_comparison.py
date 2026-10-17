
"""
Compare prograde and retrograde ISCO radii
for a rotating Kerr black hole.

Run with:
    python orbit_comparison.py
"""

import matplotlib.pyplot as plt
import numpy as np

from ISCO import calculate_isco


def main():
    """Compare ISCO radii across black hole spin values."""

    spins = [-0.9, -0.5, 0.0, 0.5, 0.9]

    print("Prograde vs. Retrograde ISCO Comparison")
    print("--------------------------------------")
    print("Negative spin: retrograde orbit")
    print("Zero spin: nonrotating black hole")
    print("Positive spin: prograde orbit")
    print()

    for spin in spins:
        radius = calculate_isco(spin)

        if spin < 0:
            orbit_type = "Retrograde"
        elif spin > 0:
            orbit_type = "Prograde"
        else:
            orbit_type = "Nonrotating"

        print(
            f"{orbit_type:12} | "
            f"Spin: {spin:+.1f} | "
            f"ISCO: {radius:.4f} GM/c^2"
        )

    # Calculate ISCO radii across the full allowed spin range.
    spin_range = np.linspace(-0.998, 0.998, 500)

    isco_radii = np.array([
        calculate_isco(float(spin))
        for spin in spin_range
    ])

    fig, ax = plt.subplots(figsize=(9, 6))

    ax.plot(
        spin_range,
        isco_radii,
        linewidth=2,
        label="ISCO radius"
    )

    ax.axvline(
        0,
        linestyle="--",
        linewidth=1.2,
        label="Nonrotating black hole"
    )

    ax.scatter(
        spins,
        [calculate_isco(spin) for spin in spins],
        s=45,
        zorder=3,
        label="Selected spin values"
    )

    ax.set_xlabel("Dimensionless black hole spin")
    ax.set_ylabel("ISCO radius (GM/c²)")
    ax.set_title("Prograde and Retrograde ISCO Comparison")

    ax.text(
        -0.95, 5.0,
        "Retrograde orbits",
        ha="left",
        va="center"
    )

    ax.text(
        0.35, 5.0,
        "Prograde orbits",
        ha="left",
        va="center"
    )

    ax.grid(True, alpha=0.25)
    ax.legend(frameon=False)
    fig.tight_layout()

    fig.savefig(
        "orbit_comparison.png",
        dpi=300,
        bbox_inches="tight"
    )

    print("\nGraph saved as orbit_comparison.png")

    plt.show()


if __name__ == "__main__":
    main()
