"""
KAPASITA
Data Inventory Agent

Tujuan:
- Scan seluruh dataset mentah
- Identifikasi file
- Simpan metadata dataset
"""

from pathlib import Path
import json
import pandas as pd


SUPPORTED_EXTENSIONS = [".csv", ".xlsx", ".xls"]


class DataInventory:

    def __init__(self, data_path: str):
        self.data_path = Path(data_path)

    def scan(self):

        inventory = []

        for file in self.data_path.rglob("*"):

            if file.suffix.lower() not in SUPPORTED_EXTENSIONS:
                continue

            try:

                metadata = {
                    "file_name": file.name,
                    "file_path": str(file),
                    "extension": file.suffix,
                    "size_mb": round(file.stat().st_size / 1024 / 1024, 2),
                }

                inventory.append(metadata)

            except Exception as e:

                inventory.append(
                    {
                        "file_name": file.name,
                        "error": str(e)
                    }
                )

        return inventory

    def save_inventory(self, output_path: str):

        inventory = self.scan()

        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(
                inventory,
                f,
                indent=4,
                ensure_ascii=False
            )

        print(
            f"[INFO] Inventory saved: {output_path}"
        )


if __name__ == "__main__":

    inventory = DataInventory(
        data_path="data/raw"
    )

    inventory.save_inventory(
        "data/mart/data_inventory.json"
    )