from django import template


filters = template.Library()


@filters.filter(name='filter_')
def censor(value):
    unwanted_words = ['нежелательное', 'еще одно'] # Замените это на список нежелательных слов
    for word in unwanted_words:
        value = value.replace(word, '*' * len(word))
    return value
