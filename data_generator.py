# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import pandas as pd
from utils.data_generator_utils import generate_random_eq, is_eq_valid
from utils.lis import eval_lisp, parse


GENERATED_SEQ_LENGTH = 10

# %%
binary_operators = ["^", "*", "+", "-", "/"]
unary_operators = ["sin", "cos"]
constants_etc = ['(', ')', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 't']
all_program_tokens = binary_operators + unary_operators + constants_etc
generate_random_eq(binary_operators, unary_operators, 3)


# %%
eqs = list(set([generate_random_eq(binary_operators, unary_operators, 3) for i in range(0, 20000)]))
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
    for i in range(1, GENERATED_SEQ_LENGTH):
        try:
            num = eval_lisp(parse(fun.replace('t', str(i))))
            int_seq.append(round(num, 2))
        except:
            pass
    X.append(int_seq)
len(X)


# %%
data = pd.DataFrame(X)
data['eqs'] = eqs
data.dropna(inplace = True)
for i in range(0, 8):
    data[i] = data[i]


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



