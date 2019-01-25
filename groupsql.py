import sqlite3
import SteamGroup


def InitializeTables(crsr):
    ''' Creates all necessary tables from scratch '''
    
    init_query = open('queries/Init.sql', 'r').read()
    crsr.executescript(init_query)
    

def addIDSFromGroup(crsr, group_url):
    '''Adds the Steam ID of every player from a specified GroupURL to the Database'''

    # Determine Group Name from URL
    group_name = group_url.strip("http://steamcommunity.com/groups/")

    # Add group to the DB if doesn't it exist already
    add_group_name_query = "INSERT INTO Groups VALUES(?)"
    crsr.execute(add_group_name_query, [group_name])

    # Get the ROWID of the group we care about
    select_group_name_query = "SELECT ROWID FROM Groups WHERE name=?"
    crsr.execute(select_group_name_query, [group_name])
    groupid = crsr.fetchone()[0]

    # Grab list of members using Steamgroup.py
    group_url += '/memberslistxml?xml=1'
    group = SteamGroup.Group(group_url)
    steamids = group.get_steam_ids()

    # Format steamid list correctly
    oneple_steamids = []
    tuple_steamid_group = []

    for steamid in steamids:
        oneple_steamids.append([steamid])
        tuple_steamid_group.append((steamid, groupid))

    # Set up Queries
    add_user_query = "INSERT OR IGNORE INTO Users VALUES(?)"
    add_group_members_query = "INSERT OR IGNORE INTO GroupMemberships VALUES(?, ?)"

    # Iterate through list of steamids and add them to the DB
    crsr.executemany(add_user_query, oneple_steamids)
    crsr.executemany(add_group_members_query, tuple_steamid_group)
