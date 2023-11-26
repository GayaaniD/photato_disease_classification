import numpy as np
import tensorflow as tf
from PIL import Image
from google.cloud import storage

# Define your custom optimizer (if it's a custom implementation)
# custom_optimizer = ...

# Load the model, passing custom_objects argument
# model = load_model('your_model.h5', custom_objects={'CustomAdam': custom_optimizer})

model = None
interpreter = None
input_index = None
output_index = None

class_names = ["Early Blight", "Late Blight", "Healthy"]

BUCKET_NAME = "ml_models_tf" # Here you need to put the name of your GCP bucket


def download_blob(bucket_name, source_blob_name, destination_file_name):
    """Downloads a blob from the bucket."""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(source_blob_name)

    blob.download_to_filename(destination_file_name)

    print(f"Blob {source_blob_name} downloaded to {destination_file_name}.")

# Define your custom optimizer class
# class CustomAdam(tf.keras.optimizers.Adam):
#     # Define your custom implementation if needed
#     pass

def predict(request):
    global model
    if model is None:
        download_blob(
            BUCKET_NAME,
            "my_models/potatoes.h5",
            "/tmp/potatoes.h5",
        )
        # custom_objects = {'CustomAdam': CustomAdam}
        # Load the Adam optimizer from the tensorflow.keras.optimizers module
        # Adam = tf.keras.optimizers.Adam

        # Load the trained ML model
        # with tf.device('/cpu:0'):
        #     model = tf.keras.models.load_model("/tmp/potatoes.h5",
        #                                        custom_objects={'Adam': Adam})
        model = tf.keras.models.load_model("/tmp/potatoes.h5",compile=False)

    image = request.files["file"]

    image = np.array(
        Image.open(image).convert("RGB").resize((256, 256)) # image resizing
    )

    image = image/255 # normalize the image in 0 to 1 range

    img_array = tf.expand_dims(image, 0)
    predictions = model.predict(img_array)

    print("Predictions:",predictions)

    predicted_class = class_names[np.argmax(predictions[0])]
    confidence = round(100 * (np.max(predictions[0])), 2)

    return {"class": predicted_class, "confidence": confidence}

