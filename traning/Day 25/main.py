import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey = len(data[data['Primary Fur Color']=='Gray'])
black = len(data[data['Primary Fur Color']=='Black'])
cinnamon = len(data[data['Primary Fur Color']=='Cinnamon'])



data_dic = {
    "Fur Color" : ['Gray', 'Cinamon', 'Black'],
    "Count" : [grey,cinnamon,black]
}

df = pd.DataFrame(data_dic)
df.to_csv('squirrel_count.csv')