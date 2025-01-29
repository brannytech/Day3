import streamlit as st
import pandas as pd
from PIL import Image
import os

# Title of the app
st.title("Researcher Profile Page")


# Collect basic information
name = "Olawale Olushola"
field = "Applied Mathematics"
institution = "University of Cape Town"


# Display basic profile information
st.header("Researcher Overview")
st.write(f"**Name:** {name}")
st.write(f"**Field of Research:** {field}")
st.write(f"**Institution:** {institution}")

# Add an image

# Get the directory of the current script
script_dir = os.path.dirname(__file__)

# Define the relative path to the image
image_path = os.path.join(script_dir, "images", "personal_pix.png")
my_pix = Image.open(image_path) 
st.image(my_pix, width = 150, caption = f"{name}")



# Add Image section

# Add a section for publications

st.header("Publications")

st.write("Do you want to view Researcher's publications?")
selection = st.radio(label = "Selection an Option", options = ["Yes", "No"])

if selection == "Yes":
    uploaded_file = st.file_uploader("Upload a CSV of Publications", type="csv")

    if uploaded_file:
        publications = pd.read_csv(uploaded_file)
        st.dataframe(publications)
    
        # Add filtering for year or keyword
        keyword = st.text_input("Filter by keyword", "")
        if keyword:
            filtered = publications[
                publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
            ]
            st.write(f"Filtered Results for '{keyword}':")
            st.dataframe(filtered)
        else:
            st.write("Showing all publications")


    
        # Add a section for visualizing publication trends
        st.header("Publication Trends")
        if uploaded_file:
            if "Year" in publications.columns:
                year_counts = publications["Year"].value_counts().sort_index()
                st.bar_chart(year_counts)
            else:
                st.write("The CSV does not have a 'Year' column to visualize trends.")

else: 
    st.write("You did not select a publication")       

# Skills section
st.header("Skills and Expertise")
skills = ["Python", "Data Analytics", "Machine Learning", "Mathematics", "Streamlit"] 
st.write("**Skills**")
for skill in skills:
    st.write(f" - {skill}")      

# Add a contact section
st.header("Contact Information")
email = "olawale.abdkabeer@gmail.com"
st.write(f"You can reach {name} at \n Email: {email}.")
github = "https://github.com/brannytech"
st.markdown("- [Github](github)")

# Add a line break'
st.markdown("---")
st.markdown(f"© 2025 {name}. All rights reserved.")