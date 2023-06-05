''' Translation from english to french and vice versa '''
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    ''' Translates english text to french '''
    mmt = MyMemoryTranslator("en", "fr")
    french_text = mmt.translate(english_text)
    return french_text

def french_to_english(french_text):
    ''' Translates french text to english '''
    mmt = MyMemoryTranslator("fr", "en")
    english_text = mmt.translate(french_text)
    return english_text
