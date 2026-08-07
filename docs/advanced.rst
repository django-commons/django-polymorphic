.. _advanced-features:

Advanced Features
=================

In the examples below, these models are being used:

.. literalinclude:: ../src/polymorphic/tests/examples/advanced/models.py
   :caption: src/polymorphic/tests/examples/advanced/models.py
   :language: python
   :lines: 1-17
   :linenos:

Filtering for classes (equivalent to python's :func:`isinstance`)
------------------------------------------------------------------

.. literalinclude:: ../src/polymorphic/tests/examples/advanced/tests.py
   :caption: src/polymorphic/tests/examples/advanced/tests.py (instance_of + Q)
   :language: python
   :pyobject: AdvancedExamplesTests.test_instance_of_and_q
   :linenos:

In general, including or excluding parts of the inheritance tree:

* ``ModelA.objects.instance_of(ModelB [, ModelC ...])``
* ``ModelA.objects.not_instance_of(ModelB [, ModelC ...])``

Polymorphic filtering (for fields in inherited classes)
-------------------------------------------------------

For example, cherry-picking objects from multiple derived classes anywhere in the inheritance tree,
using Q objects with syntax ``exact model name + three underscores + field name``:

.. literalinclude:: ../src/polymorphic/tests/examples/advanced/tests.py
   :caption: src/polymorphic/tests/examples/advanced/tests.py (field filtering)
   :language: python
   :pyobject: AdvancedExamplesTests.test_polymorphic_field_filtering
   :linenos:

Combining Querysets
-------------------

Querysets can be treated as object containers and combined using ``|`` as long as objects are
accessed through managers of a common polymorphic base class. This allows aggregation of different
subtypes while keeping the concrete model instances.

ManyToManyField, ForeignKey, OneToOneField
------------------------------------------

Relationship fields referring to polymorphic models work as expected and return concrete subclass
instances.

.. literalinclude:: ../src/polymorphic/tests/examples/advanced/models.py
   :caption: src/polymorphic/tests/examples/advanced/models.py (many-to-many model)
   :language: python
   :pyobject: RelatingModel
   :linenos:

.. literalinclude:: ../src/polymorphic/tests/examples/advanced/tests.py
   :caption: src/polymorphic/tests/examples/advanced/tests.py (many-to-many polymorphic results)
   :language: python
   :pyobject: AdvancedExamplesTests.test_many_to_many_returns_real_instances
   :linenos:

Copying Polymorphic objects
---------------------------

Copying polymorphic models is the same as copying regular multi-table models. The
:func:`~polymorphic.utils.prepare_for_copy` helper resets all required parent pointers and PK
fields before ``save()``.

.. literalinclude:: ../src/polymorphic/tests/examples/advanced/tests.py
   :caption: src/polymorphic/tests/examples/advanced/tests.py (copy + non_polymorphic behavior)
   :language: python
   :pyobject: AdvancedExamplesTests.test_copy_and_non_polymorphic
   :linenos:

Working with Fixtures
---------------------

Polymorphic models work with :django-admin:`dumpdata` and :django-admin:`loaddata`, but the same
multi-table inheritance caveats still apply:

1. Dumping only a subset of tables in an inheritance tree can produce incomplete or upcasted data.
2. ``polymorphic_ctype`` references depend on ``ContentType`` records and must remain valid between
   source and target databases.

When content type references drift, use
:func:`~polymorphic.utils.reset_polymorphic_ctype` across the full inheritance tree.

Using Third Party Models (without modifying them)
-------------------------------------------------

Third-party models can participate in polymorphic inheritance by subclassing them. You can place a
third-party base model at the root of a polymorphic tree or mix it into an existing polymorphic
branch where multiple inheritance is supported by Django model constraints.

Non-Polymorphic Queries
-----------------------

If you insert :meth:`~polymorphic.managers.PolymorphicQuerySet.non_polymorphic` anywhere into the
query chain, django-polymorphic returns base instances until you call
:meth:`~polymorphic.managers.PolymorphicQuerySet.get_real_instances`.

Restrictions & Caveats
----------------------

* Database performance considerations for concrete model inheritance still apply.
* ``values()``, ``values_list()``, and ``select_related()`` remain partially limited in polymorphic
  contexts.
* ``extra()`` still requires unique base primary keys in the result set.
* Enhanced filter definitions / polymorphic Q-object semantics work through polymorphic queryset
  APIs.
* When dumping data across environments that may differ in ``ContentType`` primary keys, use
  :option:`--natural-foreign <dumpdata.--natural-foreign>`.
