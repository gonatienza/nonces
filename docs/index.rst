Nonces
=====================

.. currentmodule:: nonces

Nonces is a module to generate nonces for cryptographic purposes.

Te module contains two main classes: :class:`nonces.Nonce` and
:class:`nonces.Nonces`.


Example of random `Nonce`.
--------------------------

.. code-block::

    from nonces import Nonce

    # This will generate a random one-time 24 bytes nonce
    nonce = Nonce.random(24)


Example of `Nonces` with counter.
---------------------------------

.. code-block::

   from nonces import Nonces

   # This will initiate an 8 bytes nonce with a 4 bytes counter
   nonces = Nonces(size=8, counter_size=4)

   # By default the counter is big endian with a random seed
   # and the counter trailing at the end of the full nonce bytes

   # Get the current nonce
   nonce = nonces.nonce

   print(nonce)

   # Update the current counter
   nonce = nonces.update()

   print(nonce)

We can update the counter:

.. code-block::

   nonce = nonces.set_counter(10)

   print(nonce)

   # Get the counter value
   print(nonces.counter)

   # Get the counter value in bytes
   nonces.counter_bytes

If we run out of nonces an OverFlowError exception will be triggered  

.. code-block::

   nonces.set_counter(nonces.max_counter)
   nonces.update()

We can also use a specific seed:

.. code-block::

   # We can create a new object with the seed and change the byte order
   # to little endian and a non-trailing counter (i.e, counter + nonce)

   seed = b"\xff" * 4
   nonces = Nonces(
      size=8,
      counter_size=4,
      seed=seed,
      order='little',
      trailing_counter=False
   )
   for i in range(10):
      nonces.update()

   b'\x01\x00\x00\x00\xff\xff\xff\xff'
   b'\x02\x00\x00\x00\xff\xff\xff\xff'
   b'\x03\x00\x00\x00\xff\xff\xff\xff'
   b'\x04\x00\x00\x00\xff\xff\xff\xff'
   b'\x05\x00\x00\x00\xff\xff\xff\xff'
   b'\x06\x00\x00\x00\xff\xff\xff\xff'
   b'\x07\x00\x00\x00\xff\xff\xff\xff'
   b'\x08\x00\x00\x00\xff\xff\xff\xff'
   b'\t\x00\x00\x00\xff\xff\xff\xff'
   b'\n\x00\x00\x00\xff\xff\xff\xff'

   assert nonces.seed_bytes == seed

We can also set the increment value:

.. code-block::

   nonces = Nonces(size=8, counter_size=4, seed=seed)

   nonces.increment = 255

   for i in range(10):
      nonces.update()

   b'\xff\xff\xff\xff\x00\x00\x00\xff'
   b'\xff\xff\xff\xff\x00\x00\x01\xfe'
   b'\xff\xff\xff\xff\x00\x00\x02\xfd'
   b'\xff\xff\xff\xff\x00\x00\x03\xfc'
   b'\xff\xff\xff\xff\x00\x00\x04\xfb'
   b'\xff\xff\xff\xff\x00\x00\x05\xfa'
   b'\xff\xff\xff\xff\x00\x00\x06\xf9'
   b'\xff\xff\xff\xff\x00\x00\x07\xf8'
   b'\xff\xff\xff\xff\x00\x00\x08\xf7'
   b'\xff\xff\xff\xff\x00\x00\t\xf6'

We can leverage bytes encoding options:

.. code-block::

   nonces = Nonces(size=8, counter_size=4)

   nonce = nonces.nonce

   nonce_hex = nonce.hex()

   new_nonce = Nonce.fromhex(nonce_hex)

   assert nonce == new_nonce


Reference
---------

.. class:: Nonce(bytes)
   
   Each unique nonce value is an instantiated
      object of this bytes subclass.

   .. method:: from_bytes(nonce)
      
      Load a unique nonce value.

      :param nonce: nonce bytes.
      :return: Nonce object.

   .. method:: random(size)
      
      Get random Nonce from a size.

      :param size: size of the nonce.
      :return: Nonce object.

.. class:: Nonces(size, counter_size, seed, order, trailing_counter)

   Nonces generator based on:
      - A given size.
      - A counter size.
      - An optional seed.
      - An optional byte order for the counter.
      - An optional trailing position argument for the counter.

   All nonces generated will use a counter.

   :param size: size of the full nonce (nonce + counter).
   :param counter_size: size of the counter.
   :param seed: seed to use for the non-counter portion of the nonce.
   :param order: byte order for the counter.
      "big" means big endian for the counter.
      "little" mean little endian for the counter.
   :param trailing_counter: trailing counter or not.
      True means nonce + counter
      False means counter + nonce

   .. method:: update()

      Update nonce value incrementing counter.

      :raises: OverflowError in case of counter overflow.
      :return: Current nonce.

   .. method:: set_counter(counter)

      Set counter to new value.

      :param counter: counter value.
      :raises: ValueError or AssertionError.
      :return: Current nonce.

   .. method:: counter_to_bytes()

      Get counter in bytes.

      :return: Counter bytes

   .. attribute:: counter_bytes

      :return: current nonce counter bytes.

   .. attribute:: seed_bytes

      :return: current nonce bytes without counter.

   .. attribute:: nonce

      :return: current nonce.

   .. attribute:: increment

      :return: current increment value.

   .. attribute:: order

      :return: current counter byte order.

   .. attribute:: counter

      :return: urrent counter value.

   .. attribute:: max_counter

      :return: max counter value.

   .. attribute:: size

      :return: full nonce size.

   .. attribute:: counter_size

      :return: counter size.

   .. attribute:: seed_size

      :return: nonce size without counter.
