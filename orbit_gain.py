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

# Global variables that Flow will use
num_satellites = 24  # Input: Number of satellites
altitude = 500000    # Input: Altitude in meters (500 km)
frequency = 2.4e9     # Input: Frequency in Hz (2.4 GHz)

# Global output variables that Flow will use
output_distance = None
output_power_loss = None
error = None

# Function to run the model
def run_model():
    global output_distance, output_power_loss, error
    try:
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

        # Set global output variables
        output_distance = distance
        output_power_loss = power_loss

    except Exception as e:
        # Set error message
        error = str(e)

# Run the model
run_model()

# Output for FlowEngineering
if error:
    print(f"Error: {error}")
else:
    print(f"The distance between the satellites is: {output_distance:.2f} meters")
    print(f"The free-space path loss (power loss) is: {output_power_loss:.2f} dB")
