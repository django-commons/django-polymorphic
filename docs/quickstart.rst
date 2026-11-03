Quickstart
===========

Install the project using::

    pip install django-polymorphic

Update the settings file:

.. code-block:: python

   INSTALLED_APPS = [
       # Required by django-polymorphic for polymorphic_ctype bookkeeping.
       "django.contrib.contenttypes",

       # Enable polymorphic model support.
       "polymorphic",
   ]

You can append these entries to an existing ``INSTALLED_APPS`` list in your project settings.

.. only:: html

    The current release of :pypi:`django-polymorphic` supports:

    .. image:: https://badge.fury.io/py/django-polymorphic.svg
        :target: https://pypi.python.org/pypi/django-polymorphic/
        :alt: PyPI version

    .. image:: https://img.shields.io/pypi/pyversions/django-polymorphic.svg
        :target: https://pypi.python.org/pypi/django-polymorphic/
        :alt: Supported Pythons

    .. image:: https://img.shields.io/pypi/djversions/django-polymorphic.svg
        :target: https://pypi.org/project/django-polymorphic/
        :alt: Supported Django


Making Your Models Polymorphic
------------------------------

Use :class:`~polymorphic.models.PolymorphicModel` instead of Django's
:class:`~django.db.models.Model`, like so:

.. literalinclude:: ../src/polymorphic/tests/examples/quickstart/models.py
   :caption: src/polymorphic/tests/examples/quickstart/models.py
   :language: python
   :linenos:

All models inheriting from your polymorphic models will be polymorphic as well.

Using Polymorphic Models
------------------------

Create objects and execute polymorphic queries exactly as documented:

.. literalinclude:: ../src/polymorphic/tests/examples/quickstart/tests.py
   :caption: src/polymorphic/tests/examples/quickstart/tests.py
   :language: python
   :pyobject: QuickstartExamplesTests
   :linenos:

This is basically all you need to know, as *django-polymorphic* mostly
works fully automatic and just delivers the expected results.

.. note::
    While :pypi:`django-polymorphic` makes subclassed models easy to use in Django,
    we still encourage to use them with caution. Each subclassed model will require
    Django to perform an ``INNER JOIN`` to fetch the model fields from the database.
    While taking this in mind, there are valid reasons for using subclassed models.
    That's what this library is designed for!
