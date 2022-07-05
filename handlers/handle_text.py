
from helpers.text_related import replace_txt


def text_tag_process(doc,dataDump):
    replace_txt(doc,dataDump["text_replaces"])