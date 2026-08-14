import fitz


class DocumentInfo:

    def analyze(self, filepath):

        document = fitz.open(filepath)

        pages = len(document)

        text = ""

        for page in document:
            text += page.get_text()


        words = len(
            text.split()
        )


        # Average speaking speed
        # 130 words per minute

        minutes = round(
            words / 130,
            1
        )


        return {

            "pages": pages,

            "words": words,

            "duration": minutes

        }