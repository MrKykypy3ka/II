# Проект по дисциплине "Системы искусственного интеллекта"
## Проект находится в папке "Project_II"
Эта программа представляет собой простое графическое приложение на Python с использованием библиотек TensorFlow и Tkinter для распознавания написанных пользователем цифр.

Сначала программа загружает обученную модель нейронной сети, которая была предварительно обучена на наборе данных MNIST (набор цифровых изображений размером 28x28 пикселей). Затем пользователь может нарисовать цифру в окошке с помощью мыши, а затем нажать кнопку «Распознать», чтобы приложение попыталось определить, какая цифра была нарисована.

Если пользователь хочет использовать уже существующее изображение вместо рисования, он может нажать кнопку «Выбрать файл», чтобы выбрать изображение из файловой системы.

Если пользователь хочет обучить модель заново, то он может нажать кнопку «Обучить». При этом загрузятся данные из набора данных MNIST, затем данные будут преобразованы и нормализованы, и наконец, модель будет обучена на этих данных. Обученная модель будет сохранена в файл mnist.h5.

Оставшиеся строки кода относятся к созданию графического интерфейса. Он использует Tkinter для создания окна приложения и элементов управления, таких как кнопки, метки и холст, на котором пользователь может рисовать. Кнопки «Распознать» и «Очистить» имеют соответствующие функции, которые вызываются при нажатии кнопки. При нажатии на кнопку "Выбрать файл" вызывается функция open_file_dialog, которая открывает диалоговое окно для выбора файла с изображением. Функция classify_handwriting используется для обработки изображения, нарисованного пользователем на холсте, а функция draw_lines отслеживает движение мыши пользователя для создания линий на холсте.