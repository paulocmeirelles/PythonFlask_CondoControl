import pandas as pd
from sqlalchemy import create_engine
from decouple import config


class Report():
    def get():
        engine = create_engine(config('DB_CONNECTION'), echo=False)
        table = pd.read_sql_query("""SELECT * FROM boleto""", engine)
        return table
