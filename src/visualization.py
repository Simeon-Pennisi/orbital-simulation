import matplotlib.pyplot as plt

def plot_trajectory(positions, filename):
    plt.figure()
    plt.plot(positions[:, 0], positions[:, 1])
    plt.xlabel("x (AU)")
    plt.ylabel("y (AU)")
    plt.gca().set_aspect("equal")
    plt.title("Earth Orbit Around Fixed Sun")
    plt.savefig(filename)
    plt.close()
