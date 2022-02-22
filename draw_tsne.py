# -*- coding: utf-8 -*-
# @Time    : 2020/9/5 0:10
# @Author  : Hui Wang

from collections import defaultdict
import tqdm
import random
import numpy as np
from sklearn.manifold import TSNE

def train_tsne_(data_name, epoch=10):

    emb = np.load(f'npys/{data_name}_{epoch}.npy') # id 的embeddding
    lines = open(f'npys/{data_name}_t-SNE.txt').readlines()
    # 每一行是
    # label1: id1, id2, id4
    # label2: id3, id5, id6
    # label3: id7, id8, id9
    all_items = []
    for i, line in enumerate(lines):
        lable, items = line.strip().split(':')
        items = items.split(',')
        for item in items:
            all_items.append(int(item))
    features = emb[all_items] # 取出所有待画id的embedding
    tsne_output = TSNE(n_components=2, random_state=1024).fit_transform(features)
    np.save(f'npys/{data_name}_{epoch}.npy', tsne_output)

# 先训练t-SNE
data_name = 'Movielens'
for epoch in [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]:
    train_tsne_(data_name, epoch)

# 再画
import matplotlib
matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42
import matplotlib.pyplot as plt
import os
plt.rcParams["font.family"] = "Times New Roman"

def get_target(data_name):
    lines = open(f'npys/{data_name}_t-SNE.txt').readlines()
    targets = []
    for i, line in enumerate(lines):
        lable, items = line.strip().split(':')
        items = items.split(',')
        targets.extend([int(i)] * len(items))
    return np.array(targets)


def plot_4(data_name, epochs):
    target = get_target(data_name)
    colors = np.array(['tomato', 'blue', 'orange', 'green', 'purple', 'deepskyblue'])
    colors = colors[target]
    fontsize = 20
    plt.figure(figsize=(20, 5))

    plt.subplot(141)
    plt.axis('off')
    X_tsne_10 = np.load(f'npys/{data_name}_{epochs[0]}.npy')
    plt.title("Start", fontsize=fontsize)
    # plt.text(-28, 25, '10 epochs', fontsize=fontsize)
    plt.scatter(X_tsne_10[:, 0], X_tsne_10[:, 1], c=colors)
    # 刻度不可见
    plt.xticks([])
    plt.yticks([])
    plt.subplot(142)
    plt.axis('off')
    X_tsne_40 = np.load(f'npys/{data_name}_{epochs[1]}.npy')
    plt.title("After Ele. Course", fontsize=fontsize)
    # plt.text(-39, 29, '40 epochs', fontsize=fontsize)
    plt.scatter(X_tsne_40[:, 0], X_tsne_40[:, 1], c=colors)
    plt.xticks([])
    plt.yticks([])
    plt.subplot(143)
    plt.axis('off')
    X_tsne_70 = np.load(f'npys/{data_name}_{epochs[2]}.npy')
    plt.title("After Ele. Course", fontsize=fontsize)
    # plt.text(-46, 27, '70 epochs', fontsize=fontsize)
    plt.scatter(X_tsne_70[:, 0], X_tsne_70[:, 1], c=colors)
    plt.xticks([])
    plt.yticks([])
    plt.subplot(144)
    plt.axis('off')
    X_tsne_100 = np.load(f'npys/{data_name}_{epochs[3]}.npy')
    plt.title("After Finetune", fontsize=fontsize)
    # plt.text(-42, 26, '100 epochs', fontsize=fontsize)
    plt.scatter(X_tsne_100[:, 0], X_tsne_100[:, 1], c=colors)
    plt.xticks([])
    plt.yticks([])
    plt.savefig(f'{data_name.lower()}_sne.pdf', format='pdf',
                bbox_inches='tight', pad_inches=0.05, dpi=100)
    plt.show()


data_name = 'Movielens'
epochs = [0, 20, 40, 60]
plot_4(data_name, epochs)
