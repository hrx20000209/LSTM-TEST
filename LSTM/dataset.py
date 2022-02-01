import torch
from torch.utils.data.dataset import Dataset


class SentimentDataset(Dataset):
    def __init__(self, path):
        self.data = []
        self.labels = []
        with open(path, "r") as file:
            for line in file:
                self.data.append(line)

    def __getitem__(self, index):
       self.data[index], self.labels[index]

    def __len__(self):
        return len(self.data)