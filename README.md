# Backend-BatikEye

## Description

This is the backend for the BatikEye project. It provides an API for identifying batik patterns in images.

## Purpose

The purpose of this backend is to provide a scalable and reliable API for identifying batik patterns.

## Functionality

The backend provides the following functionality:

*   Identifies batik patterns in images.
*   Returns the identified batik pattern and its confidence score.

## Model

The backend uses a convolutional neural network (CNN) model trained on a dataset of batik images. The model is stored in the `model_batik.h5` file.

## API Endpoints

### `POST /predict`

Identifies batik patterns in an image.

**Request Body:**

```json
{
    "image": "base64 encoded image"
}
```

**Response Body:**

```json
{
    "pattern": "name of the batik pattern",
    "confidence": 0.95
}
```

## Setup

1.  Clone the repository:

    ```bash
    git clone https://github.com/username/Backend-BatikEye.git
    ```
2.  Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  Run the backend:

    ```bash
    python main.py
    ```
2.  Send a POST request to the `/predict` endpoint with a base64 encoded image in the request body.

## Dependencies

*   Flask
*   TensorFlow
*   Keras
*   Pillow
*   requests
