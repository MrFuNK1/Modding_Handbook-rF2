.. warning::

  This page is WIP.

#########################
High-Detail Vehicle - HDV
#########################

.. sidebar:: Source

  Source of the information and descriptions herein were extracted from
  "skipbarber.hdv" file of the SkipBarber that comes with the Dev Mode
  of rFactor2 game version v1121. Where necessary and available, information and
  descriptions were amended.

The High-Detail Vehicle (HDV) file, hereinafter referred to as the "HDV file",
defines all the fine details of a vehicles's physic. All parameters included in
the HDV file do...

.. contents:: Contents
  :depth: 2
  :local:

*******************
General Notes
*******************

.. note:: These general notes are from the "skipbarber.hdv" file with some minor
  modifications or amendments.

The HDV file is It is pointed to by one or more \*.veh files.

Any range has the following values: (minimum, step size, number of steps)

Any setting refers to the step from 0 to <number of steps - 1>.

Any special follows the format (setting, non-translated value prefix, translated value postfix, instructions)
setting refers to the index, non-translated value prefix refers to the desired alphanumeric display value,
translated value postfix refers to the display unit type (i.e. lb/in, etc), instructions can be used override
specified index values allowing special instructions including non-linear adjustments.

Any caption replaces setting name within the garage page.

Everything is in SI units (kg, m, kPa, N, etc.), except:

  Engine speed is measured in RPM.

  Angles are measured in degrees.

+x = left, +y = up, +z = rear

Pushrod connections are adjusted from the values found in this file based on
the graphical location of the wheels. If the graphical location does not match
the physical location (found in a .pm file), then all suspension joints (including
the pushrods) are adjusted to match the graphical locations. It should be noted
that suspension joints are also adjusted after setting the camber, caster, and
toe-in.

The "reference plane" is equal to the ride height. Note that we have added a
graphical offset because some series' measure the ride heights to the frame of
the car, but the bodywork hangs about an inch lower (especially at the air dam).
The graphical offset does not affect the physics in any way, just the appearance
of how far the vehicle is off the ground. Note that the "undertray" points are
where the vehicle bottoms out.

Aerodynamic variables: Downforce is negative lift

************************
Sections of the HDV File
************************

.. note::	The HDV file has the following sections. Some of these sections are
  required others are optional. These details are provided at the beginning of
  each section description below.

- General - [GENERAL]
- Pit Menu
- Plugin
- Aid Penalties
- Front Wing
- Left Fender
- Right Fender
- Rear Wing
- Body Aero
- Diffuser
- Suspension
- Controls
- Engine
- Driveline
- Front Left
- Front Right
- Rear Left
- Rear Right

General - [GENERAL]
===================

Rules
	Example value:	0

	what rules to apply to garage setups (0=none, 1=stock car)

GarageDisplayFlags
	Example value:	1

	how settings are displayed in garage (add): 1=rear downforce value (vs. angle), 2=radiator (vs. grille tape), 4=more gear info, 8+16=front downforce/wing/splitter/air dam, 32+64=rear downforce/wing/spoiler, 128=flip ups (vs. fender flare)

Mass
	Example value:	629

	(567kg w liquids) all mass except fuel

Inertia
	Example value:	(628.43, 680.62, 112.5)

	all inertia except fuel

FuelTankForceDistrib
	Example value:	(0.4:front_subbody:(0,0,-0.18),0.6:rear_subbody:(0,0,0.18))

	Fraction of forces distributed on specified sub-body (sum should be 1.0 across the bodies). Subsequent bracket values represent distance offsets which may be useful for forces that should be applied to a larger area thereby reducing torques on the sub-body. Forces may be applied to ANY sub-body however care should be taken to avoid applying these forces to wheels as their orientation changes which can result in strong vibrations. If this line does not exist forces will be applied evenly across the main bod(y/ies) and torque at the relative location of that sub-body.

FuelTankPos
	Example value:	(0.0, 0.15,-0.65)

	location of tank relative to center of rear axle in reference plane

FuelTankMotion
	Example value:	(560.0,0.6)

	simple model of fuel movement in tank (spring rate per kg, critical damping ratio)

Notes
  Example value: "60km/h=~3600RPM in 1st"

  *no description provided*

Symmetric
  Example value: 1

  *no description provided*

DamageFile
	Example value:	skipbarber_Damage

	.ini file to find physical and graphical damage info

CGHeightRange
	Example value:	(0.311, 0.0, 1)

	height of body mass (excluding fuel) above reference plane

CGHeightSetting
	Example value:	0

	*no description provided*

CGRightRange
	Example value:	(0.5, 0.005, 1)

	fraction of weight on right tires

CGRightSetting
	Example value:	0

	*no description provided*

CGRearRange
	Example value:	(0.604, 0.001, 1)

	fraction of weight on rear tires

CGRearSetting
	Example	value:	0

	*no description provided*

WedgeRange
	Example value:	(0.0, 0.25, 1)

	rounds of wedge

WedgeSetting
	Example	value:	0

	*no description provided*

WedgePushrod
	Example value:	0.0

	each round of wedge changes rear-left jacking screw by this amount (0.0 to disable, use Rules to allow FR ride height)

GraphicalOffset
	Example value:	(0.0, 0.0, 0.0)

	does not affect physics!  This just moves the vehicle body for whatever reasons you may have.

Undertray00
	Example value:	( 0.25, 0.0,-1.33)

	corner offsets from center of wheels in reference plane

Undertray01
	Example value:	(-0.25, 0.0,-1.33)

	the height of the first 4 undertray points (00-03) are used in the diffuser calculations

Full undertray definition from "SkipBarber.hdv":

.. code-block::

	Undertray01=(-0.25, 0.0,-1.33)
	Undertray02=( 0.20, 0.0, 1.25)
	Undertray03=(-0.20, 0.0, 1.25)
	Undertray04=( 0.60, 0.0,-0.31)
	Undertray05=(-0.60, 0.0,-0.31)
	Undertray06=( 0.50, 0.0, 0.53)
	Undertray07=(-0.50, 0.0, 0.53)
	Undertray08=( 0.63, 0.0, 0.0)
	Undertray09=( 0.0, 0.0, 0.0)
	Undertray10=(-0.63, 0.0, 0.0)
	Undertray11=( 0.0, 0.0,-0.8)

UndertrayParams
	Example value:	(295000,5000,0.5)

	undertray spring rate, damper rate, and coefficient of friction

TireBrand
	Example value:	SkipBarber

	must appear before tire compound setting (references \*.tbc file)

FrontTireCompoundSetting
	Example value:	0

	compound index within brand

FrontTireCompoundSpecial
	Example value:	(0,"195/55 R15",,)

	*no description provided*

RearTireCompoundSetting
	Example value:	0

	*no description provided*

RearTireCompoundSpecial
	Example value:	(0,"225/50 R16",,)

	*no description provided*

FuelRange
	Example value:	(4, 1, 26)

	*no description provided*

FuelSetting
	Example value:	24

	*no description provided*

NumPitstopsRange
	Example value:	(0, 1, 2)

	*no description provided*

NumPitstopsSetting
	Example value:	0

	*no description provided*

Pitstop1Range
	Example value:	(2, 1, 29)

	*no description provided*

Pitstop1Setting
	Example value:	24

	*no description provided*

Pitstop2Range
	Example value:	(2, 1, 29)

	*no description provided*

Pitstop2Setting
	Example value:	24

	*no description provided*

Pitstop3Range
	Example value:	(2, 1, 29)

	*no description provided*

Pitstop3Setting
	Example value:	24

	*no description provided*

AIMinPassesPerTick
	Example value:	5

	minimum passes per tick (can use more accurate spring/damper/torque values, but takes more CPU)

AINegSuspForceMult
	Example value:	0.01

	0.0 means negative suspension forces are not allowed, 1.0 completely allows them (old behaviour)

AICornerRates
	Example value:	(0.4,0.4,0.4,0.4)

	spring rate adjustment for AI physics

AIBumpstop
	Example value:	(1.0,0.5,1.0,0.4)

	bumpstop rate multipliers for AI physics (<spring mult>,<rising spring mult>,<damper mult>,<rising damper mult>)

AIDamping
	Example value:	(1.0,1.0,1.0,1.0)

	damping rate adjustment for AI physics (<SlowBump>,<SlowRebound>,<FastBump>,<FastRebound>)

AIDownforceZArm
	Example value:	0.97

	hard-coded center-of-pressure offset from vehicle CG

AIDownforceBias
	Example value:	0.0

	bias between setup and hard-coded value (0.0-1.0)

AIFuelMult
	Example value:	-1.0

	PLR file override for AI fuel usage - only positive value will override, see PLR for default

AIPerfUsage
	Example value:	(-1.0,-1.0,-1.0)

	PLR file overrides for (brake power usage, brake grip usage, corner grip usage) used by AI to estimate performance - only positive values will override, see PLR for defaults

AITableParams
	Example value:	(-1.0,-1.0)

	PLR file overrides for (max load, min radius) used when computing performance estimate tables - only positive values will override, see PLR for defaults

Pit Menu - [PITMENU]
====================

StopGo
	Example value:	1

	Whether stop/go pit menu item is available (highly recommended); default=1

Fuel
	Example value:	1

	Whether fuel pit menu item is available (recommended); default=1

AllTires
	Example value:	0

	Option for changing all tires (all other tire choices should be 0); default=0

FrontRearTires
	Example value:	(0,0)

	Option for changing front tires, rear tires (all other conflicting tire choices should be 0); default=(1,1)

LeftRightTires
	Example value:	(0,0)

	Option for changing left tires, right tires (all other conflicting tire choices should be 0); default=(0,0)

IndividualTires
	Example value:	(1,1,1,1)

	Option for changing individual tire FL, FR, RL, RR (all other conflicting tire choices should be 0); default=(0,0,0,0)

FenderFlare
	Example value:	(0,0)

	Options for changing left fender flare, right fender flare; default=(0,0)

FrontWing
	Example value:	0

	Front wing adjustment (front wing repair is covered under Damage); default=1

RearWing
	Example value:	0

	Rear wing adjustment (rear wing repair is covered under Damage); default=0

Driver
	Example value:	1

	Driver change; default=1

Wedge
	Example value:	0

	Wedge adjustment; default=0

Radiator
	Example value:	0

	Radiator or grille tape adjustment; default=0

TrackBar
	Example value:	0

	Track bar adjustment; default=0

Pressure
	Example value:	(1,1,1,1)

	Tire pressure adjustment FL, FR, RL, RR; default=(0,0,0,0)

SpringRubber
	Example value:	(0,0,0,0)

	Spring rubber adjustment FL, FR, RL, RR; default=(0,0,0,0)

Damage
	Example value:	2

	Number of options to fix damage (0=none, 1=bodywork, 2=bodywork+suspension); default=1

StopGoSimultaneous
	Example value:	0

	Whether stop/go penalties can be served during a regular pit stop (time is added at end); default=0

PressureOnTheFly
	Example value:	1

	Whether tire pressures can be adjusted WITHOUT changing tires; default=0

DamagedTiresOnly
	Example value:	0

	Tire change restrictions: 0=any tire can be changed 1=only damaged tires can be changed; default=0

CompoundRestrictions
	Example value:	2

	Whether tire compounds have restrictions: 0=unrestricted 1=one dry compound from qualifying on, 2=front/rear compounds must match, 3=both; default=0

Preparation
	Example value:	(150,30,0.5,6.0)

	When crew gives up after request, crew prep time, delay multiplier for how much more time was needed to prep, max delay; default=(150.0,25.0,0.5,4.5)

FuelTime
	Example value:	(3.0,2.0,1.2,0.7,1.0)

	Fuel fill rate (L/s), random delay, nozzle insertion time, nozzle removal time, concurrent fuel filling (0.0=separate, 1.0=concurrent); default=(12.0,2.0,1.0,0.5,1.0)

TireTime
	Example value:	(15.0,32.0,7.0,1.0)

	Time to change two tires, time to change four tires, random delay on any tire, concurrent tire changes (0.0=separate, 1.0=concurrent); default=(5.5,5.5,2.0,1.0)

FenderFlareTime
	Example value:	0.0

	Time to adjust fender flare; default=3.5

FrontWingTime
	Example value:	(15,50)

	Time to adjust front wing, time to replace front wing; default=(8.0,8.0)

RearWingTime
	Example value:	(60,90)

	Time to adjust rear wing, time to replace rear wing; default=(8.0,33.0)

DriverTime
	Example value:	(40,6.0,4.0,1.0)

	Time to change driver, random delay, extra delay if vehicle is damaged, concurrent driver changes (0.0=separate, 1.0=concurrent); default=(11.0,1.5,4.0,1.0)

WedgeTime
	Example value:	0.0

	Time to adjust wedge; default=3.5

RadiatorTime
	Example value:	5.0

	Time to adjust radiator/grille tape; default=5.0

TrackBarTime
	Example value:	0.0

	Time to adjust track bar; default=3.5

PressureTime
	Example value:	5.0

	Time to adjust tire pressure WITHOUT changing tire; default=2.5

SpringRubberTime
	Example value:	3.5

	Time to adjust spring rubber; default=3.0

DamageTime
	Example value:	(12.5,12.5,300,1.0)

	Time to fix aero damage, random delay, fix suspension including broken off wheels, concurrent damage fixing (0.0=separate, 1.0=concurrent); default=(8.5,1.0,90.0,1.0)

Plugin - [PLUGIN]
=================

Whether certain sensors are available as telemetry outputs.

AerodynamicSensor
	Example value:	0

	Aerodynamic force sensors

EngineSensor
	Example value:	1

	*no description provided*

SuspensionSensor
	Example value:	1

	*no description provided*

TireForceSensor
	Example value:	0

	*no description provided*

TireTemperatureSensor
	Example value:	1

	*no description provided*

Aid Penalties - [AIDPENALTIES]
==============================

TC
	Example value:	(0,0.004,0.006)

	Weight penalties for using different levels of aids.

ABS
	Example value:	(0,0.006,0.01)

	First value is typically with the aid off so it should be 0.0.

Stability
	Example value:	(0,0.005,0.008)

	Penalties should only be applied to aids that the

Autoshift
	Example value:	(0,0.001,0.001,0.002)

	vehicle would not be allowed to run with.

Steering
	Example value:	(0,0.005,0.008,0.01)

	Penalties should typically only be used if the aid improves

Braking
	Example value:	(0,0.002,0.003)

	laptimes for a decent driver.

Invulnerable
	Example value:	(0,0.0001)

	Values are fractions of the total vehicle mass,

Opposite
	Example value:	(0,0.002)

	and are modeled as extra weight in the fuel tank.

SpinRecovery
	Example value:	(0,0.002)

	Do not use negative values.

AutoPit
	Example value:	(0,0.002)

	*no description provided*

AutoLift
	Example value:	(0,0.001)

	*no description provided*

AutoBlip
	Example value:	(0,0.004)

	*no description provided*

Front Wing - [FRONTWING]
========================

FWForceDistrib
	Example value:	(1.0:front_subbody)

	*no description provided*

FWRange
	Example value:	(8, 2, 1)

	front wing range

FWSetting
	Example value:	0

	front wing setting

FWMaxHeight
	Example value:	(0.3)

	maximum height to take account of for downforce

FWDragParams
	Example value:	( 0.012, 0.00123, 0.000000)

	base drag and 1st and 2nd order with setting

FWLiftParams
	Example value:	(-0.052,-0.00695, 0.000012)

	base lift and 1st and 2nd order with setting

FWLiftHeightPlus
	Example value:	(0.05, 0.3, 0.0)

	Half,1st,2nd order effects on lift with front wing height

FWNegRakeDrag
	Example value:	(-0.00, 0.000, 5.0)

	if rake is negative (nose up), use absolute value of rake angle: (coeff*degrees, coeff*degrees^2, maxDegrees)

FWPosRakeDrag
	Example value:	( 0.00,-0.000, 5.0)

	if rake is positive (nose down): (coeff*degrees, coeff*degrees^2, maxDegrees)

FWNegRakeLift
	Example value:	(-0.00, 0.000, 5.0)

	if rake is negative, use absolute value of rake angle: (coeff*degrees, coeff*degrees^2, maxDegrees)

FWPosRakeLift
	Example value:	( 0.00,-0.000, 5.0)

	if rake is positive: (coeff*degrees, coeff*degrees^2, maxDegrees)

FWLiftSideways
	Example value:	(0.31)

	dropoff in downforce with yaw (0.0 = none, 1.0 = max)

FWLiftPeakYaw
	Example value:	(3.0, 1.001)

	Angle of peak, multiplier at peak

FWDraftLiftMult
	Example value:	1.1

	Effect of draft on front wing's lift response (larger numbers will tend to decrease downforce when in the draft)

FWLeft
	Example value:	(-0.22, 0.02, 0.0)

	aero forces from moving left

FWRight
	Example value:	(0.22, 0.02, 0.0)

	aero forces from moving right

FWUp
	Example value:	(  0.0,-0.28,-0.020)

	aero forces from moving up

FWDown
	Example value:	(0.0, 0.28, 0.020)

	aero forces from moving down

FWAft
	Example value:	(0.0, 0.04,-0.04)

	aero forces from moving rearwards

FWFore
	Example value:	(0.0, 0.0, 0.0)

	aero forces from moving forwards (recomputed from settings)

FWRot
	Example value:	(0.10, 0.05, 0.15)

	aero torque from rotating

FWCenter
	Example value:	(0.00, 0.04,-0.68)

	center of front wing forces (offset from center of front axle in ref plane)

FlapDrag
	Example value:	(0.0,0.5)

	base drag when activated, multiplier by deactivated drag to add in

FlapLift
	Example value:	(0.0,0.7)

	base lift when activated, multiplier by deactivated lift to add in

FlapTimes
	Example value:	(0.1,0.12,0.1,0.13)

	visual activation, physical activation, visual deactivation, physical deactivation

FlapRules
	Example value:	(0.5,0.03)

	throttle threshold, brake threshold for automatic deactivation

Left Fender - [LEFTFENDER]
==========================

FenderFlareRange
	Example value:	(0, 0, 1)

	*no description provided*

FenderFlareSetting
	Example value:	0

	*no description provided*

FenderDragParams
	Example value:	( 0.016, 0.00, 0.000)

	Base, 1st, and 2nd order drag per meter flare

FenderLiftParams
	Example value:	(-0.055,-0.00, 0.000)

	Base, 1st, and 2nd order lift per meter flare

FenderDraftLiftMult
	Example value:	1.850

	Effect of draft on fender's lift response

FenderSideways
	Example value:	(0.445)

	Dropoff in downforce with yaw (0.0 = none, 1.0
	Example value:	max)

	*no description provided*


FenderPeakYaw
	Example value:	(3.00, 1.008)

	Angle of peak, multiplier at peak

FenderCenter
	Example value:	( 0.620, 0.300, 1.600)

	Center of fender forces (offset from center of front axle in ref plane)

Right Fender - [RIGHTFENDER]
============================

FenderFlareRange
	Example value:	(0, 0, 1)

	*no description provided*

FenderFlareSetting
	Example value:	0

	*no description provided*

FenderDragParams
	Example value:	( 0.016, 0.00, 0.000)

	Base, 1st, and 2nd order drag per meter flare

FenderLiftParams
	Example value:	(-0.055,-0.00, 0.000)

	Base, 1st, and 2nd order lift per meter flare

FenderDraftLiftMult
	Example value:	1.850

	Effect of draft on fender's lift response

FenderSideways
	Example value:	(0.445)

	Dropoff in downforce with yaw (0.0 = none, 1.0 = max)

FenderPeakYaw
	Example value:	(3.00, 1.008)

	Angle of peak, multiplier at peak

FenderCenter
	Example value:	(-0.620, 0.300, 1.600)

	Center of fender forces (offset from center of front axle in ref plane)

Rear Wing - [REARWING]
======================

RWForceDistrib
	Example value:	(1.0:rear_subbody)

	*no description provided*

RWRange
	Example value:	(0, 2, 1)

	rear wing range

RWSetting
	Example value:	0

	rear wing setting

RWDragParams
	Example value:	( 0.094, 0.0035, 1.0e-6)

	base drag and 1st and 2nd order with setting

RWLiftParams
	Example value:	(-0.00203,-0.0070, 4.60e-5)

	base lift and 1st and 2nd order with setting

RWDraftLiftMult
	Example value:	1.02

	Effect of draft on rear wing's lift response

RWLiftSideways
	Example value:	(0.370)

	Dropoff in downforce with yaw (0.0 = none, 1.0 = max)

RWLiftPeakYaw
	Example value:	(2.7, 1.001)

	Angle of peak, multiplier at peak

RWNegRakeDrag
	Example value:	(-0.00, 0.000, 5.0)

	if rake is negative, use absolute value of rake angle: (coeff*degrees, coeff*degrees^2, maxDegrees)

RWPosRakeDrag
	Example value:	( 0.00,-0.000, 5.0)

	if rake is positive: (coeff*degrees, coeff*degrees^2, maxDegrees)

RWNegRakeLift
	Example value:	(-0.00, 0.000, 5.0)

	if rake is negative, use absolute value of rake angle: (coeff*degrees, coeff*degrees^2, maxDegrees)

RWPosRakeLift
	Example value:	( 0.00,-0.000, 5.0)

	if rake is positive: (coeff*degrees, coeff*degrees^2, maxDegrees)

RWLeft
	Example value:	(-0.37, 0.02, 0.0)

	aero forces from moving left

RWRight
	Example value:	(0.37, 0.02, 0.0)

	aero forces from moving right

RWUp
	Example value:	(  0.0,-0.38,-0.002)

	aero forces from moving up

RWDown
	Example value:	(0.0, 0.38, 0.002)

	aero forces from moving down

RWAft
	Example value:	( 0.0, 0.08, -0.08)

	aero forces from moving rearwards

RWFore
	Example value:	(0.0, 0.0, 0.0)

	aero forces from moving forwards (recomputed from settings)

RWRot
	Example value:	(0.10, 0.05, 0.15)

	aero torque from rotating

RWCenter
	Example value:	(0.00, 0.69, 0.534)

	center of rear wing forces (offset from center of rear axle at ref plane)

FlapDrag
	Example value:	(0.0,0.5)

	base drag when activated, multiplier by deactivated drag to add in

FlapLift
	Example value:	(0.0,0.7)

	base lift when activated, multiplier by deactivated lift to add in

FlapTimes
	Example value:	(0.1,0.12,0.1,0.13)

	visual activation, physical activation, visual deactivation, physical deactivation

FlapRules
	Example value:	(0.5,0.03)

	throttle threshold, brake threshold for automatic deactivation

Body Aero - [BODYAERO]
======================

BodyAeroForceDistrib
	Example value:	(0.37:front_subbody:(0,0,-0.4),0.38:rear_subbody:(0,0,0.4),0.05:fl_spindle:(0.5,0,-1),0.05:fr_spindle:(-0.5,0,-1),0.075:rl_spindle:(0.5,0,1),0.075:rr_spindle:(-0.5,0,1))

	*no description provided*

BodyDragBase
	Example value:	(0.356)

	base drag

BodyDragHeightAvg
	Example value:	(-0.010)

	drag increase with average ride height

BodyDragHeightDiff
	Example value:	(0.218)

	drag increase with front/rear ride height difference

BodyMaxHeight
	Example value:	(0.20)

	maximum ride height that affects drag/lift

DraftBalanceMult
	Example value:	1.00

	Effect of draft on aerodynamic downforce balance of car (bigger numbers exaggerate the effect)

BodyDraftLiftMult
	Example value:	1.00

	Effect of draft on body's lift response

RadiatorDraftFract
	Example value:	1.00

	effect of draft on the radiator cooling, 0.0 (no effect) to 1.0 (full effect)

BodyNegRakeDrag
	Example value:	(-0.00, 0.000, 5.0)

	if rake is negative, use absolute value of rake angle: (coeff*degrees, coeff*degrees^2, maxDegrees)

BodyPosRakeDrag
	Example value:	( 0.00,-0.000, 5.0)

	if rake is positive: (coeff*degrees, coeff*degrees^2, maxDegrees)

BodyNegRakeLift
	Example value:	(-0.00, 0.000, 5.0)

	if rake is negative, use absolute value of rake angle: (coeff*degrees, coeff*degrees^2, maxDegrees)

BodyPosRakeLift
	Example value:	( 0.00,-0.000, 5.0)

	if rake is positive: (coeff*degrees, coeff*degrees^2, maxDegrees)

BodyLeft
	Example value:	(-0.55, 0.06, 0.00)

	aero forces from moving left

BodyRight
	Example value:	(0.55, 0.06, 0.00)

	aero forces from moving right

BodyUp
	Example value:	(  0.00,-1.15, 0.00)

	aero forces from moving up

BodyDown
	Example value:	(0.00, 1.15, 0.00)

	aero forces from moving down

BodyAft
	Example value:	( 0.00, 0.20,-0.85)

	aero forces from moving rearwards

BodyFore
	Example value:	(0.00, 0.063, 0.20)

	aero forces from moving forwards (lift value important, but drag overwritten)

BodyRot
	Example value:	(4.0, 3.0, 2.0)

	aero torque from rotating

BodyCenter
	Example value:	(0.0, 0.340,-1.110)

	center of body aero forces (offset from center of rear axle at ref plane)

RadiatorRange
	Example value:	(1.0, 1.0, 1)

	radiator range (front grille tape)

RadiatorSetting
	Example value:	0

	radiator setting

RadiatorDrag
	Example value:	(0.004)

	effect of radiator setting on drag

RadiatorLift
	Example value:	(0.002)

	effect of radiator setting on lift

BrakeDuctRange
	Example value:	(0.0, 1.0, 1)

	brake duct range

BrakeDuctSetting
	Example value:	0

	brake duct setting

BrakeDuctDrag
	Example value:	(0.001)

	effect of brake duct setting on drag

BrakeDuctLift
	Example value:	(0.001)

	effect of brake duct setting on lift

BaseDropoff
	Example value:	0.185

	RFM Drafting override: Higher number -> more drafting effect (default=0.185)

LeadingExponent
	Example value:	2.20

	RFM Drafting override: Higher number -> lower effect on leader (default=2.0)

FollowingExponent
	Example value:	2.20

	RFM Drafting override: Higher number -> lower effect on followers (default=2.0)

VehicleWidth
	Example value:	1.80

	RFM Drafting override: Helps determine base width of wake (default=1.9)

SideEffect
	Example value:	0.90

	RFM Drafting override: Negative effects of side-by-side drafting (default=0.35)

SideLeadingExponent
	Example value:	2.0

	RFM Drafting override: Added to regular LeadingExponent to affect the side wake

SideFollowingExponent
	Example value:	10.0

	RFM Drafting override: Added to regular FollowingExponent to affect the side wake

RoadModifierMults
	Example value:	(0.4,0.7)

	effect of aerodynamics on (marble_removal,water_removal) as a product of speed^2

Diffuser - [DIFFUSER]
=====================

DiffuserForceDistrib
	Example value:	(0.5:front_subbody:(0,0,-0.4),0.5:rear_subbody:(0,0,0.4))

	*no description provided*

DiffuserBasePlus
	Example value:	(-0.15, 0.01, 0.7, 1.9)

	Base lift, and Half,1st,2nd order with rear ride height

DiffuserFrontHeightPlus
	Example value:	(0.0, 0.2, 0.0, 0.1)

	Half,1st,2nd order with front ride height, and max height

DiffuserRake
	Example value:	( -0.000,-0.45, 2.0)

	Optimum rake (rear - front ride height), 1st order with current difference from opt, 2nd order

DiffuserLimits
	Example value:	(0.02, 0.11, 0.07)

	Min ride height before stalling begins (0.0=disabled), max rear ride height for computations, max rake difference for computations

DiffuserStall
	Example value:	(0.10, 0.50)

	Function to compute stall ride height (0.0=minimum, 1.0=average), downforce lost when bottoming out (0.0=none, 1.0=complete stall)

DiffuserDraftLiftMult
	Example value:	1.02

	Effect of draft on diffuser's lift response

DiffuserSideways
	Example value:	(0.355)

	Dropoff with yaw (0.0 = none, 1.0 = max)

DiffuserPeakYaw
	Example value:	(1.00, 1.001)

	Angle of peak, multiplier at peak

DiffuserCenter
	Example value:	(0.0, 0.00,-1.15)

	Center of diffuser forces (offset from center of rear axle at ref plane)

DiffuserOffsetZ
	Example value:	(0.000,-0.000)

	Rearward diffuser pressure movement with increase in ride height, and rake

Suspension - [SUSPENSION]
=========================

UltraChassis
	Example value:	SkipBarber_Chassis.ini

	If both .pm and UltraChassis lines are present, Ultrachassis will take precendence

PhysicalModelFile
	Example value:	SkipBarber.pm

	*no description provided*

ModelWheelsIncludeAllTireMass
	Example value:	1

	*no description provided*

CorrectedInnerSuspHeightAll
	Example value:	(0.20645,0.20645,0.2337,0.2337)

	inner susp height offset, correct usage is to subtract suspension design height (ground clearance) from static tire radius (-1 for original behavior)

ApplySlowToFastDampers
	Example value:	1

	whether to apply slow damper settings to fast damper settings

LimitFastDampers
	Example value:	1

	Whether to limit the fast damper rate to be less than or equal to the slow damper rate (actual rate, not numerical setting)

AdjustSuspRates
	Example value:	0

	Adjust suspension rates due to motion ratio (0 = direct measure of spring/damper rates, 1 = wheel rates)

AlignWheels
	Example value:	1

	correct for minor graphical offsets

CenterWheelsOnBodyX
	Example value:	0

	Correct for minor unintentional graphical offsets

FrontWheelTrackRange
	Example value:	(1.3525,0,1)

	if non-zero, forces the front wheels to be specified track width

FrontWheelTrackSetting
	Example value:	0

	*no description provided*

RearWheelTrackRange
	Example value:	(1.3146,0,1)

	if non-zero, forces the rear wheels to be specified track width

RearWheelTrackSetting
	Example value:	0

	*no description provided*

LeftWheelBase
	Example value:	2.458

	if non-zero, forces the left side to use specified wheelbase

RightWheelBase
	Example value:	2.458

	if non-zero, forces the right side to use specified wheelbase

FrontAntiSwayParams
	Example value:	(1, 0, 0)

	Whether antisway bar is (0=diameter-based or 1=spring-based, detachable, adjustable on the fly)

FrontAntiSwayBase
	Example value:	0.0

	Extra anti-sway from tube twisting

FrontAntiSwayRange
	Example value:	(35000, 4000, 1)

	Anti-sway rate to car center (asymmetric). This value should be half of what is provided in most car manuals (which generally use wheel to wheel rates)

FrontAntiSwaySetting
	Example value:	0

	*no description provided*

FrontAntiSwayRate
	Example value:	(1.36e11, 4.0)

	(base, power), so rate = base * (diameter in meters ^ power) (not applicable for spring-based antisway)

RearAntiSwayParams
	Example value:	(1, 0, 0)

	Whether antisway bar is (0=diameter-based or 1=spring-based, detachable, adjustable on the fly)

RearAntiSwayBase
	Example value:	0.0

	Extra anti-sway from tube twisting

RearAntiSwayRange
	Example value:	(10000, 4000, 8)

	*no description provided*

RearAntiSwaySetting
	Example value:	4

	*no description provided*

RearAntiSwayRate
	Example value:	(1.36e11, 4.0)

	not applicable with spring-based antisway

FrontToeInRange
	Example value:	(-0.2, 0.05, 51)

	*no description provided*

FrontToeInSetting
	Example value:	34

	*no description provided*

RearToeInRange
	Example value:	(0.0, 0.05, 51)

	*no description provided*

RearToeInSetting
	Example value:	31

	*no description provided*

LeftCasterRange
	Example value:	( 4.5, 0.25, 5)

	front-left caster

LeftCasterSetting
	Example value:	2

	*no description provided*

RightCasterRange
	Example value:	(4.5, 0.25, 5)

	front-right caster

RightCasterSetting
	Example value:	2

	*no description provided*

LeftTrackBarRange
	Example value:	( 0.0, 0.0, 1)

	Rear-left track bar

LeftTrackBarSetting
	Example value:	0

	*no description provided*

RightTrackBarRange
	Example value:	(0.0, 0.0, 1)

	Rear-right track bar

RightTrackBarSetting
	Example value:	0

	*no description provided*

Third Spring
------------

If the suspension has a third spring, the below parameters can be used to define
it. However, if there is no third spring you can leave these parameters commented
out or remove them from the HDV.

Front3rdBumpTravel
	Example value:	-0.000

	Travel to bumpstop with zero packers and zero ride height (5mm compression)

Front3rdReboundTravel
	Example value:	-0.055

	Prevents rebound travel (for example, when upside down), 55mm max front ride height plus 10mm leeway

Front3rdBumpStopSpring
	Example value:	60000

	Initial spring rate of bumpstop

Front3rdBumpStopRisingSpring
	Example value:	7.0e7

	Rising spring rate of bumpstop (multiplied by deflection squared)

Front3rdBumpStopDamper
	Example value:	2400

	Initial damping rate of bumpstop

Front3rdBumpStopRisingDamper
	Example value:	3.0e6

	Rising damper rate of bumpstop (multiplied by deflection squared)

Front3rdBumpStage2
	Example value:	0.060

	Speed where damper bump moves from slow to fast

Front3rdReboundStage2
	Example value:	-0.060

	Speed where damper rebound moves from slow to fast

Front3rdPackerRange
	Example value:	(0.005, 0.001, 41)

	*no description provided*

Front3rdPackerSetting
	Example value:	5

	*no description provided*

Front3rdSpringRange
	Example value:	(0, 2000, 51)

	*no description provided*

Front3rdSpringSetting
	Example value:	32

	*no description provided*

Front3rdSlowBumpRange
	Example value:	(0, 125, 25)

	*no description provided*

Front3rdSlowBumpSetting
	Example value:	6

	*no description provided*

Front3rdFastBumpRange
	Example value:	(0, 125, 21)

	*no description provided*

Front3rdFastBumpSetting
	Example value:	2

	*no description provided*

Front3rdSlowReboundRange
	Example value:	(0, 250, 33)

	*no description provided*

Front3rdSlowReboundSetting
	Example value:	4

	*no description provided*

Front3rdFastReboundRange
	Example value:	(0, 250, 29)

	*no description provided*

Front3rdFastReboundSetting
	Example value:	2

	*no description provided*

Rear3rdBumpTravel
	Example value:	-0.000

	Travel to bumpstop with zero packers and zero ride height (10mm compression)

Rear3rdReboundTravel
	Example value:	-0.090

	Prevents rebound travel (for example, when upside-down), 80mm max rear ride height plus 10mm leeway

Rear3rdBumpStopSpring
	Example value:	60000

	Initial spring rate of bumpstop

Rear3rdBumpStopRisingSpring
	Example value:	7.0e7

	Rising spring rate of bumpstop (multiplied by deflection squared)

Rear3rdBumpStopDamper
	Example value:	2400

	Initial damping rate of bumpstop

Rear3rdBumpStopRisingDamper
	Example value:	3.0e6

	Rising damper rate of bumpstop (multiplied by deflection squared)

Rear3rdBumpStage2
	Example value:	0.060

	Speed where damper bump moves from slow to fast

Rear3rdReboundStage2
	Example value:	-0.060

	Speed where damper rebound moves from slow to fast

Rear3rdPackerRange
	Example value:	(0.008, 0.001, 61)

	*no description provided*

Rear3rdPackerSetting
	Example value:	9

	*no description provided*

Rear3rdSpringRange
	Example value:	(60000, 2000, 106)

	*no description provided*

Rear3rdSpringSetting
	Example value:	15

	*no description provided*

Rear3rdSlowBumpRange
	Example value:	(3000, 125, 29)

	*no description provided*

Rear3rdSlowBumpSetting
	Example value:	12

	*no description provided*

Rear3rdFastBumpRange
	Example value:	(1500, 125, 25)

	*no description provided*

Rear3rdFastBumpSetting
	Example value:	8

	*no description provided*

Rear3rdSlowReboundRange
	Example value:	(5250, 250, 28)

	*no description provided*

Rear3rdSlowReboundSetting
	Example value:	15

	*no description provided*

Rear3rdFastReboundRange
	Example value:	(3000, 125, 29)

	*no description provided*

Rear3rdFastReboundSetting
	Example value:	12

	*no description provided*

Controls - [CONTROLS]
=====================

NominalMaxSteeringTorque
	Example value:	9.5

	Maximum steering arm torque to effect force feedback strength

TurnsLockToLock
	Example value:	1.13056

	Default steering wheel turns lock to lock

SteeringShaftBaseLeft
	Example value:	(0,-0.024786,-0.627603)

	Location of steering shaft relative to steering arm

SteeringShaftBaseRight
	Example value:	(0,-0.024786,-0.627603)

	*no description provided*

SteeringShaftAxis
	Example value:	(0.275637,0,-0.961262)

	*no description provided*

SteeringInnerTable
	Example value:	(0.34766,-0.0348,-0.624732):(-0.27484,-0.0348,-0.624732)

	Steering arm inner locations (left arm):(right arm) with maximum left steering application

SteeringInnerTable
	Example value:	(0.27484,-0.0348,-0.624732):(-0.34766,-0.0348,-0.624732)

	"" for maximum right application, more table entries can be added for non-linear steering or steering racks that don't move in a perfectly straight line

SteerLockCaption
	Example value:	"WHEEL RANGE (LOCK)"

	*no description provided*

SteerLockRange
	Example value:	(18.55,0,6)

	Maximum steering angle overridden by newer steering variables 'SteeringInnerTable' and SteeringFraction

SteerLockSetting
	Example value:	5

	*no description provided*

SteerLockSpecial=(0,"240 ","(11) deg","TurnsLockToLock=0.666667;SteeringFraction
	Example value:	0.589678")

	*no description provided*

SteerLockSpecial=(1,"270 ","(12) deg","TurnsLockToLock=0.75;SteeringFraction
	Example value:	0.663388")

	*no description provided*

SteerLockSpecial=(2,"310 ","(14) deg","TurnsLockToLock=0.861111;SteeringFraction
	Example value:	0.761668")

	*no description provided*

SteerLockSpecial=(3,"360 ","(16) deg","TurnsLockToLock=1;SteeringFraction
	Example value:	0.884517")

	*no description provided*

SteerLockSpecial=(4,"380 ","(17) deg","TurnsLockToLock=1.055556;SteeringFraction
	Example value:	0.933657")

	*no description provided*

SteerLockSpecial=(5,"407 ","(19) deg","TurnsLockToLock=1.13056;SteeringFraction
	Example value:	1")

	*no description provided*

SeatRangeLongitudinal
	Example value:	(-0.4,0.16)

	Eyepoint camera longitudinal adjustment range

SeatRangeVertical
	Example value:	(-0.07,0.04)

	Eyepoint camera vertical adjustment range

RearBrakeRange
	Example value:	(0.30, 0.005, 61)

	Rear brake balance fraction

RearBrakeSetting
	Example value:	28

	*no description provided*

BrakePressureRange
	Example value:	(0.60, 0.02, 21)

	*no description provided*

BrakePressureSetting
	Example value:	20

	*no description provided*

HandfrontbrakePressRange
	Example value:	(0.0, 0.1, 1)

	enable for front brake paddles

HandfrontbrakePressSetting
	Example value:	0

	*no description provided*

HandbrakePressRange
	Example value:	(0.00, 0.05, 1)

	Hand brake pressure. Handbrake4WDRelease represents the

HandbrakePressSetting
	Example value:	0

	handbrake value where the center diff will be completely disconnected.

Handbrake4WDRelease
	Example value:	2.0

	Start disconnecting at half this value, range is 0.0 (disconnect immediately with any handbrake) to 2.0 (default value, which will never even partially disconnect)

UpshiftAlgorithm
	Example value:	(0.995,0.0)

	Fraction of rev limit to auto-upshift, or rpm to shift at (if 0.0, uses rev limit algorithm)

DownshiftAlgorithm
	Example value:	(0.91,0.77,0.6)

	High gear downshift point, low gear downshift point, oval adjustment

AutoUpshiftGripThresh
	Example value:	0.35

	auto upshift waits until all driven wheels have this much grip (reasonable range: 0.4-0.9)

AutoDownshiftGripThresh
	Example value:	0.3

	auto downshift waits until all driven wheels have this much grip (reasonable range: 0.4-0.9)

TractionControlGrip
	Example value:	(1.4, 0.2)

	average driven wheel grip multiplied by 1st number, then added to 2nd

TractionControlLevel
	Example value:	(0.33, 1.0)

	effect of grip on throttle for low TC and high TC

ABS4Wheel
	Example value:	1

	0 = old-style single brake pulse, 1 = more effective 4-wheel ABS

ABSGrip
	Example value:	(2.0, 0.0)

	grip multiplied by 1st number and added to 2nd

ABSLevel
	Example value:	(0.31, 0.93)

	effect of grip on brakes for low ABS and high ABS

OnboardBrakeBias
	Example value:	0

	whether brake bias is allowed onboard

OnboardEngineBrakingMap
	Example value:	0

	Whether engine brake map is allowed onboard

PitcrewPushForce
	Example value:	750

	force that a pitcrew may use when in pitlane and out of fuel

MarshalPushForce
	Example value:	750

	force that a marshal may use when vehicle is apparently stuck

Engine - [ENGINE]
=================

Normal
	Example value:	SkipBarber_Engine

	engine file

GeneralTorqueMult*
	Example value:	0.93

	friction and non-optimal conditions (engine wear, etc)

GeneralPowerMult*
	Example value:	0.928

	*no description provided*

GeneralEngineBrakeMult*
	Example value:	1.0

	*no description provided*

TorqueCurveShift*
	Example value:	1.0

	*no description provided*

Driveline - [DRIVELINE]
=======================

.. note:: The SkipBarber has a Ricardo Sequential. Data below does suite this
	type of sequential.

EngineTorqueDistrib
	Example value:	(0.18:front_subbody,0.82:rear_subbody)

	*no description provided*

ClutchTorqueDistrib
	Example value:	(0.09:front_subbody,0.91:rear_subbody)

	*no description provided*

GearboxTorqueDistrib
	Example value:	(0.05:front_subbody,0.95:rear_subbody)

	*no description provided*

DifferentialTorqueDistrib
	Example value:	(1:rear_subbody)

	*no description provided*

ClutchEngineRPM
	Example value:	(1500,-1)

	clutch engagement state depends on engine speed range (-1 for second value to disable)

ClutchEngageRate
	Example value:	2.1

	How quickly clutch is engaged with auto-clutch driving aid

AIClutchEngageRate
	Example value:	2.1

	Override for AI only

ClutchInertia
	Example value:	0.0090

	Inertia of parts between clutch and transmission

ClutchTorque
	Example value:	230

	Maximum torque that can be transferred through clutch

ClutchWear
	Example value:	0.01

	Unimplemented

ClutchFriction
	Example value:	6.7

	Friction torque of parts between clutch and transmission when in gear (automatically reduced in neutral)

BaulkTorque
	Example value:	320

	Maximum torque transferred through gears while engaging them

AllowManualOverride
	Example value:	1

	Whether to allow manual shift overrides when using auto shifting

SemiAutomatic
	Example value:	0

	Whether throttle and clutch are operated automatically (1 full semi-auto for up and downshifts, 2 upshift only, 3 downshift only)

AntiStallLogic
	Example value:	(-1,1,10)

	User clutch level to deactivate (or special values -1=no anti-stall, 0="soft" anti-stall), max gear, time till ignition cut)

UpshiftDelay
	Example value:	0.120

	Delay in selecting higher gear (low for semi-automatic, higher for manual)

UpshiftClutchTime
	Example value:	0.000

	Time to ease auto-clutch in AFTER upshift

UpshiftLiftThrottle
	Example value:	0.01

	Lift to this throttle fraction while upshifting (if controlled by game not player))

DownshiftDelay
	Example value:	0.120

	Delay in selecting lower gear (low for semi-automatic, higher for manual)

DownshiftClutchTime
	Example value:	0.150

	Time to ease auto-clutch in AFTER downshift

DownshiftBlipThrottle
	Example value:	0.86

	Amount of throttle used to blip if controlled by game (instead of player)

WheelDrive
	Example value:	REAR

	Which wheels are driven: REAR, FOUR, or FRONT

GearFile
	Example value:	skipbarber_gears.ini

	Must come before final/reverse/gear settings (not relevant and in conflict if using 'special overrides' below)

AllowGearingChanges
	Example value:	0

	Whether to allow gear ratio changes (not relevant if using 'special overrides' below)

AllowFinalDriveChanges
	Example value:	0

	Whether to allow final drive ratio changes (not relevant if using 'special overrides' below)

AllowReverseAndNeutral
	Example value:	(1,1)

	whether to allow reverse (0 or 1), whether to allow neutral (0 or 1)

FinalDriveRange
	Example value:	(0,0,1)

	*no description provided*

FinalDriveSpecial
	Example value:	(0,,,"1,1,9,31")

	3.444

FinalDriveSetting
	Example value:	0

	Indexed into GearFile list

ForwardGears
	Example value:	5

	Number of forward gears available while driving (to a maximum of 9)

ReverseRange
	Example value:	(0,0,1)

	*no description provided*

ReverseSpecial
	Example value:	(0,,,"14,32")

	2.286

ReverseSetting
	Example value:	0

	*no description provided*

Gear1Range
	Example value:	(0,0,1)

	*no description provided*

Gear1Special
	Example value:	(0,,,"15,31")

	2.067

Gear1Setting
	Example value:	1

	*no description provided*

Gear2Range
	Example value:	(0,0,1)

	*no description provided*

Gear2Special
	Example value:	(0,,,"17,29")

	1.706

Gear2Setting
	Example value:	2

	*no description provided*

Gear3Range
	Example value:	(3,0,1)

	*no description provided*

Gear3Special
	Example value:	(0,,,"18,26")

	1.444

Gear3Setting
	Example value:	3

	*no description provided*

Gear4Range
	Example value:	(4,0,1)

	*no description provided*

Gear4Special
	Example value:	(0,,,"22,26")

	1.182

Gear4Setting
	Example value:	4

	*no description provided*

Gear5Range
	Example value:	(5,0,1)

	*no description provided*

Gear5Special
	Example value:	(0,,,"25,24")

	0.960

Gear5Setting
	Example value:	5

	*no description provided*

DiffPumpTorque
	Example value:	170

	at 100% pump diff setting, the torque redirected per wheelspeed difference in radians/sec (roughly 1.2kph)

DiffPumpRange
	Example value:	(0.004,0.00,1)

	differential acting on all driven wheels

DiffPumpSetting
	Example value:	0

	*no description provided*

DiffPowerRange
	Example value:	(0.0048,0.10,1)

	fraction of power-side input torque transferred through diff

DiffPowerSetting
	Example value:	0

	differential power setting

DiffCoastRange
	Example value:	(0.0048,0.10,1)

	fraction of coast-side input torque transferred through diff

DiffCoastSetting
	Example value:	0

	differential coast setting

DiffPreloadRange
	Example value:	(3.8, 1, 1)

	preload torque that must be overcome to have wheelspeed difference

DiffPreloadSetting
	Example value:	0

	preload setting

RearSplitRange
	Example value:	(1.00, 0.10, 1)

	Torque split to the rear, defaults to

RearSplitSetting
	Example value:	0

	50:50 if these entries aren't here.

Pump4WDEffect
	Example value:	(   0.0, 0.0, 1.0)

	Effect of various diff settings on

Power4WDEffect
	Example value:	(  0.0, 0.0, 1.0)

	the center diff, then the front diff,

Coast4WDEffect
	Example value:	(  0.0, 0.0, 1.0)

	and then the rear diff. Sorry, no

Preload4WDEffect
	Example value:	(0.0, 0.0, 1.0)

	separate settings for each diff.

Front Left - [FRONTLEFT]
========================

.. note:: The sections FRONTLEFT to REARRIGHT do all have the same parameters
  but the values are inverted (due to symmetry of the vehicle) or can  be
  different and inverted (due to asymmetric corners), depending on the vehicle.
  The explanation of the parameters in section are 99% the same and the only
  differ slightly due to further details in the "skipbarber.hdv" provided for
  each corner (e.g., rear bump travel is longer). So when looking for explanation
  of a parameter, you only have to look in [FRONTLEFT] (the section below).
  If expecting a difference at the rear, you may also look in :ref:`[REARLEFT] <REARLEFT>`.

BumpTravel
	Example value:	-0.000

	suspension travel upwards (base 0 ride height) (= 36mm Free bump travel - 52mm minimum static ride height = -16mm)

ReboundTravel
	Example value:	-0.120

	suspension travel downwards (base 0 ride height) (= -28mm Free rebound travel - 92mm maximum Static ride height = -120mm)

BumpStopTravels
	Example value:	(-0.0,-0.12)

	suspension travel (upwards, downwards)

BumpStopSpring
	Example value:	40000

	initial spring rate of bumpstop

BumpStopRisingSpring
	Example value:	1.20e8

	rising spring rate of bumpstop (multiplied by deflection squared)

BumpStopDamper
	Example value:	2000

	initial damping rate of bumpstop

BumpStopRisingDamper
	Example value:	4.00e6

	rising damper rate of bumpstop (multiplied by deflection squared)

FrictionTorque
	Example value:	1.98

	Newton-meters of friction between spindle and wheel

CGOffsetX
	Example value:	0.0

	x-offset from graphical center to physical center (NOT IMPLEMENTED)

PushrodOutboard
	Example value:	(1:FL_SPINDLE:(0.017,-0.10175,-0.0056))

	spring/damper connection to spindle or axle (relative to sub-body)

PushrodBody
	Example value:	(-0.461, 0.140, -0.0056)

	spring/damper connection to body (relative to wheel center)

CamberRange
	Example value:	(-3.5, 0.1, 36)

	*no description provided*

CamberSetting
	Example value:	13

	*no description provided*

PressureRange
	Example value:	(137.895146, 1.7236893, 81)

	*no description provided*

PressureSetting
	Example value:	48

	*no description provided*

PackerRange
	Example value:	(0.0127, 0.001, 1)

	*no description provided*

PackerSetting
	Example value:	0

	*no description provided*

SpringMult
	Example value:	1.00

	take into account suspension motion if spring is not attached to spindle (affects physics but not garage display)

SpringRange
	Example value:	(96757.577, 5000, 1)

	74428.9052

SpringSpecial
	Example value:	(0,425,"lb/in",)

	*no description provided*

SpringSetting
	Example value:	0

	*no description provided*

SpringRubberRange
	Example value:	(5000, 5000, 1)

	Spring rubbers can potentially be changed at pitstops if available, first value is automatically detached

SpringRubberSetting
	Example value:	0

	*no description provided*

RideHeightRange
	Example value:	(0.053975, 0.0015875, 25)

	*no description provided*

RideHeightSetting
	Example value:	18

	*no description provided*

BumpStage2
	Example value:	0.017

	speed where damper bump moves from slow to fast

ReboundStage2
	Example value:	-0.0203

	speed where damper rebound moves from slow to fast

DamperMult
	Example value:	1.00

	take into account suspension motion if damper is not attached to spindle (affects physics but not garage display)

SlowBumpRange
	Example value:	(7000, 100, 1)

	*no description provided*

SlowBumpSetting
	Example value:	0

	*no description provided*

FastBumpRange
	Example value:	(3050, 100, 1)

	*no description provided*

FastBumpSetting
	Example value:	0

	*no description provided*

SlowReboundRange
	Example value:	(7000, 250, 1)

	*no description provided*

SlowReboundSetting
	Example value:	0

	*no description provided*

FastReboundRange
	Example value:	(2600, 250, 1)

	*no description provided*

FastReboundSetting
	Example value:	0

	*no description provided*

BrakeDiscRange
	Example value:	(0.020, 0.000, 1)

	disc thickness

BrakeDiscSetting
	Example value:	0

	*no description provided*

BrakePadRange
	Example value:	(0, 1, 1)

	pad type (not implemented)

BrakePadSetting
	Example value:	0

	*no description provided*

BrakeDiscInertia
	Example value:	2.029

	inertia per meter of thickness

BrakeResponseCurve
	Example value:	(-130,265,560,1065)

	Cold temperature in Celcius (where brake torque is half optimum), min temp for optimum brake torque, max temp for optimum brake torque, and overheated temperature (where brake torque is half optimum)

BrakeWearRate
	Example value:	1.2e-11

	meters of wear per second at optimum temperature

BrakeFailure
	Example value:	(0.0125,7.0e-4)

	average and variation in disc thickness at failure

BrakeTorque
	Example value:	1401

	maximum brake torque at optimum temp

BrakeTorqueAI
	Example value:	1381

	Different brake torque for AI, as they are not currently affected by cold or faded brakes

BrakeHeating
	Example value:	0.00127

	heat added linearly with brake torque times wheel speed (at max disc thickness)

BrakeCooling
	Example value:	(0.0189,1.9e-4)

	minimum brake cooling rate (base and per unit velocity) (at max disc thickness)

BrakeDuctCooling
	Example value:	2.0e-4

	brake cooling rate per brake duct setting (at max disc thickness)

BrakeGlow
	Example value:	(550,900)

	Temperature range (in Celsius) that brake glow ramps up

Front Right - [FRONTRIGHT]
==========================

BumpStopTravels
	Example value:	(-0.0,-0.12)

	suspension travel (upwards, downwards)

BumpStopSpring
	Example value:	40000

	initial spring rate of bumpstop

BumpStopRisingSpring
	Example value:	1.2e8

	rising spring rate of bumpstop (multiplied by deflection squared)

BumpStopDamper
	Example value:	2000

	initial damping rate of bumpstop

BumpStopRisingDamper
	Example value:	4.0e6

	rising damper rate of bumpstop (multiplied by deflection squared)

FrictionTorque
	Example value:	1.98

	Newton-meters of friction between spindle and wheel

CGOffsetX
	Example value:	0.0

	x-offset from graphical center to physical center (NOT IMPLEMENTED)

PushrodOutboard
	Example value:	(1:FR_SPINDLE:(-0.017,-0.10175,-0.0056))

	*no description provided*

PushrodBody
	Example value:	( 0.461, 0.140, -0.0056)

	spring/damper connection to body (relative to wheel center)

CamberRange
	Example value:	(-3.5, 0.1, 36)

	*no description provided*

CamberSetting
	Example value:	13

	*no description provided*

PressureRange
	Example value:	(137.895146, 1.7236893, 81)

	*no description provided*

PressureSetting
	Example value:	48

	*no description provided*

PackerRange
	Example value:	(0.0127, 0.001, 1)

	*no description provided*

PackerSetting
	Example value:	0

	*no description provided*

SpringMult
	Example value:	1.0

	take into account suspension motion if spring is not attached to spindle (affects physics but not garage display)

SpringRange
	Example value:	(96757.577, 5000, 1)

	*no description provided*

SpringSpecial
	Example value:	(0,425,"lb/in",)

	*no description provided*

SpringSetting
	Example value:	0

	*no description provided*

SpringRubberRange
	Example value:	(5000, 5000, 1)

	Spring rubbers can potentially be changed at pitstops if available, first value is automatically detached

SpringRubberSetting
	Example value:	0

	*no description provided*

RideHeightRange
	Example value:	(0.053975, 0.0015875, 25)

	*no description provided*

RideHeightSetting
	Example value:	18

	*no description provided*

BumpStage2
	Example value:	0.017

	speed where damper bump moves from slow to fast

ReboundStage2
	Example value:	-0.0203

	speed where damper rebound moves from slow to fast

DamperMult
	Example value:	1.0

	take into account suspension motion if damper is not attached to spindle (affects physics but not garage display)

SlowBumpRange
	Example value:	(7000, 100, 1)

	*no description provided*

SlowBumpSetting
	Example value:	0

	*no description provided*

FastBumpRange
	Example value:	(3050, 100, 1)

	*no description provided*

FastBumpSetting
	Example value:	0

	*no description provided*

SlowReboundRange
	Example value:	(7000, 250, 1)

	*no description provided*

SlowReboundSetting
	Example value:	0

	*no description provided*

FastReboundRange
	Example value:	(2600, 250, 1)

	*no description provided*

FastReboundSetting
	Example value:	0

	*no description provided*

BrakeDiscRange
	Example value:	(0.02, 0.000, 1)

	disc thickness

BrakeDiscSetting
	Example value:	0

	*no description provided*

BrakePadRange
	Example value:	(0, 1, 1)

	pad type (not implemented)

BrakePadSetting
	Example value:	0

	*no description provided*

BrakeDiscInertia
	Example value:	2.029

	inertia per meter of thickness

BrakeResponseCurve
	Example value:	(-130,265,560,1065)

	Cold temperature in Celcius (where brake torque is half optimum), min temp for optimum brake torque, max temp for optimum brake torque, and overheated temperature (where brake torque is half optimum)

BrakeWearRate
	Example value:	1.2e-11

	meters of wear per second at optimum temperature

BrakeFailure
	Example value:	(0.0125,7.0e-4)

	average and variation in disc thickness at failure

BrakeTorque
	Example value:	1401

	maximum brake torque at optimum temp

BrakeTorqueAI
	Example value:	1381

	Different brake torque for AI, as they are not currently affected by cold or faded brakes

BrakeHeating
	Example value:	0.00127

	heat added linearly with brake torque times wheel speed (at max disc thickness)

BrakeCooling
	Example value:	(0.0189,1.90e-4)

	minimum brake cooling rate (base and per unit velocity) (at max disc thickness)

BrakeDuctCooling
	Example value:	2.0e-4

	brake cooling rate per brake duct setting (at max disc thickness)

BrakeGlow
	Example value:	(550,900)

	Temperature range (in Celsius) that brake glow ramps up

.. _REARLEFT:

Rear Left - [REARLEFT]
======================

BumpTravel
	Example value:	-0.000

	suspension travel upwards (= 40mm Free bump travel - 60mm minimum static ride height = -20mm)

ReboundTravel
	Example value:	-0.130

	suspension travel downwards (= - 50mm Free rebound travel - 80mm maximum Static ride height = -130mm)

BumpStopTravels
	Example value:	(-0.0,-0.13)

	suspension travel (upwards, downwards)

BumpStopSpring
	Example value:	40000

	initial spring rate of bumpstop

BumpStopRisingSpring
	Example value:	1.2e8

	rising spring rate of bumpstop (multiplied by deflection squared)

BumpStopDamper
	Example value:	2000

	initial damping rate of bumpstop

BumpStopRisingDamper
	Example value:	4.0e6

	rising damper rate of bumpstop (multiplied by deflection squared)

FrictionTorque
	Example value:	4.19

	Newton-meters of friction between spindle and wheel

CGOffsetX
	Example value:	-0.0

	x-offset from graphical center to physical center (NOT IMPLEMENTED)

PushrodSpindle
	Example value:	(-0.12,-0.14,-0.05)

	spring/damper connection to spindle or axle (relative to wheel center)

PushrodBody
	Example value:	(-0.413, 0.1100455,-0.05)

	spring/damper connection to body (relative to wheel center)

CamberRange
	Example value:	(-3.5, 0.1, 36)

	*no description provided*

CamberSetting
	Example value:	15

	*no description provided*

PressureRange
	Example value:	(137.895146, 1.7236893, 81)

	*no description provided*

PressureSetting
	Example value:	56

	*no description provided*

PackerRange
	Example value:	(0.0127, 0.001, 1)

	*no description provided*

PackerSetting
	Example value:	0

	*no description provided*

SpringMult
	Example value:	1.0

	take into account suspension motion if spring is not attached to spindle (affects physics but not garage display)

SpringRange
	Example value:	(96757.577, 5000, 1)

	*no description provided*

SpringSpecial
	Example value:	(0,425,"lb/in",)

	*no description provided*

SpringSetting
	Example value:	0

	*no description provided*

SpringRubberRange
	Example value:	(5000, 5000, 1)

	Spring rubbers can potentially be changed at pitstops if available, first value is automatically detached

SpringRubberSetting
	Example value:	0

	*no description provided*

RideHeightRange
	Example value:	(0.0635, 0.0015875, 12)

	*no description provided*

RideHeightSetting
	Example value:	8

	*no description provided*

BumpStage2
	Example value:	0.0167

	speed where damper bump moves from slow to fast

ReboundStage2
	Example value:	-0.0381

	speed where damper rebound moves from slow to fast

DamperMult
	Example value:	1.0

	take into account suspension motion if damper is not attached to spindle (affects physics but not garage display)

SlowBumpRange
	Example value:	(9250, 100, 1)

	*no description provided*

SlowBumpSetting
	Example value:	0

	*no description provided*

FastBumpRange
	Example value:	(2200, 100, 1)

	*no description provided*

FastBumpSetting
	Example value:	0

	*no description provided*

SlowReboundRange
	Example value:	(15000, 250, 1)

	*no description provided*

SlowReboundSetting
	Example value:	0

	*no description provided*

FastReboundRange
	Example value:	(5250, 250, 1)

	*no description provided*

FastReboundSetting
	Example value:	0

	*no description provided*

BrakeDiscRange
	Example value:	(0.020, 0.000, 1)

	disc thickness

BrakeDiscSetting
	Example value:	0

	*no description provided*

BrakePadRange
	Example value:	(0, 1, 1)

	pad type (not implemented)

BrakePadSetting
	Example value:	0

	*no description provided*

BrakeDiscInertia
	Example value:	2.029

	inertia per meter of thickness

BrakeResponseCurve
	Example value:	(-130,265,560,1065)

	Cold temperature in Celcius (where brake torque is half optimum), min temp for optimum brake torque, max temp for optimum brake torque, and overheated temperature (where brake torque is half optimum)

BrakeWearRate
	Example value:	1.2e-11

	meters of wear per second at optimum temperature

BrakeFailure
	Example value:	(0.0125,7.0e-4)

	average and variation in disc thickness at failure

BrakeTorque
	Example value:	1401

	maximum brake torque at optimum temp

BrakeTorqueAI
	Example value:	1381

	Different brake torque for AI, as they are not currently affected by cold or faded brakes

BrakeHeating
	Example value:	0.00127

	heat added linearly with brake torque times wheel speed (at max disc thickness)

BrakeCooling
	Example value:	(0.0176,1.47e-4)

	minimum brake cooling rate (base and per unit velocity) (at max disc thickness)

BrakeDuctCooling
	Example value:	1.2e-4

	brake cooling rate per brake duct setting (at max disc thickness)

BrakeGlow
	Example value:	(550,900)

	Temperature range (in Celsius) that brake glow ramps up

Rear Right - [REARRIGHT]
========================

BumpStopTravels
	Example value:	(-0.0,-0.13)

	suspension travel (upwards, downwards)

BumpStopSpring
	Example value:	40000

	initial spring rate of bumpstop

BumpStopRisingSpring
	Example value:	1.2e8

	rising spring rate of bumpstop (multiplied by deflection squared)

BumpStopDamper
	Example value:	2000

	initial damping rate of bumpstop

BumpStopRisingDamper
	Example value:	4.0e6

	rising damper rate of bumpstop (multiplied by deflection squared)

FrictionTorque
	Example value:	4.19

	Newton-meters of friction between spindle and wheel

CGOffsetX
	Example value:	0.0

	x-offset from graphical center to physical center (NOT IMPLEMENTED)

PushrodSpindle
	Example value:	( 0.120,-0.140,-0.05)

	spring/damper connection to spindle or axle (relative to wheel center)

PushrodBody
	Example value:	(0.413, 0.1100455,-0.05)

	spring/damper connection to body (relative to wheel center)

CamberRange
	Example value:	(-3.5, 0.1, 36)

	*no description provided*

CamberSetting
	Example value:	15

	*no description provided*

PressureRange
	Example value:	(137.895146, 1.7236893, 81)

	*no description provided*

PressureSetting
	Example value:	56

	*no description provided*

PackerRange
	Example value:	(0.0127, 0.001, 1)

	*no description provided*

PackerSetting
	Example value:	0

	*no description provided*

SpringMult
	Example value:	1.0

	take into account suspension motion if spring is not attached to spindle (affects physics but not garage display)

SpringRange
	Example value:	(96757.577, 5000, 1)

	*no description provided*

SpringSpecial
	Example value:	(0,425,"lb/in",)

	*no description provided*

SpringSetting
	Example value:	0

	*no description provided*

SpringRubberRange
	Example value:	(5000, 5000, 1)

	Spring rubbers can potentially be changed at pitstops if available, first value is automatically detached

SpringRubberSetting
	Example value:	0

	*no description provided*

RideHeightRange
	Example value:	(0.0635, 0.0015875, 12)

	*no description provided*

RideHeightSetting
	Example value:	8

	*no description provided*

BumpStage2
	Example value:	0.0167

	speed where damper bump moves from slow to fast

ReboundStage2
	Example value:	-0.0381

	speed where damper rebound moves from slow to fast

DamperMult
	Example value:	1.0

	take into account suspension motion if damper is not attached to spindle (affects physics but not garage display)

SlowBumpRange
	Example value:	(9250, 100, 1)

	*no description provided*

SlowBumpSetting
	Example value:	0

	*no description provided*

FastBumpRange
	Example value:	(2200, 100, 1)

	*no description provided*

FastBumpSetting
	Example value:	0

	*no description provided*

SlowReboundRange
	Example value:	(15000, 250, 1)

	*no description provided*

SlowReboundSetting
	Example value:	0

	*no description provided*

FastReboundRange
	Example value:	(5250, 250, 1)

	*no description provided*

FastReboundSetting
	Example value:	0

	*no description provided*

BrakeDiscRange
	Example value:	(0.020, 0.000, 1)

	disc thickness

BrakeDiscSetting
	Example value:	0

	*no description provided*

BrakePadRange
	Example value:	(0, 1, 1)

	pad type (not implemented)

BrakePadSetting
	Example value:	0

	*no description provided*

BrakeDiscInertia
	Example value:	2.029

	inertia per meter of thickness

BrakeResponseCurve
	Example value:	(-130,265,560,1065)

	Cold temperature in Celcius (where brake torque is half optimum), min temp for optimum brake torque, max temp for optimum brake torque, and overheated temperature (where brake torque is half optimum)

BrakeWearRate
	Example value:	1.2e-11

	meters of wear per second at optimum temperature

BrakeFailure
	Example value:	(0.0125,7.0e-4)

	average and variation in disc thickness at failure

BrakeTorque
	Example value:	1401

	maximum brake torque at optimum temp

BrakeTorqueAI
	Example value:	1381

	Different brake torque for AI, as they are not currently affected by cold or faded brakes

BrakeHeating
	Example value:	0.00127

	heat added linearly with brake torque times wheel speed (at max disc thickness)

BrakeCooling
	Example value:	(0.0176,1.47e-4)

	minimum brake cooling rate (base and per unit velocity) (at max disc thickness)

BrakeDuctCooling
	Example value:	1.2e-4

	brake cooling rate per brake duct setting (at max disc thickness)

BrakeGlow
	Example value:	(550,900)

	Temperature range (in Celsius) that brake glow ramps up
