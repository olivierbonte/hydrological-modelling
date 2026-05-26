# Data downloads

Below some extra information on the downloaded datasets. Note that all configuration settings for the download (path names, variables...) are grouped in [`conf.py`](conf.py). 

## Digital Terrain Model (DTM)

Download file: [`dtm_download.py`](dtm_download.py)

The DTM used is *Digitaal Hoogtemodel Vlaanderen II, DTM, raster, 1 m*. For the full metadata, see [here](https://metadata.vlaanderen.be/srv/api/records/f52b1a13-86bc-4b64-8256-88cc0d1a8735?language=dut). The coordinate reference system is [Belgian Lambert 72](https://www.opengis.net/def/crs/EPSG/0/31370). Data is only requested via [OWSLib](https://github.com/geopython/OWSLib) for the region around the Zwalm catchment using the [WebCoverageService (WCS) provided by the Flemish Government](https://www.vlaanderen.be/datavindplaats/catalogus/wcs-digitaal-hoogtemodel-vlaanderen). Alternatively, one could (as of 22/05/2026) also download this dataset manually via [this url](https://download.vlaanderen.be/product/939-digitaal-hoogtemodel-vlaanderen-ii-dtm-raster-1-m). 


## Waterinfo

Download file: [`waterinfo_download.py`](waterinfo_download.py)

[Waterinfo](https://www.waterinfo.vlaanderen.be/) is primary Flemish source of hydrological data. For this exercise, all data is at a daily temporal resolution. Programmatic access is carried out using [pywaterinfo](https://github.com/fluves/pywaterinfo). Following variables are downloaded:

- Discharge: Daily average discharge [$\text{m}^3$/s] measured at Nederzwalm/Zwalmbeek (L06_342)
- Precipitation: Daily total precipitation [mm] 
    - Catchment rainfall (merging radar + pluviograph) for L06_342
    - Pluviograph rainfall from Maarke-Kerkem (P06_014)
- Potential evapotranspiration: Daily total potential evapotranspiration [mm] calculated with the Penman method at the meteorological station in Waregem (ME05_019)