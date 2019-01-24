import groupsql
import unittest
import sqlite3

class Test_SNFU(unittest.TestCase):

    def test_connection(self):
        ''' Tests if the connection to the db can even be initialized'''
        testdb = sqlite3.connect("databases/TestEnv.db")
        assert testdb is not None
        testdb.close()

    def test_init(self):
        ''' Checks to see if Tables are correctly initialized '''

        testdb = sqlite3.connect("databases/TestEnv.db")
        crs = testdb.cursor()
        groupsql.InitializeTables(crs)

        testdb.commit()
        
        select_query = "SELECT name FROM sqlite_master WHERE type='table';"
        crs.execute(select_query)

        results = crs.fetchall()

        assert results is not None
        testdb.close()
    



