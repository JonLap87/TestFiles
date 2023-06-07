import requests
import yadisk

def visit (geo_logs):
    new_list = []
    for geo_rus in geo_logs:
        for geo_r, g in geo_rus.item():
            if 'Россия' in g:
                new_list.append(geo_rus)

    return new_list


def langs(ids):
    langs = []
    for lang in ids.values():
        if type(lang) == list:
            langs += lang
        else:
            langs.append(lang)
    return (set(langs))


def max_val(stats):
    max_val = max(stats.items(), key=lambda x: x[1]) 
    return (max_val[0])

def y():
    y = yadisk.YaDisk(token="y0_AgAAAABtQNFaAAoFNwAAAADk6-VddQOjr9lpQNOlxCJpr-4ieacevKA")
    if y.is_dir("New") == True:
        y.mkdir("New")
    else:
        KeyError
    return
 