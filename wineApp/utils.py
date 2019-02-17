from .models import Wine
import pandas as pd

def loadData(path):
    df = pd.read_csv(path)
    for index, row in df.iterrows():
        w = Wine(
            country = row['country'],
            description = row['description'],
            designation = row['designation'],
            points = row['points'],
            price = row['price'],
            province = row['province'],
            region_1 = row['region_1'],
            region_2 = row['region_2'],
            variety = row['variety'],
            winery = row['winery']
        )
        w.save()
        # print(row['c1'], row['c2'])
    print(df[0])