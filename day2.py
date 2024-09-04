# 多个输入和输出


import gradio as gr


# 输入文本处理程序
def greet(name, age, height):
    text = f"我叫{name},今年{age}岁,身高{height}"
    bmi_demo = age + height
    return text, bmi_demo


demo = gr.Interface(fn=greet, inputs=["text", gr.Number(), gr.Number()], outputs=["text", "number"])
if __name__ == "__main__":

    app, local_url, share_url = demo.launch(share=True)