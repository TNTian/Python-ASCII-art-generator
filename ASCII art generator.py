from PIL import Image, ImageFont, ImageDraw


def image_to_text(image, resize_width, resize_height, textFile):
    codeLib = '''@B%8&WM#*o@BdpqwmZO0QLCJUYXzcvunxrlINt\|()1{}[]?-_+~<>i!lI;:,"^`'. '''
    length = len(codeLib)  # length of codeLib 69
    print(image.size)
    image = image.resize((int(image.size[0] / resize_width), int(image.size[1] / resize_height)))
    print(image.size)
    txt = ''
    for h in range(0, image.size[1]):
        for w in range(0, image.size[0]):
            gray = image.getpixel((w, h))  # calculate the gray value of each pixel
            txt += codeLib[int(((length - 1) * gray) / 256)]  # match each pixel with the code in codeLib
        txt += '\r\n'

    textFile.write(txt)
    textFile.close()
    return txt, image.size[0], image.size[1]


def text_to_image(mode, newImage_width, newImage_height, newImage_Address):
    newImage = Image.new(mode, (newImage_width, newImage_height), (255, 255, 255))  # initialise the new image
    pen = ImageDraw.Draw(newImage)
    pen.text((0, 0), text, fill=(0, 0, 0))
    newImage = newImage.resize((int(newImage.size[0] / 1), int(newImage.size[1] / 1)))
    newImage.save(newImage_Address)
    print(newImage.size)

    return


imageAddress = "picture.jpg"  # address of the image
image = Image.open(imageAddress).convert("L")  # convert image to Black & White
resize_width = image.size[0] / (image.size[0] / 2)  # modify it if you want to resize different width
resize_height = image.size[1] / (image.size[0] / 2)  # modify it if you want to resize different height

textFile = open('textFile.txt', 'w')  # address of the text file

text, image_width, image_height = image_to_text(image, resize_width, resize_height, textFile)

# convert the .txt file to image
newImage_Address = "newPicture.jpg"
newImage_width = 6 * image_width  # modify it if you want to create different width for new image
newImage_height = 15 * image_height  # modify it if you want to create different height for new image
mode = 'RGB'  # image mode
text_to_image(mode, newImage_width, newImage_height, newImage_Address)
