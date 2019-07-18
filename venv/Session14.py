from pandas import DataFrame,read_csv
import matplotlib.pyplot as plot
import pandas as pd
import sys
import matplotlib
from matplotlib import pyplot as plt
from matplotlib import style

style.use('ggplot')


#info = ['watch','mobile','book','pen']
#data1 = [215,558,1242,80]

#dataSet = list(zip(info,data1))
#print(dataSet)

#df = pd.DataFrame(data=dataSet,columns=['Product','Price'])
#print(df)


#df.to_csv("ProductPrice.csv",index=False,header=False)

#df=pd.read_csv("UserDetails.csv")
# df=pd.read_csv("UserDetails.csv",header=None)
df=pd.read_csv("ProductPrice.csv",names=['Product','Price'])
print(df)
#print(df.dtypes)

sdf = df.sort_values(['Price'],ascending=True)
#print(sdf)

#print(sdf.head(2))
print(''
      '-----------------------------------------')

#print(df['Price'].max())


#df['Price'].plot()

plt.plot(df['Price'],'g',label='Price', linewidth=5)

plt.show()
