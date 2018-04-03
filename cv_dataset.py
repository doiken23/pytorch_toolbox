##### ################################# #####
##### This code is written by Doi Kento #####
##### ################################# #####

import torch
import torch.utils.data as data_utils
import numpy as np
import tiffile
from pathlib import Path

class CV_Dataset(data_utils.Dataset):
    """
    This dataset is for cross validation.
    Args:
        data_path (str): path of root dir.
        cv_num    (int): the number of the cross validation.
        phase     (str): training pahse (train or val).
        trains    (lst): list of transformation function.
    Returns:
        img     (array): numpy array of image.
        label   (int)  : target label (0 or 1).
    """
    def __init__(self, data_path, cv_num=1, phase='train', transform=None):
        # set the parameter
        self.root      = Path(data_path)
        self.train_dir = self.root / 'train'
        self.imgs= []
        for i in range(1,6):
            file = open(self.train_dir / 'cv_{}.txt'.format(i))
            if i != self.phase:
                for line in file:
                    img_name, label = line.split(',')
                    label = int(label.replace('\n'))
                    self.imgs.append([img_name, label])

    def __getitem__(self, idx):
        img_name, label = self.imgs[idx]
        img = tifffile.imread(self.train_dir / img_name)

        return (img, label)

    def __len__(self):
        return len(self.imgs)

def normalize(img, mean, std):
    return (img - mean) / std
