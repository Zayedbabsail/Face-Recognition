# Face Recognition System

## Overview
This project implements a face recognition system using OpenCV. It involves three main steps:
1. **Data Collection**: Capture images of faces from a video feed.
2. **Training**: Train a face recognition model using Local Binary Patterns Histogram (LBPH).
3. **Testing**: Test the trained model by recognizing faces in real-time video streams.

The project also utilizes Haar Cascade classifiers to detect faces.

## Project Structure
```
├── datacollection.py     # Script for capturing and saving face images.
├── training.py           # Script for training the LBPH face recognizer.
├── testing.py            # Script for testing the trained model in real-time.
├── haarcascade_frontalface_default.xml  # Pre-trained Haar Cascade classifier for face detection.
└── datasets/             # Directory where captured face images are saved.
```

## Requirements
To run this project, you need the following Python libraries:
- `opencv-python`
- `opencv-contrib-python`
- `numpy`
- `Pillow`

Install these dependencies using the following command:
```bash
pip install opencv-python opencv-contrib-python numpy Pillow
```

## Files Description

### 1. **Data Collection** (`datacollection.py`)
- **Description**: Captures face images from a live video feed and saves them in the `datasets/` directory. Each image is labeled with the user ID and a serial number.
- **How it Works**:
  - Prompts the user for an ID.
  - Detects faces using the Haar Cascade classifier.
  - Saves 500 images of the face in grayscale format.
- **Usage**: 
  ```bash
  python datacollection.py
  ```
- Ensure that the `haarcascade_frontalface_default.xml` file is in the same directory or provide the correct path to it.

### 2. **Training** (`training.py`)
- **Description**: Trains an LBPH face recognizer on the face images saved in the `datasets/` folder.
- **How it Works**:
  - Reads images from the `datasets/` folder.
  - Converts the images to NumPy arrays.
  - Extracts the face ID from the filename and trains the LBPH recognizer.
  - Saves the trained model as `trainer.yml`.
- **Usage**:
  ```bash
  python training.py
  ```

### 3. **Testing** (`testing.py`)
- **Description**: Uses the trained LBPH face recognizer to identify faces in real-time video streams.
- **How it Works**:
  - Loads the trained model (`trainer.yml`).
  - Detects faces using Haar Cascade classifier.
  - Predicts the identity of detected faces using the LBPH recognizer.
  - Displays the predicted name on the video feed.
- **Usage**:
  ```bash
  python testing.py
  ```

### 4. **Haar Cascade Classifier** (`haarcascade_frontalface_default.xml`)
- **Description**: This is a pre-trained model for detecting faces using the Haar Cascade method. Download it from the OpenCV repository:
  [Haar Cascade for Face Detection](https://github.com/opencv/opencv/blob/4.x/data/haarcascades/haarcascade_frontalface_default.xml)

## How to Use

### 1. **Data Collection**:
- Run `datacollection.py`.
- Enter a unique user ID when prompted.
- The script will capture 500 face images from the webcam.

### 2. **Training**:
- Run `training.py`.
- The script will process the images from the `datasets/` folder and train the model.
- After training, it saves the model as `trainer.yml`.

### 3. **Testing**:
- Run `testing.py`.
- The script will use your webcam to detect and identify faces in real-time based on the trained model.

### Notes:
- To add more users, simply rerun `datacollection.py` with a new ID and retrain the model by running `training.py`.
- You can update the `name_list` in `testing.py` with the actual names corresponding to the user IDs.
