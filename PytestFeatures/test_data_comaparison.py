import pandas as pd
import pytest
from sqlalchemy import create_engine
import cx_Oracle


oracle_conn = create_engine("oracle+cx_oracle://system:admin@localhost:1521/xe")
mysql_conn = create_engine("mysql+pymysql://root:Admin%40143@localhost:3308/demo")

def test_compare_employees_data_oracle_src_to_mysql_target():
    print("Test started.....")
    query_expected = """select empid,empname from employees"""
    df_expected  = pd.read_sql(query_expected,oracle_conn)
    print("Expected data from oracle ",df_expected)
    query_actual = """select empid,empname from employees"""
    df_actual = pd.read_sql(query_actual,mysql_conn)
    print("Actual data from mysql ", df_actual)
    assert df_actual.equals(df_expected),"Source data is not matchign with Traget data in employees table"
    print("Test Finshed.....")
    print()

def test_data_types_check():
    print("Test data type checks  started.....")
    query_actual = """select empid,empname from employees"""
    df_actual = pd.read_sql(query_actual,mysql_conn)
    dict_actual = df_actual.dtypes.to_dict()
    dict_expected = {'empid': 'int64', 'empname': 'object'}
    assert dict_actual == dict_expected ,"data type for target is not as expected"
    print("Test data type checks  finished.....")
    print()

