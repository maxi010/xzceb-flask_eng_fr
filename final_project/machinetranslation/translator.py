from deep_translator import MyMemoryTranslator

def english_to_french(englishtext):
    ''' translate english to french '''
    frenchtext = MyMemoryTranslator(source='english', target='french').translate(englishtext)
    return frenchtext

def french_to_english(frenchtext):
    ''' translate french to english '''
    englishtext = MyMemoryTranslator(source='french', target='english').translate(frenchtext)
    return englishtext
