# %% Imports
import geopandas as gpd
from conf import BBOX, CATCHMENT_INFO_PROCESSED_DIR, RAW_DATA_DIR
from loguru import logger
from shapely.geometry import box


def main():
    CATCHMENT_INFO_PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    # %% Read in
    gdf_afstroomgebied = gpd.read_file(
        RAW_DATA_DIR / "afstroomgebied" / "afstroomgebied.shp"
    )
    gdf_vha = gpd.read_file(RAW_DATA_DIR / "vlaamse_hydrografische_atlas" / "VHA.shp")

    gdf_dict = {
        "afstroomgebied": gdf_afstroomgebied,
        "vlaamse_hydrografische_atlas": gdf_vha,
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
        out_path = CATCHMENT_INFO_PROCESSED_DIR / f"{name}.shp"
        logger.info(f"Saving {name} data to {out_path}")
        gdf.to_file(out_path)


if __name__ == "__main__":
    main()
