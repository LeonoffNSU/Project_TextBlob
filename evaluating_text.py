from textblob import TextBlob
from googletrans import Translator

text = input().lower()
temporary_text = text
word_list = text.split()
syl_cnt = 0
sen_cnt = 0
translator = Translator()
detector = translator.detect(text)

if detector.lang == 'ru':
    for letter in ['а', 'о', 'у', 'э', 'ы', 'и', 'е', 'ё', 'я', 'ю']:
        syl_cnt += text.count(letter)
    if '...' in text:
        temporary_text = text.replace('...', '.')
    sen_cnt = temporary_text.count('.') + temporary_text.count('!') + temporary_text.count('?')

    translation = translator.translate(text, src='ru', dest='en')
    text = translation.text

elif detector.lang == 'en':
    pass

else:
    print('Введенный текст не относится к русскому или английскому языкам.')

text_blob_obj = TextBlob(text)
text_corrected = text_blob_obj.correct()
polarity = text_corrected.sentiment.polarity
objectivity = round((1 - text_corrected.sentiment.subjectivity) * 100, 1)

if detector.lang == 'en':
    for letter in ['a', 'e', 'i', 'o', 'u', 'y']:
        syl_cnt += str(text_corrected).count(letter)
temporary_text = str(text_corrected)
if '...' in temporary_text:
    temporary_text = text_corrected.replace('...', '.')
sen_cnt = temporary_text.count('.') + temporary_text.count('!') + temporary_text.count('?')

if polarity > 0:
    print('Тональность текста: положительная')
elif polarity < 0:
    print('Тональность текста: отрицательная')
else:
    print('Тональность текста: нейтральная')

if detector.lang == 'ru':
    flesch_index = 206.835 - 1.3*(len(word_list)/sen_cnt) - 60.1*(syl_cnt/len(word_list))
elif detector.lang == 'en':
    flesch_index = 206.835 - 1.015*(len(word_list)/sen_cnt) - 84.6*(syl_cnt/len(word_list))

print('Предложений:', sen_cnt)
print('Слов:', len(word_list))
print('Количество слогов:', syl_cnt)
print(f'Средняя длина предложения в словах: {len(word_list) / sen_cnt}')
print(f'Средняя длина слова в слогах: {syl_cnt / len(word_list)}')
print(f'Объективность: {objectivity}%')
print('Индекс удобочитаемости Флеша:', flesch_index)

if flesch_index >= 80:
    print('Текст очень легко читается')
elif flesch_index >= 50:
    print('Простой текст')
elif flesch_index >= 25:
    print('Текст немного трудно читать')
elif flesch_index < 25:
    print('Текст очень трудно читается')
