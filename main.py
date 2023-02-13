from kivy.config import Config

# config
Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 850)
Config.set('graphics', 'height', 700)

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from math import pi
import math


class Application(App):
    def click(self, instance):
        self.label.text = 'Спасибо что нажал!'

    def click2(self, instance):
        a = int(self.text.text)
        o = a * (pi / 180)
        self.label.text = f'{a} градусов = {o} радиан'

    def click3(self, instance):
        self.label.text = 'Вывод данных: '
        self.text.text = ' '

    def sqrt(self, instance):
        global a, b
        a = int(self.text.text)
        b = a ** 0.5
        self.label.text = f'Квадратный корень из числа - {a} = {b}'

    def poisk_x(self, instance):
        global a, b, c, x1, x2, d
        ur = self.text.text.split()

        a = int(ur[0])
        b = int(ur[1])
        c = int(ur[2])
        d = b ** 2 - (4 * a * c)

        if d > 0:
            x1 = (-b + (d ** 0.5)) / (2 * a)
            x2 = (-b - (d ** 0.5)) / (2 * a)
            self.label.text = f'Уравнение решено успешно!\nX1 = {x1}, X2 = {x2}'
        elif d == 0:
            x = -b / (2 * a)
            self.label.text = f'Уравнение решено успешно!\nX = {x}'
        elif d < 0:
            self.label.text = f'Уравнение не возможно решить\nтак как дискриминант меньше 0'

    def factorial(self, instance):
        global a, b
        a = int(self.text.text)
        b = math.factorial(a)
        self.label.text = f'Факториал числа - {a} = {b}'

    def update_label(self):
        self.lbl.text = self.formula

    def add_number(self, instance):
        if (self.formula == '0'):
            self.formula = ''
        self.formula += str(instance.text)
        self.update_label()

    def add_operation(self, instance):
        if (str(instance.text).lower() == 'x'):
            self.formula += '*'
        elif (str(instance.text).lower() == 'sqr'):
            self.formula += '**0.5'
        else:
            self.formula += str(instance.text)
        self.update_label()

    def clear(self, instance):
        self.formula = '0'
        self.lbl.text = '0'

    def cals_result(self, instance):
        self.lbl.text = str(eval(self.lbl.text))
        self.formula = self.lbl.text

    def clear1(self, instance):
        self.text1.text = ' '
        self.text2.text = ' '
        self.text3.text = ' '
        self.lbl1.text = 'Выходные данные'

    def sin_A(self, instance):
        a = int(self.text1.text)
        b = int(self.text2.text)
        c = int(self.text3.text)
        o = a / c
        self.lbl1.text = f'Синус = {o}'

    def sin_B(self, instance):
        a = int(self.text1.text)
        b = int(self.text2.text)
        c = int(self.text3.text)
        o = b / c
        self.lbl1.text = f'Синус = {o}'

    def sin_C(self, instance):
        self.lbl1.text = f'Синус = 1'

    def cosin_A(self, instance):
        a = int(self.text1.text)
        b = int(self.text2.text)
        c = int(self.text3.text)
        o = b / c
        self.lbl1.text = f'Косинус = {o}'

    def cosin_B(self, instance):
        a = int(self.text1.text)
        b = int(self.text2.text)
        c = int(self.text3.text)
        o = a / c
        self.lbl1.text = f'Косинус = {o}'

    def cosin_C(self, instance):
        self.lbl1.text = f'Косинус = 0'

    def tg_A(self, instance):
        a = int(self.text1.text)
        b = int(self.text2.text)
        c = int(self.text3.text)
        o = a / b
        self.lbl1.text = f'Тангенс = {o}'

    def tg_B(self, instance):
        a = int(self.text1.text)
        b = int(self.text2.text)
        c = int(self.text3.text)
        o = b / a
        self.lbl1.text = f'Тангенс = {o}'

    def tg_C(self, instance):
        self.lbl1.text = f'У угла нет тангенса'

    def ctg_A(self, instance):
        a = int(self.text1.text)
        b = int(self.text2.text)
        c = int(self.text3.text)
        o = b / a
        self.lbl1.text = f'Катангенс = {o}'

    def ctg_B(self, instance):
        a = int(self.text1.text)
        b = int(self.text2.text)
        c = int(self.text3.text)
        o = a / b
        self.lbl1.text = f'Катангенс = {o}'

    def ctg_C(self, instance):
        self.lbl1.text = f'Катангенс = 0'

    def build(self):
        # Создание экранов
        self.sm = ScreenManager()
        screen1 = Screen(name='calculator screen')
        screen2 = Screen(name='functions screen')
        screen3 = Screen(name='treug')

        # Calculator
        self.formula = '0'
        bl = BoxLayout(orientation='vertical', padding=25)
        gl = GridLayout(cols=4, spacing=3, size_hint=(1, .7))

        self.lbl = Label(text='0', font_size=80, valign='center', halign='right', size_hint=(1, .3),
                         text_size=(850 - 50, 500 * .4 - 50))
        bl.add_widget(self.lbl)

        gl.add_widget(Button(text='fun', on_press=self.toset))
        gl.add_widget(Button(text='sqr', on_press=self.add_operation))
        gl.add_widget(Button(text='**2', on_press=self.add_operation))
        gl.add_widget(Button(text='/', on_press=self.add_operation))

        gl.add_widget(Button(text='7', on_press=self.add_number))
        gl.add_widget(Button(text='8', on_press=self.add_number))
        gl.add_widget(Button(text='9', on_press=self.add_number))
        gl.add_widget(Button(text='X', on_press=self.add_operation))

        gl.add_widget(Button(text='4', on_press=self.add_number))
        gl.add_widget(Button(text='5', on_press=self.add_number))
        gl.add_widget(Button(text='6', on_press=self.add_number))
        gl.add_widget(Button(text='-', on_press=self.add_operation))

        gl.add_widget(Button(text='1', on_press=self.add_number))
        gl.add_widget(Button(text='2', on_press=self.add_number))
        gl.add_widget(Button(text='3', on_press=self.add_number))
        gl.add_widget(Button(text='+', on_press=self.add_operation))

        gl.add_widget(Button(text='C', on_press=self.clear))
        gl.add_widget(Button(text='0', on_press=self.add_number))
        gl.add_widget(Button(text='.', on_press=self.add_number))
        gl.add_widget(Button(text='=', on_press=self.cals_result))

        bl.add_widget(gl)

        # Function
        but_together1 = BoxLayout()
        but_together2 = BoxLayout()
        grid = GridLayout(cols=1)

        but1 = Button(text='Треугольник', font_size=30, background_color='cyan', on_press=self.totreug,
                      size_hint=(.37, 1))
        but2 = Button(text='calculator', font_size=30, background_color='cyan', on_press=self.tomain,
                      size_hint=(.26, 1))
        but3 = Button(text='Перевести градусы\n в радианы', font_size=30, background_color='cyan', on_press=self.click2,
                      size_hint=(.37, 1))
        but4 = Button(text='Вычислить\nквадратный корень ', font_size=30, background_color='cyan', on_press=self.sqrt)
        but5 = Button(text='Вычислить - Х\nиз квадратного\nуравнения', font_size=30, background_color='cyan',
                      on_press=self.poisk_x)
        but6 = Button(text='Вычислить\nфакториал числа', font_size=30, background_color='cyan', on_press=self.factorial)

        but0 = Button(text='Сбросить текст)', font_size=30, background_color='cyan', on_press=self.click3)

        self.text = TextInput(font_size=30, size_hint_y=None, height=100)
        self.label = Label(text='Вывод данных: ', font_size=30)

        but_together1.add_widget(but1)
        but_together1.add_widget(but2)
        but_together1.add_widget(but3)
        but_together2.add_widget(but4)
        but_together2.add_widget(but5)
        but_together2.add_widget(but6)

        grid.add_widget(but_together1)
        grid.add_widget(but_together2)
        grid.add_widget(self.text)
        grid.add_widget(self.label)
        grid.add_widget(but0)

        # Treugolnik
        Box_all = BoxLayout(orientation='vertical', padding=25)

        # 1 часть
        grid1 = GridLayout(cols=3, spacing=5, size_hint=(1, .20))
        grid1.add_widget(
            Button(text='Clear', font_size=30, background_color='cyan', size_hint=(.15, 1), on_press=self.clear1))
        self.lbl1 = Label(text='Выходные данные', font_size=30, valign='center', halign='center', size_hint=(.7, 1))
        grid1.add_widget(self.lbl1)
        grid1.add_widget(
            Button(text='fun', font_size=30, background_color='cyan', size_hint=(.15, 1), on_press=self.toset))

        # 2 часть
        grid2 = GridLayout(cols=4, spacing=5, size_hint=(1, .35))
        bl1_gr2 = BoxLayout(orientation='vertical', padding=7, size_hint=(.22, 1))
        bl2_gr2 = BoxLayout(orientation='vertical', padding=7, size_hint=(.22, 1))
        bl3_gr2 = BoxLayout(orientation='vertical', padding=7, size_hint=(.22, 1))
        # Сторона a
        self.lbl2 = Label(text='Введите сторону - a', font_size=17, valign='center', halign='center',
                          size_hint=(1, .28))
        self.text1 = TextInput(font_size=80, size_hint_y=None, height=100, size_hint=(1, .72), padding=8)
        bl1_gr2.add_widget(self.lbl2)
        bl1_gr2.add_widget(self.text1)
        # Сторона b
        self.lbl3 = Label(text='Введите сторону - b', font_size=17, valign='center', halign='center',
                          size_hint=(1, .28))
        self.text2 = TextInput(font_size=80, size_hint_y=None, height=100, size_hint=(1, .72), padding=8)
        bl2_gr2.add_widget(self.lbl3)
        bl2_gr2.add_widget(self.text2)
        # Сторона c
        self.lbl4 = Label(text='Введите сторону - c', font_size=17, valign='center', halign='center',
                          size_hint=(1, .28))
        self.text3 = TextInput(font_size=80, size_hint_y=None, height=100, size_hint=(1, .72), padding=8)
        bl3_gr2.add_widget(self.lbl4)
        bl3_gr2.add_widget(self.text3)
        # image_treug
        img = Image(source='treug.png', size_hint=(.34, 1))
        # Добавление
        grid2.add_widget(bl1_gr2)
        grid2.add_widget(bl2_gr2)
        grid2.add_widget(bl3_gr2)
        grid2.add_widget(img)

        # 3 часть
        grid3 = GridLayout(cols=3, spacing=5, size_hint=(1, .45))
        bl1_gr3 = BoxLayout(orientation='vertical', padding=3)
        bl2_gr3 = BoxLayout(orientation='vertical', padding=3)
        bl3_gr3 = BoxLayout(orientation='vertical', padding=3)
        # Угол A
        self.lbl5 = Label(text='Угол A', font_size=35, valign='center', halign='center')
        gr1 = GridLayout(cols=2, spacing=5)
        gr1.add_widget(Button(text='sin', font_size=30, background_color='cyan', on_press=self.sin_A))
        gr1.add_widget(Button(text='cos', font_size=30, background_color='cyan', on_press=self.cosin_A))
        gr1.add_widget(Button(text='tg', font_size=30, background_color='cyan', on_press=self.tg_A))
        gr1.add_widget(Button(text='ctg', font_size=30, background_color='cyan', on_press=self.ctg_A))
        bl1_gr3.add_widget(self.lbl5)
        bl1_gr3.add_widget(gr1)
        # Угол B
        self.lbl6 = Label(text='Угол B', font_size=35, valign='center', halign='center')
        gr2 = GridLayout(cols=2, spacing=5)
        gr2.add_widget(Button(text='sin', font_size=30, background_color='cyan', on_press=self.sin_B))
        gr2.add_widget(Button(text='cos', font_size=30, background_color='cyan', on_press=self.cosin_B))
        gr2.add_widget(Button(text='tg', font_size=30, background_color='cyan', on_press=self.tg_B))
        gr2.add_widget(Button(text='ctg', font_size=30, background_color='cyan', on_press=self.ctg_B))
        bl2_gr3.add_widget(self.lbl6)
        bl2_gr3.add_widget(gr2)
        # Угол C
        self.lbl7 = Label(text='Угол C', font_size=35, valign='center', halign='center')
        gr3 = GridLayout(cols=2, spacing=5)
        gr3.add_widget(Button(text='sin', font_size=30, background_color='cyan', on_press=self.sin_C))
        gr3.add_widget(Button(text='cos', font_size=30, background_color='cyan', on_press=self.cosin_C))
        gr3.add_widget(Button(text='tg', font_size=30, background_color='cyan', on_press=self.tg_C))
        gr3.add_widget(Button(text='ctg', font_size=30, background_color='cyan', on_press=self.ctg_C))
        bl3_gr3.add_widget(self.lbl7)
        bl3_gr3.add_widget(gr3)
        # Добавление
        grid3.add_widget(bl1_gr3)
        grid3.add_widget(bl2_gr3)
        grid3.add_widget(bl3_gr3)

        # Добавление в бокс
        Box_all.add_widget(grid1)
        Box_all.add_widget(grid2)
        Box_all.add_widget(grid3)

        # Работа с экранами
        screen1.add_widget(bl)
        screen2.add_widget(grid)
        screen3.add_widget(Box_all)

        self.sm.add_widget(screen1)
        self.sm.add_widget(screen2)
        self.sm.add_widget(screen3)

        self.sm.current = 'calculator screen'
        return self.sm

    # Функции переключения экранов
    def toset(self, instance):
        self.sm.current = 'functions screen'

    def tomain(self, instance):
        self.sm.current = 'calculator screen'

    def totreug(self, instance):
        self.sm.current = 'treug'


if __name__ == '__main__':
    Application().run()
