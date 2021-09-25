#TODO: Create a letter using starting_letter.txt

#for each name in invited_names.txt
with open("./Input/Names/invited_names.txt") as names:
    for name in names.readlines():
        name = name.strip()
        with open(f"./Output/ReadyToSend/{name}_letter.txt", mode="w") as invite:
            with open("./Input/Letters/starting_letter.txt") as template:
                invite_text = template.read()
                personal_text = invite_text.replace("[name]", f"{name}")
                invite.write(personal_text)
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp