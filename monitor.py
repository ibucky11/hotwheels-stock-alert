import json
from pathlib import Path


CONFIG_FILE = Path("products.json")


def load_catalogue():
    if not CONFIG_FILE.exists():
        raise FileNotFoundError("products.json was not found")

    with CONFIG_FILE.open("r", encoding="utf-8") as file:
        config = json.load(file)

    return config


def show_catalogue(config):
    catalogue = config["catalogue"]
    excluded = config["exclude"]
    notifications = config["notifications"]

    print("HOT WHEELS STOCK MONITOR")
    print("------------------------")

    print("Catalogue:", catalogue["scope"])
    print("All licensed real vehicles:",
          catalogue["include_all_licensed_real_vehicles"])

    print("Mainlines:", catalogue["include_mainlines"])
    print("Premium:", catalogue["include_premium"])
    print("Special editions:", catalogue["include_special_editions"])

    print("Exclude fantasy castings:",
          excluded["fantasy_castings"])

    print("New product alerts:",
          notifications["new_products"])

    print("In-stock alerts:",
          notifications["in_stock"])


def main():
    try:
        config = load_catalogue()
        show_catalogue(config)

        print("\nCatalogue configuration loaded successfully.")
        print("Platform stock monitoring is not connected yet.")

    except (FileNotFoundError, json.JSONDecodeError, KeyError) as error:
        print("Configuration error:", error)


if __name__ == "__main__":
    main()
