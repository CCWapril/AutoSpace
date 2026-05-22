import gradio as gr
from generator import MusicGenerator
import scipy.io.wavfile
import datetime

generator = None

def generate_music_interface(prompt, duration, style):
    global generator
    if generator is None:
        generator = MusicGenerator()
    
    full_prompt = prompt
    if style != "无":
        full_prompt = f"{style} style: {prompt}"
    
    audio, sr, gen_time = generator.generate(full_prompt, duration)
    
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    output_filename = f"generated_{timestamp}.wav"
    scipy.io.wavfile.write(output_filename, rate=sr, data=audio)
    
    report = f"创作报告\n- 算法: MusicGen\n- 提示词: {full_prompt}\n- 时长: {duration}s\n- 推理: {gen_time:.2f}s"
    
    return output_filename, report

demo = gr.Interface(
    fn=generate_music_interface,
    inputs=[
        gr.Textbox(label="音乐描述", placeholder="例如: 轻松的钢琴曲"),
        gr.Slider(minimum=2, maximum=30, value=10, label="时长 (秒)"),
        gr.Dropdown(choices=["无", "流行", "摇滚", "爵士", "古典", "电子", "嘻哈"], label="风格", value="无")
    ],
    outputs=[
        gr.Audio(label="生成结果"),
        gr.Textbox(label="报告")
    ],
    title="🎵 智能音乐创作助手",
    description="输入描述，AI 为你生成音乐。"
)

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
