# Import necessary libraries
import streamlit as st
import pandas as pd

# Streamlit app title and subtitle
st.title("Expenditure vs. Health Dashboard")
st.subheader("DataSci5193 Interactive Visualization")


# Load the dataset (Cached for performance)
@st.cache
def load_data():
    data = pd.read_csv("AllCombined.csv")

    # Convert % Population column to numeric
    data["% Population\nEnrolled in\nSoonerCare"] = (
        data["% Population\nEnrolled in\nSoonerCare"]
        .str.replace(",", "")  # Remove commas
        .str.replace("%", "")  # Remove percentage signs
        .astype(float)  # Convert to float
    )
    return data


df = load_data()

# Display the dataset in a table
st.write("### Dataset Overview")
st.dataframe(df)

# Filter by population enrolled in SoonerCare
st.write("### Filter Counties by Population Enrolled in SoonerCare")
percentage_filter = st.slider("Minimum % Population Enrolled in SoonerCare", 0, 100, 10)

# Apply filter
filtered_df = df[df["% Population\nEnrolled in\nSoonerCare"] > percentage_filter]

# Display the filtered results
st.write(f"Counties with Population Enrolled > {percentage_filter}%")
st.dataframe(filtered_df)

