import gradio as gr


def greet(name):
    return "Hello " + name + "!"


with gr.Blocks() as demo:
    # 设置输入组件
    name = gr.Textbox(label="名字",)
    # 输出
    output = gr.Textbox(label="输出")

    # 按钮
    greet_but = gr.Button("提交")
    # 设置事件
    greet_but.click(greet, name, output)

demo.launch()
