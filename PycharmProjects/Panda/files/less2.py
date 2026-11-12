import pandas as pd

titanik_df = pd.read_csv("Boston-house-price-data.csv")
# print(titanik_df)

print(titanik_df.info())#Загальна інформація
# print(titanik_df.head(5))#Перші 5 рядків
# print(titanik_df.tail(3))#Останні 5 рядків

# print(titanik_df["Name"])
# print(titanik_df[["Name","Age","Sex"]])
# print(titanik_df[titanik_df["Age"]>20])
