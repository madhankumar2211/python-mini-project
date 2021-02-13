from PIL import Image
import stepic

#Encode data into image
def encode():
	img	= input('Enter image name(with extension) : ')
	image = Image.open(img,'r')
	
	data = input("Enter data to be encoded : ")
	if (len(data) == 0):
		raise ValueError('Data is empty')
        
	img1 = stepic.encode(image, bytes(data,'utf-8'))
	new_img_name = input("Enter the name of new image(with extension) : ")
	img1.save(new_img_name, str(new_img_name.split(".")[1].upper()))
	print('date encoded into image')

#Decode the image so as to extract the hidden data from the image
def decode():
	img = input("Enter image name(with extension) : ")
	image = Image.open(img, 'r')
	
	stegoImage = stepic.decode(image)
	return(stegoImage)
	
if __name__ == '__main__' :
    a = int(input(":: Welcome to Steganography ::\n"
                        "1. Encode\n2. Decode\n"))
    if (a == 1):
        encode()
 
    elif (a == 2):
        print("Decoded Word :  " + decode())
    else:
        raise Exception("Enter correct input")

