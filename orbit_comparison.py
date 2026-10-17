"""
Compare prograde and retrograde ISCO radii
for a rotating Kerr black hole.
"""

from ISCO import calculate_isco


def main():
    spins = [-0.9, 0.0, 0.9]

    print("Prograde vs. Retrograde ISCO Comparison")
    print("--------------------------------------")

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


if __name__ == "__main__":
    main()