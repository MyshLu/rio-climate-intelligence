from pathlib import Path
import rasterio

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
print(f"CRS: {raster_res}")
print(f"Resolution: {raster_res}")
    
    
#open a raster file and print:
#1. Its width and height.
#2. Its number of bands.
#3. Its CRS.
#4. Its pixel resolution.
#A useful hint: rasterio.open() returns a dataset object. That object has properties such as .width, .height, .count, .crs and .res.

#One important detail: use with rasterio.open(...) as dataset: