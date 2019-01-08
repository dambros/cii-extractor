import logging.config
import os
import shutil
import sys
from datetime import datetime
from enum import Enum

import ciop
import config
import dh
import utils

Report = Enum('Report', 'ciop dh')


def main():
    if shutil.which('textract') is None:
        sys.exit('Textract is missing!')

    dh_metadata = get_metadata(config.DH_FOLDER_PATH, Report.dh)
    ciop_metadata = get_metadata(config.CIOP_FOLDER_PATH, Report.ciop)

    utils.write_xml(dh_metadata)
    utils.write_xml(ciop_metadata)

    if config.SUMMARY_FOLDER_PATH:
        dh_summary_path = f'{config.SUMMARY_FOLDER_PATH}/dh_summary.csv'
        utils.write_csv(dh_summary_path, dh_metadata, dh_metadata[0].keys())
        ciop_summary_path = f'{config.SUMMARY_FOLDER_PATH}/ciop_summary.csv'
        utils.write_csv(ciop_summary_path, ciop_metadata,
                        ciop_metadata[0].keys())


def get_metadata(folder_path, file_type):
    if file_type == Report.ciop:
        report_type = ciop
    else:
        report_type = dh

    files = report_type.get_files(folder_path)

    metadata = []
    for file in files:
        try:
            metadata.append(report_type.extract_info(file))
        except Exception:
            logger.error(file)

    return metadata


if __name__ == "__main__":
    logging.config.fileConfig(config.LOG_CONFIG_PATH)
    logger = logging.getLogger(os.path.basename(__file__))
    startTime = datetime.now()
    main()
    logger.info(f'Script finalizado em {datetime.now() - startTime}')
