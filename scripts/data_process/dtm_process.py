import rioxarray
from conf import (
    DATASET_DTM,
    DTM_PROCESSED_DIR,
    DTM_RAW_DIR,
    DTM_SPATIAL_RESOLUTION,
    DTM_SPATIAL_RESOLUTION_UPSCALED,
    FILENAME_DTM,
)
from loguru import logger


def main():
    DTM_PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    logger.info(f"Processing DTM: {DATASET_DTM}")
    da = rioxarray.open_rasterio(DTM_RAW_DIR / FILENAME_DTM)
    upscale_factor = DTM_SPATIAL_RESOLUTION_UPSCALED / DTM_SPATIAL_RESOLUTION
    if not upscale_factor.is_integer():
        msg = "Upscale factor must be an integer. Please check the spatial resolutions."
        logger.error(msg)
        raise ValueError(msg)
    upscale_factor = int(upscale_factor)
    logger.info(f"Upscaling DTM with factor: {upscale_factor}")
    da_coarsened = da.coarsen(
        x=upscale_factor, y=upscale_factor, boundary="trim"
    ).mean()
    output_file = (
        DTM_PROCESSED_DIR
        / f"{DATASET_DTM}_upscaled_{int(DTM_SPATIAL_RESOLUTION_UPSCALED)}m.tif"
    )
    da_coarsened.rio.to_raster(output_file)
    logger.info(f"Upscaled DTM saved to: {output_file}")


if __name__ == "__main__":
    main()
