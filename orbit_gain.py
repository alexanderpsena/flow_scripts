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

# Global variables (they should be recognized by Flow when set properly)
num_satellites = None  # Will be set by Flow
altitude = None        # Will be set by Flow
frequency = None       # Will be set by Flow

# Outputs that Flow expects
output_distance = None
output_power_loss = None
error = None

def run_model():
    global num_satellites, altitude, frequency, output_distance, output_power_loss, error

    try:
        # Check if inputs are provided and are valid
        if num_satellites is None or altitude is None or frequency is None:
            raise ValueError("Inputs 'num_satellites', 'altitude', and 'frequency' must be set.")
        
        # Validate inputs
        if not isinstance(num_satellites, int) or num_satellites <= 0:
            raise ValueError("Number of satellites must be a positive integer.")
        if not isinstance(altitude, (int, float)) or altitude <= 0:
            raise ValueError("Altitude must be a positive number.")
        if not isinstance(frequency, (int, float)) or frequency <= 0:
            raise ValueError("Frequency must be a positive number.")

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

# Call the model function to perform the calculation
run_model()

# Outputs that Flow expects
if error:
    print(f"Error: {error}")
else:
    print(f"The distance between satellites is: {output_distance:.2f} meters")
    print(f"The free-space path loss (power loss) is: {output_power_loss:.2f} dB")
