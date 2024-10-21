from cProfile import label
from tkinter import *
from PIL import Image, ImageTk#работа с изображениями
import requests
from io import BytesIO#io-работа с вводом, выводом информации. BytesIO-работа с байтами

from Scripts.графический_редактор_с_метками_для_изменения_цвета_и_загрузкой_изображений_из_файла import load_image
from выводим_список_папок_в_консоль import window

window = Tk()#создаем окно
window.title("Cats!")#заголовок окна
window.geometry("600x480")#размер окна

label = Label()#создаем метку, на которую будем выводить изображение
label.pack()

url = "https://cataas.com/cat"#url-адрес в интернете, по которому будем искать картинки
img = load_image(url)#создаем функцию загрузки изображений

if img:#делаем проверку: если img не пустая
    label.config(image=img)#изменяем параметр image присваивая ей  img.
    # таким способом устанавливаем картинку на метку
    label.image = img#для того, чтобы сборщик мусора не убрал картинку

window.mainloop()
