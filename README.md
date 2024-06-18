# Potato Disease Classification Using CNN
![image](https://github.com/GayaaniD/photato_disease_classification/assets/125920863/8e973199-b1fb-467d-ad40-66b2fb2a9442 "Images of Photato leaves with three conditions")

This project focuses on identifying potato diseases by analyzing images of potato leaves. Using Convolutional Neural Networks (CNN), the model classifies the leaves into three categories: **Early blight, Late blight, and Healthy**.

## Project Flow
### 1. Data Collection:
- Data is sourced from Kaggle, which contains images of potato leaves categorized into early blight, late blight, and healthy.
- Load the data using tf.keras.preprocessing.image_dataset_from_directory and set all image sizes to 255 x 255 with an appropriate batch size.

### 2. Data Preparation:
- Split the dataset into training (80%), validation (10%), and testing (10%) sets.
- Resize and rescale the dataset.
- Apply data augmentation techniques to enhance the dataset and improve model generalization.

### 3. Model Creation:
- Define the model architecture:
  - Apply resizing and rescaling layers.
  - Add convolutional layers with specific filter sizes, activation functions, and input shapes.
  - Apply pooling layers (e.g., max pooling) with specific stride sizes.
  - Repeat convolutional and pooling layers as needed.
  - Flatten the output and apply dense layers to build the model.
- Compile the model using the Adam optimizer, sparse categorical cross-entropy loss, and accuracy as a metric.

### 4. Model Training:
  - Train the model using the training dataset.
  - Evaluate the model using the testing dataset.
  - Make predictions on new data.
  - Save the trained model locally.

### 5. FastAPI Backend:
- Load the saved model.
- Create a prediction function and an image reading function.
- Test the backend using Postman.

### 6. Model Configuration and Deployment:
- Create a model config file to manage different model versions.
- Run the file using Docker.
- Set up TensorFlow Serving and define an endpoint URL.

### 7. Streamlit Frontend:
- Create a Streamlit application to provide a user interface.
- Connect the frontend with the FastAPI backend.

### 8. Deployment on Google Cloud Platform (GCP):
- Create a GCP account and a new project.
- Create a GCP bucket to store the model.
- Upload the saved model (model.h5) to the bucket.
- Install Google Cloud SDK and authenticate using gcloud auth login.
- Write a script to deploy the project:
  - Define a function to download the model from the GCP bucket.
  - Write a predict function to handle image input and generate predictions.
- Deploy the cloud function using gcloud functions deploy.

## How to Run
1. Install Dependencies:
- Ensure all required libraries are installed by running:
```
pip install -r requirements.txt
```

2. Run the Backend:

- Start the FastAPI backend:
```
python main.py
```

3. Run the Frontend:

- Start the Streamlit application:
```
streamlit run client.py
```

4. Testing:

Use the provided UI to test the model by uploading images of potato leaves and checking the predictions.

## Results
![image](https://github.com/GayaaniD/photato_disease_classification/assets/125920863/55b5aca0-bd41-4412-b807-0cc42b411f90 "UI Interface")
![image](https://github.com/GayaaniD/photato_disease_classification/assets/125920863/8cdf50c7-34ea-4e21-bdb0-a937df2016fd "Prediction output")

The project successfully classifies potato leaf images into early blight, late blight, and healthy categories. The model's performance can be evaluated based on accuracy, and predictions can be tested via the Streamlit UI or using Postman with the deployed FastAPI backend.

