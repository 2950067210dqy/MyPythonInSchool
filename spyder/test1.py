import pandas as pd
data={
    'name':['张三','张三1','张三2','张三3'],
    'sex':['男','男','男','女'],
    'year':[2001,2001,2003,2002],
    'city':['北京' ,'北京' ,'北京' ,'北京' ]
}
df1=pd.DataFrame(data,columns=['name','year','sex','city'])
print(df1)
df2 = df1
print(df2.reindex(['a','b','c','d','e'],fill_value=0))
