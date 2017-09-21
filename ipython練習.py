# encoding=utf8
import pandas as pd
import numpy as np

# 建立一個六列七欄的自然分布隨機數值的資料表
df1 = pd.DataFrame(np.random.randn(6,7),
                   index=list(range(0,12,2)),
                   columns=(range(0,7,1)))

print df1
print df1[:2]
print df1[2:]
# 加iloc後可以做縱切
print df1.iloc[:2,2:]