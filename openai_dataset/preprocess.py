import json

'''
each table strucure eg:

{'column_names': [[-1, '*'], [0, 'perpetrator id'], [0, 'people id'], [0, 'date'], [0, 'year'], [0, 'location'], [0, 'country'], [0, 'killed'], [0, 'injured'], [1, 'people id'], [1, 'name'], [1, 'height'], [1, 'weight'], [1, 'home town']], 'column_names_original': [[-1, '*'], [0, 'Perpetrator_ID'], [0, 'People_ID'], [0, 'Date'], [0, 'Year'], [0, 'Location'], [0, 'Country'], [0, 'Killed'], [0, 'Injured'], [1, 'People_ID'], [1, 'Name'], [1, 'Height'], [1, 'Weight'], [1, 'Home Town']], 'column_types': ['text', 'number', 'number', 'text', 'number', 'text', 'text', 'number', 'number', 'number', 'text', 'number', 'number', 'text'], 'db_id': 'perpetrator', 'foreign_keys': [[2, 9]], 'primary_keys': [1, 9], 'table_names': ['perpetrator', 'people'], 'table_names_original': ['perpetrator', 'people']}

'''

def get_column_info(table_index,column_names,column_types):
    column_dict = {}
    for columns in column_names:
        if columns[0] == table_index:
            column_index = column_names.index(columns)
            column_value = columns[1]
            column_type = column_types[column_index]
            column_dict[column_value] = column_type
    return column_dict

def return_table_with_columns_and_info(table_names,column_names,column_types):
    ''' return value eg: : 
    [ 
       {0:"perpertrator(perpetrator_id:number,people_id:number,date:text,year:number,location:text,country:text,killed:number,injured:number)"},
       {1,"people(people_id:number,name:text,height:number,weight:number,home_town:text)"},
    ]
    '''

    table_dict_with_columns_and_info = {}
    for table_index,table_name in enumerate(table_names):
        column_info = get_column_info(table_index,column_names,column_types)
        column_format = f"{table_name}({','.join(f'{key}:{value}' for key,value in column_info.items())})"
        table_dict_with_columns_and_info.update({table_index:column_format})
    return table_dict_with_columns_and_info

def get_table_info():
    db_table_info = {}
    with open('tables.json') as json_file:
        json_data_list = json.load(json_file)
        for json_data in json_data_list:
            database = json_data['db_id']
            table_names = json_data['table_names_original']
            column_names_original = json_data['column_names_original']
            column_types = json_data['column_types']
            table_dict_with_column_data = return_table_with_columns_and_info(table_names,column_names_original,column_types)
            db_table_info[database] = table_dict_with_column_data
    return db_table_info    