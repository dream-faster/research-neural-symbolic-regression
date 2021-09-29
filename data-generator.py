# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd
from utils import generate_random_eq, is_eq_valid
from lis import eval_lisp, parse


# %%
symbols = ["*", "*", "+", "-"]
generate_random_eq(symbols, 3)


# %%
eqs = list(set([generate_random_eq(symbols, 3) for i in range(0, 20000)]))
len(eqs)


# %%
ts = [1,2,3,5,10]

eqs = [eq for eq in eqs if is_eq_valid(eq, ts) == True]
len(eqs)


# %%
# because we need to wrap int casting into a try-catch block, we can't use array comprehensionran
X = []
for fun in eqs:
    int_seq = []
    for i in range(1, 10):
        try:
            int_seq.append(int(eval_lisp(parse(fun.replace('t', str(i))))))
        except:
            pass
    X.append(int_seq)
len(X)


# %%
data = pd.DataFrame(X)
data['eqs'] = eqs
data.dropna(inplace = True)
data[0] = data[0].astype(int)
data[1] = data[1].astype(int)
data[2] = data[2].astype(int)
data[3] = data[3].astype(int)
data[4] = data[4].astype(int)
data[5] = data[5].astype(int)
data[6] = data[6].astype(int)
data[7] = data[7].astype(int)
data[8] = data[8].astype(int)

data.shape[0]


# %%
data


# %%
from sklearn.model_selection import train_test_split
train, test = train_test_split(data, test_size=0.6)


# %%
train.to_csv('./data/train.csv')


# %%
test.to_csv('./data/test.csv')


# %%



