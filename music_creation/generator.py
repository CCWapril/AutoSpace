from transformers import AutoProcessor, MusicgenForConditionalGeneration
import torch
import scipy.io.wavfile
import numpy as np
import time

class MusicGenerator:
    def __init__(self, model_id="facebook/musicgen-small"):
        print(f"Loading model {model_id}...")
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.processor = AutoProcessor.from_pretrained(model_id)
        self.model = MusicgenForConditionalGeneration.from_pretrained(model_id).to(self.device)
        print("Model loaded successfully.")

    def generate(self, prompt, duration=10):
        """
        Generate music based on text prompt.
        duration: duration in seconds
        """
        # Calculate max_new_tokens based on duration
        # MusicGen generates 50 tokens per second approximately
        max_new_tokens = int(duration * 50)
        
        inputs = self.processor(
            text=[prompt],
            padding=True,
            return_tensors="pt",
        ).to(self.device)

        start_time = time.time()
        audio_values = self.model.generate(**inputs, max_new_tokens=max_new_tokens)
        end_time = time.time()
        
        # Post-process
        sampling_rate = self.model.config.audio_encoder.sampling_rate
        audio_data = audio_values[0, 0].cpu().numpy()
        
        generation_time = end_time - start_time
        return audio_data, sampling_rate, generation_time

if __name__ == "__main__":
    generator = MusicGenerator()
    prompt = "Lo-fi hip hop beat with a relaxing piano melody"
    audio, sr, gen_time = generator.generate(prompt, duration=5)
    
    output_file = "test_music.wav"
    scipy.io.wavfile.write(output_file, rate=sr, data=audio)
    print(f"Generated music saved to {output_file} (Inference time: {gen_time:.2f}s)")
