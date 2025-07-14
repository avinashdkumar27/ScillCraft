from PIL import Image

def encrypt_image(input_path,output_path,K):

    image=Image.open(input_path)

    pixels=image.load()

    width, height = image.size
    for i in range(width):
        for j in range(height):
            r,g,b = pixels[i,j]
            # Simple encryption by shifting RGB values
            r = (r ^ K) % 256
            g = (g ^ K) % 256
            b = (b ^ K) % 256
            pixels[i,j] = (r,g,b)
            
    # Save the encrypted image
    image.save(output_path)

    print(f"Image encrypted and saved to: {output_path}")

def decrypt_image(input_path, output_path, K):

    encrypt_image(input_path,output_path,K)

print("SkillCraft Task 2: Image Encryption and Decryption")

mode = input("Encrypt or Decrypt? (e/d):").lower()
input_img = input("Enter input image path:")#e.g. input.png

output_img = input("Enter output image path:")#e.g. output.png

K = int(input("Enter a numeric key (1-255)"))

if mode == 'e':
    encrypt_image(input_img,output_img,K)
elif mode == 'd':
    decrypt_image(input_img,output_img,K)
else:
    print("Invalid mode.")
    

