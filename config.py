DATABASE_TYPE = 'mysql'
DATABASE_USER = 'root'
DATABASE_PASSWORD = 'openos'
DATABASE_PORT = 3306
DATABASE_HOST = '127.0.0.1'
DATABASE_NAME = 'sqlalchemy'


engine = create_engine('mysql://root:openos@127.0.0.1:3306/sqlalchemy', echo=False)
