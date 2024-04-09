import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns 
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Flatten, MaxPooling2D
from tensorflow.keras.utils import to_categorical
from sklearn.metrics import confusion_matrix
from tensorflow.keras.callbacks import History
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from PIL import Image


def get_model() -> Sequential:
    model = Sequential([
        Conv2D(32, (3, 3), activation='relu', input_shape=(40, 40, 3)),
        MaxPooling2D((2, 2)),
        Conv2D(32, (3, 3), activation='relu', input_shape=(40, 40, 3)),
        MaxPooling2D((2, 2)),
        Flatten(),
        Dense(128, activation='relu'),
        Dense(64, activation='relu'),
        Dense(1, activation='sigmoid'),
    ])
    model.compile(loss='binary_crossentropy', metrics=['accuracy'])
    return model


def diagnostics(history: History) -> None:
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.plot(history.history['accuracy'], label='Training Accuracy')
    plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
    plt.xlabel('Epoch')
    plt.ylabel('Accuracy')
    plt.grid(True, linestyle='--', color='grey')
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(history.history['loss'], label='Training Loss')
    plt.plot(history.history['val_loss'], label='Validation Loss')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.grid(True, linestyle='--', color='grey')
    plt.legend()
    plt.tight_layout()
    plt.show()


model = get_model()
generator = ImageDataGenerator(rescale=(1.0/255.0))


trainer = generator.flow_from_directory('dogs-cats-mini/train/',
    class_mode='binary', batch_size=64, target_size=(40, 40))
tester = generator.flow_from_directory('dogs-cats-mini/test/',
    class_mode='binary', batch_size=64, target_size=(40, 40))


history = History()
model.fit_generator(trainer, steps_per_epoch=len(trainer), validation_data=tester,
                    validation_steps=len(tester), epochs=12, callbacks=[history])

_, acc = model.evaluate_generator(tester, steps=len(tester))
print(f"Accuracy: {acc*100}%")

diagnostics(history)


