import os
import snowflake.connector
from snowflake.connector.errors import DatabaseError, ProgrammingError
snowflake_account = os.environ['SNOWFLAKE_ACCOUNT']

if __name__ == '__main__':
    try:
        con = snowflake.connector.connect(
            user='bad username',       # <-------- Bad user
            password='bad password',   # <-------- Bad pass
            account=snowflake_account  # <-------- This is correct
        )
    except DatabaseError as db_ex:
        if db_ex.errno == 250001:
            print(f"Invalid username/password, please re-enter username and password...")
            # code for user to re-enter username & pass
        else:
            raise
    except Exception as ex:
        # Log this
        print(f"Some error you don't know how to handle {ex}")
        raise
    else:
        try:
            results = con.cursor().execute("select * from db.schema.table").fetchall()
            print(results)
        except ProgrammingError as db_ex:
            print(f"Programming error: {db_ex}")
            raise
        finally:
            con.close()