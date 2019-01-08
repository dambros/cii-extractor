import glob
import re

import textract

import utils

ENCODING = 'utf-8'
DATA_PATTERN = r'Data\/Hora:\s(.*?)Ocorrência'
ENDERECO_PATTERN = r'Endereço.*?((CIOP)|\d{9,11})(.*?)Tipo'
NUM_OCORRENCIA_PATTERN = r'Endereço:\s([A-Z]\d+)'


def extract_info(file_path):
    text = textract.process(file_path, encoding=ENCODING)
    text = text.decode(ENCODING, 'ignore')
    text = re.sub('\s+|\n', ' ', text)

    ciop = {
        'path': file_path,
        'data': utils.match_regex(DATA_PATTERN, text),
        'endereco': utils.match_regex(ENDERECO_PATTERN, text, tuple_pos=2),
        'num_ocorrencia': utils.match_regex(NUM_OCORRENCIA_PATTERN, text)
    }

    return ciop


def get_files(folder_path):
    path = f'{folder_path}/**/*.pdf'
    files = glob.glob(path, recursive=True)
    return files
