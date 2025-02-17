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

def run(inputs=None):
    """Function for Flow Engineering: Computes satellite spacing and power loss."""
    if inputs is None or not isinstance(inputs, dict):
        return {"error": "Invalid or missing inputs"}
    
    num_satellites = int(inputs.get("num_satellites", 14))  # Default to 14 if missing
    altitude = float(inputs.get("altitude", 450))  # Default to 450 km if missing
    
    dist_between_sats = satellite_distance(num_satellites, altitude)
    loss = power_loss(dist_between_sats)
    
    return {"outputs": {
        "distance_between_satellites_km": round(dist_between_sats, 2),
        "power_loss_dB": round(loss, 2)
    }}

if __name__ == "__main__":
    # Example parameters
    inputs = {"num_satellites": 14, "altitude": 450}
    results = run(inputs)
    
    # Output Results
    if "error" in results:
        print(results["error"])
    else:
        print(f"Distance between satellites: {results['outputs']['distance_between_satellites_km']} km")
        print(f"Power loss (FSPL): {results['outputs']['power_loss_dB']} dB")
