from PIL import Image

img = Image.open("imgs/jpg/wallpaperflare.com_wallpaper.jpg")
print(img.size)  # (3529, 4705)
img.thumbnail((200, 200))  ## thumbnail 在保持纵横比的同时将图像调整为给定大小。
print(img.size)  # (150, 200)
img.save("./imgs/maritz_thumb.jpg")
