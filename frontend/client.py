import streamlit as st
import requests
from PIL import Image
import io

# Set the background image
background_image = """
<style>
[data-testid="stAppViewContainer"] > .main {
    background-image: url("https://images.pexels.com/photos/3224117/pexels-photo-3224117.jpeg");
    background-size: 100vw 100vh;  # This sets the size to cover 100% of the viewport width and height
    background-position: center;  
    background-repeat: no-repeat;
}
</style>
"""

st.markdown(background_image, unsafe_allow_html=True)

def custom_text_color():
    st.markdown(
        f"""
        <style>
        h1 {{
            color: brown;
        }}
        p {{
            color: white;
            font-size: 20px;
            font-weight:bold;
        }}
        p {{
            color: white;
            font-size: 20px;
            font-weight:bold;
        }}
        p {{
            color: white;
            font-size: 20px;
            font-weight:bold;
        }}
        p {{
            color: white;
            font-size: 20px;
            font-weight:bold;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Call the function to set custom text colors
custom_text_color()
# Title and description
st.title('Potato Disease Classification')
st.write('Upload an image of the potato leaves to classify the disease.')

# Backend API endpoint
BACKEND_URL = 'http://localhost:8000/predict'

# File uploader widget
uploaded_file = st.file_uploader('Choose an image...', type=['jpg', 'jpeg', 'png'])
if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    
    # Prepare the image for sending to the backend
    buffered = io.BytesIO()
    image.save(buffered, format="JPEG")
    img_byte = buffered.getvalue()

    # Send POST request to backend with the uploaded image
    response = requests.post(
        BACKEND_URL,
        files={"file": img_byte}
    )
    
    # Display prediction results
    if response.status_code == 200:
        prediction = response.json()
        st.write(f"Prediction: {prediction['class']}")
        st.write(f"Confidence: {prediction['confidence']:.2f}")
    else:
        st.write('Failed to get a response from the backend. Please check the backend server.')
