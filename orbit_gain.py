import math

# Constants
EARTH_RADIUS = 6371  # in km
FREQUENCY = 2.4e9    # in Hz (example: Wi-Fi, 2.4 GHz)
SPEED_OF_LIGHT = 3e8 # in m/s

# Parameters
num_satellites = 14  # Number of satellites in orbit
altitude = 450       # Orbital altitude in km

def satellite_distance(num_satellites, altitude):
    """Calculate the distance between two adjacent satellites in a circular orbit."""
    orbit_radius = EARTH_RADIUS + altitude  # Total radius from Earth's center (km)
    circumference = 2 * math.pi * orbit_radius  # Orbit circumference (km)
    return circumference / num_satellites  # Distance between satellites (km)

def power_loss(distance_km, frequency=FREQUENCY):
    """Calculate free-space path loss (FSPL) in dB."""
    distance_m = distance_km * 1000  # Convert km to meters
    wavelength = SPEED_OF_LIGHT / frequency  # Calculate wavelength (m)
    fspl = 20 * math.log10(distance_m) + 20 * math.log10(frequency) - 147.55  # FSPL formula
    return fspl

# Calculations
dist_between_sats = satellite_distance(num_satellites, altitude)
loss = power_loss(dist_between_sats)

# Output Results
print(f"Distance between satellites: {dist_between_sats:.2f} km")
print(f"Power loss (FSPL): {loss:.2f} dB")
