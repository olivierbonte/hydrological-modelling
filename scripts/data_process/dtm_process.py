import rioxarray
from conf import (
    DATASET_DTM,
    DTM_PROCESSED_DIR,
    DTM_RAW_DIR,
    DTM_SPATIAL_RESOLUTION,
    DTM_SPATIAL_RESOLUTION_UPSCALED,
)

DTM_PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
da = rioxarray.open_rasterio(DTM_RAW_DIR / f"{DATASET_DTM}.tif")
upscale_factor = DTM_SPATIAL_RESOLUTION_UPSCALED / DTM_SPATIAL_RESOLUTION
if not upscale_factor.is_integer():
    raise ValueError(
        "Upscale factor must be an integer. Please check the spatial resolutions."
    )
upscale_factor = int(upscale_factor)
da_coarsened = da.coarsen(x=upscale_factor, y=upscale_factor, boundary="trim").mean()
output_file = (
    DTM_PROCESSED_DIR / f"{DATASET_DTM}_upscaled_{DTM_SPATIAL_RESOLUTION_UPSCALED}m.tif"
)
da_coarsened.rio.to_raster(output_file)
print(f"Upscaled DTM saved to: {output_file}")
