'''
Author: Adam Foster
Last Update: Mar 2, 2025

''' 


import os
from typing import Self

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame


#-------------------------------------------------------------------------------
class Pixel(object):
    '''
    Models a coloured Pixel for an image, with red, green, and blue components.
    All RGB values are integers between 0 and 255 inclusive.
    '''

    def __init__(self, r: int, g: int, b: int) -> None:
        '''
        Construct a Pixel with the given red/green/blue components.
        RGB values must be between 0 & 255 (inclusive).
        '''       
        self.set_r(r)
        self.set_g(g)
        self.set_b(b)
    

    def __eq__(self, other: object) -> bool:
        '''
        Return True if this Pixel has equivalent RBG to other, or False otherwise.
        '''
        if not isinstance(other, Pixel):
            return NotImplemented
        return self.__r==other.__r and self.__g==other.__g and self.__b==other.__b

    def __str__(self) -> str:
        '''
        Return a string representation of this Pixel in the form '(R-G-B)'.
        '''
        return f"({self.__r}-{self.__g}-{self.__b})"
    
    def __repr__(self) -> str:
        '''
        Return a string representation of this Pixel in the form 'Pixel(R, G, B)'.
        '''
        return f"Pixel({self.__r}, {self.__g}, {self.__b})"



    def get_r(self) -> int:
        '''
        Return this Pixel's red component.
        '''
        return self.__r

    def get_g(self) -> int:
        '''
        Return this Pixel's green component.
        '''
        return self.__g

    def get_b(self) -> int:
        '''
        Return this Pixel's blue component.
        '''
        return self.__b
    


    def set_r(self, r: int) -> None:
        '''
        Set this Pixel's red component to r (must be between 0 & 255 inclusive).
        '''
        if type(r) != int:
            raise TypeError(f"R/G/B values must be integers")
        if r < 0 or r > 255:
            raise ValueError(f"R value ({r}) out of range 0-255")
        self.__r = r

    def set_g(self, g: int) -> None:
        '''
        Set this Pixel's green component to g (must be between 0 & 255 inclusive).
        '''
        if type(g) != int:
            raise TypeError(f"R/G/B values must be integers")
        if g < 0 or g > 255:
            raise ValueError(f"G value ({g}) out of range 0-255")
        self.__g = g

    def set_b(self, b: int) -> None:
        '''
        Set this Pixel's blue component to b (must be between 0 & 255 inclusive).
        '''
        if type(b) != int:
            raise TypeError(f"R/G/B values must be integers")
        if b < 0 or b > 255:
            raise ValueError(f"B value ({b}) out of range 0-255")
        self.__b = b

        
    
    def min_rgb(self) -> int:
        '''
        Return the value of the smallest r/g/b/ component for this Pixel.
        '''
        return min(self.__r, self.__g, self.__b)

    def max_rgb(self) -> int:
        '''
        Return the value of the largest r/g/b/ component for this Pixel.
        '''
        return max(self.__r, self.__g, self.__b)


#-------------------------------------------------------------------------------
class Image(object):
    '''
    Models an Image, which can be edited, shown, and saved.
    '''
    
    def __init__(self, surface: pygame.Surface, caption: str) -> None:
        '''
        Construct an Image on the given Surface with the given title bar caption.
        '''
        self.__img = surface    
        self.__width = self.__img.get_width()
        self.__height = self.__img.get_height()
        self.__caption = caption
    
    
    def show(self) -> None:
        """
        Display the Image in a window.  The calling code will pause until
        the image window is closed.  
        """
        screen = pygame.display.set_mode((self.__width, self.__height))
        pygame.display.set_caption(self.__caption)
        keep_going = True
        while keep_going:
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    keep_going = False
            screen.blit(self.__img, (0,0))
            pygame.display.flip()
        pygame.display.set_mode((1,1), pygame.NOFRAME)        


    def save(self, file_name: str = "temp.bmp"):
        """
        Save this Image with the given file_name.
        If the file_name is an absolute path, use it as is.
        If the file_name is not an absolute path, save the
        file in the current working directory.
        If the file_name is not given at all, save the file as 'temp.bmp'
        in the current working directory.
        """
        if not os.path.isabs(file_name):
            file_name = os.path.join(os.getcwd(), file_name)
        pygame.image.save(self.__img, file_name)


    def set_caption(self, caption: str) -> None:
        """
        Set the Image's caption to the given value.
        """        
        self.__caption = caption
        
        
    def get_width(self) -> int:
        """
        Return the width of this Image (as number of pixels).
        """
        return self.__width
    
    def get_height(self) -> int:
        """
        Return the height of this Image (as number of pixels).
        """
        return self.__height
    

    def get_image(self) -> pygame.Surface:
        """
        Return the Surface for this Image.
        """
        return self.__img
    
    
    
    def get_pixel(self, x: int, y: int) -> Pixel:
        """
        Return the Pixel at the given (x, y) coordinates in this Image.
        """
        if x < 0 or x >= self.__width or y < 0 or y >= self.__height:
            raise ValueError(f"Coordinate ({x},{y}) out of range")
        rgb = self.__img.get_at((x,y))[:3]
        return Pixel(rgb[0], rgb[1], rgb[2]) # type: ignore
    

    def set_pixel(self, x: int, y: int, pix: Pixel) -> None:
        """
        Set the Pixel at the given (x, y) coordinates to the given pix.
        """
        if x < 0 or x >= self.__width or y < 0 or y >= self.__height:
            raise ValueError(f"Coordinate ({x},{y}) out of range")
        
        self.__img.set_at((x,y), [pix.get_r(), pix.get_g(), pix.get_b()])
    

    def copy(self) -> Self:
        """
        Return a distinct copy of this Image.
        """
        return Image(self.__img.copy(), self.__caption) # type: ignore
            
    
    
    def compare(self, other: Self) -> float:
        '''
        Return what percentage of the pixels in this image are equal to other's.
        Range of return percentage will be 0.0 to 1.0.
        If the two Images are not the same dimensions, returns -1.0.
        '''
        #handle dimension mismatch first
        if self.__width != other.__width or self.__height != other.__height:
            return -1.0
    
        equal_pixels = 0 #counter of equal pixels
    
        #traverse all coordinates in the Images
        for row in range (0, self.__height):
            for col in range (0, self.__width):
                #get the two corresponding Pixels at these coordinates
                p1 = self.get_pixel(col, row)
                p2 = other.get_pixel(col, row)
                
                #uses Pixel's __eq__ method that was written in Pixel class
                if p1 == p2:
                    equal_pixels += 1
        
        #percentage is the # of equal / total # of pixels
        area = self.__height * self.__width
        percentage_equal = equal_pixels/area
        return percentage_equal
    

    
#-------------------------------------------------------------------------------
class Image_File(Image):
    '''
    A custom version of an Image object, loaded from an existing image file.
    '''
    
    def __init__(self, path: str) -> None:
        '''
        Construct an Image from the given file path.
        '''
        temp_surface = pygame.image.load(path)    
        pygame.display.set_mode((1,1), pygame.NOFRAME)
        temp_surface = temp_surface.convert()
        Image.__init__(self, temp_surface, path)

    

#-------------------------------------------------------------------------------
class Image_New(Image):
    '''
    A custom version of an Image object, created as a blank white surface.
    '''
    
    def __init__(self, width: int, height: int, caption: str = "New Image") -> None:
        '''
        Constructs a blank white Image with the given width & height,
        and an optional image caption ('New Image' by default).
        '''
        if width <= 0 or height <= 0 or type(width)!= int or type(height)!= int:
            raise ValueError(f"Dimensions must be positive integers")

        temp = pygame.surface.Surface((width, height))
        pygame.display.set_mode((1,1), pygame.NOFRAME)
        temp = temp.convert()
        temp.fill((255, 255, 255))    
        Image.__init__(self, temp, caption)



#-------------------------------------------------------------------------------
class Image_Sequence(object):
    '''
    Models a sequence of Images which can be shown as an animation.
    '''
    
    def __init__(self) -> None:
        '''
        Constructs an empty sequence of Images.
        '''
        self.__images:list[Image] = []
        self.__width = 1
        self.__height = 1
        self.__eraser = pygame.surface.Surface((self.__width, self.__height))
        


    def add_image(self, image: Image) -> None:
        '''
        Adds the given image to the end of the sequence.
        '''
        self.__images.append(image)
        #update the display size as necessary
        self.__width = max(self.__width, image.get_width())
        self.__height = max(self.__height, image.get_height())
        self.__eraser = pygame.surface.Surface((self.__width, self.__height))


    def __len__(self) -> int:
        '''
        Returns the number of Images in this Image_Sequence
        '''
        return len(self.__images)
    

   
    def get_frame(self, frame_number: int) -> Image:
        '''
        Returns the Image at the given frame number (indexed from 1).
        '''
        if frame_number < 1 or frame_number > len(self.__images):
            raise ValueError(f"Frame number must be between 1 and {len(self.__images)}")        
        return self.__images[frame_number-1]



    def reverse(self) -> None:
        '''
        Reverses the order of the Images in the sequence.
        '''
        self.__images.reverse()



    def play(self, fps, audio_file: str = "") -> None:
        """
        Plays the sequence of Images with the given frames per second (fps).
        An optional audio file can be played while the sequence is displayed.
        While playing, the following interation is possible:
           -SPACEBAR: pause/unpause the animation
           -UP: increase the framerate by 1 fps
           -DOWN: decrease the framerate by 1 fps
           -RIGHT: when paused, advance one frame forward
           -LEFT: when paused, advance one frame backward
           -S: when paused, save the current frame's image
        """
        if audio_file != "":
            if type(audio_file) != str:
                raise ValueError("Argument must be a str")
            pygame.mixer.init()
            sample = pygame.mixer.Sound(audio_file)
            sample.play(-1)


        clock = pygame.time.Clock()
        
        screen = pygame.display.set_mode((self.__width, self.__height))

        keep_going = True
        count = 0
        paused = False
        while keep_going:
            pygame.display.set_caption(f"Frame {count%len(self.__images)+1} of {len(self.__images)} (@{fps} fps)")
            
            clock.tick(fps)
            for ev in pygame.event.get():
                if ev.type == pygame.QUIT:
                    keep_going = False
                    if audio_file != "":
                        sample.stop()
                 
                       
                elif ev.type == pygame.KEYDOWN:
                    #UP/DOWN KEYS will change frame rate up/down by 1 fps
                    if ev.key == pygame.K_UP:
                        fps += 1
                    elif ev.key == pygame.K_DOWN:
                        fps = max(1, fps-1)

                    #pause with space key
                    elif ev.key == pygame.K_SPACE and not paused:
                        paused = True
        
                    #when paused, more control is available
                    elif paused:
                        #LEFT/RIGHT KEYS will move frame back/forward 
                        #S-KEY will save the current pause frame as an image file
                        #SPACE KEY will unpause
                        
                        if ev.key == pygame.K_RIGHT:
                            #go forward one frame
                            count += 1                 
                            screen.blit(self.__eraser, (0,0))
                            screen.blit(self.__images[count%len(self.__images)].get_image(), (0,0))
                            pygame.display.flip()
                        elif ev.key == pygame.K_LEFT:
                            #go back one frame
                            count -= 1                 
                            screen.blit(self.__eraser, (0,0))
                            screen.blit(self.__images[count%len(self.__images)].get_image(), (0,0))
                            pygame.display.flip()
    
                        elif ev.key == pygame.K_s:
                            #save current frame as 'frame_#_of_#.bmp'
                            file_name = f"frame_{count%len(self.__images)+1}_of_{len(self.__images)}.bmp"
                            self.__images[count%len(self.__images)].save(file_name)
    
                        elif ev.key == pygame.K_SPACE:
                            #SPACE key will unpause
                            paused = False
            
                    
            if not paused:
                count += 1
                screen.blit(self.__eraser, (0,0))
                screen.blit(self.__images[count%len(self.__images)].get_image(), (0,0))
                pygame.display.flip()
                
        
        pygame.display.set_mode((1,1), pygame.NOFRAME)        



def clean_up() -> None:
    '''
    Terminates any lingering display windows for Images.
    '''
    pygame.quit()


pygame.init()


#===============================================================================
#A couple useful constants for fixed colours.
BLACK = Pixel(0, 0, 0)
WHITE = Pixel(255, 255, 255)