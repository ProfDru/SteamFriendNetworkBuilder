DROP TABLE IF EXISTS Users
DROP TABLE IF EXISTS Aliases
DROP TABLE IF EXISTS Groups
DROP TABLE IF EXISTS GroupMemberships
DROP TABLE IF EXISTS Relationships

CREATE TABLE Users
    SteamId VarChar NOT NULL,
);

CREATE TABLE Aliases(
    FOREIGN KEY(userid) REFERENCES Users(ROWID),
    name VARCHAR NOT NULL,
    recorded DATETIME
);

CREATE TABLE Groups(
    name VARCHAR
);

CREATE TABLE GroupMemberships(
    FOREIGN KEY(userid) REFERENCES Users(ROWID);
    FOREIGN KEY(groupid) REFERENCES Groups(ROWID)
);

CREATE TABLE Relationships(
    FOREIGN KEY(user1) REFERENCES Users(ROWID),
    FOREIGN KEY(user2) REFERENCES USERS(ROWID)
);