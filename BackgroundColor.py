from PIL import Image

def main():
    path = "C:\\Users\\vlada\\Documents\\Python\\BackgroundColor\\ATD401.jpg"
    picture = Image.open(path)
    """""
    sirka, vyska = obrazek.size
    x = 0
    while x < sirka:
        y = 0
        while y < vyska:
        #max r,g,b = 255, min = 0
            r, g, b = obrazek.getpixel((x,y))
            prumer = int((r+g+b)/3)
        #obrazek.putpixel((x,y), (g, b, r))
        #obrazek.putpixel((x,y), (prumer, prumer, prumer))
        #obrazek.putpixel((x,y), (255-prumer, 255-prumer, 255-prumer))
            if prumer > 127:
                obrazek.putpixel((x,y), (r+10, g+10, b+10))
            #obrazek.putpixel((x,y), (255, 255, 255))
            else:
                obrazek.putpixel((x,y), (r-10, g-10, b-10))
            #obrazek.putpixel((x,y), (0, 0, 0))
                y += 1
        x += 1
        """
    picture.show() #obrazek.show()

if __name__ == "__main__":
    main()