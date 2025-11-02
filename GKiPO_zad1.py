"""
GKiPO - zadanie 1
autor: Marcin Bukład, album: 63459

Wczytać obraz rastrowy zdalny lub lokalny. Do obrazów zdalnych można wykorzystać urllib
Wyświetlamy obraz np z użyciem matplotlib
Zmieniamy rozdzielczość (zmniejszamy np o 50%) i zmieniamy obraz na grayscale (np, z użyciem cv2)
Obracamy obraz o 90 stopni
Wyświetlamy obraz wynikowy 
Wyświetlamy macierz obrazu / w postaci tablicy liczb
"""

from PIL import Image
import urllib.request
import io
import numpy as np
import matplotlib.pyplot as plt

print("\nTen program wczytuje obraz z internetu i wykonuje podstawowe operacje na obrazie.\n")

# loading an image from a url
url = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ad/Rainbow_lorikeet_%28Trichoglossus_moluccanus_moluccanus%29_Sydney.jpg/500px-Rainbow_lorikeet_%28Trichoglossus_moluccanus_moluccanus%29_Sydney.jpg"

req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as response:
    image_data = response.read()
image = Image.open(io.BytesIO(image_data))

# show original image
plt.figure(figsize=(6,6))
plt.title("Oryginalny obraz")
plt.imshow(image)
plt.axis('off')
plt.show()

# reduce size, convert to grayscale and rotate
width, height = image.size
resized_image = image.resize((width // 2, height // 2), resample=Image.Resampling.LANCZOS)
gray_image = resized_image.convert("L")
rotated_image = gray_image.rotate(-90, expand=True)

# display the modified image
plt.figure(figsize=(6,6))
plt.title("Zmieniony obraz")
plt.imshow(rotated_image,cmap='gray')
plt.axis('off')
plt.show()

# show image matrix
image_array = np.array(rotated_image)
print("\nMacierz zmienionego obrazu:\n")
print(image_array[:10, :10])
