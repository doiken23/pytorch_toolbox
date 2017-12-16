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
            input = input.contiguous().view(-1, input.size(2)).squeeze()
        target = target(-1, 1)

        # compute the negative likelyhood
        logpt = F.log_softmax(input)
        logpt = logpt.gather(1,target)
        logpt = logpt.view(-1).squeeze()
        pt = Variable(logpt.data.exp())

        # implement the class balancing (Coming soon...)
        if self.weight is not None:
            if self.weight.type() != input.data.type():
                self.weight = self.weight.type_as(input.data)
            b_h_w, c = input.size()
            weight_tensor = torch.zeros(b_h_w, 1)
            weight_tensor[:,0] = weight[target.byte().squeeze()]

        # compute the loss
        if self.weight is not None:
            loss = -1 * weight_tensor * (1-pt)**self.gamma * logpt
        else:
            loss = -1 * (1-pt)**self.gamma * logpt

        # averaging (or not) loss
        if self.size_average:
            return loss.mean()
        else:
            return loss.sum()


