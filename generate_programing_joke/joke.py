import translator
import pyjokes

joke = pyjokes.get_joke()
print(translator.translate(joke))