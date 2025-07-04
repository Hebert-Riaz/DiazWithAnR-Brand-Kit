import base64
import os

# Create directory if not present
os.makedirs("logos/embroidery-safe", exist_ok=True)

# BEGIN BASE64 LOGO IMAGE (PART 1)
image_data = """
iVBORw0KGgoAAAANSUhEUgAAARwAAACeCAYAAABwZ0iNAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAGXRF
WHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAABElJREFUeJzt3cFqHkUYxvF/F7HcTrhIwUbA
EjRQJFJVqTWE+I9mewEJ1Kwh8E5U2UUCYGNlKCoKogjV6K4IpKFcEAhSkXy6+u1nP6HPVbsG0c7PLmXd
s19d71JdnM/YM2fPnj179uzZs2fPnj179uzZs2fPnj179uzZs2fPnj179m7z/wmrrt3pjq6atw3dmLTA
vzCcwXc8n8z3Q3Rn8Aq4hzf1bu9kNh5wNZZQb9iWvghzA4wOmFnRf9Xj6EzAqPOIVvIL77kg4wusGEHb
QX/nk43OqAmecyPQZc5uKXA/FfrvVtuDaBbgHXD+u93vRe/NDc56O3QzDBJdbwXf6S7h3OaHnQWnYccm
o2Y0DR4M2JgquKDPuAPcaE3mBzyxWUwKu/0/dicwvZxw9e2VviI55cTACQ3m0bPMH78vFwb/Aos2aXZQ
1U0N1uftr8en+8LmFPqBrf63Zx3oOflsmKbgjD0FngqL+mK3Gd7lR4e2AHWFT3mi8qN29tr8ZjxoM7mE

"""

# Decode and write the logo file
with open("logos/embroidery-safe/diazwithanr-logo-simple.png", "wb") as f:
    f.write(base64.b64decode(image_data.strip()))

print("✅ Logo generated: logos/embroidery-safe/diazwithanr-logo-simple.png")

