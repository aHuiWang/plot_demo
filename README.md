## **介绍**
提供一些常见的Python画图示例，更好赶论文

**使用的时候记得修改为**
```
fig.savefig('./pics/{name}.pdf', format='pdf')
```
这样直接导出pdf插入tex就行了

## 一些链接
[**matplotlib命令与格式：图例legend语法及设置**](https://blog.csdn.net/helunqu2017/article/details/78641290)

[**matplotlib绘画：图例与书籍**](https://github.com/rougier/scientific-visualization-book)

[**matplotlib命令与格式：标题(title),标注(annotate),文字说明(text)**](https://blog.csdn.net/helunqu2017/article/details/78659490)

[**这里可以挑 color 和 marker样式**](https://cloud.tencent.com/developer/article/1540478)

[**单行热力图 & 可以挑热力图的颜色**](https://www.codenong.com/cs106384659/)

[**其他参考图例1**](https://mp.weixin.qq.com/s/mFXjyeLzbDGdT4jyAxHDjw)

[**其他参考图例2**](https://mp.weixin.qq.com/s/cJV7WQlD15egW-fWJYJBdQ)

[**60种可视化图表总结**](https://mp.weixin.qq.com/s/T4G3wo5Zm67i4MBtdqdO6g)

### 折线图
```
plot_line()
```
![avatar](pics/line.png)

### 柱状图

```
plot_bar()
```
![avatar](pics/bar.png)

### 多柱状图
多组数据展示利器
```
plot_multi_bar()
```
![avatar](pics/multi_bar.png)

### 多柱状图（有重叠）

```
plot_multi_bar_1()
```

![avatar](pics/multi_bar_1.png)

### 柱状+折线

有时单条线或单个柱子太单调了
```
plot_bar_and_line()
```
![avatar](pics/bar_and_line.png)

### 2D柱状图

```
plot_2D()
```

![avatar](pics/hist_2D.png)

### 折线截断图

```
plt_broken()
```

![avatar](pics/broken_line.png)

### 柱状截断图

```
bar_broken()
```

![avatar](pics/broken_bar.png)

### 散点图

```
plot_scatters()
```
![avatar](pics/scatter.png)

### 箱线图

```
plot_box()
```

![avatar](pics/plot_box.png)

### 小提琴图

```
plot_violin()
```

![avatar](pics/plot_violin.png)

### 热力图

```
plot_hetmap()
```
![avatar](pics/heatmap.png)

### 3D图像

```
plot_3D()
```

![avatar](pics/plot_3D.png)

### 组合图1

喜欢用来画多个数据集的ablation,当然也可以画成4个小图在tex里拼装，但可能图之前的缝隙会比较大
```
plot_ablation_bar_in_one()
```
![avatar](pics/ablation.png)

### 组合图2

双坐标轴折线组合图，可以更加直观的观察四个组合图在两个不同指标上的变化趋势

![avatar](pics/multi_line.png)

### 组合图3

可以用在验证某方法具有泛化性，然后所有模型试一遍。难点在于一个字图省掉横坐标，且上下对齐。（其实我也不知道这样有啥好，嘻嘻）
```
plot_two_bar_in_one()
```
![avatar](pics/two_bars.png)

### 使用patchworklib包构建组合图
```
patchworklib_plot.py
```
![avatar](pics/ax1234.png)
![avatar](pics/ax12345.png)
![avatar](pics/g0123.png)
![avatar](pics/g1234.png)
### 向量可视化
t-SNE可视化，提供的例子是一个画embedding随训练变化的例子
```
draw_tsne.py
```
![avatar](pics/tsne.png)

### 快速修改图例参数

```
# 安装包 
pip install pylustrator
# 导入
import pylustrator
# 开启控件
pylustrator.start()
# 注意需要配合使用plt.show()来进行使用
```

![avatar](pics/pylustrator.png)

