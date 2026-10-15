# 🐱🐶 Cat vs Dog Image Classifier

A deep learning application that classifies an uploaded image as either a **cat** or a **dog** using TensorFlow, transfer learning, and MobileNetV2.

## 📌 Project Overview

This project uses a pretrained MobileNetV2 model to extract image features and classify images into two categories: Cat and Dog. A Streamlit web interface allows users to upload an image and view the model's prediction.

## ✨ Features

- Upload images in JPG, JPEG, or PNG format
- Classify images as Cat or Dog
- Use a pretrained MobileNetV2 model
- Interactive web interface built with Streamlit

## 🛠️ Technologies Used

- Python
- TensorFlow / Keras
- MobileNetV2
- NumPy
- Pillow
- Streamlit

## 🧠 Model Details

- **Architecture:** MobileNetV2 with a custom classification head
- **Transfer learning:** Pretrained base model with frozen weights
- **Output layer:** Sigmoid activation for binary classification
- **Loss function:** Binary cross-entropy
- **Optimizer:** Adam
- **Input image size:** 224 × 224 pixels
- **Training:** 5 epochs on a subset of 1,000 images (500 cats and 500 dogs)

## 📂 Project Structure

```text
cat-dog-cnn-classifier/
├── app.py
├── cat_dog_mobilenet.keras
├── requirements.txt
├── .gitignore
└── README.md
```

## 🚀 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/Krishna1187/cat-dog-cnn-classifier.git
cd cat-dog-cnn-classifier
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
```

On Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Launch the application

```bash
streamlit run app.py
```

Open the local URL displayed in the terminal.

## 📸 Application Preview

Add a screenshot of the running Streamlit application here when available.

## 🎯 Learning Outcomes

- Understanding transfer learning in computer vision
- Using a pretrained CNN for image classification
- Preparing images for model inference
- Saving and loading Keras models
- Building a simple deep learning web application with Streamlit

## ⚠️ Limitations

This project was trained on a limited subset of images for learning purposes. Its predictions may be inaccurate on unfamiliar images.

## 👨‍💻 Author

**Krishna Mishra**

GitHub: [Krishna1187](https://github.com/Krishna1187)

---

If you find this project useful, feel free to explore the code and suggest improvements.