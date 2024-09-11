def getHeight():
    try:
        height = int(input("Height: "))
        if height in range(1, 100):
            return int(height)
        else:
            return getHeight()
    except:
        return getHeight()


def buildBrick(height):
    n = 1
    m = height - 1
    while height >= n and m <= height:
        print(((" " * (height - n)) + (n * '#')) + "  " + (('#' * (height - m))))
        n += 1
        m -= 1


buildBrick(getHeight())
