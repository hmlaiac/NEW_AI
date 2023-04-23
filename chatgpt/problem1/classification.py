import tensorflow as tf
from tensorflow import keras

# Load the dataset
train_dataset = keras.preprocessing.image_dataset_from_directory(
    'dataset/train',
    image_size=(224, 224),
    batch_size=32,
    label_mode='binary'
)
val_dataset = keras.preprocessing.image_dataset_from_directory(
    'dataset/val',
    image_size=(224, 224),
    batch_size=32,
    label_mode='binary'
)

# Prepare the dataset
train_dataset = train_dataset.map(lambda x, y: (x / 255.0, y))
val_dataset = val_dataset.map(lambda x, y: (x / 255.0, y))

# Define the model
model = keras.Sequential([
    keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(224, 224, 3)),
    keras.layers.MaxPooling2D((2, 2)),
    keras.layers.Conv2D(64, (3, 3), activation='relu'),
    keras.layers.MaxPooling2D((2, 2)),
    keras.layers.Conv2D(128, (3, 3), activation='relu'),
    keras.layers.MaxPooling2D((2, 2)),
    keras.layers.Flatten(),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Train the model
model.fit(train_dataset, validation_data=val_dataset, epochs=10)

# Test the model
test_image = keras.preprocessing.image.load_img('test_image.jpg', target_size=(224, 224))
test_image = keras.preprocessing.image.img_to_array(test_image) / 255.0
test_image = np.expand_dims(test_image, axis=0)
prediction = model.predict(test_image)

if prediction[0][0] > 0.5:
    print('Basketball')
else:
    print('Not a basketball')