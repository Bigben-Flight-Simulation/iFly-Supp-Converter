import sqlite3
import pandas as pd
import os
from directories import *

# 数据库路径
filename = os.path.splitext(os.path.basename(db_path))[0]


# SQL 查询语句，键为表名，值为对应的SQL
queries = {
    "AIRPORT": """
        SELECT * FROM AIRPORT 
        WHERE ARPT_ICAO_CODE IN ('ZB','ZG','ZH','ZJ','ZL','ZP','ZS','ZU','ZW','ZY');
    """,
    "AIRPORT_PROCEDURE": """
        SELECT * FROM AIRPORT_PROCEDURE 
        WHERE ARPT_ICAO_CODE IN ('ZB','ZG','ZH','ZJ','ZL','ZP','ZS','ZU','ZW','ZY');
    """,
    "NDB_NAVAID": """
        SELECT * FROM NDB_NAVAID 
        WHERE NDB_ICAO_CODE IN ('ZB','ZG','ZH','ZJ','ZL','ZP','ZS','ZU','ZW','ZY');
    """,
    "RUNWAY": """
        SELECT * FROM RUNWAY 
        WHERE ARPT_ICAO_CODE IN ('ZB','ZG','ZH','ZJ','ZL','ZP','ZS','ZU','ZW','ZY');
    """,
    "VHF_NAVAID": """
        SELECT * FROM VHF_NAVAID 
        WHERE VHF_ICAO_CODE IN ('ZB','ZG','ZH','ZJ','ZL','ZP','ZS','ZU','ZW','ZY');
    """,
    "WAYPOINT": """
        SELECT * FROM WAYPOINT 
        WHERE WAYPOINT_ICAO_CODE IN ('ZB','ZG','ZH','ZJ','ZL','ZP','ZS','ZU','ZW','ZY','VH');
    """
}

def export_to_csv():
    conn = sqlite3.connect(db_path)
    for table, sql in queries.items():
        print(f"正在导出 {table} ...")
        df = pd.read_sql_query(sql, conn)
        db_filename = filename[3:]
        output_dir = f"./resource/{db_filename}"
        os.makedirs(output_dir, exist_ok=True)
        output_file = f"{output_dir}/{table}-{db_filename}.csv"
        df.to_csv(output_file, index=False, encoding="utf-8")
        print(f"{table} 导出完成 -> {output_file}")
    conn.close()

if __name__ == "__main__":
    export_to_csv()
