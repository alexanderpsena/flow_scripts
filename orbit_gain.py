import math

# Constants
speed_of_light = 3e8  # m/s
free_space_loss_constant = 20 * math.log10(4 * math.pi / speed_of_light)  # Constant for free-space path loss

# Function to calculate the distance between satellites
def calculate_satellite_distance(num_satellites, altitude):
    # Earth's radius in meters
    earth_radius = 6371e3  # meters
    orbit_radius = earth_radius + altitude  # Orbit radius = Earth's radius + altitude
    # Distance between satellites along the orbit, assuming they are evenly spaced
    angular_distance = 2 * math.pi / num_satellites
    # Distance between satellites (arc length)
    satellite_distance = orbit_radius * angular_distance
    return satellite_distance

# Function to calculate free space power loss for isotropic antenna
def calculate_power_loss(distance, frequency):
    # Free space path loss formula (in dB)
    wavelength = speed_of_light / frequency  # Wavelength in meters
    loss = free_space_loss_constant + 20 * math.log10(distance) + 20 * math.log10(frequency) - 147.55
    return loss

def run_model(inputs):
    try:
        # Extract inputs from FlowEngineering API
        num_satellites = inputs['num_satellites']
        altitude = inputs['altitude']
        frequency = inputs['frequency']

        # Ensure valid input types
        if not isinstance(num_satellites, int) or num_satellites <= 0:
            raise ValueError("Number of satellites must be a positive integer.")
        if not isinstance(altitude, (int, float)) or altitude <= 0:
            raise ValueError("Altitude must be a positive number.")
        if not isinstance(frequency, (int, float)) or frequency <= 0:
            raise ValueError("Frequency must be a positive number.")

        # Calculate distance between satellites
        distance = calculate_satellite_distance(num_satellites, altitude)

        # Calculate power loss
        power_loss = calculate_power_loss(distance, frequency)

        # Return outputs in a dictionary format
        return {
            'output_distance': distance,
            'output_power_loss': power_loss
        }
    except Exception as e:
        # Handle errors and return as output
        return {
            'error': str(e)
        }

# Example input for testing
inputs = {
    'num_satellites': 24,  # Number of satellites
    'altitude': 500000,    # Altitude in meters (500 km)
    'frequency': 2.4e9     # Frequency in Hz (2.4 GHz)
}

# Call the model with inputs
outputs = run_model(inputs)

# Print results for debugging
print(outputs)
