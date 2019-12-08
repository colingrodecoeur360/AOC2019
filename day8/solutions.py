def load_input():
    with open("day8/input.txt") as f:
        content = f.read()
    return list(content.strip())


IMAGE_WIDTH = 25
IMAGE_HEIGHT = 6
PIXELS_PER_LAYER = IMAGE_WIDTH * IMAGE_HEIGHT


def build_image_layers(pixels):
    number_layers = len(pixels) // PIXELS_PER_LAYER
    return [pixels[i * PIXELS_PER_LAYER: (i + 1) * PIXELS_PER_LAYER] for i in range(number_layers)]


def decode_pixel(layers, i):
    pixels = [layer[i] for layer in layers]
    opaque_pixels = [pixel for pixel in pixels if pixel != "2"]
    return "*" if opaque_pixels[0] == "1" else " "


def display_image(image):
    rows = [image[i * IMAGE_WIDTH: (i + 1) * IMAGE_WIDTH] for i in range(IMAGE_HEIGHT)]
    for row in rows:
        print("".join(row))


if __name__ == "__main__":
    pixels = load_input()
    layers = build_image_layers(pixels)

    layer_with_fewest_zeros = min(layers, key=lambda layer: layer.count("0"))
    print(layer_with_fewest_zeros.count("1") * layer_with_fewest_zeros.count("2"))

    decoded_image = [decode_pixel(layers, i) for i in range(PIXELS_PER_LAYER)]
    display_image(decoded_image)
