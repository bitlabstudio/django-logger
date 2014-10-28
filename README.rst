To be removed!
==============

This app is no longer maintained or developed and is soon to be removed.
It was merely a draft, but it turned out, that there are far too many better solutions for this problem.

For statistics we now use django-influxdb-metrics_ with grafana_.

.. _django-influxdb-metrics: https://github.com/bitmazk/django-influxdb-metrics
.. _grafana: http://grafana.org/

For logging certain events you might want to check out django-object-events_.

.. _django-object-events: https://github.com/bitmazk/django-object-events

Django Logger
=============

A Django application for logging events and saving them into your database so
that you can run computations and reports on them later.


Installation
------------

You need to install the following prerequisites in order to use this app::

    pip install Django

To install the latest commit from GitHub::

    $ pip install -e git://github.com/bitmazk/django-logger.git#egg=logger

Add ``logger`` to your ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        ...,
        'logger',
    )


Usage
-----
::

    from logger import Logger

    def my_function(args):
        # create a logger instance
        logger = Logger()

        # call the ``create_log`` method
        logger.create_log(
            'action_name', 'parameter_type_name', 'value')


The ``action`` argument of ``logger.create_log()`` is a string defining the
kind of action, that is logged. E.g. 'payment' 
You can see it as a way of grouping log items.

The ``parameter_type_name`` is either a string or a list of strings containing
the types of values stored. E.g. ['item count', 'payment amount', 'user']

Finally the ``value`` argument is a list of values or a single value that can
be either a string, an integer, a date or datetime, a decimal, a bool or a
django model instance. E.g. [12, decimal.Decimal('299.99'), request.user]

So the full call of ``create_log`` from the example would look like: ::
    
    logger.create_log(
        'payment',
        ['item count', 'payment amount', 'user'],
        [12, decimal.Decimal('299.99'), request.user],
    )

Currently the ``Log`` objects stored this way can be reviewed through the
django admin.


Contribute
----------

If you want to contribute to this project, please perform the following steps::

    # Fork this repository
    # Clone your fork
    $ mkvirtualenv -p python2.7 django-logger
    $ pip install -r requirements.txt
    $ ./logger/tests/runtests.sh
    # You should get no failing tests

    $ git co -b feature_branch master
    # Implement your feature and tests
    # Describe your change in the CHANGELOG.txt
    $ git add . && git commit
    $ git push origin feature_branch
    # Send us a pull request for your feature branch

Whenever you run the tests a coverage output will be generated in
``tests/coverage/index.html``. When adding new features, please make sure that
you keep the coverage at 100%.


Roadmap
-------

Check the issue tracker on github for milestones and features to come.
