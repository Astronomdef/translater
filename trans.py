from textblob import TextBlob

def translate(text, toLang):
    try:
        blob = TextBlob(text)
        translated = blob.translate(to=toLang)
        return translated
    except Exception as e:
        return f"Error: {str(e)}"

print(translate("Text to translate.", "ru"))
print(translate("نص عربي.", "en"))
print(translate("I am a great man.", "en"))
print(translate("Яблоко или груша?", "en"))
