import numpy as np
import pandas as pd
x13=pd.DataFrame({
    "A":[10,20,np.nan,40],
    "B":[50,np.nan,50,70],
    "C":[np.nan,80,90,100],
    "G":["x","y","x","y"]
})
print("original data is",x13)


x14=x13.copy()
x14["A"]=x14["A"].fillna(x14["A"].mean())
print(x14)

x15=x14.groupby("G").mean()
print(x15)





print("----------------------------------------")


print("coloumn sum is ",x14.sum(axis=1,numeric_only=True))
print("----------------------------------------")


x16=x14.groupby("G")["B"].mean()
x17=x14.groupby("G")["B"].agg(["count","mean"])

print(x16)

print(x17)
