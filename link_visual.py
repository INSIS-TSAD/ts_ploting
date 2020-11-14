from bokeh.io import output_file, show
from bokeh.layouts import gridplot
from bokeh.plotting import figure
import numpy as np
from bokeh.io import save

def link_subplot(ts1, ts1_label, ts2, ts2_label, ts2_pred, file_name="test.html"):
    """
    子图s1 和 子图s2, 两个图的x轴同时变化.
    :param ts1: 第一个子图的时序, array
    :param ts1_label: 第一个子图时序的标签, array
    :param ts2: 第二个子图的时序, array
    :param ts2_label:第二个子图时序的真实标签, array
    :param ts2_pred:第二个子图时序的预测标签, array
    :param file_name: 输出的html文件名
    :return:
    """

    ts1_label_idx = np.where(ts1_label == 1)[0]
    ts2_real_ad_idx = np.where(ts2_label == 1)[0]
    ts2_pred_ad_idx = np.where(ts2_pred == 1)[0]

    ts2_correct_pred_idx = np.array([idx for idx in ts2_real_ad_idx if idx in ts2_pred_ad_idx])

    output_file(file_name)

    x = np.arange(0, len(ts1))

    # 绘制 第一个子图
    s1 = figure(plot_height=350, plot_width=1500, title='ts1')
    s1.line(x, ts1,  color="deepskyblue", alpha=0.8, line_width= 2, legend="sr结果")  # 绘制时序
    s1.circle(x=ts1_label_idx, y=ts1[ts1_label_idx], color='red', alpha=0.8,size=8, legend="sr标签")  # 绘制异常点


    # 绘制  第二个子图
    s2 = figure(plot_height=350, plot_width=1500, x_range=s1.x_range, title="ts2")  # 两个子图联动的关键步骤: 让子图2使用子图1的x轴对象, 即x_range=s1.x_range
    s2.line(x, ts2, color="deepskyblue", alpha=0.8,line_width= 2, legend="原始时序")
    s2.circle(x=ts2_real_ad_idx, y=ts2[ts2_real_ad_idx], color='red', alpha=0.8,size=8, legend="真实标签")
    s2.circle(x=ts2_pred_ad_idx, y=ts2[ts2_pred_ad_idx], color='orange', alpha=0.8,size=8, legend="预测标签")
    s2.square(x=ts2_correct_pred_idx, y=ts2[ts2_correct_pred_idx], color='green', alpha=0.8, size=8, legend="预测正确标签")

    #
    # p = gridplot([[s1, s2, s3]], toolbar_location=None)
    p = gridplot([s1, s2], ncols=1)  # 两个子图的布局方式

    # show(p)
    save(obj=p, filename=file_name)  # 输出到html文件


