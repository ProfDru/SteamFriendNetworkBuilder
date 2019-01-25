SELECT steamid, name
FROM Users 
    CROSS JOIN GroupMemberships ON Users.ROWID = GroupMemberships.userid
    CROSS JOIN Groups ON GroupMemberships.groupid = Groups.ROWID