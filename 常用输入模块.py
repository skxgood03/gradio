import gradio as gr
# 创建输入组件列表
input_list = [
    gr.Textbox(lines=3, placeholder='请输入', label='文本输入'),
    gr.Number(label='数字输入'),
    gr.Slider(minimum=0, maximum=100, step=1, label='滑动条'),
    gr.Dropdown(choices=['选项1', '选项2', '选项3'], label='下拉选择'),
    gr.Checkbox(label='复选框'),
    gr.CheckboxGroup(choices=['选项A', '选项B', '选项C'], label='多选框组'),
    gr.Radio(choices=['选项X', '选项Y', '选项Z'], label='单选按钮'),
    gr.Image(type='pil', label='图片上传'),
    gr.File(label='文件上传'),
    gr.Audio(source='microphone', type='numpy', label='音频录制'),
    gr.Video(source='webcam', type='numpy', label='视频录制'),
    gr.ColorPicker(label='颜色选择'),
]
