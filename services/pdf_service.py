from pdf.extractor import PDFExtractor
from pdf.cleaner import TextCleaner
from ml.classifier import TextClassifier
from tts.speech import SpeechGenerator
from utils.document_info import DocumentInfo

import os
import uuid
import time


class PDFService:

    info_service = DocumentInfo()


    def process(
        self,
        filepath,
        voice,
        speed
    ):

        start_time = time.time()

        extractor = PDFExtractor(filepath)

        text = extractor.extract_text()


        cleaner = TextCleaner()

        clean_text = cleaner.clean(text)


        # Document information
        document_info = self.info_service.analyze(
            filepath
        )


        classifier = TextClassifier()

        analysis = classifier.analyze(
            clean_text
        )


        filtered_text = analysis["filtered_text"]


        audio_filename = f"{uuid.uuid4()}.mp3"


        audio_path = os.path.join(
            "audio",
            audio_filename
        )


        speaker = SpeechGenerator(
        voice=voice,
        rate=speed
        )

        speaker.convert(
            filtered_text,
            audio_path
        )

        processing_time = round(
            time.time() - start_time,
            2
        )

        return {

            "text": filtered_text,

            "audio_file": audio_filename,

            "analysis": analysis,

            "document_info": document_info,

            "processing_time": processing_time,

        }