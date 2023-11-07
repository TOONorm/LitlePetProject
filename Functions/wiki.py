import wikipedia

def get_wiki_article(article):
    wikipedia.set_lang('ru')
    try:
        return wikipedia.summary(article)
    except:
        return 'Статья не найдена'