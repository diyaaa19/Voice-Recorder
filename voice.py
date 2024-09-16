import sounddevice as sd
import wavio as wv

# Sampling frequency
freq = 44100

# Recording duration
duration = 10

# Start recorder with the given values 
# of duration and sample frequency
recording = sd.rec(int(duration * freq), 
				samplerate=freq, channels=2)

# Record audio for the given number of seconds
sd.wait()

# Convert the NumPy array to audio file
wv.write("recording1.wav", recording, freq, sampwidth=1)
