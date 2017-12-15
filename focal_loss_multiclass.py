import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.autograd import Variable
# I refered https://github.com/clcarwin/focal_loss_pytorch/blob/master/focalloss.py

class MultiClassForcalLoss(nn.Module):

    def __init__(self, gamma=0, weight=None, size_average=True):
        super(self).__init__()

        self.gamma = gamma
        self.weight = weight

    def forward(self, input, target):
        if input.dim()>2:
            input = input.view(input.size(0), input.size(1), -1)
            input = input.transpose(1,2)
            input = onput.contiguous().view(-1, input.size(2)).squeeze()
        target = target(-1, 1)

        # compute the negative likelyhood
        logpt = F.log_softmax(input)
        logpt = logpt.gather(1,target)
        logpt = logpt.view(-1).squeeze()
        pt = Variable(logpt.data.exp())

        # implement the class balancing (Coming soon...)
        # if self.weight is not None:
        #    aaaaaaa

        # compute the loss
        loss = -1 * (1-pt)**self.gamma * logpt

        # averaging (or not) loss
        if self.size_average:
            return loss.mean()
        else:
            return loss.sum()


