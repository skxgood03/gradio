import gradio as gr
import pandas as pd
from matplotlib import pyplot as plt
from sqlalchemy import create_engine
from pylab import mpl

DATABASE_TYPE = 'mysql'
DBAPI = 'pymysql'
ENDPOINT = 'localhost'  # 数据库服务器地址
USER = 'root'  # 数据库用户名
PASSWORD = 'root'  # 数据库密码
PORT = 3306  # 数据库端口
DATABASE = 'demo'  # 数据库名称

# 创建连接引擎
engine = create_engine(f'{DATABASE_TYPE}+{DBAPI}://{USER}:{PASSWORD}@{ENDPOINT}:{PORT}/{DATABASE}')
mpl.rcParams[
    'font.sans-serif'
] = ["SimHei"]


def get_expense_by_partner():
    """
    按交易对方（transaction_partner）分类统计正常支出金额和支出次数，
    不包括付款方式为‘招商银行储蓄卡(8109)’或商品说明包含‘转账’的记录。
    """
    query = """
    SELECT 
        transaction_partner,
        SUM(amount) AS total_expense,
        COUNT(*) AS expense_count
    FROM monthly_bills
    WHERE 
        income_expense = '支出'
        AND transaction_status = '交易成功'
        AND (payment_method != '招商银行储蓄卡(8109)'
             AND product_description NOT LIKE '%%转账%%')
    GROUP BY transaction_partner
    ORDER BY total_expense DESC;
    """

    df = pd.read_sql(query, engine)
    fig_m, ax = plt.subplots(figsize=(12, 6))
    bars = ax.bar(x=df['transaction_partner'], height=df['total_expense'], width=0.8, color='blue')
    ax.set_title(
        'title', fontsize=12
    )
    ax.set_ylabel("y", fontsize=12)
    ax.set_xlabel("x", fontsize=12)
    plt.xticks(rotation=45, ha='right')
    # 在每个柱子上方添加数值标签
    for bar in bars:
        yval = bar.get_height()  # 获取柱子的高度
        ax.text(bar.get_x() + bar.get_width() / 2, yval, round(yval, 2),
                ha='center', va='bottom')  # 在柱子上方显示数值
    plt.tight_layout()
    return fig_m


def greet(name):
    query = """
    SELECT 
        transaction_partner,
        SUM(amount) AS total_expense,
        COUNT(*) AS expense_count
    FROM monthly_bills
    WHERE 
        income_expense = '支出'
        AND transaction_status = '交易成功'
        AND (payment_method != '招商银行储蓄卡(8109)'
             AND product_description NOT LIKE '%%转账%%')
    GROUP BY transaction_partner
    ORDER BY total_expense DESC;
    """

    df = pd.read_sql_query(query, engine)
    return df


with gr.Blocks() as demo:
    # 设置输入组件
    # file = gr.File(label="文件", file_types=[
    #     'csv', 'txt'
    # ])
    name = gr.Textbox(
        label='name',
    )
    # 输出
    output = gr.Textbox(label="输出", )

    # 按钮
    greet_but = gr.Button("提交")
    # 设置事件
    greet_but.click(greet, name, output)
    with gr.Row():
        bike_type = gr.Plot()
    demo.load(get_expense_by_partner, inputs=None, outputs=[bike_type])

demo.launch(share=True)
