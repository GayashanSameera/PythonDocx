import copy
import pydash
from helpers.utils import replace_tags, get_tag_content, get_tag_from_string, find
import copy

def get_table_styles(table):
    return table.style

def get_table_using_table_id():
    print("match")

def get_copy_of_table(table):
    return copy.deepcopy(table)

def get_data_paths_and_table_ids(doc, data, found_match, mentioned_para):
    responce = []
    if not found_match:
        for paragraph in doc.paragraphs:
            pattern = r'\<TUP (.*?) \>'
            matches = get_tag_content(pattern, paragraph)
            for match in matches:
                data_path_and_table_id = match.split(" TID ")
                responce.append({ "table_id" : data_path_and_table_id[1], "table_data" : pydash.get(data, data_path_and_table_id[0]) })
                replace_tags(str(f"<TUP {match} >"), "", paragraph)
        return responce
    else:
        if "TID" in found_match:
            data_path_and_table_id = found_match.split(" TID ")
            responce.append({ "table_id" : data_path_and_table_id[1], "table_data" : pydash.get(data, data_path_and_table_id[0]) })
        else:
            responce.append({"table_data" : pydash.get(data, found_match) })

        replace_tags(str(f"<TUP {found_match} >"), "", mentioned_para)
        return responce

def get_create_table_data_paths_and_table_ids(doc, data, found_match, mentioned_para):
    responce = []
    if not found_match:
        for paragraph in doc.paragraphs:
            pattern = r'\<ADD_TB (.*?) \>'
            matches = get_tag_content(pattern, paragraph)
            for match in matches:
                if "CPY_TB_STY" in match:
                    data_path_and_table_id = match.split(" CPY_TB_STY ")
                    responce.append({ "table_id" : data_path_and_table_id[1], "table_data" : pydash.get(data, data_path_and_table_id[0]) })
                else:
                    responce.append({"table_data" : pydash.get(data, match) })

                replace_tags(str(f"<ADD_TB {match} >"), "", paragraph)
        return responce
    else:
        if "CPY_TB_STY" in found_match:
            data_path_and_table_id = found_match.split(" CPY_TB_STY ")
            responce.append({ "table_id" : data_path_and_table_id[1], "table_data" : pydash.get(data, data_path_and_table_id[0]) })
        else:
            responce.append({"table_data" : pydash.get(data, found_match) })

        replace_tags(str(f"<ADD_TB {found_match} >"), "", mentioned_para)
        return responce


def find_table_with_id(table, table_id_array):
    for row in table.rows:
        for cell in row.cells:
            for paragraph in cell.paragraphs:
                for t_id in table_id_array:
                    print("t_id",t_id)
                    print("paragraph.text",paragraph.text)
                    matches = get_tag_from_string(t_id, paragraph.text)
                    print("matches",matches)
                    if(matches and len(matches) > 0):
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

def get_table_styles_using_table_ids(doc,table_id_array):
    responce = []
    for table in doc.tables:
        found_table_with_id_and_data = find_table_with_id(table,table_id_array)
        if(found_table_with_id_and_data) :
            responce.append({"table_id": found_table_with_id_and_data, "style_id": table.style})

    return responce

def move_table_after(table, paragraph):
    tbl, p = table._tbl, paragraph._p
    p.addnext(tbl)
    