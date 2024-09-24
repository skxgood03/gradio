import gradio as gr

# 创建输出组件列表
output_list = [
    gr.Textbox(label='文本输出'),
    gr.Number(label='数字输出'),
    gr.Label(label='标签输出'),
    gr.Image(type='pil', label='图片输出'),
    gr.Audio(label='音频输出'),
    gr.Video(label='视频输出'),
    gr.File(label='文件输出'),
    gr.JSON(label='JSON 输出'),
    gr.Dataframe(label='数据表格输出'),
    gr.HighlightedText(label='高亮文本输出'),
    gr.Gallery(label='轮播图输出')
]

def generate_outputs():
    # 生成示例数据
    text_output = '示例文本'
    number_output = 123
    label_output = '示例标签'
    image_output = 'https://example.com/image.jpg'
    audio_output = 'https://example.com/audio.mp3'
    video_output = 'https://example.com/video.mp4'
    file_output = 'https://example.com/file.txt'
    json_output = {'key': 'value'}
    dataframe_output = [['John', 20], ['Jane', 22]]
    highlighted_text_output = {'text': 'This is some text.', 'highlights': [4, 5, 6]}
    gallery_output = ['https://example.com/image1.jpg', 'https://example.com/image2.jpg']

    # 返回一个元组
    return (
        text_output,
        number_output,
        label_output,
        image_output,
        audio_output,
        video_output,
        file_output,
        json_output,
        dataframe_output,
        highlighted_text_output,
        gallery_output
    )

# 创建 Gradio 应用
demo = gr.Interface(
    fn=generate_outputs,
    inputs=gr.Button("生成"),
    outputs=output_list
)

demo.launch()
