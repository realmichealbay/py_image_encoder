import os 

textI = input("Select Encode or Decode")

if textI.strip().lower() == "encode":
    # encode
    message = input("Enter Message to be Encoded: ")
    with open("msg.txt","w") as file:
        file.write(message)
        file.close()
    with open("shoebill.png","rb") as file:
        base_image = file.read()
        print(base_image)



    try:
        os.remove("msg.txt")
    except:
        print("Not found")
        
elif textI.strip().lower() == "decode":
    # decode
    print("wip")
else:
    raise ValueError("Has to be encode or decode")