from file_processing import *


def main():
    print("Caesar Cipher Program")
    choice = input("Choose an option:\n1. Encrypt/Decrypt Text\n2. Encrypt/Decrypt File\nEnter your choice (1/2): ").strip()

    if choice == "1":
        mode = input("Would you like to encrypt or decrypt? ").strip().lower()
        text = input("Enter the text: ").strip()
        shift = int(input("Enter the shift value: "))
        
        if mode in ["encrypt", "decrypt"]:
            result = caesar_cipher(text, shift, mode)
            print(f"The resulting text is: {result}")
        else:
            print("Invalid mode. Please choose 'encrypt' or 'decrypt'.")
    
    elif choice == "2":
        input_file = input("Enter the input file name (with extension): ").strip()
        output_file = input("Enter the output file name (with extension): ").strip()
        mode = input("Would you like to encrypt or decrypt the file? ").strip().lower()
        shift = int(input("Enter the shift value: "))
        
        if mode in ["encrypt", "decrypt"]:
            file_processing(input_file, output_file, shift, mode)
        else:
            print("Invalid mode. Please choose 'encrypt' or 'decrypt'.")
    
    else:
        print("Invalid choice. Please enter '1' or '2'.")

if __name__ == "__main__":
    main()
