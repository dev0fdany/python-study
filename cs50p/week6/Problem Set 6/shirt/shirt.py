import sys
import os
from PIL import Image, ImageOps

def main():
    try:
            if len(sys.argv) == 1:
                print("Too few command-line arguments.")
                print(f"help:\n{sys.argv[1]} path-to-image1 path-to-image2")
                sys.exit()
            elif len(sys.argv) > 3:
                print("Too many command-line arguments.") 
                print(f"help:\n{sys.argv[1]} path-to-image1 path-to-image2")
                sys.exit()
            else:
                # If does'nt end in these formats.
                if not sys.argv[1].endswith(('png',"jpg","jpeg")) and sys.argv[2].endswith(("png","jpg","jpeg")):
                    print("Not an image file.")
                    sys.exit()
                # If they are differnt.
                elif sys.argv[1][-4:] == sys.argv[2][-4:]:
                    print("Input and output have different extensions.")
                    sys.exit()
                else:
                    images = []
                    for arg in sys.argv[1:]:
                        image = Image.open(arg).convert("RGBA")
                        images.append(image)
                    # Saving width of second image
                    image_width = images[1].width
                    # Creating a size tuple
                    square_size = (image_width, image_width)
                    # Resizing the second image to be a square
                    resized_background = ImageOps.fit(images[1], square_size, centering=(0.5, 0.5))
                    resized_foreground = ImageOps.fit(images[0], square_size)
                    # Overlaying the images
                    resized_background.paste(resized_foreground,(0, 0), resized_foreground)
                    file_name = input("Output file name(no extension needed):")
                    # What splitext outputs:
                    # ("C:/Images/picture", ".jpeg")
                    # In programming, counting starts at 0.[0] represents the first part: "C:/Images/picture"[1] represents the second part: ".jpeg"By putting [1] right after the function, you tell Python: "Run the split, but only hand me back the second piece (the extension)."
                    file_extension = os.path.splitext(sys.argv[2])[1]
                    full_file_name = file_name+file_extension
                    resized_background = resized_background.convert("RGB")
                    resized_background.save(full_file_name)
    except FileNotFoundError:
        print("File does not exist.")
        sys.exit()


if __name__ == "__main__":
    main()