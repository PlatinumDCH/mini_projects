from deep_translator import GoogleTranslator


def translate(joke):
    return GoogleTranslator(source='auto',target='ru').translate(joke)

