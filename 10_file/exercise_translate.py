from translate import Translator

translator = Translator(to_lang="en", from_lang="zh")
# translation = translator.translate(
#     "需要将所有输入令牌的注意力键和值张量存储在GPU内存中 ，以生成下一个令牌。"
# )
# print(translation)

try:
    with open("data.text", mode="r") as from_file:
        text = from_file.read()
        translation = translator.translate(text)
        with open("./.data-en.text", mode="w") as to_file:
            to_file.write(translation)
except FileNotFoundError as e:
    print("Check your file path")
    print(e)
