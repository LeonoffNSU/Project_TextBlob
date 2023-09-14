from textblob import TextBlob
from googletrans import Translator

text = input().lower()
word_list = text.split()
syl_cnt = 0
translator = Translator()
detector = translator.detect(text)

if detector.lang == 'ru':
    translation = translator.translate(text, src='ru', dest='en')
    for letter in ['а', 'о', 'у', 'э', 'ы', 'и', 'е', 'ё', 'я', 'ю']:
        syl_cnt += text.count(letter)

    text_translated = translation.text

elif detector.lang == 'en':
    pass

else:
    print('Введенный текст не относится к русскому или английскому языкам.')

text_blob_obj = TextBlob(text_translated)
text_corrected = text_blob_obj.correct()
polarity = text_corrected.sentiment.polarity
objectivity = round((1 - text_corrected.sentiment.subjectivity) * 100, 1)

if detector.lang == 'en':
    for letter in ['a', 'e', 'i', 'o', 'u', 'y']:
        syl_cnt += text_corrected.count(letter)

print(text_corrected)

if polarity > 0:
    print('Тональность текста: положительная')
elif polarity < 0:
    print('Тональность текста: отрицательная')
else:
    print('Тональность текста: нейтральная')

print(f'Средняя длина слова в слогах: {syl_cnt/len(word_list)}')
print(f'Объективность: {objectivity}%')
print('Слов:', len(word_list))
print('Количество слогов:', syl_cnt)
