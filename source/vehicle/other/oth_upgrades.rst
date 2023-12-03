.. warning::

  This page is WIP.

.. sidebar:: Source

  Source of the information and descriptions herein were extracted from
  "skipbarber_Upgradesini" file of the SkipBarber that comes with the Dev Mode
  of rFactor2 game version v1121. Where necessary and available, information and
  descriptions were amended.

########
Upgrades
########

.. contents:: Contents
  :depth: 2
  :local:

************
Introduction
************

Introduction text. Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed
do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim
veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum
dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident,
sunt in culpa qui officia deserunt mollit anim id est laborum.

You can create any number of upgrades with any name you wish. Just use the
provided sample and expand upon it.

***************
Upgrade Options
***************

UpgradeType
  Example value:	"PARTS"

  Type of upgrade. This can be named anything.

Instance
  Example value:	"LVL1 Front Part"

  What instance in the GEN file to modify.

UpgradeLevel
  Example value:	"STOCK"

  What level of upgrade.

GEN=<FPARTEXISTS>
  Example value:	"//"

  This replaces the token <FPARTEXISTS> with in the GEN to comment it out

GEN
  Example value:	<FPART>=

  YOU need some definition here, even though it doesn't exist.

UpgradeLevel
  Example value:	"LVL2 Front Part"

  What level of upgrade.

Price
  Example value: 1

  This is to make sure UpgradeClass works correctly by giving this a price.

GEN
  Example value:	<RWINGEXISTS>=""

  This replaces the token <FPARTEXISTS> with nothing in the GEN. To uncomment it out.

Description
  Example value:	"Front Part lvl2"

  This is the description that goes in the in-game menus.

GEN
  Example value:	<FPART>=FPART_lvl2.gmt

  what GMT file replace that token (<RWING>) in the GEN File.

SFX
  Example value:

  You may override SFX file entries here

CPIT
  Example value:

  You may override CockpitInfo.ini entries here

HDV
  Example value:	[General]

  Section header.

HDV
  Example value:	Mass=1000

  You may override HDV entries here under the section headers.

HDV
  Example value:	Inertia\*=(1.1,1.2,1.3)

  Accepted mathematical functions include (- / \* +).

BaseVehiclePrice
  Example value:  0

  *no description provided*

****************
Original Example
****************

.. code-block:: text

  UpgradeType="PARTS"
  {
    Instance="LVL1 Front Part"
    UpgradeLevel="STOCK"
    {
      GEN=<FPARTEXISTS>="//"
      GEN=<FPART>=
    }

    UpgradeLevel="LVL2 Front Part"
    {
      GEN=<RWINGEXISTS>=""
      Description="Front Part lvl2"
      GEN=<FPART>=FPART_lvl2.gmt

      SFX=

      CPIT=

      HDV=[General]
      HDV=Mass=1000
      HDV=Inertia\*=(1.1,1.2,1.3)
    }
  }

******************
SkipBarber Example
******************

.. code-block::

  UpgradeClass="Skip_Barber_Regional"
  {
    AIList
    {
      Series=0
    }
  }

  UpgradeClass="Skip_Barber_National"
  {
    AIList
    {
      Series=1
    }
  }

  UpgradeType="Series"
  {
    UpgradeLevel="Regional"
    {
      CPIT=TireCompoundMap=(1)
      CPIT=SpinnerCompound=1
    }

    UpgradeLevel="National"
    {
      Price=1

      HDV=[General]
      HDV=Notes="Slicks Recommended Cold Pressure Front: 24 PSI, Rear: 26 PSI (Hot Front: 30 PSI, Rear: 32 PSI) 60km/h=~3690RPM in 1st.�Treaded Recommended Cold Pressure Front: 32 PSI, Rear: 34 PSI (Hot Front: 36 PSI, Rear: 38 PSI) 60km/h=~3600RPM in 1st."
      HDV=TireBrand=SkipBarber_National.tbc
      //HDV=FrontTireCompoundSpecial=(0,"205/50 R15",,)
      //HDV=FrontTireCompoundSpecial=(1,"195/55 R15",,)
      HDV=
      HDV=[CONTROLS]
      HDV=RearBrakeSetting=24
      HDV=
      HDV=[FRONTLEFT]
      HDV=PressureSetting=16
      HDV=
      HDV=[FRONTRIGHT]
      HDV=PressureSetting=16
      HDV=
      HDV=[REARLEFT]
      HDV=PressureSetting=24
      HDV=
      HDV=[REARRIGHT]
      HDV=PressureSetting=24
      HDV=
    }
  }

  UpgradeType="Visor Mod"
  {
    Instance="VISOR"
    UpgradeLevel="NO VISOR"
    {
      Description="Clear Helmet View"
      GEN=<VISORMOD>=no_visor.gmt
    }

    UpgradeLevel="VISOR MOD"
    {
      Description="Helmet View Through Visor"
      GEN=<VISORMOD>=visor_cam_OW.gmt
    }
  }
