import json
DBNAME='monitor'
HOST = "127.0.0.1"
# mysql
MDB = {
	'host':HOST,
    'channel':'root',
    'passwd':'akisj13920',
    'db':DBNAME,
    'charset':'utf8',
    'sock': '/var/img/mysql/m_mysql.sock',
    'port':3306
}
SDB = {
	'host':HOST,
    'channel':'root',
    'passwd':'akisj13920',
    'db':DBNAME,
    'charset':'utf8',
    'sock': '/var/img/mysql/m_mysql.sock',
    'port':3306
}
DB_CNF = {
    'm':{json.dumps(MDB):[DBNAME,]}, # master, other database name
    's':{json.dumps(SDB):[DBNAME,]}, # slave
}
SESSION_USER = 'monitor'