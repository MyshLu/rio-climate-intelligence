from pathlib import Path
import rasterio
import pystac
import requests


def inspect_raster(file_path: Path) -> None:
    with rasterio.open(file_path) as file:
        raster_width = file.width
        raster_height = file.height
        raster_CRS = file.crs
        raster_res = file.res
        raster_bands = file.count  
        print(f"Width: {raster_width}")
        print(f"Height: {raster_height}")
        print(f"Bands: {raster_bands}")
        print(f"CRS: {raster_CRS}")
        print(f"Resolution: {raster_res}")