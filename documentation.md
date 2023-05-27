# *shooter game documentation*

## 1. `Initializing` and `terminating` the game:
* For initializing the game we need to call this function only once:

```Python
pygame.init()
```

* And for terminating the game and free all resources we have to call another function:

```Python
pygame.quit()
```

* But it has to be inside a ***for*** loop that will check for a ***quit event*** like so:

```Python
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        pygame.quit() # Calling the quit method.
```

* In this same ***for*** loop we'll check for other ***events*** like user input. This loop and the game itself has to be contained in a ***while*** loop that will run until the game ends.

#

## 2. Defining a `window size`:
* To define a window size for the game we define a variable that contains the function that creates the window:

```Python
screen = pygame.display.set_mode((width, height))
```

* And for showing the ***name*** of the game on at the top of the window:
```Python
pygame.display.set_caption('Game Name')
```

#

## 3. Defining the `framerate`:
* We instantiate the class ***Clock***:

```Python
clock = pygame.time.Clock()
```

* And then we use its method ***tick*** for defining the framerate:

```Python
clock.tick(60) # it will run at 60 fps.
```

#

## 4. Refreshing an `image` or `surface` for each frame:
* Before we refresh an image or surface, we have to update the ***window surface*** for each frame so it will contain the other surfaces or images:

```Python
pygame.display.update()
```

* Then we can refresh an image using the ***blit()*** method with the variable containing the window information, in this case ***screen***:

```Python
screen.blit(image, (x, y)) 
# takes the image an sets it in the given position.
```

* 'blit' stands for ***Block Image Transfer***. We have to do this last step for each image or surface we want to show on screen keeping in mind the order in which we want the images to overlap each other.

#

## 5. `Loading` an image file:
* Define a variable that will contain the image so you can work with it:

````Python
image = pygame.load('directory/image.png')
````

* For better processing you should always convert the image
using the function ***convert_alpha()***:

```Python
image = pygame.load('directory/image.png').convert_alpha()
# Converting to alpha keeps the transparency 
# of the alpha channel from the png file.
# Otherwise use only convert().
```

#

## 6. Using `rectangles` to position images:
* Define another variable for the rectangle that will store the image's width and height and also will define its ***origin point*** so it'll be easier to position the image on screen.

```Python
image_rect = image.get_rect(center = (x, y))
# There's also other arguments such as:
# topleft, midright, bottomright and so on.
```

* In this case we define a rectangle using the ***image***'s width and height and then we define the ***origin point*** of the rectangle which will be the center of the image. Then we set the ***x*** and ***y*** coordinates for positioning it on the screen.
_It's always a good practice to use the ***rectangle*** for moving and placing the image._

#

# 7. Detecting `collisions`:
* Detects if there's a collision between one rectangle and the other. Returns either ***0*** or ***1*** (***True*** or ***False***).

```Python
# rect_1.colliderect(rect_2)
image_rect.colliderect(image_2_rect)
```

#