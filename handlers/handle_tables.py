from helpers.utils import get_value_array_using_array_and_key, find, get_value_array_of_keys_using_object
from helpers.table_related import get_data_paths_and_table_ids, find_table_with_id,update_table_headers, update_table_data, get_create_table_data_paths_and_table_ids , get_table_styles_using_table_ids, move_table_after

def update_existing_table(doc, paragraph, update_table_matches, dataDump):
    for update_table_match in update_table_matches:
        ids_and_data = get_data_paths_and_table_ids(doc, dataDump,update_table_match, paragraph)
        table_id_array = get_value_array_using_array_and_key(ids_and_data, "table_id")
        if(ids_and_data and len(ids_and_data) > 0):
            for table in doc.tables:
                found_table_with_id_and_data = find_table_with_id(table,table_id_array)
                if(found_table_with_id_and_data) :
                    table_data = find(ids_and_data, "table_id", found_table_with_id_and_data)
                    if(table_data):
                        data = table_data["table_data"]["data"]
                        headers = get_value_array_of_keys_using_object(data[0])
                        update_table_headers(table,headers)
                        update_table_data(table, data, headers)


def create_tables(doc, paragraph, create_table_matches, dataDump):
    for create_table_match in create_table_matches:
        ids_and_data = get_create_table_data_paths_and_table_ids(doc, dataDump,create_table_match, paragraph)
        table_id_array = get_value_array_using_array_and_key(ids_and_data, "table_id")
        table_styles = []
        if(table_id_array and len(table_id_array) > 0):
            table_styles = get_table_styles_using_table_ids(doc,table_id_array)
        if(ids_and_data and len(ids_and_data) > 0):
            for datam in ids_and_data:
                table = doc.add_table(rows=1, cols=5)
                try:
                    if datam and datam["table_id"]:
                        sty = find(table_styles, "table_id", datam["table_id"])
                        table.style = sty["style_id"]
                except:
                    print("An exception occurred")

                move_table_after(table, paragraph)
                data = datam["table_data"]["data"]
                headers = get_value_array_of_keys_using_object(data[0])
                update_table_headers(table,headers)
                update_table_data(table, data, headers)





    
    
    
    
                
            
            

        