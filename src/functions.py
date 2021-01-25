# python imports
from logging import log
import os
from os.path import getsize
import shutil
import schedule
import time
from pathlib import Path
import concurrent.futures
import asyncio

# app imports
from settings import *


def get_file_extension():
    """
        Função que obtém a extensão do 
        arquivo submetido.

        return:
            extension -> extensão dos arquivos
            não processados
    """
    
    try:
        extension = ''
        lst = [os.path.splitext(x)[1] for x in files_inside_directory]
        my_final_list = dict.fromkeys(lst)
        for ext in list(my_final_list):
            extension += ext
        return extension
    except Exception as error:
        logger.warning(error)


def get_filenames():
    """
        Função que obtém o nome do 
        arquivo submetido.

        return:
            filename -> nome dos arquivos
            não processados
    """

    try:
        filename = ''
        lst = [os.path.splitext(x)[0] for x in files_inside_directory]
        my_final_list = dict.fromkeys(lst)
        for ext in list(my_final_list):
            filename += ext
        return filename
    except Exception as error:
        logger.warning(error)


def move_files_to_processed_folder(file: object):
    """
        Essa função lê a pasta de uploads
        e envia os arquivos não processados
        para as respectivas pastas.
    """
    files = os.listdir(str(unprocessed_files))
    source = str(default_directory) + '/app/unprocessed_files/' 
    if len(os.listdir(source)) == 0:
        logger.info(f"Directory {source} is empty.")
        pass
    else:    
        try:
            for file in files:
                with concurrent.futures.ProcessPoolExecutor() as executor:
                    loop.run_in_executor(executor, shutil.move(
                        os.path.join(source, file), 
                        processed_files
                    ))
            logger.info(f"Files moved to folder {processed_files}.")
        except Exception as error:
            logger.error(error)


def file_size_verifier():
    """
        Função que verifica os tamanho dos
        arquivos, com base nos limites 
        permitidos.
    """

    root_directory = Path(str(default_directory) + '/app/unprocessed_files/')
    try:
        if len(os.listdir(str(unprocessed_files))) == 0:
            logger.info(f"Directory is empty.")
            pass
        else: 
            size = [f.stat().st_size for f in root_directory.glob('**/*') if f.is_file()]
            for s in size:
                if s > max_size_files:
                    logger.info('Arquivo maior que 500mb. O mesmo não será processado')
                else:
                    logger.info(f'Tamanho do arquivo ({s} bytes) aceitavel, o mesmo sera processado.')
    except Exception as error:
        logger.error(error)


def rename_file_and_validate(start_path = str(default_directory) + '/app/unprocessed_files/'):
    """
        Renomeando os arquivos validados antes de
        transferi-los para a pasta PROCESSED_FILES
    """
    
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            new_name_file = f'processed-{f}'
            try:
                old_file, new_file = os.rename(f'{start_path}{f}', f'{processed_files}/{new_name_file}')
                logger.info('Arquivo renomeado!')
                print(new_file)
            except Exception as error:
                logger.error(error)


def main():
    """
        Função de agrupamento
    """

    rename_file_and_validate()
        

if __name__ == "__main__":
    main()

