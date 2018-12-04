

"""
Goal: Pull articles from Wikipedia in French.
"""

import wikipedia

def get_page_sumarries(page_name):
    try:
        return {page_name, wikipedia.page(page_name).content}
    except:
        pass


"""    except wikipedia.exceptions.DisambiguationError as e:
        return [[p, wikipedia.page(p).summary] for p in e.options]
"""

def get_random_pages(pages=0):

    wikipedia.set_lang("fr")
    ret = []
    page_names = [wikipedia.random(1) for i in range(pages)]

    for p in page_names:
        try:
            for page_summary in get_page_sumarries(p):
                ret.append(page_summary)
        except:
            pass
    return ret

for i in range (1000000):
    try:
        my_list = get_random_pages(1)
        f = open("FrenchCorpus.txt", 'a+', encoding='utf-8')
        with f:
            for item in my_list:
                f.write("%s\n" % item)
        f.close()
    except:
            pass

