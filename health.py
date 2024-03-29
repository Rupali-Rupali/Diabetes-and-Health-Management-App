from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

load_dotenv()  # Load all the environment variables
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def get_gemini_response(input_prompt, image):
    if image:
        model = genai.GenerativeModel('gemini-pro-vision')
        response = model.generate_content([input_prompt, image[0]])
        return response.text


def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [{"mime_type": uploaded_file.type, "data": bytes_data}]
        return image_parts


st.set_page_config(page_title="Gemini Health App")

# Main content
st.title("Diabetes and Health Management App")

# Selection box for choosing functionality
option = st.selectbox("Select an Option", ["Calories & Glycemic Index Calculator", "Suggestions & Quantity Recommendation"])

# Sidebar
#st.sidebar.subtitle("Diabetes Mangament and Calorie Calculator App")
st.sidebar.write(
    """
    ## Welcome to the Gemini Health App!
    

    ### Functionalities:

    
    - **Calculate Total Calories**:
        * Analyze food items in the image and calculate their total calories.
    - **Check Glycemic Index**:
        *  Determine the glycemic index of food items in the image to assist in diabetes management.

    ### Importance of Managing Diabetes:
    - **Blood Sugar Control**: 
        * Monitoring and controlling blood sugar levels is crucial to prevent long-term complications.
    - **Healthy Eating**: 
        * Maintaining a balanced diet helps manage blood sugar levels and prevent complications.
    - **Regular Exercise**: 
        * Physical activity helps lower blood sugar levels and improve overall health.
    - **Medication Management**: 
        * Consistently taking prescribed medications as directed by healthcare providers is vital for diabetes management.
    
    

    """
)

st.subheader("Upload an image:")
uploaded_file = st.file_uploader("", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

    input_prompt_diabetes = """
                   As an expert specializing in assessing the suitability of fruits and foods for individuals with diabetes,
                   your task involves analyzing input images featuring various food items and .
                   based on  glycemic index of food items , provide recommendations on whether individuals with diabetes can include the detected food in their diet. 
                   and secify the recommended quantity for consumption.
                   Please provide the details of every food items with calories intake
                   is below format
    
                   1. Item 1 - Reccomended Quantity  -- Suggestion
                   2. Item 2 -  Reccomended Quantity  -- Suggestion
                   ----
                   """

    input_prompt_calorie = """
    You are an expert in nutritionist where you need to see the food items from the image
                   and calculate the total calories, also provide the details of every food items with calories intake
                   is below format
    
                   1. Item 1 - no of calories -- Glycemic Index : Values
                   2. Item 2 - no of calories -- Glycemic Index : Values
                   ----
                   ----
    """

    if option == "Calories & Glycemic Index Calculator":
        if st.button("Calories & Glycemic Index Calculator"):
            image_data1 = input_image_setup(uploaded_file)
            response1 = get_gemini_response(input_prompt_calorie, image_data1)
            st.subheader("The Response is")
            st.write(response1)

    elif option == "Suggestions & Quantity Recommendation":
        if st.button("Suggestions & Quantity Recommendation"):
            image_data2 = input_image_setup(uploaded_file)
            response2 = get_gemini_response(input_prompt_diabetes, image_data2)
            st.subheader("The Response is")
            st.write(response2)
