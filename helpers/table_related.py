import copy
import pydash
from helpers.utils import replace_tags, get_tag_content, get_tag_from_string, find

def get_table_styles(table):
    return table.style

def get_table_using_table_id():
    print("match")

def get_copy_of_table(table):
    return copy.deepcopy(table)

def get_data_paths_and_table_ids(doc, data):
    responce = []
    for paragraph in doc.paragraphs:
        pattern = r'\<TUP (.*?) \>'
        matches = get_tag_content(pattern, paragraph)
        for match in matches:
            data_path_and_table_id = match.split(" TID ")
            responce.append({ "table_id" : data_path_and_table_id[1], "table_data" : pydash.get(data, data_path_and_table_id[0]) })
            replace_tags(str(f"<TUP {match} >"), "", paragraph)
    return responce

def find_table_with_id(table, table_id_array):
    for row in table.rows:
        for cell in row.cells:
            for paragraph in cell.paragraphs:
                for t_id in table_id_array:
                    matches = get_tag_from_string(t_id, paragraph.text)
                    return matches[0]
                    break
    return False

def update_table_headers(table, headers):
    header_row = table.rows[0].cells
    i = 0
    for title in headers:
        header_row[i].text = title
        i+=1

def update_table_data(table, data, headers):
    for obj in data:
        row = table.add_row().cells
        h = 0
        for header in headers:
            row[h].text = obj[header]
            h+=1
    