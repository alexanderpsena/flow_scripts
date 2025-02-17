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

# Global Default Variables (these can be changed by Flow input)
num_satellites = 24  # Default: Number of satellites
altitude = 500000    # Default: Altitude in meters (500 km)
frequency = 2.4e9     # Default: Frequency in Hz (2.4 GHz)

# Outputs (to be populated by the model)
output_distance = None
output_power_loss = None
error = None

def run_model():
    global num_satellites, altitude, frequency, output_distance, output_power_loss, error

    try:
        # Calculate the distance between satellites
        distance = calculate_satellite_distance(num_satellites, altitude)

        # Calculate the free space power loss
        power_loss = calculate_power_loss(distance, frequency)

        # Set output variables for Flow
        output_distance = distance
        output_power_loss = power_loss
        error = None  # No error, successfully calculated

    except Exception as e:
        # Handle errors and set the global error variable
        error = str(e)
        output_distance = None
        output_power_loss = None

# Explicitly run the model
run_model()

# Output results: Flow expects these as output variables
if error:
    print(f"Error: {error}")
else:
    print(f"The distance between the satellites is: {output_distance:.2f} meters")
    print(f"The free-space path loss (power loss) is: {output_power_loss:.2f} dB")

