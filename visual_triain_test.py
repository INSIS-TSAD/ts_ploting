import numpy as np
import plotly.graph_objects as go
import plotly.io as pio


def visualization(title, train_x, train_y, test_x, test_y, pred, file_name="test.html"):
    """
    可视化训练集和测试集
    :param title: 网页的标题
    :param train_x: 训练集的ts
    :param train_y:训练集的标签
    :param test_x:测试集的ts
    :param test_y:测试集标签
    :param pred:检测结果
    :param file_name: 输出文件名
    :return:
    """
    train_ad_idx = np.where(train_y == 1)[0]

    pred_ad_idx = np.where(pred == 1)[0]
    real_ad_idx = np.where(test_y == 1)[0]
    correct_pred_idx = np.array([idx for idx in pred_ad_idx if idx in real_ad_idx])

    train_len = len(train_x)
    test_len = len(test_x)

    fig = go.Figure(layout_title_text=title)

    # 绘制训练数据
    fig.add_trace(go.Scatter(
        x=np.arange(0, train_len),
        y=train_x,
        mode='lines',
        name='train kpi', marker={"line": {"color": "orange"}}))

    # 绘制训练标签
    fig.add_trace(go.Scatter(x=train_ad_idx,
                             y=train_x[train_ad_idx],
                             mode='markers',
                             name='train label', marker={"symbol": "circle", "opacity": 0.5, "size": 8}),
                  )

    # 绘制测试数据
    fig.add_trace(go.Scatter(
        x=np.arange(train_len, train_len + test_len),
        y=test_x,
        mode='lines',
        name='test kpi', marker={"line": {"color": "black"}}))

    # 绘制测试标签
    fig.add_trace(go.Scatter(x=real_ad_idx + train_len,
                             y=test_x[real_ad_idx],
                             mode='markers',
                             name='true anomaly', marker={"symbol": "x", "opacity": 0.5, "size": 8}),

                  )

    fig.add_trace(go.Scatter(x=pred_ad_idx + train_len,
                             y=test_x[pred_ad_idx],
                             mode='markers',
                             name='false anomaly', marker={"symbol": "x", "opacity": 0.5, "size": 8}))
    try:
        fig.add_trace(
            go.Scatter(x=correct_pred_idx + train_len,
                       y=test_x[correct_pred_idx],
                       mode='markers',
                       name='detected anomaly', marker={"symbol": "circle", "opacity": 0.8, "size": 8})
        )
    except:
        pass

    # fig.show()
    # 本地保存到html
    pio.write_html(fig, file=file_name)