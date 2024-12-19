from PIL import Image
import os

image = Image.open(r"C:\Users\15min\Desktop\DimaFront\Lekce Python\Git_Lections\Lekce_12_19.12.24\witcher4.webp")

new_image = image.resize((960, 540))
new_image = new_image.rotate(90)
new_image = new_image.convert('L')

# new_image.show()

images_dir = r"C:\Users\15min\Desktop\DimaFront\Lekce Python\Git_Lections\Lekce_12_19.12.24"

for name in os.listdir(images_dir):
    if name.endswith(('.jpg', '.webp', 'png')):
        image_path = os.path.join(images_dir, name)
        print(image_path)
        # print(os.path.isfile(image_path))

        image = Image.open(image_path)
        print(image.size)

        # if image.size[0] < 346:
        #     os.remove(image_path)

        # print("=======")
        # print(image_path)
        # print(image.size)