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


def get_file_extension(file: object) -> str:
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


def get_filenames(file: object) -> str:
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

#TODO: Terminar a função que verifica o tamanho do arquivo
def file_size_verifier():
    """
        Função que verifica os tamanho dos
        arquivos, com base nos limites 
        permitidos.
    """

    total_size = 0
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
                    move_files_to_processed_folder(s)
    except Exception as error:
        logger.error(error)


def main():
    """
        Função de agrupamento
    """
    file_size_verifier()    
        
    
#if __name__ == "__main__":
#    logger.info('Script started.')
#    schedule.every(10).seconds.do(main)
#    while True:
#        schedule.run_pending()
#        time.sleep(1)

if __name__ == "__main__":
    logger.info('Script started.')
    loop = asyncio.get_event_loop()
    loop.call_soon(main)
    loop.run_forever()
    #main()

