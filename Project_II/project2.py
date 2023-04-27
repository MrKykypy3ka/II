import tensorflow as tf
from tensorflow.keras.datasets import mnist
from keras.datasets import mnist
from tkinter import *
from tkinter import filedialog
import tkinter as tk
import win32gui
from PIL import ImageGrab, Image
import numpy as np


# Загружаем сохраненную модель
model = tf.keras.models.load_model('mnist.h5')


class App(tk.Tk):
    # Графический интерфейс
    def __init__(self):
        tk.Tk.__init__(self)
        self.x = self.y = 0
        self.canvas = tk.Canvas(self, width=100, height=100, bg="white", cursor="cross")
        self.label = tk.Label(self, text="0", font=("Helvetica", 24))
        self.classify_btn = tk.Button(self, text="Распознать", command=self.classify_handwriting)
        self.button_clear = tk.Button(self, text="Очистить", command=self.clear_all)
        self.button_load = tk.Button(self, text="Выбрать файл", command=self.open_file_dialog)
        self.button_edu = tk.Button(self, text="Обучить", command=self.train_model)
        self.canvas.grid(row=0, column=0, pady=2, sticky=W, )
        self.label.grid(row=0, column=1, pady=2, padx=2)
        self.classify_btn.grid(row=1, column=1, pady=2, padx=2)
        self.button_clear.grid(row=1, column=0, pady=2)
        self.button_load.grid(row=2, column=1, pady=2)
        self.button_edu.grid(row=2, column=0, pady=2)
        self.canvas.bind("<B1-Motion>", self.draw_lines)
        self.title("Беседин О.А.")
        self.iconbitmap("ico.ico")
        self.geometry("230x170")

    def train_model(self):
        # Загружаем набор данных MNIST
        (x_train, y_train), (x_test, y_test) = mnist.load_data()
        # Преобразуем данные и нормализуем их
        x_train = x_train.reshape((60000, 28, 28, 1))
        x_test = x_test.reshape((10000, 28, 28, 1))
        x_train, x_test = x_train / 255.0, x_test / 255.0
        # Определяем модель нейронной сети
        model = tf.keras.models.Sequential([
            # входной слой
            tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
            tf.keras.layers.MaxPooling2D((2, 2)),
            tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
            tf.keras.layers.MaxPooling2D((2, 2)),
            tf.keras.layers.Flatten(),
            # скрытый слой
            tf.keras.layers.Dense(64, activation='relu'),
            # выходной слой
            tf.keras.layers.Dense(10, activation='softmax')
        ])
        # Компилируем модель
        model.compile(optimizer='adam',
                      loss='sparse_categorical_crossentropy',
                      metrics=['accuracy'])
        # Обучаем модель
        model.fit(x_train, y_train, epochs=5, validation_data=(x_test, y_test))
        # Сохраняем модель
        model.save('mnist.h5')

    def open_file_dialog(self):
        filename = filedialog.askopenfilename()
        im = Image.open(filename)
        # преобразование изображения в черно-белое и массив numpy, и нормализация значений пикселей
        image_array = np.array(im.resize((28, 28)).convert('L')) / 255.0
        # изменение размерности массива до формы (1, 28, 28, 1)
        image_array = image_array.reshape((1, 28, 28, 1))
        # Делаем предсказание
        predictions = model.predict(image_array)
        digit = np.argmax(predictions)
        self.label.configure(text=str(digit))

    def clear_all(self):
        self.canvas.delete("all")

    def classify_handwriting(self, ):
        HWND = self.canvas.winfo_id()
        rect = win32gui.GetWindowRect(HWND)
        im = ImageGrab.grab(rect)
        # преобразование изображения в черно-белое и массив numpy, и нормализация значений пикселей
        image_array = np.array(im.resize((28, 28)).convert('L')) / 255.0
        # изменение размерности массива до формы (1, 28, 28, 1)
        image_array = image_array.reshape((1, 28, 28, 1))
        # Делаем предсказание
        predictions = model.predict(image_array)
        digit = np.argmax(predictions)
        self.label.configure(text=str(digit))

    def draw_lines(self, event):
        self.x = event.x
        self.y = event.y
        r = 3
        self.canvas.create_oval(self.x - r, self.y - r, self.x + r, self.y + r, fill='black')


app = App()
mainloop()
