from tkinter import *

def miles_to_km(user_input):
    try:
        answer = float(user_input) * 1.60934
        return round(answer,2)
    except ValueError:
        return 'Please enter a number' 

def get_user_input():
    user_input = entry.get()
    print(user_input)
    return user_input

def update_result():
    result.config(text= miles_to_km(get_user_input()))

#Create a new Window and configurations
window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=400, height=120)
window.config(padx=100, pady=20)


#Entries
entry = Entry(width=10)
entry.insert(END, string='0')
entry.grid(column= 2, row= 1, padx=5, pady=5)

#Buttons
button = Button(text='Calculate', command=update_result)
button.grid(column=2,row=3)


#Labels
miles = Label(text='Miles')
miles.grid(column=3,row=1)

is_eq_to = Label(text='is equal to')
is_eq_to.grid(column=1,row=2)

result = Label(text= miles_to_km(get_user_input()))
result.grid(column=2,row=2)




window.mainloop()