import numpy as np

import matplotlib.pyplot as plt

def draw_logo():
    fig, ax = plt.subplots(figsize=(4, 4))
    # Draw a circle
    circle = plt.Circle((0.5, 0.5), 0.4, color='#3572A5', fill=True)
    ax.add_artist(circle)
    # Draw a white "G" in the center
    theta = np.linspace(np.pi/4, 2*np.pi - np.pi/4, 100)
    x = 0.5 + 0.25 * np.cos(theta)
    y = 0.5 + 0.25 * np.sin(theta)
    ax.plot(x, y, color='white', linewidth=10)
    # Draw the horizontal bar of "G"
    ax.plot([0.5, 0.65], [0.5, 0.5], color='white', linewidth=10)
    ax.set_aspect('equal')
    ax.axis('off')
    plt.tight_layout()
    plt.savefig('logo.png', dpi=200, transparent=True)
    plt.close()

if __name__ == "__main__":
    draw_logo()
import base64

# Base64-encoded image (shortened for this message — full version coming next)
image_data = """iVBORw0KGgoAAAANSUhEUgAAAYAAAAD..."""  # <--- I’ll paste the full string in the next message

with open("logos/diazwithanr-lending-team.png", "wb") as f:
    f.write(base64.b64decode(image_data))

