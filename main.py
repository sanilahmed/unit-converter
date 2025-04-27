import streamlit as st

# Function to handle all unit conversions
def perform_conversion(amount, source_unit, target_unit):
    # Predefined conversion factors
    conversion_rates = {
        # Length
        "meters_to_kilometers": 0.001,
        "kilometers_to_meters": 1000,
        "meters_to_centimeters": 100,
        "centimeters_to_meters": 0.01,
        "inches_to_centimeters": 2.54,
        "centimeters_to_inches": 0.393701,
        "miles_to_kilometers": 1.60934,
        "kilometers_to_miles": 0.621371,

        # Weight
        "grams_to_kilograms": 0.001,
        "kilograms_to_grams": 1000,
        "pounds_to_kilograms": 0.453592,
        "kilograms_to_pounds": 2.20462,
        "ounces_to_grams": 28.3495,
        "grams_to_ounces": 0.035274,

        # Time
        "seconds_to_minutes": 1/60,
        "minutes_to_seconds": 60,
        "minutes_to_hours": 1/60,
        "hours_to_minutes": 60,
    }
    
    # Handle temperature conversions separately
    if source_unit == "Celsius" and target_unit == "Fahrenheit":
        return (amount * 9/5) + 32
    elif source_unit == "Fahrenheit" and target_unit == "Celsius":
        return (amount - 32) * 5/9

    # Key for lookup
    lookup_key = f"{source_unit}_to_{target_unit}"
    
    # Apply conversion if valid
    if lookup_key in conversion_rates:
        return amount * conversion_rates[lookup_key]
    
    # If no valid conversion is found
    return None

# Set up the Streamlit page
st.set_page_config(
    page_title="Unit Converter",
    page_icon="🔄",
    layout="centered",
    initial_sidebar_state="expanded"
)
st.title("Multi-Purpose Unit Converter")


# Input value from user
input_value = st.number_input(
    label="Enter the value to convert:",
    min_value=0.0,
    step=0.1,
    format="%.2f"
)

# Define available units
units_available = [
    "meters", "kilometers", "centimeters", "inches", "miles",
    "grams", "kilograms", "pounds", "ounces",
    "seconds", "minutes", "hours",
    "Celsius", "Fahrenheit"
]

# Unit selection
source_unit = st.selectbox("From unit:", units_available)
target_unit = st.selectbox("To unit:", units_available)

# Action button to trigger conversion
if st.button("Convert Now"):
    conversion_result = perform_conversion(input_value, source_unit, target_unit)
    
    if conversion_result is not None:
        st.success(f"Result: {conversion_result:.2f} {target_unit}")
    else:
        st.warning("Sorry, this conversion is currently not supported.")
