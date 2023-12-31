from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MODEL = tf.keras.models.load_model("../saved_models/1")

CLASS_NAMES = ["Early Blight", "Late Blight", "Healthy"]


@app.get("/ping")
async def ping():
    return "Hello, I am alive"
# to make sure the server is alive

def read_file_as_image(data) -> np.ndarray:
    img=Image.open(BytesIO(data))
    resized_img = img.resize((256, 256))
    image = np.array(resized_img)
    # image = np.array(Image.open(BytesIO(data)))
    # Resize the image to 256x256
    # resized_img = image.resize((256, 256))
    return image


@app.post("/predict")
async def predict(
        file: UploadFile = File(...)
):
    image = read_file_as_image(await file.read())
    img_batch = np.expand_dims(image, 0)#add dimension at row level when axis=0

    predictions = MODEL.predict(img_batch)

    predicted_class = CLASS_NAMES[np.argmax(predictions[0])]
    confidence = np.max(predictions[0])
    return {
        'class': predicted_class,
        'confidence': float(confidence)
    }


if __name__ == "__main__":
    uvicorn.run(app, host='localhost', port=8000)