# Save this code in a file named `energy_relationships_app.py`

import streamlit as st
import pandas as pd

# Load the data
@st.cache
def load_data():
    # Replace 'Tool Development.xlsx' with the path to your Excel file
    data = pd.read_excel('Tool Development.xlsx', sheet_name='Sheet1')
    return data

def preprocess_data(data):
    # Drop any fully empty rows
    data = data.dropna(how='all')
    
    # Rename the columns for clarity based on structure
    columns = [
        'Independents', 
        'Total Energy Consumption - Increase', 'Total Energy Consumption - Reduction',
        'Energy Use Intensity - Increase', 'Energy Use Intensity - Reduction',
        'Electricity Consumption - Increase', 'Electricity Consumption - Reduction',
        'Heating Consumption - Increase', 'Heating Consumption - Reduction',
        'Cooling Consumption - Increase', 'Cooling Consumption - Reduction',
        'Gas Consumption - Increase', 'Gas Consumption - Reduction',
        'Energy Per Capita - Increase', 'Energy Per Capita - Reduction'
    ]
    data.columns = columns
    return data

data = load_data()
data = preprocess_data(data)

# Create a dropdown for Independents (determinants)
independents = data['Independents'].dropna().unique().tolist()
selected_independent = st.selectbox('Select an Independent Feature (Determinant):', independents)

# Energy outputs to choose from
energy_outputs = [
    'Total Energy Consumption', 'Energy Use Intensity',
    'Electricity Consumption', 'Heating Consumption',
    'Cooling Consumption', 'Gas Consumption', 'Energy Per Capita'
]
selected_energy_output = st.selectbox('Select an Energy Output:', energy_outputs)

# Relationship direction
direction = st.selectbox('Select the Direction of Relationship:', ['Increase', 'Reduction'])

# Filter data based on selections
column_name = f"{selected_energy_output} - {direction}"
results = data[data['Independents'] == selected_independent][column_name]

# Display results
st.write(f"Studies that show the {direction} relationship between {selected_independent} and {selected_energy_output}:")
if results.empty or results.iloc[0] == 0:
    st.write("No relevant studies found.")
else:
    st.write(results.iloc[0])

