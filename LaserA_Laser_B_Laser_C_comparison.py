def calculate_peak_power(pulse_energy, pulse_duration):
    # Peak power = Pulse energy / Pulse duration
    return pulse_energy / pulse_duration

def calculate_beam_waist(wavelength, focal_radius):
    # Beam waist w_0 = (wavelength / pi) * (focal_radius / 2)
    return (wavelength / 3.14159) * (focal_radius / 2)

def calculate_intensity(peak_power, beam_waist):
    # Intensity I = (2/pi) * (Peak power / beam_waist^2)
    return (2 / 3.14159) * (peak_power / beam_waist**2)

# Laser A parameters
wavelength_A = 300e-9  # 300 nm in meters
pulse_energy_A = 5e-3  # 5 mJ in joules
pulse_duration_A = 7e-15  # 7 fs in seconds
focal_radius_A = 30e-6  # 30 μm in meters

# Laser B parameters
wavelength_B = 700e-9
pulse_energy_B = 5e-3
pulse_duration_B = 7e-15
focal_radius_B = 40e-6

# Laser C parameters
wavelength_C = 3200e-9
pulse_energy_C = 5e-3
pulse_duration_C = 35e-15
focal_radius_C = 60e-6

# Calculate peak powers
peak_power_A = calculate_peak_power(pulse_energy_A, pulse_duration_A)
peak_power_B = calculate_peak_power(pulse_energy_B, pulse_duration_B)
peak_power_C = calculate_peak_power(pulse_energy_C, pulse_duration_C)

# Calculate beam waists
beam_waist_A = calculate_beam_waist(wavelength_A, focal_radius_A)
beam_waist_B = calculate_beam_waist(wavelength_B, focal_radius_B)
beam_waist_C = calculate_beam_waist(wavelength_C, focal_radius_C)

# Calculate intensities
intensity_A = calculate_intensity(peak_power_A, beam_waist_A)
intensity_B = calculate_intensity(peak_power_B, beam_waist_B)
intensity_C = calculate_intensity(peak_power_C, beam_waist_C)

# Find the highest intensity and corresponding laser
highest_intensity = max(intensity_A, intensity_B, intensity_C)
if highest_intensity == intensity_A:
    highest_laser = "Laser A"
elif highest_intensity == intensity_B:
    highest_laser = "Laser B"
else:
    highest_laser = "Laser C"

# Print results
print(f"Highest Intensity: {highest_intensity:.2f} PW/cm^2 (from {highest_laser})")
