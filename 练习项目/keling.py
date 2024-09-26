import time

import gradio as gr


def text_audio(text, type, duration, imagine, num, text_2):
    time.sleep(2)
    return r'C:\Users\Administrator\Downloads\高性能_看向镜头_微笑.mp4'


# demo = gr.Interface(css='style.css', fn=text_audio, title="文生视频",
#                     inputs=[gr.Textbox(lines=5, max_lines=7, placeholder='请输入要生成的内容。', label='创意描述'),
#                             gr.Radio(['标准', '高品质'], label='生成模式', elem_classes='rad'),
#                             gr.Radio(['5s', '10s'], label='生成时常'),
#                             gr.Slider(minimum=0, maximum=1, label='创意想象力'),
#                             gr.Dropdown(choices=['1条', '3条', '5条'], label='生成数量'),
#                             gr.Textbox(lines=5, max_lines=7, placeholder='不希望呈现的内容',
#                                        label='写下你不希望在视频中呈现的内容。'),
#                             ],
#                     outputs="playable_video"
#                     )

with gr.Blocks(css='style.css') as demo:
    gr.Markdown("""
    # 文生视频
    开始输入以下内容以查看输出。
    """ )
    with gr.Row():

        with gr.Column():

            text = gr.Textbox(lines=5, max_lines=7, placeholder='请输入要生成的内容。', label='创意描述')
            type = gr.Radio(['标准', '高品质'], label='生成模式', elem_classes='rad')
            duration = gr.Radio(['5s', '10s'], label='生成时常')
            imagine = gr.Slider(minimum=0, maximum=1, label='创意想象力')
            num = gr.Dropdown(choices=['1条', '3条', '5条'], label='生成数量')
            text_2 = gr.Textbox(lines=5, max_lines=7, placeholder='不希望呈现的内容',
                                label='写下你不希望在视频中呈现的内容。')
            button = gr.Button('生成',variant='primary')
        with gr.Column():
            opt = gr.Video()
            button.click(text_audio, inputs=[text, type, duration, imagine, num, text_2], outputs=opt)

demo.launch()
