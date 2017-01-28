import openerplib

con = openerplib.get_connection(hostname='localhost',port=8069,database='mcsistemas',login='admin',password='123')

con.check_login()


print con.user_id
