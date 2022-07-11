from handlers.handle_text import text_tag_process
from handlers.handle_tables import update_existing_table, create_tables
from helpers.utils import replace_tags, get_tag_content, get_tag_from_string, find

def handle_tags(doc,dataDump):
    for paragraph in doc.paragraphs:
        pattern_create_table = r'\<ADD_TB (.*?) \>'
        create_table_matches = get_tag_content(pattern_create_table, paragraph)
        if create_table_matches and len(create_table_matches) > 0:
            create_tables(doc, paragraph, create_table_matches, dataDump)

        pattern_update_table = r'\<TUP (.*?) \>'
        update_table_matches = get_tag_content(pattern_update_table, paragraph)
        if update_table_matches and len(update_table_matches) > 0:
            update_existing_table(doc, paragraph, update_table_matches, dataDump)

        pattern_text_update_table = r'\<PT (.*?) \>'
        update_text_matches = get_tag_content(pattern_text_update_table, paragraph)
        if update_text_matches and len(update_text_matches) > 0:
            text_tag_process(doc, paragraph, dataDump)
    


