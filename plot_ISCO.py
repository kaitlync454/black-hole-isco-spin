
"""
Plot the Kerr black hole ISCO radius as a function of spin.

Run with:
    python plot_ISCO.py

The radius is expressed in units of GM/c^2.
"""

import numpy as np
import matplotlib.pyplot as plt

from ISCO import calculate_isco


def main():
    """Calculate and plot ISCO radii across a range of spins."""

    # Avoid exact extremal endpoints for a clean continuous plot.
    spins = np.linspace(-0.998, 0.998, 500)

    isco_radii = np.array([
        calculate_isco(float(spin))
        for spin in spins
    ])

    # Create figure.
    fig, ax = plt.subplots(figsize=(9, 6))

    ax.plot(
        spins,
        isco_radii,
        linewidth=2.2,
        label="Kerr ISCO"
    )

    # Nonrotating black hole reference.
    ax.axvline(
        0,
        linestyle="--",
        linewidth=1.2,
        label="Zero spin"
    )

    ax.axhline(
        6,
        linestyle=":",
        linewidth=1.5,
        label="Schwarzschild ISCO = 6 GM/c²"
    )

    # Mark selected benchmark spin values.
    benchmark_spins = [-0.9, 0.0, 0.5, 0.9, 0.998]
    benchmark_radii = [
        calculate_isco(spin) for spin in benchmark_spins
    ]

    ax.scatter(
        benchmark_spins,
        benchmark_radii,
        s=35,
        zorder=3,
        label="Benchmark spins"
    )

    # Explain the two sides of the spin axis.
    ax.text(
        -0.95, 2.0,
        "Retrograde orbits",
        ha="left",
        va="center",
        fontsize=9
    )

    ax.text(
        0.35, 8.4,
        "Prograde orbits",
        ha="left",
        va="center",
        fontsize=9
    )

    # Axis labels and title.
    ax.set_xlabel("Dimensionless spin, χ")
    ax.set_ylabel("ISCO radius, r_ISCO / (GM/c²)")
    ax.set_title("Kerr Black Hole ISCO Radius vs. Spin")

    ax.set_xlim(-1.0, 1.0)
    ax.set_ylim(0, 10)

    ax.grid(True, alpha=0.25)
    ax.legend(frameon=False)
    fig.tight_layout()

    # Save at high resolution.
    fig.savefig("isco_vs_spin.png", dpi=300, bbox_inches="tight")

    print("Graph saved as isco_vs_spin.png")

    plt.show()


if __name__ == "__main__":
    main()
