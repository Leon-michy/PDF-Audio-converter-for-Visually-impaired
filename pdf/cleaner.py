import re


class TextCleaner:

    def clean(self, text):

        # Join words split by hyphen at line breaks
        text = re.sub(r'-\n', '', text)

        # Replace remaining line breaks with spaces
        text = re.sub(r'\n+', ' ', text)

        # Remove extra spaces
        text = re.sub(r'\s+', ' ', text)

        return text.strip()