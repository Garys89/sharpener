from PIL import Image


def Laplace4(img):
    print(":)")


def Laplace8(img):
    print(":)")


def Laplace9(img):
    b = list()
    r = list()
    g = list()

    pixel_map = img.load()

    width, height = img.size

    output_img = Image.new(mode="RGB", size=(width, height))
    new_pixel_map = output_img.load()

    for i in range(1, width - 1):
        for j in range(1, height - 1):
            for k in range(0, 9):
                rk, gk, bk = img.getpixel((i + int(k / 3) - 1, j + k % 3 - 1))
                r.append(rk)
                g.append(gk)
                b.append(bk)

            r0 = -1 * (r[0] + r[1] + r[2] + r[3] + r[5] + r[6] + r[7] + r[8]) + 9 * r[4]
            g0 = -1 * (g[0] + g[1] + g[2] + g[3] + g[5] + g[6] + g[7] + g[8]) + 9 * g[4]
            b0 = -1 * (b[0] + b[1] + b[2] + b[3] + b[5] + b[6] + b[7] + b[8]) + 9 * b[4]
            new_pixel_map[i, j] = (int(r0), int(g0), int(b0))

            b = list()
            r = list()
            g = list()

    output_img.save("output", format="png")

    img.show("Input")
    output_img.show("Output")


if __name__ == '__main__':
    img = Image.open("lena.png")
    Laplace9(img)
