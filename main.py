import os 
import prompt_toolkit
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.shortcuts import CompleteStyle


complete_1 = WordCompleter(["Encode","Decode"], ignore_case=True)

textI = prompt("Encode or Decode ", completer=complete_1,complete_style=CompleteStyle.MULTI_COLUMN)

if textI.strip().lower() == "encode":
    # encode
    message = input("Enter Message to be Encoded: ")
    with open("msg.txt","w") as file:
        file.write(f"MESSAGESTART{message}")
        file.close()
    os.system("copy /b shoebill.png + msg.txt shoebill_encoded.png")
    os.system("cls")
    
    try:
        os.remove("msg.txt")
    except:
        print("Not found")
        
elif textI.strip().lower() == "decode":
    # decode
    with open("shoebill.png","rb") as file:
        base_image = file.read()
        file.close()
    with open("shoebill_encoded.png","rb") as file:
        encoded_image = str(file.read())
        file.close() 
    
    index = encoded_image.find("MESSAGESTART") + 12
    print(encoded_image[index:-1])

    
else:
    raise ValueError("Has to be encode or decode (this is technically not an error dont say there was an error i could of just used a print statement)")
    