import pyaudio
import wave

def record_audio(output_filename, duration=5, sample_rate=44100, channels=2):
    audio = pyaudio.PyAudio()

    stream = audio.open(format=pyaudio.paInt16,
                       channels=channels,
                       rate=sample_rate,
                       input=True,
                       frames_per_buffer=1024)

    print("Recording...")

    frames = []
    for _ in range(0, int(sample_rate / 1024 * duration)):
        data = stream.read(1024)
        frames.append(data)

    print("Finished recording.")

    stream.stop_stream()
    stream.close()
    audio.terminate()

    with wave.open(output_filename, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(audio.get_sample_size(pyaudio.paInt16))
        wf.setframerate(sample_rate)
        wf.writeframes(b''.join(frames))

if __name__ == "__main__":
    output_filename = "recorded_audio.wav"
    duration = 10  # You can adjust the duration as needed
    record_audio(output_filename, duration)
