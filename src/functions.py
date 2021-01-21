# python imports
from logging import log
import os
import shutil
import schedule
import time

# app imports
from settings import *


def get_file_extension() -> str:
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


def get_filenames() -> str:
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


def move_files_to_processed_folder():
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
                shutil.move(
                    os.path.join(source, file), 
                    processed_files
                )
            logger.info(f"Files moved to folder {processed_files}.")
        except Exception as error:
            logger.error(error)


def main():
    """
        Função de agrupamento
    """
    get_file_extension()
    get_filenames()
    move_files_to_processed_folder()
        
    
if __name__ == "__main__":
    logger.info('Script started.')
    schedule.every(10).seconds.do(main)
    while True:
        schedule.run_pending()
        time.sleep(1)
        

