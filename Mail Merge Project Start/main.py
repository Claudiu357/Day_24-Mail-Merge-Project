#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
with open("Input/Names/invited_names.txt", 'r') as file:
    names = []
    lines = file.readlines()
    for line in lines:
        names.append(line.strip())

for name in names:
    with open("Input/Letters/starting_letter.txt", 'r') as file:
        filedata = file.read()
        replaced_text = filedata.replace("[name]", name)
        with open(f"Output/ReadyToSend/{name}_letter.txt", "w") as new_file:
            new_file.write(replaced_text)
            print(replaced_text)

