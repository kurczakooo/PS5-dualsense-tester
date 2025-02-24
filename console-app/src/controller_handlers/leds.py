import config


def calculate_lightbar_color(x, y):
    # normalize to [0, 1]
    norm_x = x / 1920
    norm_y = y / 1080
    
    red = int(255 * (1 - norm_x))
    green = int(255 * (1 - norm_y))
    blue = int(255 * norm_x)
    
    return red, green, blue

def set_lightbar_color(x, y):
    r, g, b = calculate_lightbar_color(x, y)
    config.controller.lightbar.set_color(r, g, b)