' Script to generate the reticle sprite to be used in the game. '
from PIL import Image, ImageDraw


class Reticle:
    def __init__(self, size):
        image_size = (size, size) # Size in pixels.
        transparent_image = (0, 0, 0, 0) # RGBA.
        self.image = Image.new('RGBA', image_size, transparent_image)
        self.draw = ImageDraw.Draw(self.image) # Create the transparent image.

        self.draw_reticle(size)

        # Save the image after processing it.
        self.image.save('reticle.png')


    def draw_reticle(self, size):
        symmetry_x_axis = size // 2
        symmetry_y_axis = size // 2
        rectangle_width = 80

        # Center mask for the reticle.
        mask_size = 100
        mask_x1 = symmetry_x_axis - (mask_size // 2)
        mask_x2 = symmetry_x_axis + (mask_size // 2)
        mask_y1 = symmetry_y_axis - (mask_size // 2)
        mask_y2 = symmetry_y_axis + (mask_size // 2)


        # Vertical rectangle x vertices.
        vertical_x1 = (symmetry_x_axis - (rectangle_width // 2))
        vertical_x2 = (symmetry_x_axis + (rectangle_width // 2))
        
        # First vertical segment line.
        self.draw_line(vertical_x1, 0, vertical_x2, mask_y1, 'white')
        # Second vertical segment line
        self.draw_line(vertical_x1, mask_y2, vertical_x2, size, 'white')
        
        # Horizontal rectangle y vertices.
        horizontal_y1 = (symmetry_y_axis - (rectangle_width // 2))
        horizontal_y2 = (symmetry_y_axis + (rectangle_width // 2))

        # First horizontal segment.
        self.draw_line(0, horizontal_y1, mask_x1, horizontal_y2, 'white')
        # Second horizontal segment.
        self.draw_line(mask_x2, horizontal_y1, size, horizontal_y2, 'white')

    def draw_line(self, x1, y1, x2, y2, color):
        self.draw.rectangle([(x1, y1),(x2, y2)], fill=color)


# ==================================================================
reticle = Reticle(1000)