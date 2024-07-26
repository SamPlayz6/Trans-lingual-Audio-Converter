from openai import OpenAI
from pydub import AudioSegment
import os

client = OpenAI(api_key="sk-None-jB9OBvGOXBWVHo0Z4Yu8T3BlbkFJEHEtK8V4N3cpjTQ2mWH6")

def chunk_text(text, max_length=4000):
    return [text[i:i+max_length] for i in range(0, len(text), max_length)]

def generate_audio_chunks(client, text, voice="onyx", model="tts-1"):
    chunks = chunk_text(text)
    audio_files = []
    for i, chunk in enumerate(chunks):
        response = client.audio.speech.create(
            model=model,
            voice=voice,
            input=chunk
        )
        filename = f"output/output_{i}.mp3"
        response.stream_to_file(filename)
        audio_files.append(filename)
        print(i , " :Run")
    return audio_files

def combine_audio_files(file_list, output_file):
    combined = AudioSegment.empty()
    for file in file_list:
        audio = AudioSegment.from_mp3(file)
        combined += audio
    combined.export(output_file, format="mp3")