import pandas as pd
d = {"str":["toto","titi"],"titi":[1,2]}
a = pd.DataFrame(data= d)


print(list(a["str"][a["titi"]==2])[0])
