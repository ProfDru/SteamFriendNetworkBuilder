import groupsql
import unittest
import sqlite3

class Test_SNFU(unittest.TestCase):

    def test_init():
        ''' Checks to see if Tables are correctly initialized '''

        testdb = sqlite3.connect("databases/TestEnv.db")
        crs = testdb.cursor()
        groupsql.InitializeTables(crs)

        testdb.commit()

        select_query = "SELECT * FROM Users"
        crs.execute(select_query)

        results = crs.fetchall()
    



