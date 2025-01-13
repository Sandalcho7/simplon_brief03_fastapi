from src.api.database import execute_sql
from src.utils import validate_year


# User story 1
def get_average_revenue(db_path, city):
    query = f"""
    SELECT revenu_fiscal_moyen 
    FROM foyers_fiscaux ff 
    WHERE ville = '{city.capitalize()}' 
    ORDER BY date DESC 
    LIMIT 1
    """
    return execute_sql(db_path, query)


# User story 2
def get_last_transactions(db_path, city, number):
    query = f"""
    SELECT * 
    FROM transactions_sample ts 
    WHERE ville LIKE '{city.upper()}%' 
    ORDER BY date_transaction DESC 
    LIMIT {number}
    """
    return execute_sql(db_path, query)


# User story 3
def get_transactions_count(db_path, city, year):
    year = validate_year(year)
    query = f"""
    SELECT COUNT(*) as nb_transactions 
    FROM transactions_sample ts 
    WHERE ville LIKE '{city.upper()}%' 
    AND date_transaction LIKE '{year}%'
    """
    return execute_sql(db_path, query)


# User story 4
def get_average_price_per_square_meter(db_path, year, type):
    year = validate_year(year)
    query = f"""
    SELECT AVG(prix/surface_habitable) as prix_m2_moyen 
    FROM transactions_sample ts 
    WHERE type_batiment = '{type.capitalize()}' 
    AND date_transaction LIKE '{year}%'
    """
    return execute_sql(db_path, query)


# User story 5
def get_transactions_count_by_criteria(db_path, city, year, type, rooms):
    year = validate_year(year)
    query = f"""
    SELECT COUNT(*) as nb_transactions 
    FROM transactions_sample ts 
    WHERE type_batiment = '{type.capitalize()}' 
    AND n_pieces = {rooms} 
    AND ville LIKE '{city.upper()}%' 
    AND date_transaction LIKE '{year}%'
    """
    return execute_sql(db_path, query)


# User story 6
def get_transactions_by_pieces(db_path, city, year, type):
    year = validate_year(year)
    query = f"""
    SELECT n_pieces, COUNT(*) as nb_transactions 
    FROM transactions_sample ts 
    WHERE type_batiment = '{type.capitalize()}' 
    AND ville LIKE '{city.upper()}%' 
    AND date_transaction LIKE '{year}%'
    GROUP BY n_pieces
    """
    return execute_sql(db_path, query)


# User story 7
def get_average_price_per_square_meter_by_city(db_path, city, year, type):
    year = validate_year(year)
    query = f"""
    SELECT AVG(prix/surface_habitable) as prix_m2_moyen 
    FROM transactions_sample ts 
    WHERE type_batiment = '{type.capitalize()}' 
    AND ville LIKE '{city.upper()}%' 
    AND date_transaction LIKE '{year}%'
    """
    return execute_sql(db_path, query)


# User story 8
def get_transactions_by_department(db_path):
    query = f"""
    SELECT departement, COUNT(*) as nb_transactions 
    FROM transactions_sample ts 
    GROUP BY departement 
    ORDER BY nb_transactions DESC
    """
    return execute_sql(db_path, query)


# User story 9
def get_transactions_count_by_revenue_and_type(db_path, year1, revenu, year2, type):
    query = f"""
    SELECT COUNT(*) as nb_transactions 
    FROM transactions_sample ts 
    JOIN foyers_fiscaux ff ON ts.ville = UPPER(ff.ville) 
    WHERE ff.date LIKE '{year1}%' 
    AND ff.revenu_fiscal_moyen > {revenu} 
    AND ts.date_transaction LIKE '{year2}%' 
    AND type_batiment = '{type.capitalize()}'
    """
    return execute_sql(db_path, query)


# User story 10
def get_top_10_cities_by_transactions(db_path):
    query = f"""
    SELECT ville, COUNT(*) as nb_transactions 
    FROM transactions_sample ts 
    GROUP BY ville 
    ORDER BY COUNT(*) DESC 
    LIMIT 10
    """
    return execute_sql(db_path, query)


# User stories 11 & 12
def get_top_10_cities_by_price(db_path, type):
    query = f"""
    SELECT ville, AVG(prix/surface_habitable) as prix_m2_moyen 
    FROM transactions_sample ts 
    WHERE type_batiment = '{type.capitalize()}' 
    GROUP BY ville 
    ORDER BY prix_m2_moyen ASC 
    LIMIT 10
    """
    return execute_sql(db_path, query)
