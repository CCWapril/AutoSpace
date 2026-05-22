import gradio as gr
from generator import MusicGenerator
import scipy.io.wavfile
import os
import datetime

# Initialize generator
# Note: In a real deployment, we might want to lazy-load this or use a GPU
generator = None

def generate_music(prompt, duration):
    global generator
    if generator is None:
        generator = MusicGenerator()
    
    audio, sr, gen_time = generator.generate(prompt, duration)
    
    # Save to a temporary file
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    output_filename = f"generated_{timestamp}.wav"
    scipy.io.wavfile.write(output_filename, rate=sr, data=audio)
    
    report = f"""
    ### 创作报告
    - **使用算法**: Meta MusicGen (Small)
    - **提示词**: {prompt}
    - **生成时长**: {duration} 秒
    - **推理时间**: {gen_time:.2f} 秒
    - **采样率**: {sr} Hz
    - **生成时间**: {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    """
    
    return output_filename, report

# Build Gradio UI
with gr.Blocks(title="智能音乐创作助手") as demo:
    gr.Markdown("# 🎵 智能音乐创作助手")
    gr.Markdown("输入你想要的音乐风格或情感关键词，AI 将为你生成原创音乐。")
    
    with gr.Row():
        with gr.Column():
            prompt_input = gr.Textbox(label="音乐描述 / 情感关键词", placeholder="例如: 轻松的钢琴曲, 动感的电子乐, 忧伤的萨克斯...")
            duration_slider = gr.Slider(minimum=2, maximum=30, value=10, step=1, label="生成时长 (秒)")
            style_dropdown = gr.Dropdown(choices=["无", "流行", "摇滚", "爵士", "古典", "电子", "嘻哈"], label="参考风格", value="无")
            generate_btn = gr.Button("开始创作", variant="primary")
        
        with gr.Column():
            audio_output = gr.Audio(label="生成的音乐")
            report_output = gr.Markdown()

    def handle_generation(prompt, duration, style):
        full_prompt = prompt
        if style != "无":
            full_prompt = f"{style} style: {prompt}"
        return generate_music(full_prompt, duration)

    generate_btn.click(
        fn=handle_generation,
        inputs=[prompt_input, duration_slider, style_dropdown],
        outputs=[audio_output, report_output]
    )

if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860, share=True)
