from tkinter import *
from PIL import Image, ImageTk#работа с изображениями
import requests
from io import BytesIO #io-работа с вводом, выводом информации. BytesIO-работа с байтами


def load_image(url):#создаем функцию загрузки изображений
    try:#обрабатываем исключения
        response = requests.get(url)#получаем ответ-response,
        # после того как сделали запрос-requests.get по ссылке-url
        response.raise_for_status()#строчка нужна для обработки исключений.
        # если будет какая-то ошибка, то сдесь мы ее и получим
        image_data = BytesIO(response.content)#делаем изображение:
        # в переменную-image_data положим обработанное изображение
        img = Image.open(image_data)#делаем изображение нормальной картинкой
        img.thumbnail((600, 480), Image.Resampling.LANCZOS)#создаем окно для изображения,
        # чтобы все изображения были одного размера. Image.Resampling.LANCZOS-для того,
        # чтобы качество картинки не ухудшалось, когда мы изменяум ее размер
        return ImageTk.PhotoImage(img)#функция вернет картинку-img
    except Exception as e:#если ошибка
        print(f"Произошла ошибка: {e}")
        return None#если произошла ошибка, то функция ничего не вернет

def open_new_window():#создаем функцию для открытия нового окна для каждой картинки
    img = load_image(url)  # создаем функцию загрузки изображений

    if img:  # делаем проверку: если img не пустая
        new_window = Toplevel()#создаем окно
        new_window.title("Картинка с котиком")#задаем заголовок окну
        new_window.geometry("600x480")#задаем размер окну
        label = Label(new_window, image=img)  # создаем метку в новом окне, на которую будем выводить изображение.
        # и изображение(image) положим в img
        label.pack()
        label.image = img  # для того, чтобы сборщик мусора не убрал картинку

def exit():#создаем функцию выхода
    window.destroy()#уничтожаем окно


window = Tk()#создаем окно
window.title("Cats!")#заголовок окна
window.geometry("600x520")#размер окна



menu_bar = Menu(window)#создаем меню
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Загрузить фото", command=set_image)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=exit)



url = "https://cataas.com/cat"#url-адрес в интернете, по которому будем искать картинки

set_image()#функция, при запуске которой появляется первая картинка

window.mainloop()
