from afstroomgebied_download import main as download_afstroomgebied
from conf import LOG_FORMAT, RAW_DATA_DIR, logger
from dtm_download import main as download_dtm
from vha_download import main as download_vha
from waterinfo_download import main as download_waterinfo

logger.info("Starting data download process")

if __name__ == "__main__":
    log_file = RAW_DATA_DIR / "data_download_{time}.log"
    logger.add(str(log_file), format=LOG_FORMAT, enqueue=True, mode="w")

    logger.info("Running dtm_download.py...")
    download_dtm()

    logger.info("Running waterinfo_download.py...")
    download_waterinfo()

    logger.info("Running vha_download.py...")
    download_vha()

    logger.info("Running afstroomgebied_download.py...")
    download_afstroomgebied()
