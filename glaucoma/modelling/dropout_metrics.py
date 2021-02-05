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
from fastai.basic_train import DatasetType
from fastai.torch_core import to_np
import torch
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def entropy(probs, softmax=False):
    """Return the prediction of a T*N*C tensor with :
        - T : the number of samples
        - N : the batch size
        - C : the number of classes
    """
    probs = to_np(probs)
    prob = probs.mean(axis=0)

    entrop = - (np.log(prob) * prob).sum(axis=1)
    return entrop


def uncertainty_best_probability(probs):
    """Return the standard deviation of the most probable class"""
    idx = probs.mean(axis=0).argmax(axis=1)

    std = probs[:, np.arange(len(idx)), idx].std(axis=0)

    return std


def BALD(probs):
    """Information Gain, distance between the entropy of averages and average of entropy"""
    entrop1 = entropy(probs)
    probs = to_np(probs)

    entrop2 = - (np.log(probs) * probs).sum(axis=2)
    entrop2 = entrop2.mean(axis=0)

    ig = entrop1 - entrop2
    return ig


def top_k_uncertainty(s, k=5, reverse=True):
    """Return the top k indexes"""
    sorted_s = sorted(list(zip(np.arange(len(s)), s)),
                      key=lambda x: x[1], reverse=reverse)
    output = [sorted_s[i][0] for i in range(k)]
    return output


def get_preds_sample(learn, ds_type=DatasetType.Valid, n_sample=10, reduce=None,activ=None):
    """Get MC Dropout predictions from a learner, and eventually reduce the samples"""
    preds = []
    for i in range(n_sample):
        pred, y = learn.get_preds(ds_type=ds_type,activ=activ)
        pred = pred.view((1,) + pred.shape)
        preds.append(pred)
    preds = torch.cat(preds)
    if reduce == "mean":
        preds = preds.mean(dim=0)
    return preds, y

def plot_hist_groups(pred,y,metric,bins=None,figsize=(16,16)):
    TP = to_np((pred.mean(dim=0).argmax(dim=1) == y) & (y == 1))
    TN = to_np((pred.mean(dim=0).argmax(dim=1) == y) & (y == 0))
    FP = to_np((pred.mean(dim=0).argmax(dim=1) != y) & (y == 0))
    FN = to_np((pred.mean(dim=0).argmax(dim=1) != y) & (y == 1))
    
    result = metric(pred)
    
    TP_result = result[TP]
    TN_result = result[TN]
    FP_result = result[FP]
    FN_result = result[FN]
    
    fig,ax = plt.subplots(2,2,figsize=figsize)
    
    sns.distplot(TP_result,ax=ax[0,0],bins=bins)
    ax[0,0].set_title(f"True positive")
    
    sns.distplot(TN_result,ax=ax[0,1],bins=bins)
    ax[0,1].set_title(f"True negative")
    
    sns.distplot(FP_result,ax=ax[1,0],bins=bins)
    ax[1,0].set_title(f"False positive")
    
    sns.distplot(FN_result,ax=ax[1,1],bins=bins)
    ax[1,1].set_title(f"False negative")