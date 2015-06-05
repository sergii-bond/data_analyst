
index = pd.date_range('1/1/2000', periods=8)
index

s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
s

df = pd.DataFrame(np.random.randn(8, 3), index=index,
               columns=['A', 'B', 'C'])
df
df[1:3]

np.random.randn(2, 5, 4)
wp = pd.Panel(np.random.randn(2, 5, 4), items=['Item1', 'Item2'],
           major_axis = pd.date_range('1/1/2000', periods=5),
           minor_axis = ['A', 'B', 'C', 'D'])
wp

long_series = pd.Series(np.random.randn(1000))
long_series.head()
long_series.tail(3)

df[:2]

df.columns = [x.lower() for x in df.columns]
df

s.values
df.values
wp.values

df = pd.DataFrame({'one' : pd.Series(np.random.randn(3), index=['a', 'b', 'c']),
                   'two' : pd.Series(np.random.randn(4), index=['a', 'b', 'c', 'd']),
                   'three' : pd.Series(np.random.randn(3), index=['b', 'c', 'd'])})

df
df.ix[1]
row = df.ix[1]
column = df['two']

df.sub(row, axis='columns')
df.sub(row, axis=1)

df.sub(column, axis='index')
df.sub(column, axis=0)

dfmi = df.copy()

dfmi.index = pd.MultiIndex.from_tuples([(1,'a'),(1,'b'),(1,'c'),(2,'a')],
                                    names=['first','second'])
dfmi

column
dfmi.sub(column, axis=0, level='second')

wp
wp.values
major_mean = wp.mean(axis='major')
major_mean
wp.sub(major_mean, axis='major').values
#similarly for axis="items" and axis="minor"

df
df2 = df.copy()
df2['three'][0] = 1
df2
df+df2
df.add(df2, fill_value=0)

#eq, ne, lt, gt, le, and ge to Series and DataFrame
df.gt(df2)
df.ne(df2)

#Boolean Reductions
(df>0).all()
(df>0).any()
(df>0).any().any()

df.empty
pd.DataFrame(columns=list('ABC')).empty

pd.Series([True])
pd.Series([True]).bool()
pd.Series([False]).bool()
pd.DataFrame([[True]])
pd.DataFrame([[True]]).bool()
pd.DataFrame([[False]]).bool()

np.nan == np.nan
df+df == df*2
(df+df == df*2).all()
(df+df).equals(df*2)

# Order matters during comparison
df1 = pd.DataFrame({'col':['foo', 0, np.nan]})
df2 = pd.DataFrame({'col':[np.nan, 0, 'foo']}, index=[2,1,0])
df1
df2
df1.equals(df2)
df1.equals(df2.sort())

#Comination of frames
df1 = pd.DataFrame({'A' : [1., np.nan, 3., 5., np.nan],
                  'B' : [np.nan, 2., 3., np.nan, 6.]})
df2 = pd.DataFrame({'A' : [5., 2., 4., np.nan, 3., 7.],
                  'B' : [np.nan, np.nan, 3., 4., 6., 8.]})
df1
df2
df1.combine_first(df2)

combiner = lambda x, y: np.where(pd.isnull(x), y, x)
df1.combine(df2, combiner)

np.where([[True, False], [True, True]], [[1, 2], [3, 4]], [[9, 8], [7, 6]])

x = [1, 3, 4]
y = [10, 20, 30]
condition = [True, False, True]
zip(condition,x,y)
[xv if c else yv for (c,xv,yv) in zip(condition,x,y)]
np.where(condition)
np.where(condition, x, y)

#not clear here
np.where([[0, 1], [1, 0]])
np.where([[3, 1], [1, 2]])

#descriptive statistics

        #Series: no axis argument needed
        #DataFrame: “index” (axis=0, default), “columns” (axis=1)
        #Panel: “items” (axis=0), “major” (axis=1, default), “minor” (axis=2)

s.mean()
df
df.mean(0)
df.mean(1)
df.sum(0, skipna=False)
df.sum(1, skipna=False)
df.sum(axis=1, skipna=True)

ts_stand = (df - df.mean()) / df.std()
ts_stand.mean()
ts_stand.std()
xs_stand = df.sub(df.mean(1), axis=0).div(df.std(1), axis=0)
xs_stand.std(1)

df.cumsum()
df.cumprod()

#count   Number of non-null observations
#sum     Sum of values
#mean    Mean of values
#mad     Mean absolute deviation
#median  Arithmetic median of values
#min     Minimum
#max     Maximum
#mode    Mode
#abs     Absolute Value
#prod    Product of values
#std     Unbiased standard deviation
#var     Unbiased variance
#sem     Unbiased standard error of the mean
#skew    Unbiased skewness (3rd moment)
#kurt    Unbiased kurtosis (4th moment)
#quantile        Sample quantile (value at %)
#cumsum  Cumulative sum
#cumprod         Cumulative product
#cummax  Cumulative maximum
#cummin  Cumulative minimum

np.mean(df['one'])
np.mean(df['one'].values)

series = pd.Series(np.random.randn(500))
series[20:500] = np.nan
series[10:20]  = 5
series.nunique()

series = pd.Series(np.random.randn(1000))
series[::2] = np.nan
series[::2]
series
series.describe()
series.describe(percentiles=[.05, .25, .75, .95])
frame = pd.DataFrame(np.random.randn(1000, 5), columns=['a', 'b', 'c', 'd', 'e'])
frame
frame.ix[::2] = np.nan
frame
frame.describe()

s = pd.Series(['a', 'a', 'b', 'b', 'a', 'a', np.nan, 'c', 'd', 'a'])
s.describe()

frame = pd.DataFrame({'a': ['Yes', 'Yes', 'No', 'No'], 'b': range(4)})
frame.describe()

frame.describe(include=['object'])
frame.describe(include=['number'])
frame.describe(include='all')

s1 = pd.Series(np.random.randn(5))
s1
s1.idxmin(), s1.idxmax()
df1 = pd.DataFrame(np.random.randn(5,3), columns=['A','B','C'])
df1
df1.idxmin(axis=0)
df1.idxmax(axis=1)

df3 = pd.DataFrame([2, 1, 1, 3, np.nan], columns=['A'], index=list('edcba'))
df3
df3['A'].idxmin()

#text histogram
data = np.random.randint(0, 7, size=50)
data
s = pd.Series(data)
s.value_counts()
pd.value_counts(data)

#most frequent values
s5 = pd.Series([1, 1, 3, 3, 3, 5, 5, 7, 7, 7])
s5.mode()
df5 = pd.DataFrame({"A": np.random.randint(0, 7, size=50), 
"B": np.random.randint(-10, 15, size=50)})
df5.mode()

#make bins
arr = np.random.randn(20)
arr
factor = pd.cut(arr, 4)
factor
A
factor = pd.cut(arr, [-5, -1, 0, 1, 5])
factor

arr = np.random.randn(30)
factor = pd.qcut(arr, [0, .25, .5, .75, 1])
factor
pd.value_counts(factor)

arr = np.random.randn(20)
factor = pd.cut(arr, [-np.inf, 0, np.inf])
factor

#function application
df.apply(np.mean)
df.apply(np.mean, axis=1)
df.apply(lambda x: x.max() - x.min())
df.apply(np.cumsum)
df.apply(np.exp)

tsdf = pd.DataFrame(np.random.randn(1000, 3), columns=['A', 'B', 'C'], 
        index=pd.date_range('1/1/2000', periods=1000))
tsdf.apply(lambda x: x.idxmax())

def subtract_and_divide(x, sub, divide=1):
    return (x - sub) / divide

df
df.apply(subtract_and_divide, args=(5,), divide=1)
df
df.apply(pd.Series.interpolate)

#elementwise application of a function
f = lambda x: len(str(x))
df['one'].map(f)
df.applymap(f)

s = pd.Series(['six', 'seven', 'six', 'seven', 'six'],
   index=['a', 'b', 'c', 'd', 'e'])
t = pd.Series({'six' : 6., 'seven' : 7.})
s
s.map(t)


#iterators
        #Series: values
        #DataFrame: column labels
        #Panel: item labels

for col in df:
  print(col)

        #Series: (index, scalar value) pairs
        #DataFrame: (column, Series) pairs
        #Panel: (item, DataFrame) pairs

for item, frame in wp.iteritems():
  print(item)
  print(frame)

for row_index, row in df.iterrows():
  print('%s\n%s' % (row_index, row))

df2 = pd.DataFrame({'x': [1, 2, 3], 'y': [4, 5, 6]})

print(df2)
print(df2.T)
df2_t = pd.DataFrame(dict((idx,values) for idx, values in df2.iterrows()))
print(df2_t)

for r in df2.itertuples():
  print(r)

#Selection
dates = pd.date_range('1/1/2000', periods=8)
df = pd.DataFrame(np.random.randn(8, 4), index=dates, columns=['A', 'B', 'C', 'D'])
panel = pd.Panel({'one' : df, 'two' : df - df.mean()})

s = df['A']
s[dates[5]]
panel['two']

df
df[['B', 'A']] = df[['A', 'B']]
df


sa = pd.Series([1,2,3],index=list('abc'))
dfa = df.copy()
sa.b
dfa.A
panel.one

sa.a = 5
sa

dfa
dfa.A = list(range(len(dfa.index)))  # ok if A already exists, otherwise nothing is created and no error message
dfa

dfa['G'] = list(range(len(dfa.index))) # use this form to create a new column
dfa

x = pd.DataFrame({'x': [1, 2, 3], 'y': [3, 4, 5]})
x.iloc[1]
x.iloc[1] = dict(x=9, y=99)
x
x.iloc[1] = (9, 99)
x

s
s[:5]
s[::2]
s[::-1]
s2 = s.copy()
s2[:5] = 0
s2
df[:3]
df[::-1]

s1 = pd.Series(np.random.randn(6),index=list('abcdef'))
s1
s1.loc['c':]
s1.loc['b']
s1.loc['c':] = 0
s1

df1 = pd.DataFrame(np.random.randn(6,4), index=list('abcdef'),
   columns=list('ABCD'))
df1
df1.loc[['a','b','d'],:]
df1.loc['d':,'A':'C']
df1.loc['a']
df1.loc['a']>0
df1.loc[:,df1.loc['b']>0]
df1.loc['a','A']

s = pd.Series(["a","b","c","a"], dtype="category")
s

df = pd.DataFrame({"A":["a","b","c","a"]})
df
df["B"] = df["A"].astype('category')
df
df.describe()

s = pd.Series(range(-3, 4))
s
s[s>0]
s[(s < -1) | (s > 0.5)]
s[~(s < 0)]
df[df['A'] > 0]

df2 = pd.DataFrame({'a' : ['one', 'one', 'two', 'three', 'two', 'one', 'six'],
   'b' : ['x', 'y', 'y', 'x', 'y', 'x', 'x'],
   'c' : np.random.randn(7)})
df2.columns.values
df2
criterion = df2['a'].map(lambda x: x.startswith('t'))
criterion
df2[criterion]

# equivalent but slower
df2[[x.startswith('t') for x in df2['a']]]

df2[criterion & (df2['b'] == 'x')]
df2.loc[criterion & (df2['b'] == 'x'),'b':'c']

s = pd.Series(np.arange(5),index=np.arange(5)[::-1],dtype='int64')
s
s.isin([2, 4, 6])
s[s.isin([2, 4, 6])]
s[s.index.isin([2, 4, 6])]
s[[2, 4, 6]] #for comparison

np.random.randint(0, 2)

s1 = pd.Series([1,2,3,4,6,8,12])
s1
s1.diff()

#shapiro test for normality
w,p = scipy.stats.shapiro(data)
u, p = scipy.stats.mannwhitneyu(x, y)

#numpy
x = np.array([1, 2, 3])
x
y = x - np.mean(x)
y
y^2
pow(-1.0, 2)
np.repeat(2, 4)
a = np.array([[1,2], [3,4]])
a
np.insert(a, 1, 5, axis = 1)
