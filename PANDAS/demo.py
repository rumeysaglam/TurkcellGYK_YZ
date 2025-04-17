import pandas as pd 

# Series -> Tek boyutlu diziler
# DataFrame -> Tablolar

dailySales = pd.Series([1500, 2500, 3500, 200, 1500, 1000, 6000])
print(dailySales)

print("Index : ", dailySales.index)
print("Values : ", dailySales.values)
print("Mean : ", dailySales.mean())
print("Max : ", dailySales.max())
print("Min : ", dailySales.min())

print(dailySales[3])

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
dailySales2 = pd.Series([1500, 2500, 3500, 200, 1500, 1000, 6000], index=days)
#print(dailySales2[3]) #Deprecated
print(dailySales2["Thursday"])

#SQL
#API
#salesData = #requests-> getSales("http://turkcell.com.tr//pasaj//sales", "get")
salesData = {
    "ProductName":["Elma", "Armut", "Üzüm", "İncir", "Portakal", "Elma", "Elma", "Portakal"],
    "Price":[200, 100, 500, 300, 40, 50, 120, 120],
    "QuantitySold":[20, 3, 5, 8, 9, 14, 26, 12]
}

df = pd.DataFrame(salesData)
print(df)

print(df["ProductName"])
print(type(df["ProductName"])) #Serie
print(df["Price"].mean())

print(df[["ProductName", "Price"]])
print(type(df[["ProductName", "Price"]])) #DataFrame

print(df.iloc[2]) #iloc -> index location
print(df.loc[df["ProductName"] == "Elma"])#loc, sqldeki where ile aynı işlemi yaptı

bestSales = df[df["QuantitySold"] > 10]
print(bestSales)

df["TotalIncome"] = df["Price"] * df["QuantitySold"]
print(df)

print(df.groupby("ProductName")["QuantitySold"].sum())

#Eksik verilerle çalışmak
salesData2 = {
    "ProductName":["Elma", "Armut", "Üzüm", "İncir", "Portakal", "Elma", "Elma", "Portakal"],
    "Price":[200, 100, 500, 300, None, 50, None, 120],
    "QuantitySold":[20, 3, None, 8, 9, 14, 26, 12]
}

df = pd.DataFrame(salesData2)

print(df.isnull().sum())

df["Price"].fillna(df["Price"].mean(), inplace=True)
print(df)

df.dropna(inplace=True) # 2 Üzüm ... verisi silindi.
print(df) 

print(df.sort_values("Price", ascending=True))

df.to_csv("salesDataAnalysis.csv", index=False)
df.to_excel("salesDataAnalysis.xlsx", index=False)