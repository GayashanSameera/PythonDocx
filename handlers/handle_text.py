
from helpers.text_related import replace_txt


def text_tag_process(doc, paragraph, dataDump):
    replace_txt(doc, paragraph, dataDump["text_replaces"])