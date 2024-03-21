from PIL import Image, ImageFilter

img = Image.open("./imgs/panda.png")

# 把图片转成灰色
converted_img = img.convert("L")
# print(converted_img)
# converted_img.save("./imgs/converted.png")
# converted_img.show()

filtered_img = img.filter(ImageFilter.BLUR)
# filtered_img.save("./imgs/filtered.png", "png")
# filtered_img.show()  # show the image

rotated_img = img.rotate(180)
# rotated_img.show()

o_width, o_height = img.size
resize_scale = 3
resized_img = img.resize((o_width * resize_scale, o_height * resize_scale))
# resized_img.show()

box = [100, 100, 300, 300]
cropped_img = img.crop(box)
cropped_img.show()
