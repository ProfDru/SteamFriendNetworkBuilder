import sqlite3


def InitializeTables(crsr):
    ''' Creates all necessary tables from scratch '''
    
    init_query = open('queries/init.sql', 'r').read() 
    crsr.execute(init_query)
    
