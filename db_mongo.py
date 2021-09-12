#
#
#
#
#
from pymongo import MongoClient
import os


class DbMng:
    def __init__(self):
        self.classtest()
        self.conn_str = self.create_connection_string()
        self.cli_conn = MongoClient(self.conn_str, serverSelectionTimeoutMS=5000)

        try:
            print(self.cli_conn.server_info())
        except Exception:
            print("Unable to connect to server")

        self.ml_db = self.cli_conn['ML-Database']
        self.ml_tb_raw = self.ml_db['Raw-Table']
        self.ml_tb_company = self.ml_db['Company-Info']

        pass

    def classtest(self):
        print("Setting Variables")
        os.environ['DB_USER'] = 'admin'
        os.environ['DB_PASS'] = 'True0919'

    def create_connection_string(self):
        connection_string = "mongodb+srv://ML_Admin:<password>@ml-predictor.4zecl.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
        conn_pass = os.environ['DB_PASS']
        conn_user = os.environ['DB_USER']
        connection_string = connection_string.replace("<password>", conn_pass)
        return connection_string

    def input_mult_raw_data(self, rawData):
        print("Input Many")
        try:
            self.ml_tb_raw.insert_many(rawData)
        except Exception:
            print("Failed to install all inserts")
        pass

    def input_one_raw_data(self, rawData):
        print("Input ONE")
        try:
            self.ml_tb_raw.insert_one(rawData)
        except Exception:
            print("Failed Document Input")
        pass

    def insert_new_company(self, newCompany):
        print("Input insert Stock")
        stock_tag = newCompany['stk_indx']

        if self.ml_tb_company.find(stock_tag) == None:
            try:
                self.ml_tb_company.insert_one(newCompany)
            except Exception:
                print("New Company Could Not be Inserted")
        else:
            print("Company already exists")


def test_db_mng():
    test_class = DbMng()


test_db_mng()
