from textblob import TextBlob
from langdetect import detect

text = input()
print(detect(text))    # эта штука определит язык, print уберем
text_blob_obj = TextBlob(text)
text_corrected = text_blob_obj.correct()
polarity = text_corrected.sentiment.polarity
objectivity = round((1 - text_corrected.sentiment.subjectivity) * 100, 1)

print(text_corrected)

if polarity > 0:
    print('Тональность текста: положительная')
elif polarity < 0:
    print('Тональность текста: отрицательная')
else:
    print('Тональность текста: нейтральная')

print(f'Объективность: {objectivity}%')
print('Слов:', len(text_corrected.words))


