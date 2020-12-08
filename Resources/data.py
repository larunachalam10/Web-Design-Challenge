import pandas as pd 

file= pd.read_csv("./Resources/cities.csv")
print(file)


print(file.to_html(index=True))