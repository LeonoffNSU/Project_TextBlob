from textblob import TextBlob
import nltk

text = input()
text_blob_obj = TextBlob(text)

polarity = text_blob_obj.sentiment.polarity
objectivity = round((1 - text_blob_obj.sentiment.subjectivity) * 100, 1)

if polarity > 0:
    print('Тональность текста: положительная')
elif polarity < 0:
    print('Тональность текста: отрицательная')
else:
    print('Тональность текста: нейтральная')

print(f'Объективность: {objectivity}%')
print('Слов:', len(text_blob_obj.words))


