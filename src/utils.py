from fastapi import HTTPException


# Checks that the year input is a 4 figures number
def validate_year(year: str):
    if not year.isdigit() or not (len(year) == 4):
        raise HTTPException(
            status_code=400,
            detail="Year input invalid, must be a 4 figures long number.",
        )

    return year
