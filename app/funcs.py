import json, psycopg2, hvac, os

client = hvac.Client(url='http://127.0.0.1:8200', token=os.getenv("VAULT_TOKEN"))
read_response = client.secrets.kv.read_secret_version(
    mount_point="secret",
    path="config/pg_pass"
)

DB_PASS = read_response["data"]["data"]["password"]

def get_db():
    conn = psycopg2.connect(f"dbname=TaskManag_DB user=postgres password={DB_PASS}")
    return conn

file_json = "database.json"

def read_data():
    try:
        with open(file_json, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data(data):
    with open(file_json, "w") as file:
        json.dump(data, file, indent=4)
