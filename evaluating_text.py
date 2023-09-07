from textblob import TextBlob

text = input()
text_blob_obj = TextBlob(text)
text_corrected = text_blob_obj.correct()
polarity = text_corrected.sentiment.polarity
objectivity = round((1 - text_corrected.sentiment.subjectivity) * 100, 1)

if polarity > 0:
    print('Тональность текста: положительная')
elif polarity < 0:
    print('Тональность текста: отрицательная')
else:
    print('Тональность текста: нейтральная')

print(f'Объективность: {objectivity}%')
print('Слов:', len(text_corrected.words))
print(text_corrected)

