from tkinter import *
from PIL import Image, ImageTk#работа с изображениями
import requests
from io import BytesIO #io-работа с вводом, выводом информации. BytesIO-работа с байтами

from pygame.examples.cursors import image


def load_image():#создаем функцию загрузки изображений
    try:#обрабатываем исключения
        response = requests.get(url)#получаем ответ-response,
        # после того как сделали запрос-requests.get по ссылке-url
        response.raise_for_status()#строчка нужна для обработки исключений.
        # если будет какая-то ошибка, то сдесь мы ее и получим
        image_data = BytesIO(response.content)#делаем изображение:
        # в переменную-image_data положим обработанное изображение
        img = Image.open(image_data)#делаем изображение нормальной картинкой
        return ImageTk.PhotoImage(img)#функция вернет картинку-img
    except Exception as e:#если ошибка
        print(f"Произошла ошибка: {e}")
        return None#если произошла ошибка, то функция ничего не вернет

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
