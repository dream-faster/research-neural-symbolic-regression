import pandas as pd
from torch.utils.data import Dataset
from utils.lis import parse_with_parens

class SymbolicRegressionDataset(Dataset):
    def __init__(self, file_name):

        data = pd.read_csv(file_name)

        self.y = data["eqs"]
        self.X = data.drop('eqs', axis = 1)
        self.X = self.X[["0", "1", "2", "3", "4", "5", "6", "7", "8"]].to_numpy()

    def __len__(self):
        return self.X.shape[0]

    def __getitem__(self, idx):

        value = self.X[idx]
        label = parse_with_parens(self.y[idx])

        return value, label
