import sqlite3


def InitializeTables(crsr):
    ''' Creates all necessary tables from scratch '''
    
    init_query = open('queries/Init.sql', 'r').read()
    crsr.executescript(init_query)
    
