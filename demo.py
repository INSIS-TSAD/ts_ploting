from link_visual import link_subplot
from visual_triain_test import visualization
import numpy as np

# demo for link_visual
ts1 = np.random.random(size=[50])
ts1_label = np.zeros(50)
ts1_label[ts1 > 0.9] = 1 # ts1标签

ts2 = ts1 * 2  # 一般ts1与ts2是有关联关系的, 才回用到两个子图联动, 这里假设ts2 是 ts1 的两倍
ts2_label = ts1_label.copy()
ts2_pred = np.zeros(50)
ts2_pred[ts1 > 0.85] = 1

link_subplot(ts1, ts1_label, ts2, ts2_label, ts2_pred, file_name="link_visual.html")


# demo for visualization
title = "demo fro using plotly"
x = np.random.random(size=100)
y = np.zeros(100)
y[x > 0.9] = 1
train_x = x[:70]
train_y = y[:70]
test_x = x[70:]
test_y = y[70:]
pred = np.zeros(30)
pred[test_x > 0.85] = 1
visualization(title, train_x, train_y, test_x, test_y, pred, file_name="visual_triain_test.html")

