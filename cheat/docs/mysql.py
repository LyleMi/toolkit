#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .base import BaseDoc


class MySQLDoc(BaseDoc):

    _doc = {
        "user": """SELECT Host, User FROM mysql.user;
CREATE USER 'username'@'localhost' IDENTIFIED BY 'password';
GRANT SELECT, INSERT, UPDATE, DELETE ON databasename.tablename TO 'username'@'host';
GRANT all ON databasename.tablename TO 'username'@'host';
SHOW GRANTS FOR 'username'@'host';
REVOKE all PRIVILEGES ON databasename.tablename FROM 'username'@'host';
DROP USER 'username'@'host';""",
        "password": """sudo service mysql stop
sudo mysqld_safe --skip-grant-tables &
mysql -uroot
UPDATE mysql.user SET password=PASSWORD('123456') WHERE user='root';
# mysql 5.7 or higher
UPDATE mysql.user SET authentication_string=PASSWORD('123456') WHERE User='root';
FLUSH PRIVILEGES;""",
        "insert": """INSERT INTO table_name (column_name) VALUES ("foo"),("bar");
INSERT INTO table_name VALUES ('foo', '2000-08-31');""",
        "update": """UPDATE table_name SET column_name = "new_value" WHERE record_name = "value";""",
        "alter": """ALTER TABLE table_name MODIFY column_name VARCHAR(200) NOT NULL;""",
    }


if __name__ == '__main__':
    MySQLDoc.show()
