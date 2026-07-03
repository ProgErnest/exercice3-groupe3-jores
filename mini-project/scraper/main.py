from openfoodfacts import API,Environment
import json
import pathlib
BASE_URL = pathlib.Path(__file__).parent.parent
JSON_DESTINATION = BASE_URL / "web" / "data" / "data.json"
api = API(
    user_agent="Nouveau projet nurtriments",
    environment=Environment.net
)

codes = ["3068320055008","5449000000996","3608580713883",
         "3033710065066","3560070048893","3155250001191","3021140003463"
         "3033490004552"]
tableau_codes = [
    "3017620422003","4008400120120", "3608580713883", 
    "3350030198750", "3155251205352", "8410076470014", "3046920022651", 
    "7622210449283", "7622210204424", "5000159461122", "5000159418546", 
    "3029944002054",
    "5449000000996", "3068320055008", "3124480184422", "5025301362947", 
    "3012993555715", "3124480186174", "5449002149111",
    "8076809513739", "3168930009071", "8715700114393", "5053990138722", 
    "3168930010879", "3082561001115", "3038359000483", "3021140003463", 
    "3250390151194", "3560070048893",
    "3228021010020", "3033490004552", "3073720221087", "7613034626844", 
    "3250390002144", "3155250001191", "3228022160021", "3033490084530", 
    "3222472600124", "3029940114058"
]
datas = {}
try:
    # product = api.product.get(code, fields=["product_name", "brands", "categories", "nutriments"])
    # print(product)
    i=0
    for code in tableau_codes:
        product_data = api.product.get(code, fields=["code", "product_name","brands", "image_url", "ingredients_text", "categories_tags"])
        print(product_data)
        datas[i] = product_data
        i += 1

    with open(JSON_DESTINATION, "w") as f:
        json.dump(datas, f, indent=4)
except Exception as e:
    print(f"An error occurred: {e}")