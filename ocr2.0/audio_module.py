#!/usr/bin/env python3
import argparse
import os
from gtts import gTTS 

#TTS
def text_to_speech(file, audiopath):
	with open(file, 'r') as f:
		file_text = f.read()
	language = 'kn'
	audio = gTTS(text=file_text, lang=language, slow=False)
	audio.save(audiopath)

#main audio
def audio(input_dir, output_dir):
	if not os.path.exists(output_dir):
		os.makedirs(output_dir)

	files = os.listdir(input_dir)
	filenames = filter(lambda x: x[-4:]== '.txt', files)

	for (i,file_name) in enumerate(filenames):
		file_path = os.path.join(input_dir, file_name)
		audio_name = os.path.splitext(file_name)[0] + '.mp3'
		audio_path = os.path.join(output_dir, audio_name)
		text_to_speech(file_path, audio_path)

#main
if __name__ == '__main__':
	
	ap = argparse.ArgumentParser()
	ap.add_argument("-i", "--input", required=True, help="path to input directory")
	ap.add_argument("-o", "--output", required=True, help="path to the output directory")
	args = vars(ap.parse_args())

	input_dir = args["input"]
	output_dir = args["output"]

	audio(input_dir, output_dir)

	print("DONE")
