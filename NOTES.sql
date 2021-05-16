DROP DATABASE IF EXISTS NOTES;
CREATE DATABASE IF NOT EXISTS NOTES;
USE NOTES;

CREATE TABLE Notes (
    noteID INT PRIMARY KEY AUTO_INCREMENT,
    note VARCHAR(500) NOT NULL
);