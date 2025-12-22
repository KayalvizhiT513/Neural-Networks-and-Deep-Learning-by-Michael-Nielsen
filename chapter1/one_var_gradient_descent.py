import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Cost function and gradient
def C(x):
    return x**2

def grad_C(x):
    return 2*x

# Gradient descent parameters
eta = 0.1          # learning rate
x = 4.0            # initial position
steps = 40

# Store trajectory
xs = [x]
for _ in range(steps):
    x = x - eta * grad_C(x)
    xs.append(x)

xs = np.array(xs)
ys = C(xs)

# Plot setup
x_curve = np.linspace(-5, 5, 400)
y_curve = C(x_curve)

fig, ax = plt.subplots()
ax.plot(x_curve, y_curve, label="C(x) = x²")
ball, = ax.plot([], [], 'ro', markersize=10, label="Ball")
path, = ax.plot([], [], 'r--', alpha=0.5)

ax.set_xlim(-5, 5)
ax.set_ylim(-1, 25)
ax.set_xlabel("x")
ax.set_ylabel("C(x)")
ax.set_title("Gradient Descent: Ball Rolling Down a Curve")
ax.legend()

# Animation update function
def update(frame):
    ball.set_data(xs[frame], ys[frame])
    path.set_data(xs[:frame+1], ys[:frame+1])
    return ball, path

ani = FuncAnimation(fig, update, frames=len(xs), interval=300)

plt.show()

