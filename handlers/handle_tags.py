from handlers.handle_text import text_tag_process
from handlers.handle_tables import update_existing_table


def handle_tags(doc,dataDump):
    update_existing_table(doc, dataDump)
    text_tag_process(doc,dataDump)
    


