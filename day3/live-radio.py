# Interface添加live=True参数，只要输入发生变化，结果马上发生改变。
# Radio 单选按钮
import gradio as gr


def calculator(num1, operation, num2):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        return num1 / num2


demo = gr.Interface(calculator,
                    # 设置输入
                    ["number", gr.Radio(["add", "subtract", "multiply", "divide"]), "number"],
                    # 输出
                    "number",
                    # 立马改变
                    live=True,
                    # 设置输入参数示例
                    examples=[
                        [5, "add", 3],
                        [4, "divide", 2],
                        [-4, "multiply", 2.5],
                        [0, "subtract", 1.2],
                    ],
                    # 标题

                    title="计算器",
                    # 描述
                    description="左上角，这是一个计算器",
                    # 左下角描述
                    article="左下角描述"
                    )

if __name__ == "__main__":
    demo.launch()
