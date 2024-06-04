import pyaudio
import wave
import os

def capture_audio(sample_rate=16000, audio_duration=6):
    # 设置录音参数
    audio_format = pyaudio.paInt16
    channels = 1
    chunk = 1024

    # 创建 PyAudio 对象
    audio = pyaudio.PyAudio()

    # 打开麦克风流
    stream = audio.open(format=audio_format,
                        channels=channels,
                        rate=sample_rate,
                        input=True,
                        frames_per_buffer=chunk)

    print("Recording...")

    frames = []

    # 开始录音
    for i in range(0, int(sample_rate / chunk * audio_duration)):
        data = stream.read(chunk)
        frames.append(data)

    print("Recording finished.")

    # 停止录音
    stream.stop_stream()
    stream.close()
    audio.terminate()

    # 保存录音到 WAV 文件
    # Get the directory path of the current file
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Set the audio file path relative to the current file
    audio_file = os.path.join(current_dir, "captured_audio.wav")
    with wave.open(audio_file, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(audio.get_sample_size(audio_format))
        wf.setframerate(sample_rate)
        wf.writeframes(b''.join(frames))

    return audio_file



if __name__ == "__main__":
    audio_file = capture_audio()
    # text = generate_text(audio_file)
    # print(text)
