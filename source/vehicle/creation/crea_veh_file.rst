.. warning::

  This page is WIP.

.. sidebar:: Source

  Source of the information and descriptions herein were extracted from
  "skipbarber_05.veh" file of the SkipBarber that comes with the Dev Mode of
  rFactor2 game version v1121. Where necessary and available, information
  and descriptions were amended.

##################
VEH - Vehicle File
##################

The file defines a vehicle, driver, and team.

.. contents:: Contents
  :depth: 2
  :local:

***************
VEH File Format
***************

The first section defines what maps to load for the new vehicle skinning
technology. The first line defines a "prefix" to be used for all generic maps.
Currently, generic maps are used for the livery, wing, driver, driver arms,
driver helmet, and pit crew. The second line will replace the default livery
with the new specified, for the track specified. The format is as follows:

DefaultLivery
  Example value:	"PREFIX"

  PREFIX is the base texture map name, assumed to be BMP unless specified

PitCrewLivery
  Example value:	"PREFIX"

  This is only needed if it differs from the default livery PREFIX

TrackLivery
  Example value:	"TRACK, PREFIX"

  TRACK is the track name as defined in the event GDB

TrackLivery
  Example value:	"TRACK, PREFIX"

  For example, "2001_Monza"

TrackLivery
  Example value:	"TRACK, PREFIX"

  You can have an infinite # of these lines

DefaultLivery
  Example	"SkipBarber_05.dds"

  *no description provided*

HDVehicle
  Example	SkipBarber\SkipBarber.hdv

  *no description provided*

Graphics
  Example	SkipBarber\SkipBarber.gen

  *no description provided*

Spinner
  Example	SkipBarber\SkipBarber_spinner.gen

  *no description provided*

GenString
  Example value:

  Used to generate GMT names in \*.gen file

Sounds
  Example value:	SkipBarber.sfx

  *no description provided*

Cameras
  Example value:	SkipBarber.cam

  Defaults to default.cfg in UserData directory

HeadPhysics
  Example value:	HeadPhysics.ini

  Affects driver eyepoint only

Cockpit
  Example	value: SkipBarber_cockpitinfo.ini

  *no description provided*

Upgrades
  Example	value: SkipBarber_upgrades.ini

  *no description provided*

AIUpgradeClass
  Example	value: Skip_Barber_Regional

  *no description provided*

Number
  Example	value: 05

  *no description provided*

Team
  Example	value: "ISI Racing School"

  *no description provided*

PitGroup
  Example	value: "Group1"

  *no description provided*

Driver
  Example	value: "Terence Calder"

  *no description provided*

Description
  Example	value: "SkipBarber #05"

  *no description provided*

Engine
  Example	value: "ISI"

  *no description provided*

Manufacturer
  Example	value: "ISI"

  *no description provided*

Classes
  Example	value: "Skip_Barber Skip_Barber_Regional"

  *no description provided*

FullTeamName
  Example	value: "ISI Racing School"

  *no description provided*

TeamFounded
  Example	value: ""

  *no description provided*

TeamHeadquarters
  Example	value: ""

  *no description provided*

TeamStarts
  Example	value: 246

  *no description provided*

TeamPoles
  Example	value: 81

  *no description provided*

TeamWins
  Example	value: 83

  *no description provided*

TeamWorldChampionships
  Example	value: 4

  *no description provided*

Category
  Example	value: "SkipBarber 2013"

  *no description provided*

********************
Example file content
********************

.. code-block:: text

    DefaultLivery="SkipBarber_05.dds"

    HDVehicle=SkipBarber\SkipBarber.hdv
    Graphics=SkipBarber\SkipBarber.gen
    Spinner=SkipBarber\SkipBarber_spinner.gen
    GenString=
    Sounds=SkipBarber.sfx
    Cameras=SkipBarber.cam
    HeadPhysics=HeadPhysics.ini
    Cockpit=SkipBarber_cockpitinfo.ini
    Upgrades=SkipBarber_upgrades.ini
    AIUpgradeClass=Skip_Barber_Regional

    Number=05
    Team="ISI Racing School"
    PitGroup="Group1"
    Driver="Terence Calder"
    Description="SkipBarber #05"
    Engine="ISI"
    Manufacturer="ISI"

    Classes="Skip_Barber Skip_Barber_Regional"

    FullTeamName="ISI Racing School"
    TeamFounded=
    TeamHeadquarters=""
    TeamStarts=246
    TeamPoles=81
    TeamWins=83
    TeamWorldChampionships=4

    Category="SkipBarber 2013"
