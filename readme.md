### what is this?

两个时序可视化的样例代码, 输出到html文件中, 很方便的移动和放缩坐标, 便于观察.

* link_visual.py 实现两个子图的x轴同时联动, 使用的是bokeh, 文档:https://docs.bokeh.org/en/latest/
* visual_train_test.py 实现训练集和测试集时序和标签的可视化, 使用的是plotly, 文档:https://plotly.com/python/

使用样例见demo.py



### link_visual, using bokeh

改变任意一个子图的x轴坐标, 另外一个子图同时自动做相同的变化.

![image-20201114121329503](https://gitee.com/kris_poul/imagebed/raw/master/imgbed/20201114121329.png)



### visual_train_test, using plotly

![image-20201114121708167](https://gitee.com/kris_poul/imagebed/raw/master/imgbed/20201114121708.png)