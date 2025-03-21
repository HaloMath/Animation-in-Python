# импортируем пакеты
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation

# Временной массив
t = np.linspace(0, 60, 500)

# Позиционные массивы и данные для них
x0 = 0
y0 = 0
z0 = -20
R = 10
a = 1
h = 1
x = x0 + R * np.cos(0.1*a*t) * np.cos(2*a*t)
y = y0 + R * np.cos(0.1*a*t) * np.sin(2*a*t)
z = z0 + h * t

# Задаем набор данных для анимации
dataSet = np.array([x, y, z]) # комбинирум наши позицонные координаты
numDataPoints = len(t)

def animate_func(num):
    ax.clear() # очищаем фигуру для обновления линии, точки, заголовка и осей

    # Обновление линии траектории
    ax.plot3D( dataSet[0, :num + 1],  dataSet[1, :num + 1], dataSet[2, :num + 1], c = 'blue')

    # Обновляем локацию точки
    ax.scatter(dataSet[0, num],  dataSet[1, num], dataSet[2, num], c = 'blue', marker = 'o')

    # Добавляем постоянную начальную точку
    ax.plot3D(dataSet[0, 0], dataSet[1, 0], dataSet[2, 0], c = 'blue', marker = 'o')

    # Задаем пределы для осей
    ax.set_xlim3d([-20, 20])
    ax.set_ylim3d([-20, 20])
    ax.set_zlim3d([-20, 20])

    # Добавляем метки
    ax.set_title('Траектория: время: ' + str(np.round(t[num], decimals = 2)) + ' сек')

fig = plt.figure() # создаем объект
ax = plt.axes(projection = '3d')
line_ani = animation.FuncAnimation( fig, animate_func, interval = 100, frames = numDataPoints)

plt.show() # включить показ графики, отображения созданных объектов

# Сохранить анимацию
f = r"animation.gif"
writergif = animation.PillowWriter(fps = numDataPoints/6)
line_ani.save(f, writer = writergif)
 
