import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

# COMMENT OUT THE GRAPHS YOU DO NOT WANT TO PLOT OR ADD YOUR OWN GRAPHS TO MODEL OTHER SITUATIONS HAVE FUN!!

#   GLOBAL VARIABLES
e = 0.01  # small time interval
# g = acceleration due to gravity
# mu = resistance factor (recommended values between zero and 2)
# L = length of the string of the pendulum

# Initial values

theta_double_dot = "(-mu * theta_dot) - ((g/L)* np.sin(theta))"  # string expression that defines acceleration
initial_theta_dot = 0
initial_theta = 1  # in radians
total_time = 15


def coordinate_points(total_time, initial_theta, initial_theta_dot, e, theta_double_dot, mu, g, L):
    t_list = []
    theta_List = []
    t_list.append(0)
    # Initialisation
    t = 0.05
    theta_dot = initial_theta_dot
    theta = initial_theta
    theta_List.append(theta)
    a = eval(theta_double_dot)
    while t <= total_time:
        theta_dot += e * a
        theta += e * theta_dot
        theta_List.append(theta)
        t += e / 2
        t_list.append(t)
        a = eval(theta_double_dot)
        t += e / 2

    return [t_list, theta_List]


coordinates = coordinate_points(total_time, initial_theta, initial_theta_dot, e, theta_double_dot, 0.2, 9.8, 1)   # typical example
plt.plot(coordinates[0], coordinates[1], 'b', label='t v/s θ for mu = 0.2')


coordinates_2 = coordinate_points(total_time, initial_theta, initial_theta_dot, e, theta_double_dot, -0.1, 9.8, 1)  # pendulum with negative resistance
plt.plot(coordinates_2[0], coordinates_2[1], 'g', label='t v/s θ for mu =  - 0.1 (negative resistance)')


coordinates_3 = coordinate_points(total_time, initial_theta, initial_theta_dot, e, theta_double_dot, 0, 9.8, 3)     # pendulum with no resistance
plt.plot(coordinates_3[0], coordinates_3[1], 'r', label='t v/s θ for mu = 0 (no resistance)')


coordinates_4 = coordinate_points(total_time, initial_theta, initial_theta_dot, e, theta_double_dot, 0.2, 9.8, 2)     # pendulum for double length
plt.plot(coordinates_4[0], coordinates_4[1], 'k', label='t v/s θ for L = 2 (double length),  mu = 0,2')

x1 = np.arange(0, 15, 0.01)                                                                                             # pure cosine graph
plt.plot(x1, np.cos(0.5*(9.8/3)*x1), 'c', label='pure cosine (solution of small angle approximations)')


plt.title('t v/s θ Relation of a Oscillator, Evolution of Different Physical situations.')
plt.xlabel('t (time in seconds))')
plt.ylabel('Position of particle (in metre)')
x_ticks = []
i = 0
while i * np.pi <= total_time:
    x_ticks.append(i * np.pi)
    i += 1

plt.xticks(x_ticks)
plt.grid()
plt.legend()

plt.show()
