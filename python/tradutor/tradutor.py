from googletrans import Translator, constants
from pprint import pprint
 
translator = Translator()
def translate(text):
    # translate a spanish text to english text (by "default")
    translation = translator.translate(text, dest="en")
    print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")
    return translation.text
 
 
