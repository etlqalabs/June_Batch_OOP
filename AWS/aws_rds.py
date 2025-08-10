import pandas as pd
from sqlalchemy import create_engine

# Create mysql engine
mysql_engine = create_engine('mysql+pymysql://admin:password@mysqldb.cnkoc8gg2fb4.ap-south-1.rds.amazonaws.com:3306/demo')

def read_from_rds_mysql():
    query = """select * from Employees;"""
    # Read the table employees from RDS - MYSQL
    df = pd.read_sql(query, mysql_engine)
    print(df)
   # Write to employees_deptno_10 on RDS - MYSQL
    df.to_sql("employees_target", mysql_engine, index=False, if_exists='replace')

read_from_rds_mysql()
