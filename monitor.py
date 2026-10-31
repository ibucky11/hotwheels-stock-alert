import json
from pathlib import Path

from matcher import match_product

CONFIG_FILE = Path("products.json")


def load_catalogue():
    if not CONFIG_FILE.exists():
        raise FileNotFoundError("products.json was not found")

    with CONFIG_FILE.open("r", encoding="utf-8") as file:
        return json.load(file)


def test_product_matcher():
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
        },
        {
            "title": "Matchbox Sports Car",
            "brand": "Matchbox"
        }
    ]

    print("\nPRODUCT MATCHER TEST")
    print("--------------------")

    for product in samples:
        result = match_product(product)
        print(product["title"], "->", result)


def main():
    try:
        config = load_catalogue()

        print("HOT WHEELS STOCK MONITOR")
        print("------------------------")

        print("Catalogue:", config["catalogue"]["scope"])
        print(
            "All licensed real vehicles:",
            config["catalogue"]["include_all_licensed_real_vehicles"]
        )
        print("Mainlines:", config["catalogue"]["include_mainlines"])
        print("Premium:", config["catalogue"]["include_premium"])
        print(
            "Special editions:",
            config["catalogue"]["include_special_editions"]
        )
        print(
            "Exclude fantasy castings:",
            config["exclude"]["fantasy_castings"]
        )

        test_product_matcher()

        print("\nCatalogue configuration loaded successfully.")
        print("Matcher tests completed.")
        print("Platform stock monitoring is not connected yet.")

    except (FileNotFoundError, json.JSONDecodeError, KeyError) as error:
        print("Configuration error:", error)


if __name__ == "__main__":
    main()
