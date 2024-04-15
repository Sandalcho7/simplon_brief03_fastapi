import sqlite3

from fastapi import HTTPException

from config import DATA_PATH



if DATA_PATH:
    con = sqlite3.connect(DATA_PATH)
    print(f"Connexion à la base de données avec l'URL : {DATA_PATH}")
else:
    print("Aucune URL de base de données spécifiée dans le fichier de configuration.")


# Checks that the year input is a 4 figures number
def validate_year(year: str):
    if not year.isdigit() or not (len(year) == 4) :
        raise HTTPException(status_code=400, detail="Year input invalid, must be a 4 figures long number.")
    
    return year


# Connects to the database and execute the given query
def execute_sql(con, query):
    cur = con.cursor()
    res = cur.execute(query)

    result = res.fetchall()
    columns = [column[0] for column in cur.description]
    result_with_columns = [dict(zip(columns, row)) for row in result]

    if not result:
        raise HTTPException(status_code=404, detail="Can't find any result")
    
    return result_with_columns