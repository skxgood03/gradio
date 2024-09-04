import gradio as gr


# 输入文本处理程序
def greet(name):
    return name + name


# 接口创建函数
# fn设置处理函数，inputs设置输入接口组件，outputs设置输出接口组件
# fn,inputs,outputs都是必填函数
"""
fn：包装的函数
inputs：输入组件类型，（例如：“text”、"image）或者gr.Number()
ouputs：输出组件类型，（例如：“text”、"image）或者gr.Number()


最常用的基础模块构成。

应用界面：gr.Interface(简易场景), gr.Blocks(定制化场景)

输入输出：gr.Image(图像), gr.Textbox(文本框), gr.DataFrame(数据框), gr.Dropdown(下拉选项), gr.Number(数字), gr.Markdown, gr.Files

控制组件：gr.Button(按钮)

布局组件：gr.Tab(标签页), gr.Row(行布局), gr.Column(列布局)


"""
# demo = gr.Interface(fn=greet, inputs="text", outputs="text")
# demo = gr.Interface(fn=greet, inputs=gr.Number(), outputs=gr.Number())

# 自定义

demo = gr.Interface(fn=greet,
                    inputs=gr.Textbox(lines=3, placeholder='请输入', label='my input'),
                    outputs='text')

if __name__ == "__main__":
    """
    app，为 Gradio 演示提供支持的 FastAPI 应用程序
    local_url，本地地址
    share_url，公共地址，当share=True时生成
    """
    app, local_url, share_url = demo.launch(share=True)
