# %% Imports
import geopandas as gpd
from conf import (
    AFSTROOMGEBIED_RAW_DIR,
    BBOX,
    CATCHMENT_INFO_PROCESSED_DIR,
    FILENAME_AFSTROOMGEBIED,
    FILENAME_VHA,
    VLAAMSE_HYDROGRAFISCHE_ATLAS_RAW_DIR,
)
from loguru import logger
from shapely.geometry import box


# %%
def main():
    CATCHMENT_INFO_PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    # %% Read in
    gdf_afstroomgebied = gpd.read_file(AFSTROOMGEBIED_RAW_DIR / FILENAME_AFSTROOMGEBIED)
    gdf_vha = gpd.read_file(VLAAMSE_HYDROGRAFISCHE_ATLAS_RAW_DIR / FILENAME_VHA)

    gdf_dict = {
        FILENAME_AFSTROOMGEBIED: gdf_afstroomgebied,
        FILENAME_VHA: gdf_vha,
    }
    # %% Check if bbox of interest is contained in bbox of the data
    bbox_interest = box(*BBOX)
    for name, gdf in gdf_dict.items():
        bbox_data = box(*gdf.total_bounds)
        if not bbox_data.contains(bbox_interest):
            raise ValueError(
                f"The bounding box of the {name} data does not contain the bounding box of interest."
            )
        else:
            logger.info(
                f"The bounding box of the {name} data contains the bounding box of interest."
            )
        out_path = CATCHMENT_INFO_PROCESSED_DIR / name
        logger.info(f"Saving {name} data to {out_path}")
        gdf.to_file(out_path)


if __name__ == "__main__":
    main()
