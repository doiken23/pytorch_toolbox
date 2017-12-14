import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.autograd import Variable

class MultiClassForcalLoss(nn.Module):

    def __init__(self, gamma=0, weight=None):
        super(self).__init__()

        self.gamma = gamma
        self.weight = weight

    def forward(self, input, target):
        if input.dim()>2:
            input = input.view(input.size(0), input.size(1), -1)
            input = input.transpose(1,2)
            input = onput.contiguous().view(-1, input.size(2)).squeeze()
        target = target(-1, 1)

        logpt = F.log_softmax(input)
        logpt = logpt.gather(1,target)
        logpt = logpt.view(-1).squeeze()
        pt = Variable(logpt.data.exp())

        loss = -1 * (1-pt)**self.gamma * logpt

        return loss.sum()


