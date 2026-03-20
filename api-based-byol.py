import requests
import json

DATABRICKS_HOST = "https://<<>>.cloud.databricks.com"
TOKEN = '<<>>'

headers = {
    "Authorization": f"Bearer {TOKEN}"
}

url = f"{DATABRICKS_HOST}/api/2.0/lineage-tracking/external-metadata"

print(url)
payload = {
  "columns": [
    "BUS_DT",
    "STORE_NBR",
    "POS_SALES",
    "POS_QTY",
    "FTPR_NMRTR",
    "ON_HAND_QTY",
    "FTPR_DNMNTR"
  ],
  "description": "Data recieving from snowflake stream",
  "entity_type": "Table",
  "name": "byol_snowflake_api_1",
  "properties": {
    "compression.enabled": "true",
    "compression.format": "zstd",
    "topic": "prod.security.events.raw"
  },
  "system_type": "SNOWFLAKE",
  "url": "https://kmb71999.snowflakecomputing.com"
}
response = requests.post(url, headers=headers, json=payload)

print(response.status_code)
print(response.text)