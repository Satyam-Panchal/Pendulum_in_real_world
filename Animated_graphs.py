
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation


# e = small time interval
# expression = string expression that defines acceleration of the body as a function of its postions and velocity
# v = second derivative of x

def coordinate_points(total_time, initial_x, initial_v, e, expression):
    t_list = []
    x_list = []
    t_list.append(0)
    # Initialisation
    t = 0.05
    v = initial_v
    x = initial_x
    x_list.append(x)
    a = eval(expression)
    while t <= total_time:
        v += e * a
        x += e * v
        x_list.append(x)
        t += e / 2
        t_list.append(t)
        a = eval(expression)
        t += e / 2

    return t_list, x_list



fig = plt.figure()
ax = plt.subplot(1, 1, 1)

data_skip = 5


#
def init_func():
    ax.clear()
    plt.xlabel('time')
    plt.ylabel('theta')

x1 = coordinate_points(10, 1, 0, 0.01, '(-0.2 * v) - ((9.8)* np.sin(x))')[0]    #non linear damped pendulum with resistance factor 0.2
y1 = coordinate_points(10, 1, 0, 0.01, '(-0.2 * v) - ((9.8)* np.sin(x))')[1]

x2 = coordinate_points(10, 1, 0, 0.01, '(0.2 * v) - ((9.8)* np.sin(x))')[0]
y2 = coordinate_points(10, 1, 0, 0.01, '(0.2 * v) - ((9.8)* np.sin(x))')[1]     #pendulum with positive resistance factor

x3 = coordinate_points(10, 1, 0, 0.01, '(-0.2 * v) - ((1.625)* np.sin(x))')[0]
y3 = coordinate_points(10, 1, 0, 0.01, '(-0.2 * v) - ((1.625)* np.sin(x))')[1]  #pendulum on moon


def anim(i):
    ax.plot(x1[i:i + data_skip], y1[i:i + data_skip], color='k')
    ax.plot(x2[i:i + data_skip], y2[i:i + data_skip], color='r')
    ax.plot(x3[i:i + data_skip], y3[i:i + data_skip], color='g')
    plt.xlim(x1[0], x1[-1])
    plt.ylim((-5, 5))


anim1 = FuncAnimation(fig, anim, frames=np.arange(0, len(x1), data_skip), init_func=init_func, interval=5)

plt.show()
anim1.save('animations.mp4', dpi=150, fps=60, writer='ffmpeg')

