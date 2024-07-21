from armstrong import is_armstrong_number 
from encryption import generate_key , encrypt_message , decrypt_message

def secure_data_flow(user_input , color_code , message):
    if is_armstrong_number(user_input):
        key = generate_key(color_code)
        encrypted_message = encrypt_message(message , key)
        return encrypted_message
    else:
        raise ValueError("Invalid Armstrong number")
    
if __name__ == "__main__":
    user_input = int(input("Enter an Armstrong number: "))
    color_code = input("Enter a color code: ")
    message = input("Enter a mesage") 

    try: 
        encrypted_message = secure_data_flow(user_input , color_code , message) 
        print(f"Encrypted message: {encrypted_message}")
    except ValueError as e :
        print(e)      