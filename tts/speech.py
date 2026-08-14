import asyncio
import edge_tts


class SpeechGenerator:

    def __init__(
        self,
        voice="en-US-AriaNeural",
        rate="+0%"
    ):

        self.voice = voice
        self.rate = rate


    async def generate_audio(
        self,
        text,
        output_file
    ):

        communicate = edge_tts.Communicate(
            text=text,
            voice=self.voice,
            rate=self.rate
        )

        await communicate.save(
            output_file
        )


    def convert(
        self,
        text,
        output_file
    ):

        asyncio.run(
            self.generate_audio(
                text,
                output_file
            )
        )