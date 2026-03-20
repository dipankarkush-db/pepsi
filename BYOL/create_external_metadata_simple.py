"""
Simple script to create external metadata in Unity Catalog using the Databricks SDK.
"""

from databricks.sdk import WorkspaceClient
from databricks.sdk.service.catalog import ExternalMetadata, SystemType

w = WorkspaceClient(profile="azurefielddemo")

result = w.external_metadata.create_external_metadata(
    external_metadata=ExternalMetadata(
        name="byol_snowflake_sdk",
        description="Data recieving from snowflake stream",
        columns=[
            "BUS_DT",
            "STORE_NBR",
            "POS_SALES",
            "POS_QTY",
            "FTPR_NMRTR",
            "ON_HAND_QTY",
            "FTPR_DNMNTR",
        ],
        entity_type="Table",
        system_type=SystemType.SNOWFLAKE,
        url="https://kmb71999.snowflakecomputing.com",
        properties={
            "compression.enabled": "true",
            "compression.format": "zstd",
            "topic": "prod.security.events.raw",
        },
    )
)

print(f"Created external metadata: {result.name} (ID: {result.id})")
