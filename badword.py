import attrs
import nltk
import re
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
import string

@attrs.define
class BadWordDetection:

    def stemming_text(self, text: str):
        lowercase_sentence = text.lower()

        return lowercase_sentence


    def TokenizeText(self, text: str):

        remove_punctuation = text.translate(str.maketrans('', '', string.punctuation))
        text = self.stemming_text(remove_punctuation)
        # remove angka
        text = re.sub(r'\d+', '', text)

        # remove punctuation
        text = re.sub(r'[^\w\s]', '', text)

        # remove multiple whitespace
        text = re.sub(r'\s+', ' ', text)
        factory = StemmerFactory()
        stemmer = factory.create_stemmer()

        rokens = nltk.tokenize.word_tokenize(text)
        output = []
        for i in rokens:
            output.append(stemmer.stem(i))
        return output

    def detect_bad_word(self, text: str):
        p = self.TokenizeText(text)
        a = []
        open_data = open('/home/wonka/Documents/kerjaan/ml/indobadoword.csv', 'rb')
        for line in open_data:
            a.append(line.decode('utf-8').strip())
        punten = []

        for i in p:
            if i in a:
                punten.append(i)

        return punten


if __name__ == '__main__':
    p = BadWordDetection()
    print(p.detect_bad_word("dasar kau menganjing!!, tempikan tenan"))
