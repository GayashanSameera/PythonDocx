from helpers.utils import get_value_array_using_array_and_key, find, get_value_array_of_keys_using_object
from helpers.table_related import get_data_paths_and_table_ids, find_table_with_id,update_table_headers, update_table_data

def update_existing_table(doc, dataDump):
    ids_and_data = get_data_paths_and_table_ids(doc, dataDump)
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
                
            
            

        