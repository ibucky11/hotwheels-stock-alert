import re


def is_hot_wheels_product(product):
    title = product.get("title", "").lower()
    brand = product.get("brand", "").lower()

    if "hot wheels" not in title and "hot wheels" not in brand:
        return False

    return True


def is_fantasy_casting(product):
    """
    Do not guess whether a casting is fantasy.
    Unknown models must be reviewed.
    """
    return product.get("casting_type") == "fantasy"


def match_product(product):
    if not is_hot_wheels_product(product):
        return "NOT_HOT_WHEELS"

    if is_fantasy_casting(product):
        return "EXCLUDED_FANTASY"

    if product.get("licensed_real_vehicle") is True:
        return "MATCH"

    return "NEEDS_REVIEW"


if __name__ == "__main__":
    samples = [
        {
            "title": "Hot Wheels Porsche 911 Carrera",
            "brand": "Hot Wheels",
            "licensed_real_vehicle": True
        },
        {
            "title": "Hot Wheels Fantasy Racer",
            "brand": "Hot Wheels",
            "casting_type": "fantasy"
        },
        {
            "title": "Hot Wheels Unknown Model",
            "brand": "Hot Wheels"
        }
    ]

    for product in samples:
        print(product["title"], "->", match_product(product))
