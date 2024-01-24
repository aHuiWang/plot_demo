# -*- coding: utf-8 -*-
# @Time    : 2022/10/2
# @Author  : XiuYuan Qin

import numpy as np
import matplotlib
import seaborn as sns
import pylustrator
pylustrator.start()

matplotlib.rcParams['pdf.fonttype'] = 42
matplotlib.rcParams['ps.fonttype'] = 42

import matplotlib.pyplot as plt
plt.rcParams["font.family"] = "Times New Roman"


def plot_bar():
    result1 = [0.0714, 0.0840, 0.0784, 0.0709]
    # Arial
    # plt.rcParams['font.sans-serif'] = ['Times New Roman']  # 如果要显示中文字体,则在此处设为：SimHei
    # plt.rcParams['axes.unicode_minus'] = False  # 显示负号

    plt.figure(figsize=(5, 4))
    plt.ylim(0.067, 0.088)
    labels = ['1', '2', '3', '4']

    # from matplotlib.font_manager import FontProperties
    # myfont = FontProperties(fname='times.ttf', size=25)
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)

    colors = ['tomato'] * 4
    # /,  \, |, -, +, x, o, O,., * 。
    plt.bar(np.arange(len(result1)), result1, ec='b', hatch=2 * '.', width=0.5,
            tick_label=labels,
            color=colors)
    plt.tight_layout()
    plt.savefig(f'pics/bar.png', format='png')  # 建议保存为svg格式,再用inkscape转为矢量图emf后插入word中
    plt.show()

def plot_line():

    x = np.array([1, 2, 3, 4, 5])
    model1 = np.array([0.2160, 0.1925, 0.1854, 0.1513, 0.1132])
    Ours = np.array([0.2416, 0.2331, 0.2165, 0.1943, 0.1715])

    # label在图示(legend)中显示。若为数学公式,则最好在字符串前后添加"$"符号
    # color：b:blue、g:green、r:red、c:cyan、m:magenta、y:yellow、k:black、w:white、、、
    # 线型：-  --   -.  :    ,
    # marker：.  ,   o   v    <    *    +    1
    plt.figure(figsize=(5, 4))
    # linestyle = "-"
    plt.grid(linestyle="-.")  # 设置背景网格线为虚线
    ax = plt.gca()
    # ax.spines['top'].set_visible(False)  # 去掉上边框
    # ax.spines['right'].set_visible(False)  # 去掉右边框

    linewidth = 2.0
    markersize = 7

    plt.plot(x, model1, marker='s', markersize=markersize, color="blue", label="Model1", linewidth=linewidth)
    plt.plot(x, Ours, marker='X', markersize=markersize, color="tomato", label="Ours", linewidth=linewidth)


    group_labels = ['-', '20%', '40%', '60%', '80%']
    plt.xticks(x, group_labels, fontsize=15)  # 默认字体大小为10
    y_ticks = [0.10, 0.15, 0.20, 0.25, 0.30]
    y_lables = ['0.10', '0.15', '0.20', '0.25', '0.30']
    plt.yticks(np.array(y_ticks), y_lables, fontsize=15)
    # plt.title("example", fontsize=12, fontweight='bold')  # 默认字体大小为12
    # plt.text(1, label_position, dataset,fontsize=25, fontweight='bold')
    # plt.xlabel("Edge Miss Rate", fontsize=15)
    plt.ylabel(f"HR@20", fontsize=15)
    plt.xlim(0.5, 5.5)  # 设置x轴的范围
    plt.ylim(0.08, 0.30)

    # plt.legend()
    # 显示各曲线的图例 loc=3 lower left
    plt.legend(loc=0, numpoints=1, ncol=2)
    leg = plt.gca().get_legend()
    ltext = leg.get_texts()
    plt.setp(ltext, fontsize=15)
    # plt.setp(ltext, fontsize=25, fontweight='bold')  # 设置图例字体的大小和粗细
    plt.tight_layout()
    plt.savefig(f'pics/line.png', format='png')  # 建议保存为svg格式,再用inkscape转为矢量图emf后插入word中
    plt.show()

def plot_multi_bar():

    model1 = np.array([0.0409, 0.0543, 0.0943, 0.1115, 0.1363])
    model2 = np.array([0.0351, 0.0557, 0.0916, 0.1315, 0.1860])
    model3 = np.array([0.0586, 0.0865, 0.1046, 0.1476, 0.2160])

    Ours = np.array([0.1043, 0.1344, 0.1638, 0.2035, 0.2446])

    # label在图示(legend)中显示。若为数学公式,则最好在字符串前后添加"$"符号
    # color：b:blue、g:green、r:red、c:cyan、m:magenta、y:yellow、k:black、w:white、、、
    # 线型：-  --   -.  :    ,
    # marker：.  ,   o   v    <    *    +    1
    plt.figure(figsize=(7, 4))
    # linestyle = "-"
    x = np.arange(5)
    # n 为有几个柱子
    total_width, n = 0.8, 4
    width = total_width / n
    x = x - (total_width - width) / n


    # low = 0.05
    # up = 0.44
    low = 0.02
    up = 0.27
    plt.ylim(low, up)
    # plt.xlabel("Amount of Data", fontsize=15)
    plt.ylabel(f"HR@20", fontsize=20)
    labels = ['Model1', 'Model2', 'Model3', 'Ours']

    # 'tomato', 'blue', 'orange', 'green', 'purple', 'deepskyblue'
    plt.bar(x, model1, width=width, color='blue', edgecolor='w')  # , edgecolor='k',)
    plt.bar(x + width, model2, width=width, color='green', edgecolor='w')  # , edgecolor='k',)
    plt.bar(x + 2*width, model3, width=width, color='orange', edgecolor='w')  # , edgecolor='k',)
    plt.bar(x + 3*width, Ours, width=width, color='tomato', edgecolor='w')  # , edgecolor='k',)

    plt.xticks(x +1.5*width, labels=['20%', '40%', '60%', '80%', '100%'], fontsize=20)

    y_lables = ['0.02', '0.08', '0.14', '0.20', '0.26']
    y_ticks = [float(i) for i in y_lables]
    # plt.yscale('linear')
    # y_ticks = [0.25, 0.30, 0.35, 0.40, 0.45]
    # y_lables = ['0.25', '0.30', '0.35', '0.40', '0.45']
    plt.yticks(np.array(y_ticks), y_lables, fontsize=20)#bbox_to_anchor=(0.30, 1)
    plt.legend(labels=labels, ncol=2,
               prop={'size': 14})

    plt.tight_layout()
    plt.savefig('./pics/multi_bar.png', format='png')
    plt.show()
    # 建议保存为svg格式,再用inkscape转为矢量图emf后插入word中

def plot_bar_and_line():
    fontsize=20
    result1 = [0.1967, 0.2103, 0.2398, 0.2446, 0.2387]
    l = [i for i in range(5)]

    lx = ['2', '3', '4', '5', '6']

    fig = plt.figure()
    ax1 = fig.add_subplot(111)
    plt.bar(l, result1, alpha=0.3, color='blue', label='HR@20')

    # left_axis.set_ylim(0.80, 0.96)
    # left_axis.set_yticks(np.arange(0.80, 0.97, 0.04))
    ax1.set_ylim([0.18, 0.26])
    ax1.set_yticks(np.arange(0.18, 0.26, 0.015))
    # ax1.set_ylabel('AUC', fontsize=fontsize)
    plt.legend(loc="upper left", prop={'size': 15})
    plt.xticks(l, lx, fontsize=fontsize)
    plt.yticks(fontsize=fontsize)

    result2 = [0.0823, 0.0976, 0.1054, 0.1185, 0.1045]

    ax2 = ax1.twinx()  # this is the important function
    ax2.plot(l, result2, 'or-', label='NDCG@20', color='green')
    ax2.legend(loc=2)
    ax2.set_ylim([0.07, 0.13])
    ax2.set_yticks(np.arange(0.07, 0.13, 0.01))
    # ax2.set_ylabel('Log-loss', fontsize=fontsize)
    plt.text(1.5, 0.06, "Num", fontsize=20)
    plt.legend(loc="upper right", prop={'size': 15})
    plt.yticks(fontsize=fontsize)
    plt.tight_layout()
    # , bbox_inches='tight', pad_inches=0.05, dpi=100
    plt.savefig('pics/bar_and_line.png', format='png')
    plt.show()

def plot_scatters():

    # label在图示(legend)中显示。若为数学公式,则最好在字符串前后添加"$"符号
    # color：b:blue、g:green、r:red、c:cyan、m:magenta、y:yellow、k:black、w:white、、、
    # 线型：-  --   -.  :    ,
    # marker：.  ,   o   v    <    *    +    1
    plt.figure(figsize=(5, 4))
    # linestyle = "-"
    # plt.grid(linestyle = "-.")  # 设置背景网格线为虚线
    ax = plt.gca()
    # ax.spines['top'].set_visible(False)  # 去掉上边框
    # ax.spines['right'].set_visible(False)  # 去掉右边框

    linewidth = 2.0
    markersize = 25

    plt.scatter(np.array([0.1394]), np.array([2.4]), marker='o', s=markersize, color="tomato", label="Model1")
    plt.scatter(np.array([0.1353]), np.array([3.7]), marker='d', s=markersize, color="orange", label="Model2")
    plt.scatter(np.array([0.1860]), np.array([8.7]), marker='+', s=markersize, color="gray", label="Model3")

    plt.scatter(np.array([0.1478]), np.array([60]), marker='<', s=markersize, color="purple", label="Model4")
    plt.scatter(np.array([0.1363]), np.array([6.7]), marker='^', s=markersize, color="peru", label="Model5")

    plt.scatter(np.array([0.1683]), np.array([16]), marker='p', s=markersize, color="maroon", label="Model6")
    plt.scatter(np.array([0.1922]), np.array([9.8]), marker='s', s=markersize, color="blue", label="Model7")
    plt.scatter(np.array([0.1823]), np.array([90]), marker='>', s=markersize, color="lime", label="Model8")
    plt.scatter(np.array([0.1875]), np.array([100.54]), marker='x', s=markersize, color="green", label="Model9")
    plt.scatter(np.array([0.2160]), np.array([228]), marker='d', s=markersize, color="blue", label="Model10")
    plt.scatter(np.array([0.2446]), np.array([66.02]), marker='*', s=markersize, color="red", label="Ours")



    x_labels = ['0.11', '0.15', '0.19', '0.23', '0.27']
    x_ticks = [float(i) for i in x_labels]
    plt.xticks(np.array(x_ticks), x_labels, fontsize=15)

    plt.xlabel("HR@20", fontsize=15)
    plt.ylabel(f"Inference Time", fontsize=15)
    plt.xlim(0.11, 0.27)  # 设置x轴的范围

    plt.ylim(0, 250)

    y_labels = ['0', '50', '100', '150', '200', '250']
    y_ticks = [int(i) for i in y_labels]
    plt.yticks(np.array(y_ticks), y_labels, fontsize=15)
    # plt.legend()          #显示各曲线的图例
    plt.legend(loc=0, numpoints=1, ncol=1, bbox_to_anchor=(1.05, 1.0), borderaxespad=0.)
    leg = plt.gca().get_legend()
    ltext = leg.get_texts()
    plt.setp(ltext, fontsize=10)  # 设置图例字体的大小和粗细
    plt.tight_layout()
    plt.savefig(f'./pics/scatter.png', format='png')  # 建议保存为svg格式,再用inkscape转为矢量图emf后插入word中
    plt.show()


def plot_hetmap():
    import seaborn as sns
    import numpy as np
    x = np.array(
        [[0.3761, 0.3704, 0.3674],
         [0.3568, 0.3318, 0.3319],
         [0.3461, 0.3335, 0.3182]]
    )
    # x = x.T

    plt.figure(figsize=(5, 4))

    ax = sns.heatmap(x, annot=True, fmt=".4f", annot_kws={'size': 15, 'color': 'black'}, # 'weight': 'bold'
                linewidths=0.5, cmap='YlOrRd', square=True)

    x_lables = ['Model1', 'Model2', 'Model3']

    ax.set_yticklabels(ax.get_yticklabels(), rotation=0)
    ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
    ax.xaxis.tick_top()

    # plt.title('Target Model', fontsize=15)
    plt.xlabel('Target Model', fontsize=15)
    plt.ylabel('Complementary Model', fontsize=15)
    plt.xticks([0.5, 1.5, 2.5], x_lables, fontsize=15)  # 默认字体大小为10
    plt.yticks([0.5, 1.5, 2.5], x_lables, fontsize=15)  # 默认字体大小为10

    cax = plt.gcf().axes[-1]
    cax.tick_params(labelsize=15)

    plt.tight_layout()
    plt.savefig('./pics/heatmap.png', format='png')
    plt.show()

# text的位置确认有点拉
def plot_ablation_bar_in_one():

    models = ['Base', '$\\neg$ A', '$\\neg$ B', '$\\neg$ C', "Ours"]

    x_label_size = 35
    rotation = 0
    # 从这里开始选择数据

    labels = models

    # plt.rcParams['font.sans-serif'] = ['Times New Roman']  # 如果要显示中文字体,则在此处设为：SimHei
    # plt.rcParams['axes.unicode_minus'] = False  # 显示负号
    # # plt.rcParams['savefig.dpi'] = 300  # 图片像素
    # plt.rcParams['figure.dpi'] = 300  # 分辨率

    plt.figure(figsize=(40, 7))
    colors = ['blue', 'green', 'red']

    low = 0.34
    up = 0.391
    Beauty = [0.3488, 0.3687, 0.3688, 0.3546, 0.3761]
    data=Beauty
    plt.subplot(141)
    plt.ylim(low, up)
    position = (up - low) * 0.9 + low
    plt.text(1.4, position, 'Beauty', fontsize=40)
    plt.xticks(fontsize=x_label_size, rotation=rotation)

    my_y_ticks = np.arange(low, up, 0.01)
    plt.yticks(my_y_ticks, fontsize=40)
    # plt.xlabel("Meituan", fontsize=20, fontweight='bold')
    # hatches = ["\\"] + ["."] * 4 + ["/"]
    # /,  \, |, -, +, x, o, O,., * 。
    plt.bar([0], data[0], width=0.5, color=colors[0], hatch=".", edgecolor='w')
    plt.bar([1, 2, 3], data[1:4], width=0.5, color=colors[1], hatch=".", edgecolor='w')
    plt.bar([4], data[4], width=0.5, color=colors[2], hatch=".", edgecolor='w')
    plt.xticks([0, 1, 2, 3, 4], labels)
    # plt.bar(np.arange(len(data)), data, width=0.5, tick_label=labels, color=colors, hatches=hatches)

    low = 0.32
    up = 0.361
    Sport = [0.328, 0.3385, 0.3346, 0.3335, 0.3473]
    data = Sport

    plt.subplot(142)
    plt.ylim(low, up)
    position = (up - low) * 0.9 + low
    plt.text(1.4, position, 'Sports', fontsize=40)
    plt.xticks(fontsize=x_label_size, rotation=rotation)
    my_y_ticks = np.arange(low, up, 0.01)
    plt.yticks(my_y_ticks, fontsize=40)
    # plt.xlabel("Beauty", fontsize=20, fontweight='bold')
    # colors = ['darkorange'] * 1 + ['royalblue'] * 4 + ['red']
    # /,  \, |, -, +, x, o, O,., * 。
    # plt.bar(np.arange(len(data)), data, hatch=2 * '.', width=0.5,
    #         tick_label=labels, color=colors,
    #         # edgecolor='k'
    #         )
    plt.bar([0], data[0], width=0.5, color=colors[0], hatch="\\", edgecolor='w')
    plt.bar([1, 2, 3], data[1:4], width=0.5, color=colors[1], hatch=".", edgecolor='w')
    plt.bar([4], data[4], width=0.5, color=colors[2], hatch="/", edgecolor='w')
    plt.xticks([0, 1, 2, 3, 4], labels)

    low = 0.34
    up = 0.391

    Toys = [0.3455, 0.3671, 0.3588, 0.3611, 0.3749]

    data = Toys

    plt.subplot(143)
    plt.ylim(low, up)
    position = (up - low) * 0.9 + low
    plt.text(1.4, position, 'Toys', fontsize=40)
    plt.xticks(fontsize=x_label_size, rotation=rotation)
    my_y_ticks = np.arange(low, up, 0.01)
    plt.yticks(my_y_ticks, fontsize=40)
    # plt.xlabel("Sports", fontsize=20, fontweight='bold')
    # colors = ['darkorange'] * 1 + ['royalblue'] * 4 + ['red']
    # /,  \, |, -, +, x, o, O,., * 。
    # plt.bar(np.arange(len(data)), data, hatch=2 * '.', width=0.5,
    #         tick_label=labels, color=colors,
    #         # edgecolor='k'
    #         )
    plt.bar([0], data[0], width=0.5, color=colors[0], hatch="\\", edgecolor='w')
    plt.bar([1, 2, 3], data[1:4], width=0.5, color=colors[1], hatch=".", edgecolor='w')
    plt.bar([4], data[4], width=0.5, color=colors[2], hatch="/", edgecolor='w')
    plt.xticks([0, 1, 2, 3, 4], labels)

    low = 0.49
    up = 0.54

    Yelp = [0.496, 0.523, 0.5231, 0.5167, 0.53]
    data = Yelp
    plt.subplot(144)
    plt.ylim(low, up)
    position = (up - low) * 0.9 + low
    plt.text(1.6, position, 'Yelp', fontsize=40)
    plt.xticks(fontsize=x_label_size, rotation=rotation)
    my_y_ticks = np.arange(low, up, 0.01)
    plt.yticks(my_y_ticks, fontsize=40)
    # plt.xlabel("Toys", fontsize=20, fontweight='bold')
    # colors = ['darkorange'] * 1 + ['royalblue'] * 4 + ['red']
    # /,  \, |, -, +, x, o, O,., * 。
    # plt.bar(np.arange(len(data)), data, hatch=2 * '.', width=0.5,
    #         tick_label=labels, color=colors,
    #         # edgecolor='k'
    #         )
    plt.bar([0], data[0], width=0.5, color=colors[0], hatch="\\", edgecolor='w')
    plt.bar([1, 2, 3], data[1:4], width=0.5, color=colors[1], hatch=".", edgecolor='w')
    plt.bar([4], data[4], width=0.5, color=colors[2], hatch="/", edgecolor='w')
    plt.xticks([0, 1, 2, 3, 4], labels)

    plt.tight_layout()
    plt.subplots_adjust(wspace=0.3, hspace=0)
    # 建议保存为svg格式,再用inkscape转为矢量图emf后插入word中
    plt.savefig('./pics/ablation.png', format='png')
    plt.show()

import matplotlib.patches as mpatches

# 上下对齐的两个子图
def plot_two_bar_in_one():

    beauty_base = [0.14, 0.16, 0.23, 0.25, 0.27, 0.30, 0.33, 0.34]
    beauty_grow = [0.15, 0.17, 0.24, 0.26, 0.28, 0.31, 0.34, 0.35]
    toys_base = [0.14, 0.16, 0.23, 0.25, 0.27, 0.30, 0.33, 0.34]
    toys_grow = [0.15, 0.17, 0.24, 0.26, 0.28, 0.31, 0.34, 0.35]

    # plt.xlabel("Extend", fontsize=20, fontweight='bold')
    # plt.ylabel("NDCG@10", fontsize=25)
    # plt.text(0.1, 0.55, data_name, fontsize=20, fontweight='bold')

    x = np.arange(8)
    total_width, n = 0.8, 2
    width = total_width / n
    x = x - (total_width - width) / n


    lables = ['Model1', 'Model2', 'Model3', 'Model4',
              'Model5', 'Model6', 'Model7', 'Model8']

    # plt.rcParams['font.sans-serif'] = ['Times New Roman']  # 如果要显示中文字体,则在此处设为：SimHei
    # plt.rcParams['axes.unicode_minus'] = False  # 显示负号
    # # from matplotlib.font_manager import FontProperties
    # myfont = FontProperties(fname='times.ttf', size=25)
    fig, (ax1, ax2) = plt.subplots(
        2, 1, sharex=True, figsize=(20, 16), dpi=100)

    beauty_base = np.array(beauty_base)
    beauty_grow = np.array(beauty_grow)

    low = 0.13
    up = 0.41
    ax1.set_ylim(low, up)
    ax1.bar(x, beauty_base, width=width, color='royalblue', hatch=".", edgecolor='w')  # , edgecolor='k',)
    ax1.bar(x + width, beauty_grow, width=width, color='tomato', hatch="/", edgecolor='w')  # , edgecolor='k',)
    position = (up - low) * 0.9 + low
    ax1.text(2.6, position, 'Beauty', fontsize=40)
    y_ticks = [0.15, 0.20, 0.25, 0.30, 0.35, 0.40]
    y_lables = ['0.15', '0.20', '0.25', '0.30', '0.35', '0.40']
    ax1.set_yticks(np.array(y_ticks))

    ax1.set_yticklabels(y_lables, fontsize=40)

    toys_base = np.array(toys_base)
    toys_grow = np.array(toys_grow)
    low = 0.11
    up = 0.41
    ax2.set_ylim(low, up)
    ax2.bar(x, toys_base, width=width, color='royalblue', hatch=".", edgecolor='w')

    ax2.bar(x + width, toys_grow, width=width, color='tomato', hatch="/", edgecolor='w')
    position = (up - low) * 0.9 + low
    ax2.text(2.7, position, 'Toys', fontsize=40)
    ax2.set_xticks(x + (width / 2))
    ax2.set_xticklabels(lables, fontsize=40, rotation=20)

    y_ticks = [0.15, 0.20, 0.25, 0.30, 0.35, 0.40]
    y_lables = ['0.15', '0.20', '0.25', '0.30', '0.35', '0.40']
    ax2.set_yticks(np.array(y_ticks))

    ax2.set_yticklabels(y_lables, fontsize=40)

    leg1 = mpatches.Patch(color='royalblue', hatch='.')
    leg2 = mpatches.Patch(color='tomato', hatch='/')

    labels = ['Original', 'Final']
    fig.legend(handles=[leg1, leg2], labels=labels, loc='upper center', bbox_to_anchor=(0.2, 1), ncol=1, prop={'size': 40})

    fig.tight_layout()
    fig.show()
    # 建议保存为svg格式,再用inkscape转为矢量图emf后插入word中
    fig.savefig('./pics/two_bars.png', format='png')


def plot_twice(x,y_1,y_2,save_name,loc,x_label):
    # matplotlib.use('PDF')

    plt.rcParams['font.family'] = ['SimHei']  # 因为图中有中文避免中文显示乱码
    plt.rcParams['figure.figsize'] = (16.0, 4)

    plt.rcParams['ps.useafm'] = True
    plt.rcParams['pdf.use14corefonts'] = True
    plt.rcParams['text.usetex'] = True

    ax1 = plt.subplot(1, 4, 1)  # 添加子图参数第一个和第二个分别是子图的行数和列数，第三个参数是子图的序号
    ax2 = plt.subplot(1, 4, 2)
    ax3 = plt.subplot(1, 4, 3)
    ax4 = plt.subplot(1, 4, 4)


    ax1.set_title('Sports')  # 设置第一个子图的x轴标签
    ax1.set_xlabel(x_label)
    ax1.set_ylabel("HR@20")
    width = range(len(x))
    line1=ax1.plot(width, y_1[0],c="c",label="HR@20",marker="o")
    # ax1.legend("upper right")
    ax1.set_xticks(range(len(x)),x)
    ax1_1=ax1.twinx()
    ax1_1.set_ylabel('NDCG@20')  # 设置第一个子图的y轴标签
    line2=ax1_1.plot(width,y_2[0],c="orange",marker="D",linestyle="--",label="NDCG@20")
    # ax1_1.legend("upper right")
    lines=line1+line2
    labs=[l.get_label() for l in lines]
    ax1.legend(lines,labs,loc=loc)
    plt.tight_layout()  # 使子图适应作图区域避免坐标轴标签信息显示混乱



    ax2.set_title('Beauty')  # 设置第一个子图的x轴标签
    ax2.set_xlabel(x_label)
    ax2.set_ylabel("HR@20")
    line1 = ax2.plot(width, y_1[1], c="c",marker="o",label="HR@20")
    ax2.set_xticks(range(len(x)), x)
    # ax1.legend("upper left")
    ax2_1 = ax2.twinx()
    ax2_1.set_ylabel('NDCG@20')  # 设置第一个子图的y轴标签
    line2 = ax2_1.plot(width, y_2[1], c="orange", marker="D",linestyle="--",label="NDCG@20")
    # ax1_1.legend("upper right")
    lines = line1 + line2
    labs = [l.get_label() for l in lines]
    ax2.legend(lines, labs, loc=loc)
    plt.tight_layout()  # 使子图适应作图区域避免坐标轴标签信息显示混乱


    ax3.set_title('Toys')  # 设置第一个子图的x轴标签
    ax3.set_xlabel(x_label)
    ax3.set_ylabel("HR@20")
    line1 = ax3.plot(width, y_1[2], c="c",marker="o",label="HR@20")
    ax3.set_xticks(range(len(x)), x)
    # ax1.legend("upper left")
    ax3_1 = ax3.twinx()
    ax3_1.set_ylabel('NDCG@20')  # 设置第一个子图的y轴标签
    line2 = ax3_1.plot(width, y_2[2], c="orange", marker="D",linestyle="--",label="NDCG@20")
    # ax1_1.legend("upper right")
    lines = line1 + line2
    labs = [l.get_label() for l in lines]
    ax3.legend(lines, labs, loc=loc)
    plt.tight_layout()  # 使子图适应作图区域避免坐标轴标签信息显示混乱



    ax4.set_title('ML-1M')  # 设置第一个子图的x轴标签
    ax4.set_xlabel(x_label)
    ax4.set_ylabel("HR@20")
    line1 = ax4.plot(width, y_1[3], c="c",marker="o",label="HR@20")
    # ax1.legend("upper left")
    ax4.set_xticks(range(len(x)), x)
    ax4_1 = ax4.twinx()
    ax4_1.set_ylabel('NDCG@20')  # 设置第一个子图的y轴标签
    line2 = ax4_1.plot(width, y_2[3], c="orange", marker="D",linestyle="--",label="NDCG@20")
    # ax1_1.legend("upper right")
    lines = line1 + line2
    labs = [l.get_label() for l in lines]
    ax4.legend(lines, labs, loc=loc)
    plt.tight_layout()  # 使子图适应作图区域避免坐标轴标签信息显示混乱
    plt.savefig("./pics/%s.png"%save_name)


def plot_box(save_name):
    plt.rcParams['font.family'] = ['SimHei']  # 因为图中有中文避免中文显示乱码
    plt.rcParams['figure.figsize'] = (12, 5)

    plt.rcParams['ps.useafm'] = True
    plt.rcParams['pdf.use14corefonts'] = True
    plt.rcParams['text.usetex'] = True
    f,(ax)=plt.subplots(1,1,figsize=(12,4))
    plt.title("Plot_Box",fontsize=20)
    data_dic={"x":[i for i in range(10)]*10,"y":np.arange(0.5,100,1.0)}
    # x=np.arange(0.,10,0.1)
    # y=np.arange(0.5,100,1.0)
    # print(len(x),len(y))
    sns.boxplot("x","y",data=data_dic,ax=ax)
    ax.set_xlabel("X",size=20,alpha=0.8)
    ax.set_ylabel("Y",size=20,alpha=0.8)
    plt.savefig("./pics/%s.png" % save_name)

def plot_violin(save_name):
    plt.rcParams['font.family'] = ['SimHei']  # 因为图中有中文避免中文显示乱码
    plt.rcParams['figure.figsize'] = (12, 5)

    plt.rcParams['ps.useafm'] = True
    plt.rcParams['pdf.use14corefonts'] = True
    plt.rcParams['text.usetex'] = True
    f,(ax)=plt.subplots(1,1,figsize=(12,4))
    plt.title("Plot_Box",fontsize=20)
    data_dic={"x":[i for i in range(10)]*10,"y":np.arange(0.5,100,1.0)}
    sns.violinplot("x","y",data=data_dic,ax=ax)
    ax.set_xlabel("X",size=20,alpha=0.8)
    ax.set_ylabel("Y",size=20,alpha=0.8)
    plt.savefig("./pics/%s.png" % save_name)


def plot_3D(save_name):
    plt.rcParams['font.family'] = ['SimHei']  # 因为图中有中文避免中文显示乱码
    plt.rcParams['figure.figsize'] = (12, 5)

    plt.rcParams['ps.useafm'] = True
    plt.rcParams['pdf.use14corefonts'] = True
    plt.rcParams['text.usetex'] = True
    fig=plt.figure(figsize=(8,6))
    ax=fig.add_subplot(111,projection="3d")
    xs=np.arange(0.,1,0.01)
    ys=np.arange(0.5,100,1)
    zs=np.arange(1,101,1)
    ax.scatter(xs,ys,zs,s=50,alpha=0.6,edgecolor="w")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    plt.savefig("./pics/%s.png" % save_name)

def plot_marker(save_name):
    plt.rcParams['font.family'] = ['SimHei']  # 因为图中有中文避免中文显示乱码
    plt.rcParams['figure.figsize'] = (12, 5)

    plt.rcParams['ps.useafm'] = True
    plt.rcParams['pdf.use14corefonts'] = True
    plt.rcParams['text.usetex'] = True

    rng=np.random.RandomState(0)
    for marker in ['o','.',",",'x','+','v','^','<','>','s','d','p','*','-']:
        plt.plot(rng.rand(5),rng.rand(5),marker,label="<=marker")
    plt.legend()
    plt.xlim(0,1.8)
    plt.savefig("./pics/%s.png" % save_name)


def plot_multi_bar_1(save_name):
    plt.rcParams['font.family'] = ['SimHei']  # 因为图中有中文避免中文显示乱码
    plt.rcParams['figure.figsize'] = (12, 5)

    plt.rcParams['ps.useafm'] = True
    plt.rcParams['pdf.use14corefonts'] = True
    plt.rcParams['text.usetex'] = True

    x1=np.random.normal(0,0.8,1000)
    x2=np.random.normal(-2,1,1000)
    x3=np.random.normal(3,2,1000)
    kwargs=dict(histtype="stepfilled",alpha=0.3,density=True,bins=40)
    plt.hist(x1,**kwargs)
    plt.hist(x2,**kwargs)
    plt.hist(x3,**kwargs)
    plt.savefig("./pics/%s.png" % save_name)

def plot_2D(save_name):


    plt.rcParams['font.family'] = ['SimHei']  # 因为图中有中文避免中文显示乱码
    plt.rcParams['figure.figsize'] = (12, 5)

    plt.rcParams['ps.useafm'] = True
    plt.rcParams['pdf.use14corefonts'] = True
    plt.rcParams['text.usetex'] = True

    mean=[0,0]
    cov=[[1,1],[1,2]]
    x,y=np.random.multivariate_normal(mean,cov,10000).T

    plt.hist2d(x,y,bins=30,cmap="Blues")
    cb=plt.colorbar()
    cb.set_label("counts in bin")

    plt.savefig("./pics/%s.png" % save_name)
    plt.show()




dropout_r = [0.1, 0.2, 0.3, 0.4, 0.5]
y_1_d = [[0.0705, 0.0738, 0.0765, 0.0775, 0.0794], [0.1171, 0.1260, 0.1289, 0.1302, 0.1289],
         [0.1219, 0.1269, 0.1307, 0.1344, 0.1368], [0.4518, 0.4389, 0.4260, 0.3985, 0.3846]]
y_2_d = [[0.0347, 0.0359, 0.0380, 0.0382, 0.0393], [0.0614, 0.0648, 0.0669, 0.0672, 0.0663],
         [0.0666, 0.0695, 0.0716, 0.0735, 0.0736], [0.2297, 0.2207, 0.2124, 0.1920, 0.1802]]
if __name__ == '__main__':
    plot_bar()
    plot_line()
    plot_multi_bar()
    plot_bar_and_line()
    plot_scatters()
    plot_hetmap()
    plot_ablation_bar_in_one()
    plot_two_bar_in_one()
    plot_twice(dropout_r, y_1_d, y_2_d, "dropout_t", "best", "dropout rate ")
    plot_box("plot_box")
    plot_violin("plot_violin")
    plot_3D("plot_3D")
    plot_marker("plot_marker")
    plot_multi_bar_1("multi_bar_1")
    plot_2D("hist_2D")

