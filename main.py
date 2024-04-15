from fastapi import FastAPI, Path

from functions import con, validate_year, execute_sql



app = FastAPI()


# User story 1
@app.get("/average_revenue/{city}", description="Renvoie le revenu fiscal moyen de l'année la plus récente pour une ville donnée")
async def average_revenue(city: str = Path(description="Ville")):
    query = f"SELECT revenu_fiscal_moyen FROM foyers_fiscaux ff WHERE ville = '{city.capitalize()}' ORDER BY date DESC LIMIT 1"
    return execute_sql(con, query)


# User story 2
@app.get("/last_transactions/{city}_last_{number}", description="Renvoie le nombre choisi de dernières transactions pour une ville donnée")
async def last_transactions(city: str = Path(description="Ville"),
                            number: int = Path(description="Nombre de transactions à afficher")):
    query = f"SELECT * FROM transactions_sample ts WHERE ville LIKE '{city.upper()}%' ORDER BY date_transaction DESC LIMIT {number}"
    return execute_sql(con, query)


# User story 3
@app.get("/transactions_count/{city}_{year}", description="Renvoie le nombre de transactions pour une ville et une année donnés")
async def transactions_count(city: str = Path(description="Ville"),
                             year: str = Path(description="Année")):
    year = validate_year(year)
    query = f"SELECT COUNT(*) as nb_transactions FROM transactions_sample ts WHERE ville LIKE '{city.upper()}%' AND date_transaction LIKE '{year}%'"
    return execute_sql(con, query)


# User story 4
@app.get("/average_price_per_square_meter/{year}_{type}", description="Renvoie le prix moyen par m2 pour une année et un type de biens donnés")
async def average_price_per_square_meter(type: str = Path(description="Type de biens"),
                        year: str = Path(description="Année")):
    year = validate_year(year)
    query = f"SELECT AVG(prix/surface_habitable) as prix_m2_moyen FROM transactions_sample ts WHERE type_batiment = '{type.capitalize()}' AND date_transaction LIKE '{year}%'"
    return execute_sql(con, query)


# User story 5
@app.get("/transactions_count2/{city}_{year}_{type}_{rooms}", description="Renvoie le nombre de transactions pour une ville, une année, un type de biens et un nombre de pièces donnés")
async def transactions_count2(city: str = Path(description="Ville"),
                              type: str = Path(description="Type de biens"),
                              year: str = Path(description="Année"),
                              rooms: int = Path(description="Nombre de pièces")):
    year = validate_year(year)
    query = f"SELECT COUNT(*) as nb_transactions FROM transactions_sample ts WHERE type_batiment = '{type.capitalize()}' AND n_pieces = {rooms} AND ville LIKE '{city.upper()}%' AND date_transaction LIKE '{year}%'"
    return execute_sql(con, query)


# User story 6
@app.get("/transactions_by_pieces/{city}_{year}_{type}", description="Renvoie la répartition des transactions en fonction du nombre de pièces, pour une ville, une année et un type de biens donnés")
async def transactions_by_pieces(city: str = Path(description="Ville"),
                      year: str = Path(description="Année"),
                      type: str = Path(description="Type de biens")):
    year = validate_year(year)
    query = f"SELECT n_pieces, COUNT(*) as nb_transactions FROM transactions_sample ts WHERE type_batiment = '{type.capitalize()}' AND ville LIKE '{city.upper()}%' AND date_transaction LIKE '{year}%' GROUP BY n_pieces"
    return execute_sql(con, query)


# User story 7                                                                                                                                                                                                   
@app.get("/average_price_per_square_meter2/{city}_{year}_{type}", description="Renvoie le prix moyen par m2 pour une ville, une année et un type de biens donnés")
async def average_price_per_square_meter2(city: str = Path(description="Ville"),
                          year: str = Path(description="Année"),
                          type: str = Path(description="Type de biens")):
    year = validate_year(year)
    query = f"SELECT AVG(prix/surface_habitable) as prix_m2_moyen FROM transactions_sample ts WHERE type_batiment = '{type.capitalize()}' AND ville LIKE '{city.upper()}%' AND date_transaction LIKE '{year}%'"
    return execute_sql(con, query)


# User story 8
@app.get("/transactions_by_dpt/", description="Renvoie le classement des départements en fonction du nombre de transactions réalisées")
async def transactions_by_dpt():
    query = f"SELECT departement, COUNT(*) as nb_transactions FROM transactions_sample ts GROUP BY departement ORDER BY nb_transactions DESC"
    return execute_sql(con, query)


# User story 9
@app.get("/transactions_count3/{year1}_{revenu}_{year2}_{type}", description="Renvoie le nombre total de ventes d'un type de biens à une année donnée, pour les villes ayant un revenu fiscal moyen supérieur à la valeur renseignée au cours de l'année choisie")
async def transactions_count3(year1: str = Path(description="Année concernant le revenu fiscal moyen"),
                              revenu: int = Path(description="Revenu fiscal moyen minimum"),
                              year2: str = Path(description="Année concernant le nombre de ventes"),
                              type: str = Path(description="Type de biens")):
    query = f"SELECT COUNT(*) as nb_transactions FROM transactions_sample ts JOIN foyers_fiscaux ff ON ts.ville = UPPER(ff.ville) WHERE ff.date LIKE '{year1}%' AND ff.revenu_fiscal_moyen > {revenu} AND ts.date_transaction LIKE '{year2}%' AND type_batiment = '{type}'"
    return execute_sql(con, query)


# User story 10
@app.get("/cities_top10_transactions/", description="Renvoie les 10 villes avec le plus de transactions immobilières recensées")
async def cities_top10():
    query = f"SELECT ville, COUNT(*) as nb_transactions FROM transactions_sample ts GROUP BY ville ORDER BY COUNT(*) DESC LIMIT 10"
    return execute_sql(con, query)


# User stories 11 & 12
@app.get("/cities_top10_price/{type}", description="Renvoie les 10 villes avec le prix moyen au m2 le plus attractif pour un type de biens donné")
async def cities_top10_price(type: str = Path(description="Type de biens")):
    query = f"SELECT ville, AVG(prix/surface_habitable) as prix_m2_moyen FROM transactions_sample ts WHERE type_batiment = '{type.capitalize()}' GROUP BY ville ORDER BY prix_m2_moyen ASC LIMIT 10"
    return execute_sql(con, query)



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)