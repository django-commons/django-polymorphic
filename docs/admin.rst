Admin Integration
=================

Of course, it's possible to register individual polymorphic models in the
:doc:`Django admin interface <django:ref/contrib/admin/index>`.

Setup
-----

Both the parent model and child model need to have a :class:`~django.contrib.admin.ModelAdmin`
class.

.. _admin-example:

Example
-------

.. literalinclude:: ../src/polymorphic/tests/examples/admin/models.py
   :caption: src/polymorphic/tests/examples/admin/models.py
   :language: python
   :lines: 1-20
   :linenos:

.. literalinclude:: ../src/polymorphic/tests/examples/admin/admin.py
   :caption: src/polymorphic/tests/examples/admin/admin.py (parent/child admin setup)
   :language: python
   :lines: 1-47
   :linenos:

Filtering child types
---------------------

Child model types can be filtered by adding a
:class:`~polymorphic.admin.PolymorphicChildModelFilter` to
:attr:`~django.contrib.admin.ModelAdmin.list_filter`.

Inline models
-------------

.. literalinclude:: ../src/polymorphic/tests/examples/admin/admin.py
   :caption: src/polymorphic/tests/examples/admin/admin.py (polymorphic inlines)
   :language: python
   :pyobject: PaymentInline
   :linenos:

Using polymorphic models in standard inlines
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. literalinclude:: ../src/polymorphic/tests/examples/admin/admin.py
   :caption: src/polymorphic/tests/examples/admin/admin.py (standard inline integration)
   :language: python
   :pyobject: ModelBInline
   :linenos:

.. literalinclude:: ../src/polymorphic/tests/examples/admin/admin.py
   :caption: src/polymorphic/tests/examples/admin/admin.py (standard model admin registration)
   :language: python
   :pyobject: StandardModelAdmin
   :linenos:

Verification
------------

.. literalinclude:: ../src/polymorphic/tests/examples/admin/tests.py
   :caption: src/polymorphic/tests/examples/admin/tests.py
   :language: python
   :pyobject: AdminExamplesTests
   :linenos:
