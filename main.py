
# %%
from torch.utils import data
from binary_encoder import float2bin_sequence
from utils.dataset import SymbolicRegressionDataset
from torch.utils.data import DataLoader
from torchtext.legacy.data.field import Field
from torchtext.data.utils import get_tokenizer
from utils.lis import parse_with_parens
from data_generator import all_program_tokens
from utils.program_tokenizer import build_vocab, one_hot_decode_program, one_hot_encode_program

dataset_test = SymbolicRegressionDataset('data/test.csv')
dataset_train = SymbolicRegressionDataset('data/train.csv')

# %%
# Build the vocabulary for equations
program_vocab = build_vocab(all_program_tokens)
program_vocab

dataloader = DataLoader(dataset_test, batch_size=10, shuffle=True)
dataloader

# %%
one_hot_encode_program(dataset_test[0][1], program_vocab)

# %%
# EQS = Field(lambda x: x, init_token = '<sos>', eos_token = '<eos>', batch_first = True)
# EQS.build_vocab(data_train)

# %%
# data_loader = DataLoader(data_test, batch_size=64, shuffle=True)
