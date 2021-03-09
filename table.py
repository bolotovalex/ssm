json_list = [{'host': 'example.exampldomain.com', 'port': '22', 'user': 'SuperAdm', 'comment': 'abrakadabrasadfsdfasdfasf'}, {'host': 'exampldomain.com', 'port': '2022', 'user': 'SuperAdmdddd', 'comment': 'abrakadabrasadfsdfasdfasf'}, {'host': 'exampldomain.com', 'port': '2022', 'user': 'SuperAdmdddd', 'comment': 'abrakadabrasadfsdfasdfasf'}, {'host': 'exampldomain.com', 'port': '2022', 'user': 'SuperAdmdddd', 'comment': 'abrakadabrasadfsdfasdfasf'}, {'host': 'exampldomain.com', 'port': '2022', 'user': 'SuperAdmdddd', 'comment': 'abrakadabrasadfsdfasdfasf'}, {'host': 'exampldomain.com', 'port': '2022', 'user': 'SuperAdmdddd', 'comment': 'abrakadabrasadfsdfasdfasf'}, {'host': 'exampldomain.com', 'port': '2022', 'user': 'SuperAdmdddd', 'comment': 'abrakadabrasadfsdfasdfasf'}, {'host': 'exampldomain.com', 'port': '2022', 'user': 'SuperAdmdddd', 'comment': 'abrakadabrasadfsdfasdfasf'}, {'host': 'exampldomain.com', 'port': '2022', 'user': 'SuperAdmdddd', 'comment': 'abrakadabrasadfsdfasdfasf'}, {'host': 'exampldomain.com', 'port': '2022', 'user': 'SuperAdmdddd', 'comment': 'abrakadabrasadfsdfasdfasf'}, {'host': 'exampldomain.com', 'port': '2022', 'user': 'SuperAdmdddd', 'comment': 'abrakadabrasadfsdfasdfasf'}, {'host': 'exampldomain.com', 'port': '2022', 'user': 'SuperAdmdddd', 'comment': 'abrakadabrasadfsdfasdfasf'}, {'host': 'exampldomain.com', 'port': '2022', 'user': 'SuperAdmdddd', 'comment': 'abrakadabrasadfsdfasdfasf'}, {'host': 'exampldomain.com', 'port': '2022', 'user': 'SuperAdmdddd', 'comment': 'abrakadabrasadfsdfasdfasf'}]
#json_list = []
class Table(object):
    def __init__(self):
        self.field_name = []
        self.rows = []
        self.max_cell = 1
        self.cell_width = {}
        self.number = 1
        self.lsit_for_print_table= []

    def field_table(self, json_list):
        '''Create Field table. Check max lenght cell'''
        if len(json_list) != 0:
            self.field_name.append('№')
            for self.key, self.value in json_list[0].items():
                self.field_name.append(self.key)
        self.i = 0
        for self.j in self.field_name:
            self.cell_width[self.i] = len(self.j) + 2
            self.i += 1
        self.max_cell = len(self.field_name)

    def rows_table(self, json_list):
        '''Add row to table. Check max lenght cell'''
        if len(json_list) != 0 :
            for self.i in json_list:
                self.row = []
                self.row.append(self.number)
                for self.key, self.value in self.i.items():
                    self.row.append(self.value)
                self.number += 1
                self.rows.append(self.row)
        for self.row in self.rows:
            for self.i in range(len(self.row)):
                if self.cell_width[self.i] < len(str(self.row[self.i])) + 2:
                    self.cell_width[self.i] = len(str(self.row[self.i])) + 2
        self.max_cell = len(self.field_name)


    def print_table(self, json_list):
        self.field_table(json_list)
        self.rows_table(json_list)
        return self.field_name, self.rows, self.max_cell, self.cell_width
table = Table()
print(table.print_table(json_list))