import numpy as np
import matplotlib.pyplot as plt 
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import plot_model

# Load the iris dataset
iris =load_iris()
X = iris.data
y = iris.target

# Preprocess the data
# Scale the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Encode the labels
encoder = OneHotEncoder(sparse_output=False)
y_encoded = encoder.fit_transform(y.reshape(-1, 1))

# Split the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_encoded, test_size=0.3, random_state=41)

# Define the model
model = Sequential([
    Dense(64, activation='tanh', input_shape=(X_train.shape[1],)),
    Dense(64, activation='tanh'),
    Dense(y_encoded.shape[1], activation='softmax')
    ])

# Compile the model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Train the model
history = model.fit(X_train, y_train, epochs=100, validation_split=0.2)

# Evaluate the model on the test set
test_loss, test_accuracy = model.evaluate(X_test, y_test, verbose=0)
print(f"Test Accuracy: {test_accuracy*100:.2f}%")

# Plot the learning curve
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='train accuracy')
plt.plot(history.history['val_accuracy'], label='validation accuracy')
plt.title('Model accuracy')
plt.ylabel('Accuracy')
plt.xlabel('Epoch')
plt.grid(True, linestyle='--', color='grey')
plt.legend()
plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='train loss')
plt.plot(history.history['val_loss'], label='validation loss')
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.grid(True, linestyle='--', color='grey')
plt.legend()
plt.tight_layout()
plt.show()

# Save the model
model.save('iris_model.keras')

# Plot and save the model architecture
plot_model(model, to_file='model_plot.png', show_shapes=True, show_layer_names=True)



# PYTANIA
# a) Co robi StandardScaler? Jak transformowane są dane liczbowe?

# StandardScaler, wg. dokumentacji scikit-learn.preprocessing, skaluje dane
# odejmując od każdej danej osobno średnią wszystkich, i dzieląc przez odchylenie standardowe wszystkich.

# b) Czym jest OneHotEncoder (i kodowanie „one hot” ogólnie)? Jak etykiety klas są transformowane przez ten encoder?

# OneHotEncoder to klasa obiektów zdolna do kodowania one-hot.
# Kodowanie one-hot zamienia dane w jednej kolumnie na grupę kolumn z wartościami binarnymi.
# np. kolumnę "Fruits" z wartościami "Apple" i "Banana" zamieni na 2 kolumny o nazwie "Apple" i "Banana" z wartościami
# binarnymi 1 lub 0 zależnie od tego, który owoc wystąpił na tym miejscu w oryginalnej kolumnie "Fruits".

# c) Model ma 4 warstwy: wejściową, dwie ukryte warstwy z 64 neuronami każda i warstwę wyjściową. 
# Ile neuronów ma warstwa wejściowa i co oznacza X_train.shape[1]? Ile neuronów ma warstwa wyjściowa i co oznacza y_encoded.shape[1]?

# Warstwa wejściowa siłą rzeczy musi mieć 4 neurony - 1 na każdą kolumnę danych. To model, po odpowiednim treningu
# na dostępnych danych, ma stwierdzić jaką wagę przypisuje każdej z kolumn.
# w obu przypadkach (X_train oraz y_encoded) pole shape zawiera tablicę wymiarów zmiennej typu numpy.ndarray.
# To oznacza, że shape[1] oznacza ilość kolumn. 
# Warstwa wyjściowa ma 3 neurony. Jeden na każdy możliwy "werdykt".

# d) Czy funkcja aktywacji relu jest najlepsza do tego zadania? Spróbuj użyć innej funkcji i obejrzyj wynik

# Nie, nie jest. W moim przypadku zastosowanie funkcji aktywacji tanh (tangens hiperboliczny) uzyskał o wiele lepsze wyniki
# (funkcja straty z ponad 2x mniejszą wartością, brak problemu overfittingu w 100 epokach)

# e) Model jest konfigurowany do treningu za pomocą polecenia compile. Tutaj wybieramy optymalizator 
# (algorytm, który używa gradientu straty do aktualizacji wag), funkcję straty, metrykę do oceny modelu.
# Eksperymentuj ze zmianą tych parametrów na inne i uruchom program. Czy różne optymalizatory lub funkcje straty dają różne wyniki?
#  Czy możemy dostosować szybkość uczenia się w optymalizatorze? 

# Tak, oczywiście, że dają różne wyniki. Trochę bez sensu by było, gdyby zmiana parametrów nic nie zmieniała...
# Da się dostosować szybkość uczenia się w optymalizatorze. W tym celu możemy skorzystać z obiektu keras.optimizers.<nazwa>
# zamiast prostego stringa podanego na przykładzie keras-iris.py (który działa, ale tylko na domyślnych parametrach).

# f) W linii model.fit sieć neuronowa jest trenowana. Czy jest sposób, by zmodyfikować tę linię tak, 
# aby rozmiar partii był równy 4 lub 8 lub 16? Jak wyglądają krzywe uczenia się dla różnych parametrów? 
# Jak zmiana partii wpływa na kształt krzywych? Wypróbuj różne wartości i uruchom program. 

# Owszem, da się, za pomocą opcjonalnego parametru batch_size. Po wypróbowaniu batch_size = 4, 8, 16,
# model osiągnął najlepsze wyniki (najniższa wartość funkcji błędu) przy batch_size = 16.
# W moich testach batch_size = 8 lub 16 polepszył trochę wynik funkcji błędu. batch_size = 4
# trochę pogorszył wynik oraz wcześnie zaczął overfitting.

# g) Co możesz powiedzieć o wydajności sieci neuronowej na podstawie krzywych uczenia? 
# W której epoce sieć osiągnęła najlepszą wydajność? 
# Czy ta krzywa sugeruje dobrze dopasowany model, czy mamy do czynienia z niedouczeniem lub przeuczeniem?

# W moim przypadku po zastosowaniu i zostaniu przy funkcji aktywacji tanh, każdy model, który próbowałem
# osiągał najlepsze wyniki w ostatniej epoce. Sugeruje to, że wyniki mogłyby być jeszcze trochę lepsze przy
# nieco dłuższym treningu. Krzywa natomiast sugeruje dobrze dopasowany model.

# TODO: podpunkt h)