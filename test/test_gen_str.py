server_list = [
    "designer_data_data_10",
    "designer_data_data_13",
    "designer_data_data_14",
    "designer_data_data_15",
    "designer_data_data_16",
    "designer_data_data_2",
    "designer_data_data_3",
    "designer_data_data_4",
    "designer_data_data_5",
    "designer_data_data_7",
    "designer_data_data_8",
]
update_datetime_template_str = "alter table {0} add column update_datetime timestamp not null default current_timestamp on update current_timestamp;"
create_datetime_template_str = "alter table {0} add column create_datetime timestamp not null default current_timestamp;"
if __name__ == '__main__':
    for item in server_list:
        print(update_datetime_template_str.format(item))
        print(create_datetime_template_str.format(item))
