import pandas as pd
import numpy as np
g7_pop=pd.Series([35.467,63.951,80.940,60.665,127.061,64.511,318.523])
print(g7_pop)
g7_pop.name='g7 population in millions'
print(g7_pop)
print(g7_pop.dtype)
print(g7_pop.values)
print(type(g7_pop.values))
print(g7_pop[0])
print(g7_pop[1])
print(g7_pop.index)
g7_pop.index=['Canada','France','Germany','Italy','Japan','United Kingdom','United States']
print(g7_pop)
cap=pd.Series({
    "Switzerland" : "Bern",
    "Norway" : "Oslo",
    "Sweden" : "Stockholm",
    "Finland" : "Helsinki",
    "Iceland" : "Reykjavík"
},name="Capital of countries")
print(cap)
cap1=pd.Series(["Bern","Oslo","Stockholm","Helsinki","Reykjavík"]
               ,index=["Switzerland","Norway","Sweden","Finland","Iceland"]
               ,name="Capital of countries1")
print(cap1)
print(pd.Series(g7_pop,index=["France","Germany","Italy","Spain"]))

print("\n=====Indexing=====\n")

print(g7_pop['Canada'])
print(g7_pop['Japan'])
print(g7_pop.iloc[0])
print(g7_pop.iloc[-1])
print(g7_pop[["Italy","France"]])
print(g7_pop.iloc[[0,2]])
print(g7_pop["Canada":"Italy"])
print(g7_pop[1:4])

print("\n=====Conditional Selection=====\n")

print(g7_pop>70)
print(g7_pop[g7_pop>70])
print("The mean is: ",g7_pop.mean())
print(g7_pop>g7_pop.mean())
print(g7_pop[g7_pop>g7_pop.mean()])
print("The standard deviation is: ",g7_pop.std())

print("\n=====Operations and Methods=====\n")

print(g7_pop*1000000)
print(cap*10000)
print(cap+"wow!!")
print("The mean from France to Italy is: ",g7_pop["France":"Italy"].mean())
print(np.log(g7_pop))

print("\n=====Boolean Arrays=====\n")
print(g7_pop>80)
print(g7_pop[g7_pop>80])
print(g7_pop[(g7_pop>80) | (g7_pop<40)])
print(g7_pop[(g7_pop>80) & (g7_pop<200)])

print("\n=====Modifying Series=====\n")

g7_pop['Canada']=40.5
print(g7_pop)
g7_pop["Iceland"]=1.34
print(g7_pop)
print("Last element value:",g7_pop.iloc[-1])
g7_pop.iloc[-1]=500
print(g7_pop)
g7_pop[g7_pop<70]=99.99
print(g7_pop)
