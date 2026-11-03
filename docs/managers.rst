Managers & Querysets
====================

Using a Custom Manager
----------------------

A nice feature of Django is the possibility to define one's own custom object managers.
This is fully supported with :pypi:`django-polymorphic`.

.. literalinclude:: ../src/polymorphic/tests/examples/managers/models.py
   :caption: src/polymorphic/tests/examples/managers/models.py (custom manager)
   :language: python
   :pyobject: TimeOrderedManager
   :linenos:

.. literalinclude:: ../src/polymorphic/tests/examples/managers/models.py
   :caption: src/polymorphic/tests/examples/managers/models.py (polymorphic models + manager)
   :language: python
   :lines: 14-24
   :linenos:

Manager Inheritance
-------------------

Polymorphic models inherit/propagate all managers from their base models, as long as these are
polymorphic.

.. literalinclude:: ../src/polymorphic/tests/examples/managers/tests.py
   :caption: src/polymorphic/tests/examples/managers/tests.py (manager inheritance behavior)
   :language: python
   :pyobject: ManagerExamplesTests.test_custom_manager_and_inheritance
   :linenos:

Using a Custom Queryset Class
-----------------------------

.. literalinclude:: ../src/polymorphic/tests/examples/managers/models.py
   :caption: src/polymorphic/tests/examples/managers/models.py (from_queryset pattern)
   :language: python
   :lines: 27-34
   :linenos:

.. literalinclude:: ../src/polymorphic/tests/examples/managers/models.py
   :caption: src/polymorphic/tests/examples/managers/models.py (as_manager pattern)
   :language: python
   :pyobject: MyOtherModel
   :linenos:

.. literalinclude:: ../src/polymorphic/tests/examples/managers/tests.py
   :caption: src/polymorphic/tests/examples/managers/tests.py (queryset manager verification)
   :language: python
   :pyobject: ManagerExamplesTests.test_custom_queryset_manager_patterns
   :linenos:
