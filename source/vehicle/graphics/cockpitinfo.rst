.. warning::

  This page is WIP.

.. sidebar:: Source

  Source of the information and descriptions herein were extracted from
  "skipbarber_cockpitinfo.ini" file of the SkipBarber that comes with the Dev Mode
  of rFactor2 game version v1121. Where necessary and available, information and
  descriptions were amended.

===========
Cockpitinfo
===========

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

****************************
Camera and Graphical Effects
****************************

Eyepoint
	Example value:	( 0.0, 0.66, 0.17)

	Cockpit eyepoint (left/right, up/down, front/back).

CameraTarget
	Example value:	(0.0, 0.55, 0.35)

	Target for all other cameras.

TVOffset
	Example value:	( 0.0, 0.0, 0.0)

	Additional offset for tv cockpit view (defaults to 0,0,0).

MirrorPos
	Example value:	(0.0, 0.56,-0.40)

	Mirror position.

FrontWheelsInCockpit
	Example value:	1

	Whether to render front wheels in cockpit view.

CockpitVibrationMag
	Example value:	0.003

	Default 0.006.

SteeringWheelAxis
	Example value:	(0.0, 0.269, 0.963)

	Second value is SINE of the wheel angle, third value is COSINE of the wheel
	angle.

SteeringDegreesPerFrame
	Example value:	2.0

	Degrees of rotation per arm animation frame.

Variables to control the helmet movement as seen from the outside:

HeadMaxPos
	Example value:	(0.024,0.015,0.015)

	Defaults (0.06,0.02,0.02), first number is left-to-right movement with the
	head roll.

HeadMaxOri
	Example value:	(0.050,0.050,0.120)

	Defaults (0.10,0.10,0.30), last number is head roll.

WheelSpeedAnims
	Example value:	3

	Default is 3, but up to 6 *speed* anims allowed, multiplied by any number of
	graphical tire compounds.

.. note::  Wheel speed and tire compound are combined into a single animation
  index. For example, the first three animation frames would usually be the
  tire speed blur animations for a dry-weather tire.  You can define more using
  GraphicalTireCompounds.

WheelSpeedRPM
	Example value:	(168,672,1000,1500,2000)

	RPM thresholds to switch animations between *speed* anims)

GraphicalTireCompounds
	Example value:	2

	Number of graphical tire compounds (may be less than number of physical tire
	compounds if some look the same).

TireCompoundMap
	Example value:	(0,1)

	Up to 16 entries allowed, maps the physical compound to the graphical one.

SpinnerCompound
	Example value:	0

	Index to use for spinner display tyres.

**************************
Cockpit and Gauge Settings
**************************

.. note:: All fonts are assumed to be .BMP, to change, just include the
  extension, e.g., "FONTMONKEY.TGA".

SpeedometerRange
	Example value:	(0, 260, 231, 310)

	Unit is km/h (<minvalue>, <maxvalue>, <beginangle>, <endangle>).

SpeedometerNonlinear
	Example value:	(155,155)

	Starting at 155km/h, it rises.

SpeedometerNonlinear
	Example value:	(241.4,198.2)

	At roughly half the rate.

SpeedometerBackground
	Example value:	rter_speedo.BMP

	*no description provided*

SpeedometerNeedleMAP
	Example value:	rter_SNEEDLE.BMP

	*no description provided*

SpeedometerNeedle
	Example value:	(1.8, 1.8)

	*no description provided*

TachometerRange
	Example value:	(0, 10000, 268, 357)

	Unit is RPM.

TachometerCenter
	Example value:	(0.50, 0.53)

	Where needle rotates from (0.0-1.0, 0.0-1.0).

TachometerBackground
	Example value:	rter_rpm.tga

	*no description provided*

TachometerNeedle
	Example value:	(1.5,1.5)

	Dimensions of the needle with (<needlewidth>, <needleheight>)

TachometerNeedlemap
	Example value:	rter_SNEEDLE.dds

	*no description provided*

TachometerClockwise
	Example value:	1

	Switch between 0 = counterclockwise and 1 = clockwise (this is obviously the
	default) orientation of the tacho.

RelativeTachometer
	Example value:	0

	Ignores <maxvalue> and uses default rev limit instead (which makes it work
	better for upgrades)

WaterTempRange
	Example value:	(71.1, 126.7, 197, 27)

	Values in °C.

WaterTempBackGround
	Example value:	rter_water_temp.tga

	*no description provided*

WaterTempCenter
	Example value:	(0.50, 0.55)

	*no description provided*

WaterTempNeedle
	Example value:	(0.9,0.9)

	*no description provided*

WaterTempNeedlemap
	Example value:	rter_SNEEDLE.dds

	*no description provided*

OilTempRange
	Example value:	(60, 148.9, 150, 44)

	Values in °C.

OilTempBackground
	Example value:	rter_oil_temp.tga

	*no description provided*

OilTempCenter
	Example value:	(0.50, 0.65)

	*no description provided*

OilTempNeedle
	Example value:	(1.0,1.0)

	*no description provided*

OilTempNeedlemap
	Example value:	rter_SNEEDLE.dds

	*no description provided*
