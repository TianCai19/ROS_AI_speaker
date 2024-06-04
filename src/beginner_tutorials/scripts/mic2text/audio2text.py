# 导入所需的库
import io
import os
from google.cloud import speech
import os

# Get the current directory of the Python file
current_directory = os.path.dirname(os.path.abspath(__file__))
print(current_directory)

# Set the path to the speech-to-text-key.json file relative to the Python file
key_file_path = os.path.join(current_directory, "speech-to-text-key.json")
print(key_file_path)

if os.path.exists(key_file_path):
    print("File exists.")
else:
    print("File does not exist.")



# Set the environment variable to the key file path
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = key_file_path
# 这里的 json 文件是你的服务账号密钥,


# 定义一个函数，用于从音频文件中提取文本
def audio2text(input_file):
    """
    Convert audio file to text using Google Cloud Speech API.

    Args:
        input_file (str): The path to the input audio file.

    Returns:
        str: The transcribed text from the audio file.
    """
    # Rest of the code...
def audio2text(input_file):
    # 创建一个 Google Cloud Speech 客户端
    client = speech.SpeechClient()
    
    # 指定输入音频文件的名称
    # file_name = os.path.join(os.path.dirname(__file__), input_file)
    
    # 使用二进制方式打开音频文件
    with io.open(input_file, "rb") as audio_file:
        # 读取音频文件的内容
        content = audio_file.read()
        # 创建一个表示音频的 RecognitionAudio 对象
        audio = speech.RecognitionAudio(content=content)

    # 配置语音识别的参数
    config = speech.RecognitionConfig(
        # 指定音频编码为 LINEAR16 格式，这是一种常见的音频编码格式
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        # 指定要识别的语言为英语 (美国)
        language_code="en-US",
    )

    # 调用 Google Cloud Speech API 进行语音识别，传递配置和音频数据
    response = client.recognize(request={"config": config, "audio": audio})

    # 处理语音识别的结果
    # for result in response.results:

        # 打印识别结果中的第一个备选项（通常是最高置信度的结果）的文本
        # print("Text to Speech Output : {}".format(result.alternatives[0].transcript))
    
    # 返回一个示意值（在这里是 1），可以根据需要修改
    ##
    first_result = response.results[0]
    return first_result.alternatives[0].transcript

if __name__ == "__main__":
    audio_file_path = os.path.join(os.path.dirname(__file__), "captured_audio.wav")

    if os.path.exists(audio_file_path):
        print("File exists.")
    else:
        print("File does not exist.")
    
    question = audio2text(audio_file_path)
    print(question)