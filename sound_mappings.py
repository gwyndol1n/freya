from pydub import AudioSegment
from pydub.playback import play

def say_hello():
	hello_mp3 = AudioSegment.from_file('/media/jimmy/HDD/Projects/Python/FREYA/hello.mp3')
	play(hello_mp3)