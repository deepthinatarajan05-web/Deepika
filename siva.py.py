#PIL (Python Imaging Library) is a popular library for image processing in Python.
#pip install Pillow

# LOGIN + IMAGE PROCESSING (only if login correct)

from PIL import Image
# LOGIN
while True: 
     username = input("Enter your name: ")
     password = input("Enter your password: ")

     if username == "deepika" and password == "123":
         print("Login successful")
         break
     else:
         print("Invalid username or password")


#IMAGE LOAD

filename = "siva.jpg"
try:
        with Image.open(filename) as img:
            img.load()
            print(type(img))
            print(isinstance(img, Image.Image))
            img.show()

# CONVERTED IMAGE (Flip vertically) 
            convertedimg = img.transpose(Image.FLIP_TOP_BOTTOM)
            convertedimg.show()

# CROPPED IMAGE  
            print("Original size:", img.size)
            left, top = 400, 400
            right, bottom = 1600, 1600
            right = min(right, img.width)
            bottom = min(bottom, img.height)

            if right > left and bottom > top:
                croppedimg = img.crop((left, top, right, bottom))
                print("Cropped size:", croppedimg.size)
                croppedimg.show()
            else:
                print("Cannot crop: image too small for these coordinates.")

 # CROPPED IMAGE 
            width, height = img.size
            crop_width, crop_height = 200, 100
            crop_width = min(crop_width, width)
            crop_height = min(crop_height, height)

            left = (width - crop_width) // 2
            top = (height - crop_height) // 2
            right = left + crop_width
            bottom = top + crop_height
            croppedimg = img.crop((left, top, right, bottom))
            print("Cropped img size:", croppedimg.size)
            croppedimg.show()
            
#width=355, crop_width=200
#left = (355 - 200) // 2 = 77
#top = (240 - 100) // 2 = 70
#right = 77 + 200 = 277
#bottom = 70 + 100 = 170
#So the crop box is (77, 70, 277, 170)'''
            
# RESIZE #(200, 100),(50,25)lowres_img = croppedimg.resize((croppedimg.width // 4, croppedimg.height // 4)) print("Low-res size:", lowres_img.size)lowres_img.show()

# ROTATE
            rotatedimg = img.rotate(45, expand=True)
            rotatedimg.show()
            rotatedimg = img.rotate(45)
            rotatedimg.show()

except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")



    

