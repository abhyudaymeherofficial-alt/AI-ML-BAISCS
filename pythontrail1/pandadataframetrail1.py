
import pandas as pd
import numpy as np
from matplotlib.pyplot import figure

df=pd.DataFrame({
    "Population" : [35.67,63.951,80.94,60.665,127.061,64.511,318.523],
    "GDP" : [1785387,2833687,3874437,2167744,4602367,2950039,17348075],
    "Surface Area" : [9984670,640679,357114,301336,377930,242495,9525067],
    "HDI" : [0.913,0.888,0.916,0.873,0.891,0.907,0.915],
    "Continent" : ["America","Europe","Europe","Europe","Asia","Europe","America"]
})
print(df)

df.index=["Canada","France","Germany","Italy","Japan","United Kingdom","United States"]
print(df)

print("\n")
print(df.columns)
print(df.index)
print("\n")


print(df.info())
print(df.size)
print(df.shape)

print("\n")
print(df.describe())

print("\n")
print(df.dtypes)
print(df.dtypes.value_counts())

print("\n")
print("+++++Indexing, Selection and Slicing+++++")
print("\n")

print(df.loc['Canada'])
print(df.iloc[-1])
print(df["Population"])

print("\n")
print(df["Population"].to_frame())

print("\n")
print(df[["Population","GDP"]])

print("\n")
print(df[1:3])
print(df.loc["Italy"])
print(df.loc["France":"Japan"])
print(df.loc["France":"Japan","Population"])

print("\n")
print(df.loc["France":"Japan",["Population","GDP"]])
print(df.iloc[0])
print(df.iloc[-1])
print(df.iloc[[0,1,-1]])
print(df.iloc[1:3])
print(df.iloc[1:5,3])
print(df.iloc[1:4,[2,-1]])
print(df.iloc[1:4,2:4])

print("======Conditional Statement=======\n")

print(df["Population"]>70)
print(df.loc[df["Population"]>70])
print(df.loc[df["Population"]>70,"GDP"])
print(df.loc[df["Population"]>70,["HDI","Surface Area","Continent"]])

print("======Dropping Stuff=======\n")
print(df.drop("Canada"))
print(df)
df=df.drop("Canada")
print(df)
print(df.drop(["France","Japan"]))
print(df.drop(columns=["Population","HDI"]))
print(df.drop(["Italy","United States"],axis=0))
print(df.drop(["HDI","Surface Area"],axis=1))
print(df.drop(["Italy","United States"],axis="rows"))
print(df.drop(["HDI","Surface Area"],axis="columns"))

print("======Operations=======\n")

print(df[["GDP","Surface Area"]])
print(df[["GDP","Surface Area"]]/100)

crisis=pd.Series([-100000,-0.3],index=["GDP","HDI"])
print(crisis)

print(df[["GDP","HDI"]]+crisis)

print("\n=======Modifying DataFrame=========\n")
langs=pd.Series(["French","German","Italian"],index=["France","Germany","Italy"],name="Language")
print(langs)
df["Langs"]=langs
print(df)

print("\n=======Replacing values per coloumns=========\n")

df['Langs']="English"
print(df)

print("\n=======Renaming coloumns=========\n")
print(df)
print(df.index)
print(df.columns)
df=df.rename(
    columns={
        "HDI" : "Human Development Index",
    },index={
        "United States":"USA",
        "United Kingdom":"UK",
    }
)
print(df)
print(df.rename(index=str.upper))
print(df.rename(index=lambda x:x.lower()))


print("\n=======Dropping Cols=========\n")
df=pd.DataFrame({
    "Population" : [35.67,63.951,80.94,60.665,127.061,64.511,318.523],
    "GDP" : [1785387,2833687,3874437,2167744,4602367,2950039,17348075],
    "Surface Area" : [9984670,640679,357114,301336,377930,242495,9525067],
    "HDI" : [0.913,0.888,0.916,0.873,0.891,0.907,0.915],
    "Continent" : ["America","Europe","Europe","Europe","Asia","Europe","America"]
})
df.index=["Canada","France","Germany","Italy","Japan","United Kingdom","United States"]
print(df.drop(columns=["HDI","GDP","Surface Area"]))

print("\n=======Adding values=========\n")

#df.append(pd.Series({"Population":3,"GDP":5},name="China")) <--- old version
#print(df)
df = pd.concat([
    df,
    pd.Series({"Population":3, "GDP":5}, name="China").to_frame().T # new version
])
print(df)

df.loc["China"]=pd.Series({"Population":140,"Continent":"Asia"})
print(df)

print("\n=======Creating new cols with other cols=========\n")

df["GDP per Capita"]=df["GDP"]/df["Population"]
print(df)

print("\n=======Statistical Info=========\n")

print(df.head())
print(df.describe())
population=df["Population"]
print("The min and max population are:",population.min(),population.max())
print(population.sum())
print(population.mean())
print(population.std())
print(population.median())
print(population.describe())
print(population.quantile(0.25))
print(population.quantile([0.2,0.4,0.6,0.8,1]))

print("\n=======Reading external data and plotting=========\n")
import matplotlib.pyplot as plt
df=pd.read_csv("C:/Users/91943/Downloads/Social_Network_Ads_with_datetime.csv")
print(df)

print(df.head())

df=pd.read_csv("C:/Users/91943/Downloads/Social_Network_Ads_with_datetime.csv",header=None)
print(df.head())

df.columns=["ID","M/F","AGE","EstimatedSalary","Purchase","Date/Time"]
print(df)

print("The shape is:",df.shape)
print(df.info())

print(df.tail(3))

print(df.dtypes)

print(pd.to_datetime(df["Date/Time"],format="%d-%m-%Y %H:%M").dt.date.head())
print(pd.to_datetime(df["Date/Time"],format="%d-%m-%Y %H:%M").dt.time.head())

print(df.head())
df.set_index("Date/Time", inplace=True)
print(df.head())

print("\n")
print(df.loc["23-04-2025 04:45"])

print("\n")
print(df.loc["02-02-2024 14:54":"19-04-2021 07:32"])

print("\n=========Putting everthing Together==========\n")

df=pd.read_csv("C:/Users/91943/Downloads/Social_Network_Ads_with_datetime.csv",
               names=["ID","Gender","Age","Salary","Purchase","date"],header=None,
               index_col="date",parse_dates=["date"],date_format="%d-%m-%Y %H:%M")
print(df)

'''print("\n=========Plotting Basics==========\n")

df.plot()
plt.show()

df["Salary"].plot()
plt.show()

df[["Age", "Purchase"]].plot()
plt.show()

df.plot(x="Age", y=["Salary", "Purchase"])
plt.show()

x=np.arange(-10,11)
plt.plot(x,x**2)
plt.show()

plt.title("My nice plot")
plt.plot(x,-1*(x**2))
plt.show()

df.plot(x="Age", y=["Salary", "Purchase"],figsize=(16,9),title="Sales data")
plt.show()'''

print("\n=========A more challenging parsing==========\n")

eth=pd.read_csv("C:/Users/91943/Downloads/crypto_prices_500_rows.csv",
                parse_dates=["Date(UTC)"])
print(eth.dtypes)
print(eth.head())

print("\n")
print(pd.to_datetime(eth["UnixTimeStamp"].head()))
print("\n")

print(pd.to_datetime(eth["Date(UTC)"].head()))
print("\n")

print(pd.read_csv("C:/Users/91943/Downloads/crypto_prices_500_rows.csv",
                  parse_dates=[0]).head())
print("\n")

eth=pd.read_csv("C:/Users/91943/Downloads/crypto_prices_500_rows.csv",
                parse_dates=["Date(UTC)"],index_col=0)
print(eth.head())
print("\n")


prices=pd.DataFrame(index=eth.index)
print(prices.head())
prices["Bitcoin"]=eth["UnixTimeStamp"]
prices["Ether"]=eth["Value"]
print(prices.head())

'''prices.plot(figsize=(12,6))
plt.show()

prices.loc["05-01-2024":"6-01-2024"].plot(figsize=(12,6))
plt.show()'''


print("\n=========Handling missing data==========\n")

print(pd.isnull(np.nan))
print(pd.isnull(None))
print(pd.isna(np.nan))
print(pd.isna(None))

print("\n=========Opposite one also exists==========\n")
print(pd.notnull(None))
print(pd.notnull(np.nan))
print(pd.notnull(3))

print("\n=========this will work with series and dataframe==========\n")
print(pd.isnull(pd.Series([1,np.nan,7])))
print(pd.notnull(pd.Series([1,np.nan,7])))
print(pd.isnull(pd.DataFrame({"Column A":[1,np.nan,7],
                              "Column B":[np.nan,2,3],
                              "Column C":[np.nan,2,np.nan]})))

print("\n=========Pandas operation with missing values==========\n")
print(pd.Series([1,5,np.nan]).count())
print(pd.Series([1,9,np.nan]).sum())
print(pd.Series([1,4,np.nan]).mean())

print("\n=========Filtering missing data==========\n")
s=pd.Series([1,2,3,np.nan,np.nan,4])
print(s)
print(pd.notnull(s))
print(pd.notnull(s).count())
print(pd.isnull(s).sum())
print(s[pd.notnull(s)])
print(pd.isnull(s))
print(pd.notnull(s))
print(s[pd.notnull(s)])

print("\n=========Dropping null values==========\n")

print(s.dropna())
df=pd.DataFrame({
    "Col A":[1,np.nan,30,np.nan],
    "Col B":[2,8,31,np.nan],
    "Col C":[np.nan,9,32,100],
    "Col D":[5,8,34,110]
})
print(df)
print(df.isnull())
print(df.isnull().sum())
print(df.dropna(axis=0))
print(df.dropna(axis=1))
df2=pd.DataFrame({
    "Col A":[1,np.nan,30],
    "Col B":[2,np.nan,31],
    "Col C":[np.nan,np.nan,100]
})
print(df2)

print("*******************************")
print(df.dropna(how="all"))
print("*******************************")
print(df.dropna(how="any"))
print("*******************************")
print(df)
print("*******************************")
print(df.dropna(thresh=3))
print("*******************************")
print(df.dropna(thresh=3,axis="columns"))

print("\n=========Filling null values==========\n")

print(s)
print(s.fillna(0))
print(s.fillna(s.mean()))
print(s.fillna(method="ffill"))
print(s.fillna(method="bfill"))
print(pd.Series([np.nan,3,np.nan,9]).fillna(method="ffill"))
print(pd.Series([1,np.nan,3,np.nan,np.nan]).fillna(method="bfill"))

print("\n=========Filling null values in dataframe==========\n")
print(df)
print(df.fillna({"Col A":0,"Col B":99,"Col C":df["Col C"].mean()}))
print(df.ffill(axis=0))
print(df.ffill(axis=1))

print("\n=========Checking if there is NA==========\n")
print(s)
print(s.dropna().count())
missing_values=len(s.dropna())!=len(s)
print(missing_values)
print(len(s))
print(s.count())
missing_values=s.count!=len(s)
print(missing_values)
print(pd.Series([True,False,False]).any())
print(pd.Series([True,False,False]).all())
print(pd.Series([True,True,True]).all())
print(s.isnull())
print(pd.Series([1,np.nan]).isnull().any())
print(pd.Series([1,2]).isnull().any())
print(s.isnull().any())
print(s.isnull().values)
print(s.isnull().values.any())
print("========cleaning not null values=========")
df=pd.DataFrame({"Sex":["M","F","F","D","?"]
                 ,"Age":[29,30,24,290,25]})
print(df)
print(df["Sex"].unique())
print(df["Sex"].value_counts())
print(df["Sex"].replace("D","F"))
print(df.replace({
    "Sex":{"D":"F","N":"M"},
    "Age":{290:29}
}))
print(df[df["Age"]>100])
df.loc[df["Age"]>100,"Age"]=df.loc[df["Age"]>100,"Age"]/10
print(df)

print("======Duplicates======")
ambassadors = pd.Series([
    'France',
    'United Kingdom',
    'United Kingdom',
    'Italy',
    'Germany',
    'Germany',
    'Germany'
], index=[
    'Gérard Araud',
    'Kim Darroch',
    'Peter Westmacott',
    'Armando Varricchio',
    'Peter Wittig',
    'Stefan Amonn',
    'Klaus Scharioth'
])
print(ambassadors)
print(ambassadors.duplicated())
print(ambassadors.duplicated(keep="last"))

