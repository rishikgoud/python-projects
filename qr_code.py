import qrcode 
user_input = input("Enter the text or URL: ")
img = qrcode.make(user_input)
# type(img)
file_location = input("Enter the file name: ")
img.save(file_location)