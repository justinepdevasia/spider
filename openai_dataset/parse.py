import json
from preprocess import get_table_info
import csv

table_dict = get_table_info()

# write to csv file called prompt_data.csv
with open('prompt_data.csv', 'w') as csv_file:
    writer = csv.writer(csv_file)
    # set headers
    writer.writerow(['prompt','completion'])
    with open('train_spider.json') as json_file:
        json_data_list = json.load(json_file)
        for json_data in json_data_list:
            db_id = json_data['db_id']
            query = json_data['query']
            question = json_data['question']
            table_index_list = [tables[1] for tables in json_data['sql']['from']['table_units']]

            db_info = table_dict[db_id]
            table_string= ""
            for table_index in table_index_list:
                if type(table_index) == int:
                    table = db_info[table_index]
                    table_string += table + "\n"
                else:
                    table_string=""
                    break

            if len(table_string)>0:
                PROMPT_FORMAT = f"CREATE ERROR FREE SQL STATEMENT:{table_string}query:{question}[END]"
                writer.writerow([PROMPT_FORMAT," "+query+"[END]"])
