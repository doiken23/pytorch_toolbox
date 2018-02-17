import torch

import numpy as np
import random

class Numpy_Flip(object):

    def __init__(self):
        pass

    def __call__(self, image_array, p=0.5):
        if random.random() < p:
            image_array = image_array[:,:,::-1]

        if random.random() < p:
            image_array = image_array[:,::-1,:]

        return image_array

class Numpy_Rotate(object):

    def __init__(sel):f
        pass

    def __call__(self, image_array):
        angle = random.choices([0, 1, 2, 3])

        image_array = np.rot90(image_array, angle[0], (1,2))

        return image_array
