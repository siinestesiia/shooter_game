' Script to generate the target sprite to be used in the game. '
from PIL import Image, ImageDraw

class RoundTarget:
    def __init__(self, size):
        image_size = (size, size) # Size in pixels.
        transparent_image = (0, 0, 0, 0) # RGBA.
        self.image = Image.new('RGBA', image_size, transparent_image)
        self.draw = ImageDraw.Draw(self.image) # Create the transparent image.
        
        self.image_center = (size // 2, size // 2)

        # Round target of red and white circles.
        self.draw_circle(size, 'red')
        self.draw_circle(size * 0.8, 'white')
        self.draw_circle(size * 0.6, 'red')
        self.draw_circle(size * 0.4, 'white')
        self.draw_circle(size * 0.2, 'red')


        # Save the image after processing it.
        self.image.save('round_target.png')

    
    def draw_circle(self, size, color):
        self.draw.circle(self.image_center, size // 2, fill=color,
                         outline='black', width=2)


# =============================================================================
target = RoundTarget(1000)

