# Imports
# from gtts import gTTS # Google text-to-speech
import pyttsx # different tts library
import shutil # high-level file operations
import speech_recognition as sr # provides Microphone, Recognizer
from recog import *
from sound_mappings import *
import sys, os, re # allow for OS cli commands; regex
from tempfile import NamedTemporaryFile # allow for TempFile object creation
import io

from pydub import AudioSegment # creates AudioSegment object from bytes
from pydub.utils import which

AudioSegment.converter = which("ffmpeg")
from pydub.playback import play # plays AudioSegment object

def main():
	r = sr.Recognizer()
	mic = sr.Microphone()

	while True:
		print("Say some shit.")
		input = recognize_speech_from_mic(r, mic)

		print(input["transcription"])

		if input["transcription"] == "hello":
			print("hello!")
			say_hello()
		if input["transcription"] in {"shutdown", "shut down"}:
			os.system("shutdown now -h")
		if "say" in input["transcription"]:
			transcription = input["transcription"].replace("say ", "")
			print("saying {}".format(transcription))
			create_tts(transcription)


# create TTS tempfile and play it, w/ additional param to keep file
def create_tts(text, save_file=None):
	try:
		if save_file is None:
			save_file = False

		if text is not None:
			tts_engine = pyttsx.init()
			tts_engine.setProperty('voice', 'english+f1')

			# file_name = "voice_files/{}.mp3".format(re.sub(r'\s+', "_", text.lower()))
			# tts = gTTS(text, 'en')
			# tts.save(file_name)
			tts_engine.say(text)
			tts_engine.runAndWait()
			# play(AudioSegment.from_file(file_name))
			# if (not save_file):
				# os.remove(file_name)

		else:
			print("Please provide a text string to create a tts file.")
	except:
		type, value, traceback = sys.exc_info()
		print("An error occured in the create_and_play_tts function.")
		print('Error %s' % (value))

# main()

# def hello_test():
# 	mp3_fp = BytesIO()
# 	tts = gTTS('tiddies', 'en')
# 	tts.save('/media/jimmy/HDD/Projects/Python/FREYA/tiddies.mp3')
# 	# tts.write_to_fp(mp3_fp)
# 	song = AudioSegment.from_file('/media/jimmy/HDD/Projects/Python/FREYA/tiddies.mp3')
# 	play(song)

#hello_test()
# from freya import create_and_play_tts
# create_and_play_tts("Fondant")