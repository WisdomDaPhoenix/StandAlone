from translate import Translator
source = input("Enter source language: ")
dest = input("Enter destination language: ")
t = Translator(from_lang=source,to_lang=dest)
translation = t.translate("Este es mi coche. Tengo frio. "
                          "Vamos. ajer. Mucho gusto ")

print(translation)

