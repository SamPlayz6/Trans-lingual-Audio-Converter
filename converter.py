from inputscript import *
from audioChunkJoiner import *
import time

english = True
start_time = time.time()

# Input audio
audio_file = open(get_input(), "rb")
print(f"Selected file: {audio_file}")



print("1: ", str(time.time() - start_time))


# audio_file= open("sampleAudio/To find work you love dont follow your passion Benjamin Todd TEDxYouthTallinn [TubeRipper.com].mp3", "rb")
#Transcribing Audio
transcription = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file
)
# print(transcription.text) # Printing the Transcription



print("2: ", str(time.time() - start_time))
if english == True:
    #Target Language Prompt in English
    target_language = input("Input your target language: ")
else:
  #Target Language Prompt in Source Language
  input_request_in_source_language = output_requested_language_input_prompt(transcription.text)
  print(input_request_in_source_language, "/n/n")

  target_language = input(input_request_in_source_language)



print("3: ", str(time.time() - start_time))

#Translation
translation = client.chat.completions.create(
  model="gpt-4o-mini",
  messages=[
    {"role": "system", "content": "You are a translator who translates texts from one language to another requested language with full meaning kept and with casual language between langauges."},
    {"role": "user", "content": f"Translate this text: {transcription.text} /nTo the language: {target_language}"}
  ]
)


print("4: ", str(time.time() - start_time))



with open('output/output.txt', 'w', encoding='utf-8') as f:
    f.write(str(translation.choices[0].message.content))


#Text to Speach
with open('output/output.txt', 'r', encoding='utf-8') as f:
    content = f.read()



print("5: ", str(time.time() - start_time))



# response = client.audio.speech.create(
#     model="tts-1",
#     voice="onyx",
#     input=content[:3000], #This is a temporary fix. Must find a work around for longer scripts.
# )

# response.stream_to_file("output/output.mp3")




#Audio file Combination - 4000 Character Limit Work Around
audio_files = generate_audio_chunks(client, content)
combine_audio_files(audio_files, "output/final_output.mp3")

# Clean up individual chunk files
for file in audio_files:
    os.remove(file)

print("Audio generation complete. Final output saved as 'output/final_output.mp3'")

print("6: ", str(time.time() - start_time))