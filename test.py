# -*- coding: utf-8 -
#

from config import Config
import logging
import satapi
from satapi import set_logging

if __name__ == '__main__':
    # configuramos nivel de log para libreria satapi
    set_logging('debug')

    # establecemos el mismo nivel de log para la ejecucion del script
    log = logging.getLogger('satapi')

    # leemos el fichero de configuracion
    conn = Config(file('config/connection.cfg'))

    # ejemplo de invocacion al metodo de busqueda de hosts
    log.info('Invocando al API')
    try:
        # consulta de hosts
        r = satapi.hosts(conn).search('caj10.c8834n.tnd.mercadona.es')
        result = r.body_string()
        log.debug(result)

        # consulta de hostgroups
        r = satapi.hosts(conn).search('qcc2016-20.96-caj-64')
        result = r.body_string()
        log.debug(result)
        log.info('Todo en orden')
    except Exception as e:
        # impresion del error
        log.debug('Exception: %s' % e)
        log.info('Algo ha ido mal')
