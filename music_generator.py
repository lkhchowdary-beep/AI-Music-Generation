from midiutil import MIDIFile
import random

music = MIDIFile(1)
track = 0
time = 0

music.addTrackName(track, time, "AI Music")
music.addTempo(track, time, 120)

for i in range(20):
    pitch = random.choice([60, 62, 64, 65, 67, 69, 71, 72])
    music.addNote(track, 0, pitch, time, 1, 100)
    time += 1

with open("ai_music.mid", "wb") as output_file:
    music.writeFile(output_file)

print("Music file created: ai_music.mid")