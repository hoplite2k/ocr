#!/usr/bin/env python3
import pytesseract
import argparse
import cv2
from imutils import paths
import os

#text from image
def image_to_text(image, psm):
	language = "kan"
	options = "-l {} --psm {}".format(language, psm)
	text = pytesseract.image_to_string(image, config=options)
	return text

#file formation
def file_formation(file, text):
	with open(file, 'w') as f:
		f.write(text)

#main ocr
def ocr(input_dir, output_dir, psm):
	if not os.path.exists(output_dir):
		os.makedirs(output_dir)

	imagepaths = list(paths.list_images(input_dir))

	for (i,image_path) in enumerate(imagepaths):
		img_name = image_path.split(os.path.sep)[-1]
		file_name = os.path.splitext(img_name)[0] + '.txt'
		file_path = os.path.join(output_dir, file_name)
		img = cv2.imread(image_path)
		rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
		text = image_to_text(rgb, psm)
		file_formation(file_path, text)


#main
if __name__ == '__main__':
	
	ap = argparse.ArgumentParser()
	ap.add_argument("-i", "--input", required=True, help="path to input directory")
	ap.add_argument("-p", "--psm", type=int, default=13, help="Tesseract PSM mode")
	ap.add_argument("-o", "--output", required=True, help="path to the output directory")
	args = vars(ap.parse_args())

	input_dir = args["input"]
	output_dir = args["output"]
	psm = args["psm"]

	ocr(input_dir, output_dir, psm)

	print("DONE")