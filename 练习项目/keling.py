import gradio as gr


def text_audio(text, type, duration, imagine, num):
    return r'C:\Users\Administrator\Downloads\高性能_看向镜头_微笑.mp4'



demo = gr.Interface(fn=text_audio, title="文生视频",
                    inputs=[gr.Textbox(lines=5, max_lines=7, placeholder='请输入要生成的内容', label='创意描述'),
                            gr.Radio(['标准', '高品质'], label='生成模式'),
                            gr.Radio(['5s', '10s'], label='生成时常'),
                            gr.Slider(minimum=0, maximum=1, label='创意想象力'),
                            gr.Dropdown(choices=['1', '3', '5'], label='生成数量')
                            ],
                    outputs="playable_video"
                    )

demo.launch()
