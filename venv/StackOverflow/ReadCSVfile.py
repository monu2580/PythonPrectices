"""import pandas as pd
import requests

url = 'http://www.smartroadsense.it/bb/12.335513/42.035682/12.758896/42.050826'
response = requests.get(url).json()

df = pd.DataFrame(response['data'])

print(df)"""

from pandas import DataFrame,read_csv
import pandas as pd
import sys

from matplotlib import pyplot as plt
from matplotlib import style


#ds = pd.read_csv("CsvFile1.csv",names=["Heading1","Heading2","Heading3","Heading4","Heading5","Heading6","Heading7","Heading8","Heading9","Heading10","Heading11","Heading12","Heading13","Heading14","Heading15","Heading16"])
#ds = pd.read_csv("CsvFile1.csv")
#print(ds.head(2))
#print(ds[0])


ds = pd.read_csv("CsvFile2.csv",names=['Total Cases for Trial during the Year (Col.5) = (Col.3+4)','S. No. (Col.1)'])
#print(ds['S. No. (Col.1)'],["Total Cases for Trial during the Year (Col.5) = (Col.3+4)"])  #Show all Column
print(ds["Total Cases for Trial during the Year (Col.5) = (Col.3+4)"])

#print(ds.'Arms Act, 1959 (Col.3))
#sortData = ds.sort_values(["Col4"])

# for i in ds.head(0):
#     print(i)

# plt.xlabel("X-Axis")
# plt.ylabel("Y-Axis")
# plt.style.
# plt.plot(ds.Col4)
# plt.show()
#