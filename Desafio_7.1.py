import logging
from unittest import result

logging.basicConfig(filename="arquivo_log.kill",
                    level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def contar_passaros(a,b):
    logging.info(f"A função foi chamada pelo usuário com os valores {a} e {b}")
    try:
        resultado = a-b
        logging.info(f"O resultado é {resultado}")
    except ZeroDivisionError:
        logging.error(f"Erro ao dar negativo")
        resultado < 0

contar_passaros(10,11)
