About
-----

SatAPI is an REST client wrapper to interact with `Red Hat Satellite 6 <https://www.redhat.com/es/technologies/management/satellite>` REST API.

This module is an initial version of a previous one. Moving from the `previous version <http://github.com/soukron/satapi>` is an ongoing work.


Installation
------------

SatAPI requires Python 2.x superior to 2.6 due to Restkit dependency (Python 3 support is coming soon according to them)

To install SatAPI using pip you must make sure you have a
recent version of distribute installed::

    $ curl -O http://python-distribute.org/distribute_setup.py
    $ sudo python distribute_setup.py
    $ easy_install satapi


To install from source, run the following command::

    $ git clone https://github.com/soukron/satapi2.git
    $ cd satapi2
    $ pip install -r requirements.txt
    $ python setup.py install

From pypi::

    $ pip install satapi


License
-------

SatAPI is available under the GPLv3 license.
