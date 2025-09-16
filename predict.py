import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import json
import os
from PIL import Image

# Load model
model = load_model("model_batik.h5")

# Define image size (as used during training)
IMG_SIZE = (150, 150)

# Load label mapping
label_map = {}
if os.path.exists("label_map.json"):
    with open("label_map.json", "r") as f:
        label_map = json.load(f)
    label_map = {v: k for k, v in label_map.items()}  # reverse mapping

# Load metadata
metadata = {}
if os.path.exists("metadata.json"):
    with open("metadata.json", "r") as f:
        metadata = json.load(f)

def predict_batik(image_path):
    # Load and preprocess image
    img = Image.open(image_path).convert("RGB")
    img = img.resize(IMG_SIZE)
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Predict
    predictions = model.predict(img_array)
    predicted_class = np.argmax(predictions, axis=1)[0]
    confidence = float(np.max(predictions))

    # Map to class label
    class_name = label_map.get(predicted_class, str(predicted_class))

    # Get metadata info
    motif_info = metadata.get(class_name, {
        "origin": "-",
        "philosophy": "-",
        "history": "-",
        "colors": [],
        "usage": "-"
    })

    # Return final response
    return {
        "prediction": class_name,
        "confidence": round(confidence, 4),
        "info": motif_info
    }

# Optional: test locally
if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python predict.py <image_path>")
    else:
        result = predict_batik(sys.argv[1])
        print(json.dumps(result, indent=2, ensure_ascii=False))
