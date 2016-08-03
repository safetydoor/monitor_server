import json
import socket
hostName = socket.getfqdn(socket.gethostname())
ipAddress = socket.gethostbyname(hostName)

DB_NAME='monitor'
DB_HOST = "127.0.0.1"

SERVER_PORT = 8088
SERVER_ADDRESS = 'http://%s:8088' % ipAddress

# mysql
MDB = {
	'host':DB_HOST,
    'channel':'root',
    'passwd':'akisj13920',
    'db':DB_NAME,
    'charset':'utf8',
    'sock': '/var/img/mysql/m_mysql.sock',
    'port':3306
}
SDB = {
	'host':DB_HOST,
    'channel':'root',
    'passwd':'akisj13920',
    'db':DB_NAME,
    'charset':'utf8',
    'sock': '/var/img/mysql/m_mysql.sock',
    'port':3306
}
DB_CNF = {
    'm':{json.dumps(MDB):[DB_NAME,]}, # master, other database name
    's':{json.dumps(SDB):[DB_NAME,]}, # slave
}
SS_SERVERS = ["127.0.0.1:11000"]
COOKIE_NAME = 'session_id'
COOKIE_SECRET= 'FPdaUI5QAGaDdkL5gEmGeJJFuYh7EQnp2XdTP1'
SESSION_USER = 'monitor_user'