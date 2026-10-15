
import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

model = tf.keras.models.load_model("cat_dog_mobilenet.keras")

st.title("Cat vs Dog Classifier")

file = st.file_uploader("Upload a cat or dog image", type=["jpg", "jpeg", "png"])

if file:
    img = Image.open(file).convert("RGB").resize((224, 224))
    st.image(img)

    x = np.array(img)
    x = np.expand_dims(x, axis=0)
    score = model.predict(x, verbose=0)[0][0]

    result = "Dog" if score >= 0.5 else "Cat"
    st.subheader("Prediction: " + result)
