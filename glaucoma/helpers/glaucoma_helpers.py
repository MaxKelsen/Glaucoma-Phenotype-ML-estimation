"""
This file is part of the Glaucoma Phenotype ML Estimation project.

 Glaucoma Phenotype ML Estimation is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.


The Glaucoma Phenotype ML Estimation project is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with the Glaucoma Phenotype ML Estimation project.  If not, see <http://www.gnu.org/licenses/>.

"""
import os
from typing import List

from matplotlib import pyplot as plt
from fastai.torch_core import flatten_model
from fastai.layers import CrossEntropyFlat
from fastai.vision import *
import torch
from torch import tensor
import matplotlib.image as mpimg
from sklearn.metrics import accuracy_score
from multiprocessing import Pool
from PIL import Image


def arch_summary(arch):
    model = arch(False)
    tot = 0
    for i, l in enumerate(model.children()):
        n_layers = len(flatten_model(l))
        tot += n_layers
        print(f'({i}) {l.__class__.__name__:<12}: {n_layers:<4}layers (total: {tot})')


def get_groups(model, layer_groups):
    group_indices = [len(g) for g in layer_groups]
    curr_i = 0
    group = []
    for layer in model:
        group_indices[curr_i] -= len(flatten_model(layer))
        group.append(layer.__class__.__name__)
        if group_indices[curr_i] == 0:
            curr_i += 1
            print(f'Group {curr_i}:', group)   
            group = []
            
            
class FakeData:
    def __init__(self):
        self.c = 2
        self.path = ''    
        self.device = None
        self.loss_func = CrossEntropyFlat(axis=1)

def is_number(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def parse_files(path, key_string = ''):
    files = []
    for r,d,f in os.walk(path):
        for file in f:
            if key_string in file:
                files.append(os.path.join(r,file))
    return files

def return_uniq_index(list_file):
    seen = set()
    uniq = []
    for i,x in enumerate(list_file):
        if x not in seen:
            uniq.append((i,x))
            seen.add(x)

def return_duplicates(list_file):
    seen = set()
    uniq = []
    repeated =[]
    for x in list_file:
        if x not in seen:
            uniq.append(x)
            seen.add(x)
        else:
            repeated.append(x)
    return repeated

def plot_idx(unzipped_files, idx):
    img=mpimg.imread(unzipped_files[idx])
    h,_ = os.path.split(unzipped_files[idx])
    print(h)
    imgplot = plt.imshow(img)
    plt.show()


def split_unzipped(unzipped_files: List):
    unzipped_head =[]
    unzipped_tail =[]
    for file in unzipped_files:
        h,t = os.path.split(file)
        unzipped_head.append(h)
        unzipped_tail.append(t)
    return unzipped_head, unzipped_tail

def categorical_convert_metrics(preds):
    y = preds[1] *2
    y_hat = preds[0].t().numpy()[0]
    #round up to closest bin:
    y_hat_round = torch.reshape(tensor([round(float(num*2))/2. for num in y_hat]),(-1,1)) *2 
    acc = accuracy_score(y_hat_round,y)
    print("accuracy: " +str(acc))
    return y_hat_round, y


def crop_files(list_of_images, crop_tuple, save_path = None, num_cpu = 1):
    #crop tuple format (left,top,right,bottom)
    #use all cpus
    cropped_images = []
    arguments = [(image, crop_tuple, save_path) for image in list_of_images]
    with Pool(processes = num_cpu) as pool:
        results = pool.starmap(crop_file, arguments)
        
        
def crop_file(image_file, crop_tuple, save_path = None):
    assert len(crop_tuple) == 4
    im = Image.open(image_file)
    iml = im.crop(crop_tuple)
    if save_path:
        iml.save(save_path / os.path.basename(image_file))
    else:
        return iml