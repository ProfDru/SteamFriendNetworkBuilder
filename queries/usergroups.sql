SELECT steamid, name
FROM Users u
    CROSS JOIN GroupMemberships gm ON u.ROWID = gm.userid
    LEFT JOIN  Groups g ON g.ROWID = groupid
    LIMIT 50
