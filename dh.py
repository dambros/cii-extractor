import glob
import re

import textract

import utils

ENCODING = 'utf-8'
FILENAME_PATTERN = r'^.*Relat[oó]rio\s\d+.*\.(doc|docx)$'
NUM_RELATORIO_PATTERN = r'RELATÓRIO\sNº\s(\d+\/\d+)'
DATA_PATTERN = r'(\d{1,2}\/\d{1,2}\/\d{1,2})'
HORARIO_ACIONAMENTO_PATTERN = r'(\d{1,2}hs?\d{1,2}m?i?n?s?|\d{1,2}:\d{1,2}:?\d{1,2})'
ENDERECO_PATTERN = r'Endereço do fato:\s(\(.*?\))?(.*?)Circunscrição Policial'
COLETAS_VESTIGIOS_PATTERN = r'Vest[ií]gios.*apreendidos\?\s(\(.*?\))(.*?)Objetos.*criminosa'
ARMAS_PATTERN = r'Tipos\sde\s\s(.*?)Armas:'
VEICULOS_PATTERN = r'Armas:\s+Ve[ií]culo(.*?)s:'


def extract_info(file_path):
    text = textract.process(file_path, encoding=ENCODING)
    text = text.decode(ENCODING, 'ignore')
    text = re.sub('\s+|\n|\|', ' ', text)

    dh = {
        'path': file_path,
        'num_relatorio': utils.match_regex(NUM_RELATORIO_PATTERN, text),
        'data_acionamento': utils.match_regex(DATA_PATTERN, text),
        'horario_acionamento': utils.match_regex(HORARIO_ACIONAMENTO_PATTERN,
                                                 text),
        'horario_chegada': utils.match_regex(HORARIO_ACIONAMENTO_PATTERN,
                                             text, 1),
        'endereco': utils.match_regex(ENDERECO_PATTERN, text, tuple_pos=1),
        'coletas_vestigios': utils.match_regex(COLETAS_VESTIGIOS_PATTERN,
                                               text,
                                               tuple_pos=1),
        'armas': utils.match_regex(ARMAS_PATTERN, text),
        'veiculos': utils.match_regex(VEICULOS_PATTERN, text)
    }

    return dh


def get_files(folder_path):
    path = f'{folder_path}/**/*'
    files = glob.glob(path, recursive=True)
    r = re.compile(FILENAME_PATTERN)
    relevant_files = []
    for file in files:
        match = r.match(file)
        if match:
            relevant_files.append(match.group())
    return relevant_files
