#!/usr/bin/env python3
import ocr_module
import audio_module
from audio_module import audio
from ocr_module import ocr
import argparse

#main
if __name__ == "__main__":
	
	ap = argparse.ArgumentParser()
	ap.add_argument("-i", "--input", required=True, help="path to input directory")
	ap.add_argument("-p", "--psm", type=int, default=13, help="Tesseract PSM mode")
	ap.add_argument("-o", "--output", required=True, help="path to the output text file")
	ap.add_argument("-a", "--audio", required=True, help="path to the output audio file")
	args = vars(ap.parse_args())

	input_dir = args["input"]
	output_dir = args["output"]
	psm = args["psm"]
	audio_dir = args["audio"]

	#ocr
	ocr(input_dir, output_dir, psm)

	#audio
	audio(output_dir, audio_dir)

	print("DONE")