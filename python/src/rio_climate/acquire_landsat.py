
from pathlib import Path
import planetary_computer
from pystac_client import Client


# 1. Define our project paths
PROJECT_ROOT = Path(__file__).resolve().parents[3]
OUTPUT_DIR = PROJECT_ROOT / "data" / "raw" / "landsat"

# 2. Define our study area: Rio de Janeiro
# Format: west, south, east, north
RIO_BBOX = [-43.80, -23.10, -43.00, -22.70]


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # 3. Connect to the satellite catalogue
    catalog = Client.open(
        "https://planetarycomputer.microsoft.com/api/stac/v1",
        modifier=planetary_computer.sign_inplace,
    )

    # 4. Search for Landsat observations
    search = catalog.search(
        collections=["landsat-c2-l2"],
        bbox=RIO_BBOX,
        datetime="2024-01-01/2025-12-31",
        query={"eo:cloud_cover": {"lt": 20}},
        max_items=20,
    )

    items = list(search.items())

    if not items:
        print("No suitable satellite images found.")
        return

    # 5. Select the observation with the least cloud cover
    best_item = min(
        items,
        key=lambda item: item.properties["eo:cloud_cover"],
    )

    print("Selected satellite image:", best_item.id)
    print(
        "Cloud cover:",
        best_item.properties["eo:cloud_cover"],
        "%",
    )

    # 6. Find the red spectral band
    print("Available assets:", sorted(best_item.assets.keys()))

    red_band = best_item.assets["red"]

    # 7. Download the GeoTIFF
    output_file = OUTPUT_DIR / f"{best_item.id}_SR_B4.tif"

    import requests

    response = requests.get(red_band.href, timeout=120)
    response.raise_for_status()

    output_file.write_bytes(response.content)

    print("Download completed!")
    print("Saved to:", output_file)
    print("File size:", output_file.stat().st_size, "bytes")


if __name__ == "__main__":
    main()
