def color_to_grayscale(image):
    """
    Convert an RGB image to grayscale using luminance weights.
    """
    return [[0.2990 * pixel[0] + 0.5870 * pixel[1] + 0.1140 * pixel[2] 
             for pixel in row] 
            for row in image]
