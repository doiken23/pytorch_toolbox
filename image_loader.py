import numpy as np
import random
import torch
import torch.utils.data as data_utils
from PIL import Image
import glob

class ImageDataset(data_utils.Dataset):
    """
    data loader of any image
    Args:
        img_dir (str): path of image directory.
    """
    def __init__(self, img_dir, transform=None):
        self.img_dir = img_dir
        self.img_list = glob.glob(img_dir + '/*')
        self.img_list.sort()
        self.transform = transform

    def __getitem__(self, idx):
        img_path = self.img_list[idx]
        img = Image.open(img_path)

        if self.transform is not None:
            img = self.transform(img)

        return img

    def __len__(self):
        return len(self.img_list)
