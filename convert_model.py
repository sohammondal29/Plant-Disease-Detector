import tensorflow as tf

print("TensorFlow version:", tf.__version__)

# load old model
model = tf.keras.models.load_model(
    "plant_disease_prediction_model.h5",
    compile=False
)

# save it in the new keras format
model.save("plant_model_fixed.keras")

print("Model successfully converted")
