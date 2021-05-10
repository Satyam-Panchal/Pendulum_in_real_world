import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
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

x = coordinate_points(30, 1, 0, 0.001, '(-0.2 * v) - ((9.8)* np.sin(x))')[0]
y = coordinate_points(30, 1, 0, 0.001, '(-0.2 * v) - ((9.8)* np.sin(x))')[1]

fig = plt.figure()
ax = plt.subplot(1, 1, 1)

data_skip  = 50
#
def init_func():
    ax.clear()
    plt.xlabel('time')
    plt.ylabel('theta')

def update_plot_1(i):
    ax.plot(x[i:i+data_skip], y[i:i+data_skip], color='k')
    plt.xlim(x[0], x[-1])
    plt.ylim((-5, 5))


anim = FuncAnimation(fig, update_plot_1, frames=np.arange(0, len(x), data_skip), init_func=init_func, interval=10)

x2 = coordinate_points(30, 1, 0, 0.001, '(-0.2 * v) - ((1.625)* np.sin(x))')[0]
y2 = coordinate_points(30, 1, 0, 0.001, '(-0.2 * v) - ((1.625)* np.sin(x))')[1]                                    # pendulum on moon

def update_plot_2(i):
    ax.plot(x2[i:i + data_skip], y2[i:i + data_skip], color='r')
    plt.xlim(x2[0], x2[-1])
    plt.ylim((-5, 5))

anim = FuncAnimation(fig, update_plot_2, frames=np.arange(0, len(x2), data_skip), init_func=init_func, interval=10)

# x3 = np.arange(0, 30, 0.001)
# y3 = np.cos(np.sqrt(9.8) * x3)
#
# def update_plot_3(i):
#     ax.plot(x3[i:i + data_skip], y3[i:i + data_skip], color='b')                                                # purecosine
#     plt.xlim(x3[0], x3[-1])
#     plt.ylim((-1, 1))
#
# anim = FuncAnimation(fig, update_plot_3, frames=np.arange(0, len(x3), data_skip), init_func=init_func, interval=20)
#
#
plt.show()
#
#
# anim.save('Pendulumgif',dpi=150, fps=60, writer='ffmpeg' )