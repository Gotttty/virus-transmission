import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


# 定义一个人的类，具有x坐标，y坐标，颜色（是否被感染）三个属性
class People:
    def __init__(self):
        self.x = int(np.random.random() * 100)
        self.y = int(np.random.random() * 100)
        self.color = 'g'

    # 在周期性边界条件下进行一次随机移动
    def move(self):
        '''randd = np.random.rand()
        if randd < 0.25:
            self.x += 1.5
        elif 0.25 <= randd < 0.5:
            self.x -= 1.5
        elif 0.5 <= randd < 0.75:
            self.y += 1.5
        elif 0.75 <= randd < 1:
            self.y -= 1.5'''
        m = 2 * math.pi * np.random.random()
        self.x += 2 * math.sin(m)
        self.y += 2 * math.cos(m)

        if self.x > 100:
            self.x = self.x - 100
        elif self.x < 0:
            self.x = self.x + 100

        if self.y > 100:
            self.y = self.y - 100
        elif self.y < 0:
            self.y = self.y + 100

    def location(self):
        return self.x, self.y

    def get_color(self):
        return self.color


# 创建一百个在People类下的实例并确定第一例感染者

fig, ax = plt.subplots()
plt.xlim(0, 100)
plt.ylim(0, 100)
ax.set_aspect('equal')

l = []
j = 0
a = int(np.random.random() * 100)
b = np.zeros(shape=(100, 2))

for i in range(0, 100):
    j = j + 1
    s = People()
    if j == a:
        s.color = 'r'
    l.append(s)

sc = plt.scatter([x.location()[0] for x in l], [x.location()[1] for x in l], c=[x.get_color() for x in l], s=15)

def init():
    sc.set_offsets([[x.location()[0], x.location()[1]] for x in l])
    sc.set_color([x.get_color() for x in l])
    return sc

def animate(frame):
    # 所有人随机移动并记录感染者坐标
    k = 0
    for u in l:
        u.move()
        if u.color == 'r':
            b[k] = [u.x, u.y]
            k = k + 1
    # 判断周围人是否被感染并改变被感染者的颜色
    for u in b[:99]:
        if u[0] + u[1] != 0:
            for h in l:
                if math.sqrt((h.x - u[0]) ** 2 + (h.y - u[1]) ** 2) <= 4:
                    h.color = 'r'

    sc.set_offsets([[x.location()[0], x.location()[1]] for x in l])
    sc.set_color([x.get_color() for x in l])
    return sc


ani = animation.FuncAnimation(fig=fig, func=animate, frames=300, init_func=init,interval=70, blit=False)
plt.show()
ani.save('virus.gif')
