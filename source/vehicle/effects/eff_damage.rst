.. warning::

  This page is WIP.

.. sidebar:: Source

  Source of the information and descriptions herein were extracted from
  "skipbarber_damage.ini" file of the SkipBarber that comes with the Dev Mode
  of rFactor2 game version v1121. Where necessary and available, information and
  descriptions were amended.

.. _vehicles-eff-damage:

#######
Damage
#######

.. contents:: Contents
  :depth: 2
  :local:

************
Introduction
************

Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud
exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute
irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat
nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa
qui officia deserunt mollit anim id est laborum.

.. WIP: referenced in HDV

.. WIP: any file extension possible, but must be text file

The damage file has two sections: In the first section the physical damage is
defined. In the second section the vertex deformation is defined.

****************************
Physical Damage - [PHYSICAL]
****************************

RadiusAdd
	Example value:	0.6

	Base radius to apply damage

RadiusMult
	Example value:	0.00014

	Multiplied by collision impulse to increase radius

RadiusMax
	Example value:	1.6

	Maximum radius to apply damage

Engine
	Example value:	9500

	Impulse to seize engine

AeroDiv
	Example value:	2.2e-5

	Multiplied by impulse to affect aerodynamics and vertices

AeroMin
	Example value:	800

	Minimum impulse to damage aero and verts (unlike everything else, computed
	BEFORE damage multiplier)

VertMult
	Example value:	1.0

	Multiplied by aero damage to get vert damage

RadiatorCoverInstance
	Example value:	RadCover

	If this gets knocked off, engine cools but aerodynamics suffer

DeactivateInstance
	Example value:	LowDetailEngine

	Deactivate this instance if any parts get knocked off

ActivateInstance
	Example value:	HighDetailEngine

	Activate this instance if any parts get knocked off

FLSuspIns
	Example value:	Debris5

	Instance (used for suspension movement on front-left wheel)

FLSuspConn
	Example value:	(0.16,0.95)

	Connection points for suspension movement (relative to inboard and outboard
	verts)

FRSuspIns
	Example value:	Debris7

	Instance (used for suspension movement on front-right wheel)

FRSuspConn
	Example value:	(0.16,0.95)

	Connection points for suspension movement (relative to inboard and outboard verts)

RLSuspIns
	Example value:	Debris6

	Instance (used for suspension movement on rear-left wheel)

RLSuspConn
	Example value:	(0.08,0.94)

	Connection points for suspension movement (relative to inboard and outboard verts)

RRSuspIns
	Example value:	Debris8

	Instance (used for suspension movement on rear-right wheel)

RRSuspConn
	Example value:	(0.08,0.94)

	Connection points for suspension movement (relative to inboard and outboard verts)

WallSkidThresh
	Example value:	3000

	Minimum impulse to generate wall skid (ignores damage setting and multiplier)

FrontWingDetach
	Example value:	1800

	Minimum impulse to detach front wing (doesn't apply to WC cars)

FrontWingRandom
	Example value:	0.95

	Fraction of time wing breaks off

FrontWingPos
	Example value:	(0,0,0)

	If zero, automatically finds position of wing from graphics to check for damage

FrontWingMassInertia
	Example value:	(10, 1, 0.5, 1.5)

	Mass and inertia

FrontWingCollParams
	Example value:	(3600, 65, 0.6)

	Spring/damper/friction

RearWingDetach
	Example value:	3190

	Minimum impulse to detach front wing (doesn't apply to WC cars)

RearWingRandom
	Example value:	0.60

	Fraction of time wing breaks off

RearWingPos
	Example value:	(0,0,0)

	If zero, automatically finds position of wing from graphics to check for damage

RearWingMassInertia
	Example value:	(10, 1, 0.5, 1.5)

	Mass and inertia

RearWingCollParams
	Example value:	(3600, 65, 0.6)

	Spring/damper/friction

TireCutDull
	Example value:	(6000, 0.25)

	Impulse and fraction of incidents to cut tire with dull object

TireCutSharp
	Example value:	(500, 0.65)

	Impulse and fraction of incidents to cut tire with sharp object (body panel or wing)

WheelBend
	Example value:	980

	Impulse to bend wheel

WheelDetach
	Example value:	2350

	Threshold to detach wheel

WheelRandom
	Example value:	0.57

	Fraction of incidents where wheel actually breaks off

Wheel0MassInertia
	Example value:	(20, 1.5, 1, 1)

	Mass and inertia

Wheel0CollParams
	Example value:	(11100, 105, 1)

	Spring/damper/friction

Wheel1MassInertia
	Example value:	(20, 1.5, 1, 1)

	*no description provided*

Wheel1CollParams
	Example value:	(11100, 105, 1)

	*no description provided*

Wheel2MassInertia
	Example value:	(26, 1.5, 1, 1)

	*no description provided*

Wheel2CollParams
	Example value:	(11100, 105, 1)

	*no description provided*

Wheel3MassInertia
	Example value:	(26, 1.5, 1, 1)

	*no description provided*

Wheel3CollParams
	Example value:	(11100, 105, 1)

	*no description provided*

Part0Detach
	Example value:	8700

	Impulse to make part become debris (see .gen file)

Part0Random
	Example value:	0.4

	Fraction of time part breaks off

Part0Pos
	Example value:	(0,0,0)

	If zero, automatically finds position of part from graphics to check for damage

Part0MassInertia
	Example value:	(20, 2, 4, 2)

	Mass and inertia

Part0CollParams
	Example value:	(7200, 100, 0.6)

	Spring/damper/friction

Part1Detach
	Example value:	8800

	Impulse to make part become debris (see .gen file)

Part1Random
	Example value:	0.2

	Fraction of time part breaks off

Part1Pos
	Example value:	(0,0,0)

	If zero, automatically finds position of part from graphics to check for damage

Part1MassInertia
	Example value:	(10, 1, 1, 1)

	Mass and inertia

Part1CollParams
	Example value:	(3600, 65, 0.6)

	Spring/damper/friction

Part2Detach
	Example value:	8600

	Impulse to make part become debris (see .gen file)

Part2Random
	Example value:	0.2

	Fraction of time part breaks off

Part2Pos
	Example value:	(0,0,0)

	If zero, automatically finds position of part from graphics to check for damage

Part2MassInertia
	Example value:	(10, 1, 1, 1)

	Mass and inertia

Part2CollParams
	Example value:	(3600, 65, 0.6)

	Spring/damper/friction

Part3Detach
	Example value:	8900

	Impulse to make part become debris (see .gen file)

Part3Random
	Example value:	0.2

	Fraction of time part breaks off

Part3Pos
	Example value:	(0,0,0)

	If zero, automatically finds position of part from graphics to check for damage

Part3MassInertia
	Example value:	(10, 1, 1, 1)

	Mass and inertia

Part3CollParams
	Example value:	(3600, 65, 0.6)

	Spring/damper/friction

Part4Detach
	Example value:	9000

	Impulse to make part become debris (see .gen file)

Part4Random
	Example value:	0.2

	Fraction of time part breaks off

Part4Pos
	Example value:	(0,0,0)

	If zero, automatically finds position of part from graphics to check for damage

Part4MassInertia
	Example value:	(10, 1, 1, 1)

	Mass and inertia

Part4CollParams
	Example value:	(3600, 65, 0.6)

	Spring/damper/friction

Part5Postreq
	Example value:	Wheel0

	Define parts which break off together with the current part

Part5Detach
	Example value:	4300

	Impulse to make part become debris (see .gen file)

Part5Random
	Example value:	0.4

	Fraction of time part breaks off

Part5Pos
	Example value:	(0,0,0)

	If zero, automatically finds position of part from graphics to check for damage

Part5MassInertia
	Example value:	(10, 1, 1, 1)

	Mass and inertia

Part5CollParams
	Example value:	(3600, 65, 0.6)

	Spring/damper/friction

Part6Postreq
	Example value:	Wheel2

	Define parts which break off together with the current part

Part6Detach
	Example value:	4600

	Impulse to make part become debris (see .gen file)

Part6Random
	Example value:	0.4

	Fraction of time part breaks off

Part6Pos
	Example value:	(0,0,0)

	If zero, automatically finds position of part from graphics to check for damage

Part6MassInertia
	Example value:	(10, 1, 1, 1)

	Mass and inertia

Part6CollParams
	Example value:	(3600, 65, 0.6)

	Spring/damper/friction

Part7Postreq
	Example value:	Wheel1

	Define parts which break off together with the current part

Part7Detach
	Example value:	4300

	Impulse to make part become debris (see .gen file)

Part7Random
	Example value:	0.4

	Fraction of time part breaks off

Part7Pos
	Example value:	(0,0,0)

	If zero, automatically finds position of part from graphics to check for damage

Part7MassInertia
	Example value:	(10, 1, 1, 1)

	Mass and inertia

Part7CollParams
	Example value:	(3600, 65, 0.6)

	Spring/damper/friction

Part8Postreq
	Example value:	Wheel3

	Define parts which break off together with the current part

Part8Detach
	Example value:	4600

	Impulse to make part become debris (see .gen file)

Part8Random
	Example value:	0.4

	Fraction of time part breaks off

Part8Pos
	Example value:	(0,0,0)

	If zero, automatically finds position of part from graphics to check for damage

Part8MassInertia
	Example value:	(10, 1, 1, 1)

	Mass and inertia

Part8CollParams
	Example value:	(3600, 65, 0.6)

	Spring/damper/friction

Part9Detach
	Example value:	8800

	Impulse to make part become debris (see .gen file)

Part9Random
	Example value:	0.4

	Fraction of time part breaks off

Part9Pos
	Example value:	(0,0,0)

	If zero, automatically finds position of part from graphics to check for damage

Part9MassInertia
	Example value:	(10, 1, 1, 1)

	Mass and inertia

Part9CollParams
	Example value:	(3600, 65, 0.6)

	Spring/damper/friction

Part10Detach
	Example value:	8800

	Impulse to make part become debris (see .gen file)

Part10Random
	Example value:	0.4

	Fraction of time part breaks off

Part10Pos
	Example value:	(0,0,0)

	If zero, automatically finds position of part from graphics to check for damage

Part10MassInertia
	Example value:	(10, 1, 1, 1)

	Mass and inertia

Part10CollParams
	Example value:	(3600, 65, 0.6)

	Spring/damper/friction

Part11Detach
	Example value:	8800

	Impulse to make part become debris (see .gen file)

Part11Random
	Example value:	0.4

	Fraction of time part breaks off

Part11Pos
	Example value:	(0,0,0)

	If zero, automatically finds position of part from graphics to check for damage

Part11MassInertia
	Example value:	(10, 1, 1, 1)

	Mass and inertia

Part11CollParams
	Example value:	(3600, 65, 0.6)

	Spring/damper/friction

************************
Vertex Damage - [VERTEX]
************************

This section defines how verts can be moved. There are two available rules currently:

1) You can restrict all verts within a given sphere to move a given distance:

- RestrictionLimit=<maximum movement>

- RestrictionSphere=(<x>, <y>, <z>, <radius>)

You can change the limit before each sphere, or continue to use the last one defined.

2) You can prevent all verts from entering a given sphere:

- ForceFieldSphere=(<x>, <y>, <z>, <radius>)

Verts within the sphere cannot get any closer to the center.

Note that the verts here are relative to the graphics model, not the physical CG.
To make things difficult, the graphics model isn't necessarily centered or anything.

DefaultLimit
	Example value:	1.00

	By default, all verts can move up to a meter

RestrictionLimit
	Example value:	0.10

	Restricted verts can only move this far

RestrictionSphere
	Example value:	(0.40, 1.05, 0.08, 0.95)

	Don't crush verts too much around driver's head or the helmet might poke through the roof

ForceFieldSphere
	Example value:	( 0.40, 0.40,-0.90, 0.45)

	Protect driver's legs

ForceFieldSphere
	Example value:	( 0.00, 0.35,-1.85, 0.45)

	Keep body verts out of radiator

ForceFieldSphere
	Example value:	( 0.74, 0.35,-1.62, 0.47)

	Keep verts away from FL wheel

ForceFieldSphere
	Example value:	(-0.74, 0.35,-1.62, 0.47)

	Keep verts away from FR wheel

ForceFieldSphere
	Example value:	( 0.74, 0.35, 1.44, 0.47)

	Keep verts away from RL wheel

ForceFieldSphere
	Example value:	(-0.74, 0.35, 1.44, 0.47)

	Keep verts away from RR wheel

DeformableInstance
	Example value:	SLOT

	This is a *special* keyword indicating the main body of the slot (which is named on-the-fly)

DeformableInstance
	Example value:	FWING

	You can leave these even if your vehicle doesn't have one

DeformableInstance
	Example value:	RWING

	*no description provided*

DeformableInstance
	Example value:	DEBRIS0

	*no description provided*

DeformableInstance
	Example value:	DEBRIS1

	*no description provided*

DeformableInstance
	Example value:	DEBRIS2

	*no description provided*

DeformableInstance
	Example value:	DEBRIS3

	*no description provided*

DeformableInstance
	Example value:	DEBRIS4

	*no description provided*

DeformableInstance
	Example value:	DEBRIS5

	*no description provided*

DeformableInstance
	Example value:	DEBRIS6

	*no description provided*

DeformableInstance
	Example value:	DEBRIS7

	*no description provided*

DeformableInstance
	Example value:	DEBRIS8

	*no description provided*

DeformableInstance
	Example value:	DEBRIS9

	*no description provided*

DeformableInstance
	Example value:	DEBRIS10

	*no description provided*

DeformableInstance
	Example value:	DEBRIS11

	*no description provided*

DeformableInstance
	Example value:	EXHAUST

	*no description provided*

DeformableInstance
	Example value:	WWELL

	*no description provided*

DeformableInstance
	Example value:	SIDESKIRTS

	*no description provided*
