import numpy as np
import matplotlib.pyplot as plt

def T_N(x, y, N):
    s = np.zeros_like(x)
    for n in range(1, N + 1):
        s += 400 * (n*3.14**(-1)) * np.sin(n * 3.14 * x / 10) * np.exp(-n * 3.14 * y) / 10
    return s

def V_N(x, y, N):
    s = np.zeros_like(x)
    for n in range(1, N + 1):
        s += 2 * (-n)**(-1) * np.sin(n * x) * np.exp(-n * y)
    return s

# Domain
x = np.linspace(0, np.pi, 300)
y = np.linspace(0, 3, 300)
X, Y = np.meshgrid(x, y)

# Compute solution
N = 10
W = T_N(X, Y, N)
Z = V_N(X, Y, N)


# Plot 1
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, W)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('T(x,y)')
ax.set_title(f'Problem 4: N={N}')
plt.show()

# Plot 2
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('V(x,y)')
ax.set_title(f'Problem 5: N={N}')
plt.show()