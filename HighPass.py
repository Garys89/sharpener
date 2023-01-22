from PIL import Image


if __name__ == '__main__':
    img = Image.open("lena.png")
    pixel_map = img.load()

    width, height = img.size

    output_img = Image.new(mode="RGB", size=(width, height))
    new_pixel_map = output_img.load()

    for i in range(1, width-1):
        for j in range(1, height-1):
            r1, g1, b1 = img.getpixel((i-1, j-1))
            r2, g2, b2 = img.getpixel((i-1, j))
            r3, g3, b3 = img.getpixel((i-1, j+1))
            r4, g4, b4 = img.getpixel((i, j-1))
            r5, g5, b5 = img.getpixel((i, j))
            r6, g6, b6 = img.getpixel((i, j+1))
            r7, g7, b7 = img.getpixel((i+1, j-1))
            r8, g8, b8 = img.getpixel((i+1, j))
            r9, g9, b9 = img.getpixel((i+1, j+1))

            r = -1*(r1 + r2 + r3 + r4 + r6 + r7 + r8+ r9) + 9*r5
            g = -1*(g1 + g2 + g3 + g4 + g6 + g7 + g8+ g9) + 9*g5
            b = -1*(b1 + b2 + b3 + b4 + b6 + b7 + b8+ b9) + 9*b5
            new_pixel_map[i, j] = (int(r), int(g), int(b))

    output_img.save("output", format="png")

    img.show("Input")
    output_img.show("Output")


