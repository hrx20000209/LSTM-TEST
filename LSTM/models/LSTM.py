import torch


class LSTM(torch.nn.Module):
    def __init__(self, vocab_dim, embedding_dim, hidden_dim):
        super(LSTM, self).__init__()
        self.embedding = torch.nn.Embedding(vocab_dim, embedding_dim)
        self.lstm = torch.nn.LSTM(input_size=embedding_dim, hidden_size=hidden_dim, num_layers=1)
        self.output = torch.nn.Linear(hidden_dim, 2)

    def forward(self, x):
        pass
