import math

# Constants
EARTH_RADIUS = 6371  # in km
FREQUENCY = 2.4e9    # in Hz (example: Wi-Fi, 2.4 GHz)
SPEED_OF_LIGHT = 3e8 # in m/s

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

def calculate_satellite_metrics(inputs):
    """Calculate satellite distance and power loss based on inputs for Flow Engineering."""
    num_satellites = inputs.get("num_satellites", 14)
    altitude = inputs.get("altitude", 450)
    
    dist_between_sats = satellite_distance(num_satellites, altitude)
    loss = power_loss(dist_between_sats)
    
    return {
        "distance_between_satellites_km": round(dist_between_sats, 2),
        "power_loss_dB": round(loss, 2)
    }

if __name__ == "__main__":
    # Example parameters
    inputs = {"num_satellites": 14, "altitude": 450}
    results = calculate_satellite_metrics(inputs)
    
    # Output Results
    print(f"Distance between satellites: {results['distance_between_satellites_km']} km")
    print(f"Power loss (FSPL): {results['power_loss_dB']} dB")
