from PIL import Image, ImageDraw

def change_background_color(source, background_color, output):
    
    picture = Image.open(source).convert("RGBA")
    picture_update = Image.new("RGBA", picture.size, background_color)
    picture_update.paste(picture, (0, 0), picture)
    picture_update.save(output)  # Save the modified image to a file
    picture_update.show()  # Display the modified image
    
def main():
    path_source = "C:\\Users\\vlada\\Documents\\Python\\BackgroundColor\\ATD401.png"
    path_target = "C:\\Users\\vlada\\Documents\\Python\\BackgroundColor\\ATD401_update.png"
    background = (10, 30, 50)
    change_background_color(path_source, background, path_target)

if __name__ == "__main__":
    main()