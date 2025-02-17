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

# Input from the user
num_satellites = int(input("Enter the number of satellites in the orbit: "))
altitude = float(input("Enter the altitude of the orbit in kilometers: ")) * 1e3  # Convert km to meters

# Frequency set to 2.4 GHz (2.4e9 Hz)
frequency = 2.4e9

# Calculate distance between satellites
distance = calculate_satellite_distance(num_satellites, altitude)
print(f"The distance between the satellites is: {distance:.2f} meters")

# Calculate power loss
power_loss = calculate_power_loss(distance, frequency)
print(f"The free-space path loss (power loss) is: {power_loss:.2f} dB")
