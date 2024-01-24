# -*- encoding: utf-8 -*-
'''
@File    :   broken_plot.py
@Time    :   2022/06/07 21:59:01
@Author  :   QinHsiu
@Version :   1.0
@Contact :   QinHsiu@github.com
'''

# here put the import lib
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import matplotlib

def cm2inch(a,b):
    return a/2.54,b/2.54

def plot_broken(ax1,ax2):
    #绘制断裂处的标记
    d = .85  #设置倾斜度
    kwargs = dict(marker=[(-1, -d), (1, d)], markersize=5,
    linestyle='none', color='k', mec='k', mew=1, clip_on=False)
    ax2.plot([0, 1], [0, 0],transform=ax2.transAxes, **kwargs)
    ax1.plot([0, 1], [1, 1], transform=ax1.transAxes, **kwargs)
    ax2.spines['bottom'].set_visible(False)#关闭子图2中底部脊
    ax1.spines['top'].set_visible(False)##关闭子图1中顶部脊
    ax2.set_xticks([])

def pl_broken(x,y,para_name,label_name,save_name):
    size1 = 20
    # matplotlib.use('PDF')
    plt.rcParams['font.family'] = ['Times New Roman']  # 因为图中有中文避免中文显示乱码
    # # plt.rcParams['figure.figsize'] = (8, 6)
    plt.rcParams['font.size'] = 20
    plt.rcParams['ps.useafm'] = True
    plt.rcParams['pdf.use14corefonts'] = True
    plt.rcParams['text.usetex'] = True

    # 构造fig,ax
    fig = plt.figure(figsize=(cm2inch(19, 15)))
    ax1 = fig.add_axes([0.15, 0.15, 0.8, 0.35])
    ax2 = fig.add_axes([0.15, 0.55, 0.8, 0.35])
    width=range(len(x))
    ax1.plot(width, y[2], c="gray", marker="s", label="Toys")
    ax1.plot(width, y[1],c="orange",marker="D",label="Beauty")
    ax1.plot(width, y[0], c="m", label="Sports", marker="o")
    ax2.plot(width, y[3], c="c", marker="p", label="ML-1M")
    ax2.plot(width, y[2], c="gray", marker="s", label="Toys")
    ax2.plot(width, y[1],c="orange",marker="D",label="Beauty")
    ax2.plot(width, y[0], c="m", label="Sports", marker="o")

    if label_name==r"HR@20":
        ax1.set_ylim(0.05, 0.15)
        ax2.set_ylim(0.3, 0.48)
        ax1.set_yticks(np.arange(0.05,0.175,0.025),weight="bold")
        ax2.set_yticks(np.arange(0.300, 0.48, 0.042),weight="bold")
        ax1.set_xticks(width,x,weight="bold")
        plt.legend(loc=(0.03, -0.2))  # drop
    else:
        ax1.set_ylim(0.025, 0.076)
        ax2.set_ylim(0.175, 0.235)  # drop
        ax1.set_yticks(np.arange(0.025, 0.076, 0.015),weight="bold")
        ax2.set_yticks(np.arange(0.175, 0.235, 0.015),weight="bold")  # drop
        ax1.set_xticks(width, x,weight="bold")
        plt.legend(loc=(0.03, -0.18))  # beta



    plot_broken(ax1, ax2)
    ax1.set_xlabel(para_name,weight="bold")
    # ax2.set_ylabel(r'%s'%label_name,weight="bold")  # 空格调节令ylabel居中
    plt.savefig(r'f_%s.png'%save_name, dpi=600)



def bar_broken(x, y, y1, y2, y3,y4, save_name, loc, x_label, y_label, y_value=None):
    # matplotlib.use('PDF')
    plt.rcParams['font.family'] = ['Times New Roman']  # 因为图中有中文避免中文显示乱码
    plt.rcParams['figure.figsize'] = (8, 6)
    plt.rcParams['font.size'] = 20
    plt.rcParams['ps.useafm'] = True
    plt.rcParams['pdf.use14corefonts'] = True
    plt.rcParams['text.usetex'] = True
    # wheat
    # palette = ["pink", "#ffeda0", "#9ecae1","bisque"]
    palette = ["bisque", "#ffeda0", "pink", "#9ecae1","orange"]
    type = 0
    x = [1.8 * i for i in range(len(x))]

    fig = plt.figure(figsize=(cm2inch(19, 15)))
    ax1 = fig.add_axes([0.15, 0.15, 0.8, 0.35])
    ax2 = fig.add_axes([0.15, 0.55, 0.8, 0.35])

    if type == 1:
        x_2 = [i for i in x]
        plt.bar(x_2, y3,
                width=0.4,
                color=palette[3],
                label=y_label[3]
                , hatch="\\\\")
        # 填充形状

        x_1 = [i for i in x]
        plt.bar(x_1, y2,
                width=0.4,
                color=palette[2],
                label=y_label[2]
                , hatch="/")
        # 填充形状

        x_ = [i for i in x]
        plt.bar(x_, y1,
                width=0.4,
                color=palette[1],
                label=y_label[1]
                , hatch=".")
        # 填充形状

        plt.bar(x, y,
                width=0.4,
                color=palette[0],
                label=y_label[0]
                , hatch="//")

    else:
        ax1.bar(x, y,
                width=0.2,
                color=palette[0],
                label=y_label[0]
                , hatch="//")

        x_ = [i + 0.2 for i in x]
        ax1.bar(x_, y1,
                width=0.2,
                color=palette[1],
                label=y_label[1]
                , hatch=".")

        x_1 = [i + 0.2 for i in x_]
        ax1.bar(x_1, y2,
                width=0.2,
                color=palette[2],
                label=y_label[2]
                , hatch="/")

        x_2 = [i + 0.2 for i in x_1]
        ax1.bar(x_2, y3,
                width=0.2,
                color=palette[3],
                label=y_label[3]
                , hatch="\\\\")
        x_3 = [i + 0.2 for i in x_2]
        ax1.bar(x_3, y4,
                width=0.2,
                color=palette[4],
                label=y_label[4]
                , hatch="-")

        ax2.bar(x, y,
                width=0.2,
                color=palette[0],
                label=y_label[0]
                , hatch="//")


        ax2.bar(x_, y1,
                width=0.2,
                color=palette[1],
                label=y_label[1]
                , hatch=".")


        ax2.bar(x_1, y2,
                width=0.2,
                color=palette[2],
                label=y_label[2]
                , hatch="/")


        ax2.bar(x_2, y3,
                width=0.2,
                color=palette[3],
                label=y_label[3]
                , hatch="\\\\")

        ax2.bar(x_3, y4,
                width=0.2,
                color=palette[4],
                label=y_label[4]
                , hatch="-")
        ax1.set_xticks([i + 0.5 for i in x], x_label, fontproperties='Times New Roman', size=20, weight='bold')
        plot_broken(ax1, ax2)


        if y_value=="HR@20":
            ax1.set_ylim(0.01, 0.15)
            ax2.set_ylim(0.3, 0.48)
            ax1.set_yticks(np.arange(0.01,0.15,0.025),weight="bold")
            ax2.set_yticks(np.arange(0.300, 0.48, 0.042),weight="bold")
            plt.legend(loc=(0, -0.1))
        else:
            ax1.set_ylim(0.005, 0.07)
            ax2.set_ylim(0.08, 0.25)
            ax1.set_yticks(np.arange(0.008, 0.07, 0.025), weight="bold")
            ax2.set_yticks(np.arange(0.08, 0.25, 0.042), weight="bold")
            plt.legend(loc=(0, -0.1))



    plt.savefig(save_name+".png")


def split(l):
    temp=[[],[],[],[],[]]
    for i in l:
        for k in range(len(i)):
            temp[k].append(i[k])
    return temp



if __name__ == '__main__':
    dropout_r=[0.1,0.2,0.3,0.4,0.5]
    # HR@20
    y_1_d=[[0.0705,0.0738,0.0765,0.0775,0.0794],[0.1171,0.1260,0.1289,0.1302,0.1289],[0.1219,0.1269,0.1307,0.1344,0.1368],[0.4518,0.4389,0.4260,0.3985,0.3846]]
    # NDCG@20
    y_2_d=[[0.0347,0.0359,0.0380,0.0382,0.0393],[0.0614,0.0648,0.0669,0.0672,0.0663],[0.0666,0.0695,0.0716,0.0735,0.0736],[0.2297,0.2207,0.2124,0.1920,0.1802]]
    pl_broken(dropout_r, y_2_d, para_name='Dropout Rate', label_name=r"NDCG@20", save_name="drop_n")

    x_=["Sports","Beauty","Toys","ML-1M"]
    y_=["w/o M","w/o F","w/o S","w/o U","Original"]
    HR=[[0.0411,0.0786,0.0788,0.0782,0.0794],[0.0752,0.1290,0.1292,0.1318,0.1298],[0.0635,0.1367,0.1343,0.1366,0.1368],[0.1379,0.4315,0.4513,0.4455,0.4518]]
    NDCG=[[0.0205,0.0384,0.0390,0.0389,0.0393],[0.0378,0.0667,0.0661,0.0679,0.0663],[0.0366,0.0738,0.0720,0.0733,0.0736],[0.0668,0.2157,0.2274,0.2272,0.2297]]

    HR=split(HR)
    NDCG=split(NDCG)
    bar_broken(x_,HR[0],HR[1],HR[2],HR[3],HR[4],"HR_ablation","lower right",x_,y_,"HR@20")


