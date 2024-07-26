import tkinter as tk
from tkinter import filedialog
# import yt_dlp
import os
from openai import OpenAI
client = OpenAI(api_key="sk-None-jB9OBvGOXBWVHo0Z4Yu8T3BlbkFJEHEtK8V4N3cpjTQ2mWH6")

def select_file():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    file_path = filedialog.askopenfilename(filetypes=[("Audio files", "*.mp3 *.wav *.ogg")])
    return file_path

# def download_youtube_audio(url):
#     ydl_opts = {
#         'format': 'bestaudio/best',
#         'postprocessors': [{
#             'key': 'FFmpegExtractAudio',
#             'preferredcodec': 'mp3',
#             'preferredquality': '192',
#         }],
#         'outtmpl': 'output/%(title)s.%(ext)s'
#     }
#     with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#         info = ydl.extract_info(url, download=True)
#         return os.path.join('output', f"{info['title']}.mp3")

def get_input():
    print("Choose input method:")
    print("1. Select local file")
    print("2. Enter YouTube URL")
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        return select_file()
    elif choice == '2':
        url = input("Enter YouTube URL: ")
        # return download_youtube_audio(url)
    else:
        print("Invalid choice. Exiting.")
        exit()

def get_source_language(inputText):
    inputCommand = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are to output the language that this input text is in and nothing more."},
        {"role": "user", "content": f"{inputText[:20]}"}
    ]
    )

    return input(inputCommand)

def output_requested_language_input_prompt(inputText):
    source_language = get_source_language(inputText)

    input_prompt = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": f"You always answer in {source_language}"},
        {"role": "user", "content": f"Answer only, 'Input your target language' in {source_language}. nd with ': ' also"}
    ]
    )

    return input_prompt
