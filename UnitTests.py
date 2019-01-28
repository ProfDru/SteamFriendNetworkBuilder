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

    def test_addition(self):
        ''' Tests adding steamids from a group '''
        
        # Define Cursor
        testdb = sqlite3.connect("databases/TestEnv.db")
        crs = testdb.cursor()

        # Initalize Database
        groupsql.InitializeTables(crs)
        testdb.commit()

        # Add IDS from group to DB
        groupsql.addIDSFromGroup(crs, "http://steamcommunity.com/groups/SteamLadder")
        testdb.commit()

        # Execute query to ensure it worked out
        select_query = open("queries/usergroups.sql").read()
        crs.execute(select_query)
        results = crs.fetchall()

        assert results is not None
        testdb.close()



    



