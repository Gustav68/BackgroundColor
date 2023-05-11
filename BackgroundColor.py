from PIL import Image

def main():
    path = "C:\\Users\\vlada\\Documents\\Python\\BackgroundColor\\ATD401.jpg"
    picture = Image.open(path)
    
    width, height = picture.size
    x = 0
    while x < width:
        y = 0
        while y < height:
        #max r,g,b = 255, min = 0
            r, g, b = picture.getpixel((x,y))
            average = int((r+g+b)/3)
        #obrazek.putpixel((x,y), (g, b, r))
        #obrazek.putpixel((x,y), (prumer, prumer, prumer))
        #obrazek.putpixel((x,y), (255-prumer, 255-prumer, 255-prumer))
            if average > 127:
                picture.putpixel((x,y), (r+10, g+10, b+10))
            #picture.putpixel((x,y), (255, 255, 255))
            else:
                picture.putpixel((x,y), (r-10, g-10, b-10))
            #picture.putpixel((x,y), (0, 0, 0))
                y += 1
        x += 1
    
    picture.show() #obrazek.show()

if __name__ == "__main__":
    main()