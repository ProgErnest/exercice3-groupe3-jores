from openfoodfacts import API,Environment
import json
import pathlib
BASE_URL = pathlib.Path(__file__).parent.parent
JSON_DESTINATION = BASE_URL / "web" / "data" / "product.json"
api = API(
    user_agent="Foods",
    environment=Environment.org
)

codes = ["3068320055008","5449000000996","3017620422003","8076809513739"]
datas = {}
try:
    # product = api.product.get(code, fields=["product_name", "brands", "categories", "nutriments"])
    # print(product)
    i=0
    for code in codes:
        product_data = api.product.get(code, fields=["code", "product_name","brands", "image_url", "ingredients_text", "categories_tags"])
        print(product_data)
        datas[i] = product_data
        i += 1

    with open(JSON_DESTINATION, "w") as f:
        json.dump(datas, f, indent=4)
except Exception as e:
    print(f"An error occurred: {e}")