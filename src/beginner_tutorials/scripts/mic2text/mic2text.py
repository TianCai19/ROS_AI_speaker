from audio2text import audio2text
from capture_mirc_audio import capture_audio


question= audio2text(capture_audio())
print(question)