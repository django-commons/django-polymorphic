Formsets
========

.. versionadded:: 1.0

Polymorphic models can be used in formsets.

The implementation is almost identical to the regular Django :doc:`django:topics/forms/formsets`.
As extra parameter, the factory needs to know how to display the child models.

.. literalinclude:: ../src/polymorphic/tests/examples/formsets/tests.py
   :caption: src/polymorphic/tests/examples/formsets/tests.py (factory setup)
   :language: python
   :lines: 1-16
   :linenos:

The formset can be used just like all other formsets:

.. literalinclude:: ../src/polymorphic/tests/examples/formsets/tests.py
   :caption: src/polymorphic/tests/examples/formsets/tests.py (POST + save flow)
   :language: python
   :pyobject: FormsetsExamplesTests.test_formset_factory_and_save
   :linenos:

Like standard Django :doc:`django:topics/forms/formsets`, there are 3 factory methods available:

* :func:`~polymorphic.formsets.polymorphic_modelformset_factory` - create a regular model formset.
* :func:`~polymorphic.formsets.polymorphic_inlineformset_factory` - create a inline model formset.
* :func:`~polymorphic.formsets.generic_polymorphic_inlineformset_factory` - create an inline formset
  for a generic foreign key.
