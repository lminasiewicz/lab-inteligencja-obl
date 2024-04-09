import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns 
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Flatten, MaxPooling2D
from tensorflow.keras.utils import to_categorical
from sklearn.metrics import confusion_matrix
from tensorflow.keras.callbacks import History

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

train_images = train_images.reshape((train_images.shape[0], 28, 28, 1)).astype('float32') / 255
test_images = test_images.reshape((test_images.shape[0], 28, 28, 1)).astype('float32') / 255

train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)
original_test_labels = np.argmax(test_labels, axis=1)

model = Sequential([
    Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(64, activation='relu'),
    Dense(10, activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

history = History()
model.fit(train_images, train_labels, epochs=5, batch_size=64, validation_split=0.2, callbacks=[history])
print(history.history)

test_loss, test_acc=model.evaluate(test_images, test_labels)
print(f"Test accuracy: {test_acc:.4f}")

predictions = model.predict(test_images)
predicted_labels = np.argmax(predictions, axis=1)

# Confusion matrix
cm = confusion_matrix(original_test_labels, predicted_labels)
plt.figure(figsize=(10, 7))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.xlabel('Predicted')
plt.ylabel('True')
plt.title('Confusion Matrix')
plt.show()

# Plotting training and validation accuracy
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='Training Accuracy')
plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.grid(True, linestyle='--', color='grey')
plt.legend()

# Plotting training and validation loss
plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.grid(True, linestyle='--', color='grey')
plt.legend()
plt.tight_layout()
plt.show()

# Display 25 images from the test set with their predicted labels
plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(test_images[i].reshape(28,28), cmap=plt.cm.binary)
    plt.xlabel(predicted_labels[i])
plt.show()

model.save('cyfry_model.keras')



# a) Co się dzieje w preprocessing? Do czego służy funkcja reshape, to_categorical i np.argmax?

# reshape służy do zmieniania kształtu tablicy, wraz z możliwością zmiany liczby wymiarów tablicy
# zależnie od parametrów. to_categorical to funkcja, która jest w stanie zamienić klasy numeryczne na
# formę tablicy binarnej (chociaż szczerze mówiąc nie wiem po co to jest).
# np.argmax to funkcja która zwraca największą wartość w tablicy. W przypadku wyznaczenia opcjonalnego
# parametru axis, funkcja ta zwróci listę indeksów największych elementów w każdej osi wyznaczonej przez
# parametr opcjonalny axis.

# b) Jak dane przepływają przez sieć i jak się w niej transformują? Co każda z warstw dostaje na wejście i co wyrzuca na wyjściu?
# Conv2D: Warstwa konwolucyjna, która przyjmuje obraz jako macierz i filtruje go 32 fitlrami 3x3 idąc co 1 piksel.
# MaxPooling2D: Warstwa max-pooling, która redukuje obraz redukując każdy kwadrat 2x2 tylko do jego najjaśniejszego (max) piksela.
# Flatten: Warstwa która spłaszcza obraz (macierz) do 1 wymiarowej tablicy w celu późniejszego przetwarzania przez warstwy w pełni połączone (Dense)
# Dense: Standardowa warstwa sieci neuronowej. Ostatnia z nich ma 10 neuronów, co oznacza, że mamy 10 możliwych klas, co pokrywa się z naszymi danymi.

# c) Jakich błędów na macierzy błędów jest najwięcej. Które cyfry są często mylone z jakimi innymi?

#Najwięcej (bo 14) w moim przypadku było błędów True=6, Predicted=5. Czyli model oznaczył cyfrę 6 jako 5.

# d) Co możesz powiedzieć o krzywych uczenia się. Czy mamy przypadek przeuczenia lub niedouczenia się?

# Wydaje się być w granicach nazwania tego good fit, ale wciąż jest troszkę dystansu między krzywymi, i obie wydają się wciąż iść w dół,
# co sugeruje, że wypadałoby chyba jeszcze trochę podtrenować model aby osiągnąć optymalne wyniki.

# e) Można zdefiniować niestandardowy callback (klasę dziedziczącą po keras.callbacks.Callback), zapisać w nim wartość najmniejszego wyniku funkcji straty,
# oraz napisać w nim metodę on_epoch_end w której warunkowo ustawi się nową wartość najlepszego wyniku funkcji straty oraz jeśli nowy wynik jest lepszy od poprzedniego
# to zapisać model za pomocą self.model.save().