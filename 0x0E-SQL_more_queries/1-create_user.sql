-- Creates the MySQL server user user_0d_1.
CREATE USER
IF NOT EXISTS 'user_0d_1'@'localhost'
    IDENTIFIED BY 'user_0d_1_pwd';
-- GRant user_od_1 all privileges.
GRANT ALL
ON *.*
TO 'user_0d_1'@'localhost'
IDENTIFIED BY 'user_0d_1_pwd';
