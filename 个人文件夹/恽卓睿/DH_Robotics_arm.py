from numpy import *
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

# -------------------- DH Matrix --------------------
def DH_matrix(alpha, a, d, theta):
    return array([
        [cos(theta), -sin(theta), 0, a],
        [sin(theta)*cos(alpha), cos(theta)*cos(alpha), -sin(alpha), -sin(alpha)*d],
        [sin(theta)*sin(alpha), cos(theta)*sin(alpha), cos(alpha), cos(alpha)*d],
        [0, 0, 0, 1]
    ])

# -------------------- Parameters --------------------
L0 = 1.2
L1 = L2 = 0.5
L3 = L4 = L5 = 1

t_total = 3      # total time (s)
N = 100          # number of frames
t = linspace(0, t_total, N)

# Variables vary linearly with time
d_vals = linspace(0, 1.2, N)
theta1_vals = linspace(0, deg2rad(90), N)
theta2_vals = linspace(0, deg2rad(150), N)
theta3_vals = linspace(deg2rad(90), deg2rad(-90), N)

# -------------------- Forward Kinematics --------------------
def forward_kinematics(theta1, theta2, theta3, d):
    # Frame 0 to 1
    T01 = DH_matrix(0, 0, L0, theta1)
    # Frame 1 to 2
    T12 = DH_matrix(0, sqrt(L1**2 + L2**2), d, 0)
    # Frame 2 to 3
    T23 = DH_matrix(0, L3, 0, theta2)
    # Frame 3 to 4
    T34 = DH_matrix(0, L4, 0, theta3)
    # Frame 4 to 5 (末端)
    T45 = DH_matrix(0, L5, 0, 0)

    T02 = T01 @ T12
    T03 = T02 @ T23
    T04 = T03 @ T34
    T05 = T04 @ T45

    # Extract joint positions
    p0 = array([0, 0, 0])
    p1 = T01[0:3, 3]
    p2 = T02[0:3, 3]
    p3 = T03[0:3, 3]
    p4 = T04[0:3, 3]
    p5 = T05[0:3, 3]

    return [p0, p1, p2, p3, p4, p5]

# -------------------- Animation Setup --------------------
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim([-3, 3])
ax.set_ylim([-3, 3])
ax.set_zlim([0, 3])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title("Manipulator Motion Animation")

line, = ax.plot([], [], [], 'o-', lw=2, color='b')

def init():
    line.set_data([], [])
    line.set_3d_properties([])
    return line,

def update(i):
    points = forward_kinematics(theta1_vals[i], theta2_vals[i], theta3_vals[i], d_vals[i])
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    zs = [p[2] for p in points]
    line.set_data(xs, ys)
    line.set_3d_properties(zs)
    return line,

ani = FuncAnimation(fig, update, frames=N, init_func=init, blit=True, interval=100)

# -------------------- Save as GIF --------------------
ani.save('manipulator_motion.gif', writer=PillowWriter(fps=30))
plt.show()
