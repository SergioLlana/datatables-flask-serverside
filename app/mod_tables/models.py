from app.mod_tables.serverside.serverside_table import ServerSideTable
from app.mod_tables.serverside import table_schemas

DATA_SAMPLE = [
    {'A': 'Hello!', 'B': 'How is it going?', 'C': 3, 'D': 4},
    {'A': 'These are sample texts', 'B': 0, 'C': 5, 'D': 6},
    {'A': 'Mmmm', 'B': 'I do not know what to say', 'C': 7, 'D': 16},
    {'A': 'Is it enough?', 'B': 'Okay', 'C': 8, 'D': 9},
    {'A': 'Just one more', 'B': '...', 'C': 10, 'D': 11},
    {'A': 'Thanks!', 'B': 'Goodbye.', 'C': 12, 'D': 13}
]

class TableBuilder(object):

    def collect_data_clientside(self):
        return {'data': DATA_SAMPLE}

    def collect_data_serverside(self, request):
        columns = table_schemas.SERVERSIDE_TABLE_COLUMNS
        return ServerSideTable(request, DATA_SAMPLE, columns).output_result()
