
# %%
from torch.utils import data
from binary_encoder import float2bin_sequence
from utils.dataset import SymbolicRegressionDataset
from torch.utils.data import DataLoader
from torchtext.legacy.data.field import Field
from torchtext.data.utils import get_tokenizer
from utils.lis import parse_with_parens
from data_generator import binary_operators, unary_operators
from utils.tokenizer import build_vocab

dataset_test = SymbolicRegressionDataset('data/test.csv')
dataset_train = SymbolicRegressionDataset('data/train.csv')

# %%
# Build the vocabulary for equations
eq_vocab = build_vocab(binary_operators + unary_operators)
eq_vocab

dataloader = DataLoader(dataset_test, batch_size=10, shuffle=True)
dataloader

# %%
# EQS = Field(lambda x: x, init_token = '<sos>', eos_token = '<eos>', batch_first = True)
# EQS.build_vocab(data_train)

# %%
# data_loader = DataLoader(data_test, batch_size=64, shuffle=True)
