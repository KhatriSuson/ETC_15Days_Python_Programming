# pip install PyPDF2 gTTS

import PyPDF2
from gtts import gTTS
import os


def pdf_to_text(pdf_path):
    text = ""
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)
        for page_num in range(num_pages):
            page = reader.pages[page_num]
            text += page.extract_text()
    return text


def text_to_audio(text, output_file):
    tts = gTTS(text=text, lang="en")
    tts.save(output_file)


def main():
    pdf_file = input("Enter the path to the PDF file: ")
    if not os.path.isfile(pdf_file) or not pdf_file.lower().endswith(".pdf"):
        print("Invalid PDF file path or file format.")
        return

    output_file = input("Enter the path for the output audio file (e.g., output.mp3): ")

    text = pdf_to_text(pdf_file)
    text_to_audio(text, output_file)  # Function call
    print(f"Audio file saved as {output_file}")


if __name__ == "__main__":
    main()
