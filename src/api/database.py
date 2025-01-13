import sqlite3
from fastapi import HTTPException


# Function to get a database connection
def get_db_connection(path):
    """
    Establish and return a connection to the database.
    """
    try:
        connection = sqlite3.connect(path)
        return connection
    except sqlite3.Error as e:
        raise HTTPException(status_code=500, detail=f"Database connection error: {e}")


# Executes the given query using the provided database connection
def execute_sql(path, query):
    """
    Execute a SQL query and return the results as a list of dictionaries.
    """
    with get_db_connection(path) as con:
        try:
            cur = con.cursor()
            res = cur.execute(query)
            result = res.fetchall()
            columns = [column[0] for column in cur.description]
            result_with_columns = [dict(zip(columns, row)) for row in result]

            if not result:
                raise HTTPException(status_code=404, detail="Can't find any result")

            return result_with_columns
        except sqlite3.Error as e:
            raise HTTPException(status_code=500, detail=f"Database query error: {e}")
