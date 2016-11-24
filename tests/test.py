# -*- coding: utf-8 -
#
# This file is part of SatAPI released under the GPLv3 license.

from config import Config
import logging
import satapi
from satapi import set_logging

def main():
    # set logging level and get logger
    set_logging('debug')
    log = logging.getLogger('satapi')

    # read connection details
    conn = Config(file('connection.cfg'))

    # sample code to search hosts
    log.info('Looking for hosts')
    try:
        r = satapi.hosts(conn).search()
        result = r.body_string()
        log.debug(result)
    except Exception as e:
        log.info('Exception: %s' % e)

if __name__ == '__main__':
    main()
