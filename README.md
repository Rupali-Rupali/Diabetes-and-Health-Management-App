# Diabetes-and-Health-Management-App
Gemini Health App

Gemini Health App is a web application that helps individuals manage their health, particularly focusing on analyzing images of food items for individuals with diabetes. It provides functionalities for calculating total calories and checking the glycemic index of food items in uploaded images.

Features:

- Calculate Total Calories: Analyze food items in the image and calculate their total calories.
- Check Glycemic Index: Determine the glycemic index of food items in the image to assist in diabetes management.

Getting Started:

To run the Gemini Health App locally, follow these steps:

1. Clone the repository:

git clone https://github.com/your-username/gemini-health-app.git

2. Navigate to the project directory:

cd gemini-health-app

3. Install the required dependencies:

pip install -r requirements.txt

4. Set up your Google API key:
   
   - Create a .env file in the root directory of the project.
   - Add your Google API key to the .env file:

   GOOGLE_API_KEY=your-api-key

5. Run the Streamlit app:

streamlit run app.py

6. Access the app in your web browser by visiting http://localhost:8501.

Usage:

- Upon running the application, you will be presented with the main page of the Gemini Health App.
- Upload an image containing food items that you want to analyze.
- Choose the desired functionality from the dropdown menu.
- Click the corresponding button to perform the selected analysis.
- The results will be displayed on the page.

Contributing:

Contributions are welcome! If you have any suggestions, feature requests, or bug reports, please open an issue or submit a pull request.

License:

This project is licensed under the MIT License.
