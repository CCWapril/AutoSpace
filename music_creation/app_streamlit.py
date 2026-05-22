import streamlit as st
from generator import MusicGenerator
import scipy.io.wavfile
import datetime
import os
import pandas as pd

st.set_page_config(page_title="智能音乐创作助手", layout="wide")

# Initialize session state for history
if 'history' not in st.session_state:
    st.session_state.history = []

st.title("🎵 智能音乐创作助手")
st.markdown("输入你想要的音乐风格或情感关键词，AI 将为你生成原创音乐。")

# Initialize generator in session state to avoid reloading
if 'generator' not in st.session_state:
    with st.spinner("正在加载模型 (首次运行需较长时间)..."):
        st.session_state.generator = MusicGenerator()

tab_create, tab_history = st.tabs(["🎹 开始创作", "📚 创作历史"])

with tab_create:
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("创作参数")
        prompt = st.text_input("音乐描述 / 情感关键词", placeholder="例如: 轻松的钢琴曲, 动感的电子乐...")
        duration = st.slider("生成时长 (秒)", 2, 30, 10)
        style = st.selectbox("参考风格", ["无", "流行", "摇滚", "爵士", "古典", "电子", "嘻哈"])
        
        if st.button("开始创作", type="primary"):
            full_prompt = prompt
            if style != "无":
                full_prompt = f"{style} style: {prompt}"
            
            with st.spinner("AI 正在创作中..."):
                try:
                    audio, sr, gen_time = st.session_state.generator.generate(full_prompt, duration)
                    
                    # Save to file
                    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
                    output_filename = f"generated_{timestamp}.wav"
                    scipy.io.wavfile.write(output_filename, rate=sr, data=audio)
                    
                    # Add to history
                    history_item = {
                        "timestamp": timestamp,
                        "prompt": full_prompt,
                        "duration": duration,
                        "filename": output_filename,
                        "gen_time": gen_time
                    }
                    st.session_state.history.append(history_item)
                    
                    st.success("创作完成！")
                    st.audio(output_filename)
                    
                    st.markdown("### 创作报告")
                    st.info(f"""
                    - **算法**: Meta MusicGen (Small)
                    - **提示词**: {full_prompt}
                    - **生成时长**: {duration} 秒
                    - **推理时间**: {gen_time:.2f} 秒
                    - **采样率**: {sr} Hz
                    - **文件格式**: WAV (由于环境限制，暂不支持 MP3)
                    """)
                except Exception as e:
                    st.error(f"创作过程中出错: {e}")

    with col2:
        st.subheader("使用小贴士")
        st.write("- **提示词越详细越好**: 尝试描述乐器、节奏、氛围。")
        st.write("- **风格参考**: 选择风格可以帮助 AI 更好地把握基调。")
        st.write("- **硬件建议**: 本地生成依赖 CPU/GPU，时长较长时请耐心等待。")
        
        if st.session_state.history:
            st.write("---")
            st.write("### 最新作品预览")
            last_item = st.session_state.history[-1]
            st.write(f"**提示词**: {last_item['prompt']}")
            st.audio(last_item['filename'])

with tab_history:
    st.subheader("您的创作足迹")
    if not st.session_state.history:
        st.write("暂无历史记录，快去创作吧！")
    else:
        for item in reversed(st.session_state.history):
            with st.expander(f"{item['timestamp']} - {item['prompt'][:30]}..."):
                st.write(f"**完整提示词**: {item['prompt']}")
                st.write(f"**时长**: {item['duration']} 秒 | **生成耗时**: {item['gen_time']:.2f} 秒")
                st.audio(item['filename'])
                with open(item['filename'], "rb") as f:
                    st.download_button(
                        label="下载音频",
                        data=f,
                        file_name=item['filename'],
                        mime="audio/wav"
                    )

st.divider()
st.info("提示：首次运行需要下载约 1GB 的模型文件，请确保网络连接正常。")
