from inputscript import *


# Input audio and language
input_file = get_input()
target_language = get_target_language()



print(f"Selected file: {input_file}")
print(f"Target language: {target_language}")

#Audio Intake
audio_file= open("sampleAudio/To find work you love dont follow your passion Benjamin Todd TEDxYouthTallinn [TubeRipper.com].mp3", "rb")
transcription = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file
)
print(transcription.text)


#Translation
translation = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "You are a translator who translates texts from one language to another requested langauge with full meaning kept between langauges."},
    {"role": "user", "content": f"Translate this text: {transcription.text} /nTo the language: {trans_to_lang}"}
  ]
)


with open('output/output.txt', 'w', encoding='utf-8') as f:
    f.write(str(translation.choices[0].message.content))


#Text to Speach
with open('output/output.txt', 'r', encoding='utf-8') as f:
    content = f.read()


response = client.audio.speech.create(
    model="tts-1",
    voice="onyx",
    input=content[:3000], #This is a temporary fix. Must find a work around for longer scripts.
)

response.stream_to_file("output/output.mp3")