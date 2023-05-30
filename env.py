user = 'kalpana_1823'
password = 'Oi6iuiaeBJRD2sfsQG2adN2NyvOaNmgb'
host = '157.230.209.171'

li_username = 'rio.mmontana@gmail.com'
li_pw = 'Cl@r1f1C@t10n2014*!'

def get_connection(user, password, host, database):
    return f'mysql+pymysql://{user}:{password}@{host}/{database}'
