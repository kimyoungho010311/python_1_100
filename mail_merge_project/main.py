#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open('mail_merge_project/Input/Names/invited_names.txt',mode= 'r') as names:
    name_list = names.readlines()

with open('mail_merge_project/Input/Letters/starting_letter.txt', mode= 'r') as file:
    letter = file.read()
    for name in name_list:
        stripped_name = name.strip()
        new_letter = letter.replace('[name]', stripped_name)
        with open(f'mail_merge_project/Output/ReadyTosend/letter_for_{stripped_name}.txt',mode = 'w') as com_letter:
            com_letter.write(new_letter)