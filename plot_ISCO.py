
"""
Plot the ISCO radius as a function of Kerr black hole spin.

Run with:
    python plot_isco.py
"""

import numpy as np
import matplotlib.pyplot as plt

from ISCO import calculate_isco


def main():
    """Calculate and plot ISCO radii across a range of spins."""

    # Dimensionless spin values, avoiding exact extremal endpoints.
    spins = np.linspace(-0.998, 0.998, 500)

    # Calculate ISCO radius for each spin.
    isco_radii = np.array([
        calculate_isco(float(spin))
        for spin in spins
    ])

    # Create the figure.
    plt.figure(figsize=(9, 6))

    plt.plot(
        spins,
        isco_radii,
        label="Kerr ISCO",
        linewidth=2
    )

    # Reference lines.
    plt.axvline(
        0,
        linestyle="--",
        label="Nonrotating black hole"
    )

    plt.axhline(
        6,
        linestyle=":",
        label="Schwarzschild ISCO (6 GM/c²)"
    )

    # Labels and formatting.
    plt.xlabel("Dimensionless black hole spin (χ)")
    plt.ylabel("ISCO radius (GM/c²)")
    plt.title("Innermost Stable Circular Orbit vs. Black Hole Spin")

    plt.grid(True, alpha=0.3)
    plt.legend()
    plt.tight_layout()

    # Save the figure.
    plt.savefig("isco_vs_spin.png", dpi=300)

    print("Graph saved as isco_vs_spin.png")

    # Display the graph.
    plt.show()


if __name__ == "__main__":
    main()
