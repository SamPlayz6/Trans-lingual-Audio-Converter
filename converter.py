from inputscript import *
from audioChunkJoiner import *

# Input audio and language
audio_file = open(get_input(), "rb")
print(f"Selected file: {audio_file}")


#Audio Intake
# audio_file= open("sampleAudio/To find work you love dont follow your passion Benjamin Todd TEDxYouthTallinn [TubeRipper.com].mp3", "rb")
transcription = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file
)
print(transcription.text)

target_language = get_target_language(transcription.text)


#Translation
translation = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "You are a translator who translates texts from one language to another requested language with full meaning kept and with casual language between langauges."},
    {"role": "user", "content": f"Translate this text: {transcription.text} /nTo the language: {target_language}"}
  ]
)


with open('output/output.txt', 'w', encoding='utf-8') as f:
    f.write(str(translation.choices[0].message.content))


#Text to Speach
with open('output/output.txt', 'r', encoding='utf-8') as f:
    content = f.read()


# response = client.audio.speech.create(
#     model="tts-1",
#     voice="onyx",
#     input=content[:3000], #This is a temporary fix. Must find a work around for longer scripts.
# )

# response.stream_to_file("output/output.mp3")




audio_files = generate_audio_chunks(client, content)
combine_audio_files(audio_files, "output/final_output.mp3")

# Clean up individual chunk files
for file in audio_files:
    os.remove(file)

print("Audio generation complete. Final output saved as 'output/final_output.mp3'")