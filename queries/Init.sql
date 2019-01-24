DROP TABLE IF EXISTS Users;
DROP TABLE IF EXISTS Aliases;
DROP TABLE IF EXISTS Groups;
DROP TABLE IF EXISTS GroupMemberships;
DROP TABLE IF EXISTS Relationships;

CREATE TABLE Users(
    SteamId VarChar NOT NULL
);

CREATE TABLE Aliases(
    userid INTEGER,
    alias VARCHAR(255),
    recorded DATETIME,
    FOREIGN KEY (userid) REFERENCES Users(ROWID)
);

CREATE TABLE Groups(
    name VARCHAR
);

CREATE TABLE GroupMemberships(
    userid INTEGER,
    groupid INTEGER,
    FOREIGN KEY (userid) REFERENCES Users (ROWID),
    FOREIGN KEY (groupid) REFERENCES Groups (ROWID)
);

CREATE TABLE Relationships(
    user1 INTEGER,
    user2 INTEGER,
    FOREIGN KEY (user1) REFERENCES Users (ROWID),
    FOREIGN KEY (user2) REFERENCES Users (ROWID)
);
