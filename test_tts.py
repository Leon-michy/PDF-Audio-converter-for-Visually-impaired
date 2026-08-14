from tts.speech import SpeechGenerator

speaker = SpeechGenerator()

text = """
Hello.

This is a test of my final year project.

The PDF has been converted into speech successfully.
"""

speaker.convert(
    text,
    "audio/test.mp3"
)

print("Audio generated successfully!")