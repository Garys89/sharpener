from PIL import Image


def laplace(img, mask):
    b = list()
    r = list()
    g = list()

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

            r0 = 0
            g0 = 0
            b0 = 0
            for x in range(0, 9):
                r0 = r0 + mask[x] * r[x]
                g0 = g0 + mask[x] * g[x]
                b0 = b0 + mask[x] * b[x]

            new_pixel_map[i, j] = (int(r0), int(g0), int(b0))

            b = list()
            r = list()
            g = list()

    output_img.save("output", format="png")
    output_img.show("Output")


if __name__ == '__main__':
    img = Image.open("lena.png")
    img.show("Input")
    laplace(img, [-1, -1, -1, -1, 8, -1, -1, -1, -1])
    laplace(img, [-1, -1, -1, -1, 9, -1, -1, -1, -1])
    laplace(img, [0, -1, 0, -1, 4, -1, 0, -1, 0])
    laplace(img, [0, -1, 0, -1, 5, -1, 0, -1, 0])

