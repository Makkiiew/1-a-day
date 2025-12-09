pyrimid_size = int(input("How big will your pyrimid be? "))
canvas_width = pyrimid_size * 2
for row in range(pyrimid_size):
    block_count = (row * 2) + 1
    layer = block_count * "#"
    print(layer.center(canvas_width))
