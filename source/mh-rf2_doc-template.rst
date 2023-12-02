.. sidebar shall be the very first element when used to allow proper placement

.. sidebar:: Source

  Source of the information and descriptions herein were extracted from
  "skipbarber_engine.ini" file of the SkipBarber that comes with the Dev Mode
  of rFactor2 game version v1121. Where necessary and available, information and
  descriptions were amended.

####
Part
####


Introduction text. Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed
do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim
veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum
dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident,
sunt in culpa qui officia deserunt mollit anim id est laborum.

.. table of contents for sections (if longer and additional navigation helps to provide a better overview)

.. contents:: Contents
  :depth: 2
  :local:

.. toctree is especially useful if page is the first of section with multiple pages

.. toctree::
	:maxdepth: 3

	index

*********************
Samples and templates
*********************

Admonitions
===========

.. note:: Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do
  eiusmod tempor incididunt ut labore et dolore magna aliqua.

.. danger:: Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do
  eiusmod tempor incididunt ut labore et dolore magna aliqua.

.. warning:: Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do
  eiusmod tempor incididunt ut labore et dolore magna aliqua.

Containers
==========

.. container:: tocdescr

  .. container:: descr

    .. figure:: _static/img/placeholder_600x120.png
      :target: general/index.html

    :doc:`general/index`
      *put desc here*

  .. container:: descr

    .. figure:: _static/img/placeholder_600x120.png
      :target: general/DevMode.html

    :doc:`general/DevMode`
      *put desc here*

Images
======

.. image reference needs full relative path

.. image:: general/img/rF2_steam_launch.jpg

References
==========

.. references need full path to support unique references (otherwise we cannot
  use the same title multiple times and have references automatically generated)

  Text may have a reference. Then the reference needs to be in <>.

:ref:`This is a sample reference. <archive/isi_mod_tut/car/car_physics:Unit Conversion>`

Reference to the first `Part`_

This is a hyperlink with text:

`Creative Commons Attribution-NonCommercial 4.0 International License <http://creativecommons.org/licenses/by-nc/4.0/>`_

This is a hyperlink without text:

`<http://creativecommons.org/licenses/by-nc/4.0/>`_

This is an inline reference to a glossary term of :term:`Dev Mode`.

.. The following will create a link in HTML that opens in a new window.

|link|

.. |link| raw:: html

   <a href="http://" target="_blank">text here</a>

Tables
======

.. table:: Table Title
  :widths: grid

  +---------------+---------------+
  | Column 1      | Column 2      |
  +===============+===============+
  | Cell 1.1      | Cell 1.2      |
  +---------------+---------------+
  | Cell 2.2      | Cell 2.2      |
  +---------------+---------------+

Helper
======

Make everything indented afterwards only visible in the HTML build:

`.. only:: builder_html`

or

`.. only:: builder_html and (not singlehtml)`

Make everything indented afterwards only visible in the epub or singlehtml build:

`.. only:: latex or epub or singlehtml`

*******
Chapter
*******

Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore
eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt
in culpa qui officia deserunt mollit anim id est laborum.

Section
=======

Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore
eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt
in culpa qui officia deserunt mollit anim id est laborum.

Subsection
==========

Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore
eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt
in culpa qui officia deserunt mollit anim id est laborum.

Subsubsection
-------------

Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore
eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt
in culpa qui officia deserunt mollit anim id est laborum.

Subsubsubsection
^^^^^^^^^^^^^^^^

Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore
eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt
in culpa qui officia deserunt mollit anim id est laborum.

Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore
eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt
in culpa qui officia deserunt mollit anim id est laborum.

Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore
eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt
in culpa qui officia deserunt mollit anim id est laborum.

Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore
eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt
in culpa qui officia deserunt mollit anim id est laborum.
