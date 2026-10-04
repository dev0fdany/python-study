import pygame as p # to make window and display
import cv2 # to get image fps, and video into code
from PIL import Image # to load image and get pixel info
p.init() # pygame initializer
p.mixer.init() # for playing audio
screen = p.display.set_mode((1366,768))
clock = p.time.Clock() #clock for limiting fps

# chars for ascii
chars = " .'`^,:;Il!i><~+_-?][}{1)(|/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
ascii_mode = False

# pieces
piece_mode = False
pieces = [
    "bK.png",
    "bQ.png",
    "bR.png",
    "bB.png",
    "bN.png",
    "bp.png",

    "wp.png",
    "wN.png",
    "wB.png",
    "wR.png",
    "wQ.png",
    "wK.png"
]
# display segment
segments = 16
pixel_size = 30
    
# Loading Bad Apple 
video = cv2.VideoCapture("/home/dwtop/Pictures/VIDEO/Bad_Apple.mp4")
video_fps = video.get(cv2.CAP_PROP_FPS)
# Load audio
p.mixer.music.load("/home/dwtop/Pictures/VIDEO/Bad_Apple.wav")

def main():
    # this was for only one image
    #frame = Image.open("/home/dwtop/Pictures/walls/ikuyo.png")

    piece_images = []

    for filename in pieces:
        image = p.image.load("pieces/" + filename)
        image = p.transform.scale(image, (pixel_size, pixel_size))
        piece_images.append(image) 

    # read the first frame of video 
    success, frame_opencv = video.read()
    if not success:
        print("Couldn't read the first frame.")
        return
    # Fix color so PIL can use it
    frame_opencv = cv2.cvtColor(frame_opencv, cv2.COLOR_BGR2RGB)
    frame = Image.fromarray(frame_opencv)

    # Setup Ascept ratio
    pixel_art_width = segments
    pixel_art_height =  int(pixel_art_width * frame.height / frame.width)

    # creates list of the first frame
    display = create_display(frame, pixel_art_width, pixel_art_height, piece_images)


    # Sizing with which the pixel is overlayed on screen
    pixel_art_display_width = pixel_art_width * pixel_size
    pixel_art_display_height = pixel_art_height * pixel_size
    # Calculate offset (so it displays in the centre)
    offset_x = (screen.get_width() - pixel_art_display_width) // 2
    offset_y = (screen.get_height() - pixel_art_display_height) // 2
    
    # playing the audio
    p.mixer.music.play()
    running = True
    while running:
        # check if the user quits
        for event in p.event.get():
            if event.type == p.QUIT:
               running = False 
        # returns how much the audio has played (divided by 1000 cuz it returns in mili second, i want second)
        audio_time = p.mixer.music.get_pos() / 1000 # audio_time in second
        target_frame = int(audio_time * video_fps) 
        # if audio is not playing exit
        if not p.mixer.music.get_busy():
            running = False
        # clears the screen to ready it for the new frame
        screen.fill((0, 0, 0))
        # Display list to screen
        # Draw the frame to screen
        for row in range(pixel_art_height):
            for column in range(pixel_art_width):
                    # value where it should draw
                    horizontal = offset_x + column * pixel_size
                    vertical = offset_y + row * pixel_size
                    # this line draws it
                    if ascii_mode:
                        character = display[row][column]
                        p.font.init()
                        font = p.font.SysFont("monospace", pixel_size)
                        text = font.render(character, True, (255,255,255))
                        screen.blit(text, (horizontal, vertical))
                    elif piece_mode:
                            piece = display[row][column]
                            screen.blit(piece, (horizontal, vertical)) 
                    else:
                        color = display[row][column]
                        p.draw.rect(screen, color, ( horizontal, vertical, pixel_size, pixel_size))

        # sync video frame to audio
        video.set(cv2.CAP_PROP_POS_FRAMES, target_frame) 
        # read next frame
        success, frame_opencv = video.read()
        frame_opencv = cv2.cvtColor(frame_opencv, cv2.COLOR_BGR2RGB)
        frame = Image.fromarray(frame_opencv)
        # next frame list
        display = create_display(frame, pixel_art_width, pixel_art_height, piece_images)
        # update to it actually updates what's happening
        p.display.update()
        clock.tick(video_fps)
    # if audio is done just quit
    p.mixer.music.stop()
    p.quit()
    quit()

def create_display(frame, pixel_art_width, pixel_art_height, piece_images):
    # Store the image pixel to display
    display = [] #empty list
    # Empty list sizeof aspect ratio
    for _ in range(pixel_art_height):
        row = [None] * pixel_art_width
        display.append(row)
    # Resize image to segment 
    frame = frame.resize((pixel_art_width, pixel_art_height), Image.Resampling.NEAREST)
    # converting it to grayscale
    frame = frame.convert("L")
    # Read pixel and store brightness
    for row in range(pixel_art_height):
        for column in range(pixel_art_width):
                brightness = frame.getpixel((column, row))

                if ascii_mode:
                    index = brightness * len(chars) / 256
                    character = chars[int(index)]
                    display[row][column] = character
                elif piece_mode:
                    piece_index = int(brightness * len(pieces) / 256)
                    display[row][column] = piece_images[piece_index]
                else:
                    red = green = blue = int(brightness)
                    color = red, green, blue 
                    display[row][column] = color
    return display


if __name__ == "__main__":
    main()