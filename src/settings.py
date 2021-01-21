import pathlib
import logging
import logging.config
import os
from os import listdir
from os.path import isfile, join


# Pegando o diretorio raiz do projeto
default_directory = pathlib.Path(__file__).parent.absolute()

# Arquivos a serem processados
# 'WindowsPath' Necessita que o agregamento seja por strings
unprocessed_files = str(default_directory) + '/app/unprocessed_files/'
# Arquivos processados
processed_files = str(default_directory) + '/app/processed_files/'

# Obtendo uma lista dos arquivos dentro da pasta uploads
files_inside_directory = [f for f in listdir(unprocessed_files) if isfile(join(unprocessed_files, f))]

# Configuração do log de arquivo
logging.config.fileConfig('log_settings.ini')
logger = logging.getLogger()