st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg,#bcbcbc,#cfe2f3);
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    h1 {
        text-align: center;
        font-size: 36px;
        color: #333333;
    }
    .stButton>button {
        background: linear-gradient(135deg,#bcbcbc,#cfe2f3);
        color: white;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        transition: background 0.3s ease;
        box-shadow: 0 2px 5px rgba(0,0,0,0.2);
    }
    .stButton>button:hover {
        transform: scale(1.05);
        background: linear-gradient(135deg,#bcbcbc,#a2d2ff);
        color: black;
    }
    .result-box {
        font-size: 24px;
        font-weight: bold;
        text-align: center;
        background: rgba(135, 194, 243, 0.2);
        padding: 25px;
        border-radius: 10px;
        box-shadow: 0 5px 8px rgba(0, 201, 255, 0.3);
    }
    .footer {
        text-align: center;
        margin-top: 50px;
        font-size: 14px;
        color: #666666;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and description
st.markdown("<h1>Google Unit Converter</h1>", unsafe_allow_html=True)
st.write("Easily convert between different units of length, weight, and temperature.")

# Select conversion type
conversion_types = st.sidebar.selectbox("Choose conversion type", ["Length", "Weight", "Temperature"])
value = st.number_input("Enter the value to convert")

# Define columns for unit selection
col1, col2 = st.columns(2)

if conversion_types == "Length":
    with col1:
        from_unit = st.selectbox("Select unit", ["Meter", "Kilometer", "Mile", "Yard", "Foot", "Inch"])
    with col2:
        to_unit = st.selectbox("Select unit", ["Meter", "Kilometer", "Mile", "Yard", "Foot", "Inch"])

elif conversion_types == "Weight":
    with col1:
        from_unit = st.selectbox("Select unit", ["Kilogram", "Gram", "Milligram", "Pound", "Ounce"])
    with col2:
        to_unit = st.selectbox("Select unit", ["Kilogram", "Gram", "Milligram", "Pound", "Ounce"])

elif conversion_types == "Temperature":
    with col1:
        from_unit = st.selectbox("Select unit", ["Celsius", "Fahrenheit", "Kelvin"])
    with col2:
        to_unit = st.selectbox("Select unit", ["Celsius", "Fahrenheit", "Kelvin"])

# Conversion functions
def length_conversion(value, from_unit, to_unit):
    length_units = {
        "Meter": 1.0,
        "Kilometer": 1000.0,
        "Mile": 1609.34,
        "Yard": 0.9144,
        "Foot": 0.3048,
        "Inch": 0.0254
    }
    return value * length_units[from_unit] / length_units[to_unit]

def weight_conversion(value, from_unit, to_unit):
    weight_units = {
        "Kilogram": 1.0,
        "Gram": 0.001,
        "Milligram": 0.000001,
        "Pound": 0.453592,
        "Ounce": 0.0283495
    }
    return value * weight_units[from_unit] / weight_units[to_unit]

def temperature_conversion(value, from_unit, to_unit):
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        return (value + 459.67) * 5/9
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        return (value * 9/5) - 459.67
    return value  # If from_unit == to_unit, return the same value

# Perform conversion
if st.button("Convert"):
    if conversion_types == "Length":
        result = length_conversion(value, from_unit, to_unit)
    elif conversion_types == "Weight":
        result = weight_conversion(value, from_unit, to_unit)
    elif conversion_types == "Temperature":
        result = temperature_conversion(value, from_unit, to_unit)

    st.markdown(f"<div class='result-box'>Result: {result:.4f} {to_unit}</div>", unsafe_allow_html=True)

# Footer
st.markdown("<div class='footer'>Developed by Muhammad Noman</div>", unsafe_allow_html=True)

     
