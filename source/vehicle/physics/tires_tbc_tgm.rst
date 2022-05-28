.. warning::

  This page is WIP.

.. sidebar:: Source

  Source of the information and descriptions herein were extracted from
  "SkipBarber.tbc" and "BFGoodrich_g-ForceSport_195-55-R15x7.tgm" files of the
  SkipBarber that comes with the Dev Mode of rFactor2 game version v1121.
  Where necessary and available, information and descriptions were amended.

#####
Tires
#####

.. contents:: Contents
  :depth: 2
  :local:

***
TBC
***

Tire brand found in \*.hdv files refer to file name.

The TBC is primarily for AI use, although some things are still used to define
player physics.

Slip curves do not represent the coefficient of grip. Instead they represent the
reaction to the current slip. Regardless of the peak value in this curve, it
will be automatically normalized to have a peak of 1.0.

The peak of the slip curve is dynamically adjusted to higher or lower slip
values based on current load and speed. The second value of "SpeedEffects" is an
equivalency value for load and speed. To calculate the slip peak, we use the
following input which is a combination of load and speed: <load/speed
combination> = <load> + (<speed> * <equivalency>) Obviously a larger equivalency
value will make speed a more dominant factor in the calculation of the peak. See
the SpeedEffects, LatPeak, and LongPeak tire parameters for more info.

Slip curve data points are connected using a cubic spline, so there is no
need to use a massive amount of data points unless the curve is really busy.

Lateral slip angles are normalized so that you need to take the sine of the
angle to get the slip. For example, 12 degrees is a slip of 0.208 and vice
versa. Longitudinal slip ratios closely match the SAE definition.

All curves should probably go out to at least a slip of 2.0, even the lateral
and braking curves. Although locking up your brakes is a slip of 1.0, there
are situations where you can spin your wheels in the opposite direction of your
velocity (like shifting into reverse while moving forwards).

Note that the initial slope of the curve may have an effect on how some
features behave, such as traction control, ABS, skids, and tire smoke.

The "DropoffFunction" is a new feature in the :ref:`[SLIPCURVE]<tbc-slipcurve>`
section. It describes how the slip curve dropoff is affected when the peak of
the slip curve changes. The peak of the slip curve may move to a smaller or
larger slip when load or speed changes. When this happens, the slip curve is
stretched or shrunk to match.

The "DropoffFunction" parameter allows you to affect the behavior beyond the
peak when this happens:

  -1.0 = dropoff occurs faster when peak increases

  0.0 = dropoff curve does NOT change shape when the peak changes

  1.0 = dropoff curve is stretched or shrunk with the rest of the curve,
  which means the dropoff may feel more gradual as the peak increases. This
  is the default.

Note that you can pick in-between values for a blend of behaviors.

.. _tbc-slipcurve:

[SLIPCURVE]
===========

Name
  Example value:	"Default"

  *No description provided*

Step
	Example value:	0.009

	Slip step

DropoffFunction
	Example value:	0.00

	See explanation above

Data
  Example value:	0.000000 0.174836 0.349483 0.518060 0.668882 0.790665 0.878928

  *No description provided*

  Skippy example data:

  .. code-block::

    Data:
    0.000000 0.174836 0.349483 0.518060 0.668882 0.790665 0.878928 0.936783 0.971287 0.989751
    0.997978 1.000000 0.999947 0.999795 0.999544 0.999195 0.998749 0.998206 0.997567 0.996835
    0.996010 0.995094 0.994089 0.992997 0.991821 0.990562 0.989222 0.987806 0.986315 0.984752
    0.983119 0.981420 0.979659 0.977836 0.975957 0.974023 0.972039 0.970006 0.967929 0.965810
    0.963652 0.961458 0.959232 0.956976 0.954693 0.952385 0.950057 0.947709 0.945345 0.942968
    0.940580 0.938182 0.935778 0.933370 0.930959 0.928548 0.926139 0.923733 0.921332 0.918938
    0.916552 0.914176 0.911811 0.909458 0.907120 0.904796 0.902488 0.900196 0.897923 0.895668
    0.893433 0.891218 0.889024 0.886851 0.884700 0.882571 0.880466 0.878383 0.876324 0.874289
    0.872278 0.870291 0.868329 0.866391 0.864478 0.862590 0.860727 0.858888 0.857074 0.855285
    0.853521 0.851781 0.850066 0.848375 0.846708 0.845065 0.843446 0.841851 0.840280 0.838731
    0.837206 0.835704 0.834224 0.832767 0.831331 0.829918 0.828526 0.827156 0.825807 0.824478
    0.823170 0.821882 0.820615 0.819367 0.818138 0.816929 0.815738 0.814566 0.813413 0.812277
    0.811159 0.810059 0.808976 0.807909 0.806860 0.805827 0.804810 0.803809 0.802823 0.801853
    0.800898 0.799958 0.799033 0.798121 0.797224 0.796341 0.795472 0.794616 0.793773 0.792943
    0.792126 0.791321 0.790529 0.789749 0.788981 0.788224 0.787479 0.786745 0.786022 0.785310
    0.784609 0.783918 0.783238 0.782568 0.781908 0.781257 0.780617 0.779985 0.779364 0.778751
    0.778147 0.777552 0.776965 0.776388 0.775818 0.775257 0.774704 0.774159 0.773621 0.773092
    0.772570 0.772055 0.771547 0.771047 0.770554 0.770068 0.769588 0.769115 0.768649 0.768189
    0.767736 0.767289 0.766848 0.766413 0.765984 0.765560 0.765143 0.764731 0.764325 0.763924
    0.763528 0.763138 0.762753 0.762373 0.761998 0.761629 0.761263 0.760903 0.760548 0.760197
    0.759850 0.759508 0.759171 0.758837 0.758508 0.758184 0.757863 0.757546 0.757234 0.756925
    0.756620 0.756320 0.756022 0.755729 0.755439 0.755153 0.754870 0.754591 0.754315 0.754042
    0.753773 0.753507 0.753244 0.752985 0.752728 0.752475 0.752224 0.751977 0.751732 0.751491
    0.751252 0.751016 0.750783 0.750552 0.750324 0.750099 0.750000

Note that the dry and wet performance numbers are NOT relative.

They will still be scaled by the terrain dry/wet values in terrain.tdf.

For example, if normal pavement has the scaling parameters dry=1.0 and wet=0.8,
and a rain tire has scaling parameters of dry=1.30 and wet=1.35, then the overall
grip in the dry will be (1.0 * 1.30) = 1.3, while the overall grip in the wet
will be (0.8 * 1.35) = 1.08.

FYI - we may add "Compound" to each name in order to translate it, because
these names are not necessarily unique to tire compounds.

.. _tbc-compound:

[COMPOUND]
==========

Name
  Example value:	"Treaded"

  *No description provided*

WetWeather
  Example value:	1

  *No description provided*

ARGUMENT
  Example value:	FRONT

  Arguments: ALL, FRONT, REAR, LEFT, RIGHT, FRONTLEFT, FRONTRIGHT, REARLEFT,
  REARRIGHT

TGM
  Example value:	"BFGoodrich_g-ForceSport_195-55-R15x7"

  Physical tire model (\*.tgm) file

DryLatLong
  Example value:	(1.29, 1.28)

  Lateral/longitudinal coefficients in dry weather

WetLatLong
  Example value:	(1.24, 1.22)

  Lateral/longitudinal coefficients in wet weather

RoadGripEffects
  Example value:	(0.09,-0.06,-0.0,-0.25)

  Effect of maximum (<groove>,<marbles>,<dampness>,<wetness>) on grip, where
  dampness is fully saturated before standing water and wetness represents
  maximum standing water

RoadSqrdGripEffects
  Example value:	-0.01

  Effect of <groove>\*<groove> on grip

RoadModifierMults
  Example value:	(1.0,1.0,1.0,1.0)

  Multipliers for the tires' effect on (<groove_addition>,<marble_removal>,
  <marble_addition>,<water_removal>)

Radius
  Example value:	0.2957

  Radius of tire

RadiusRPM
  Example value:	2.01e-6

  Increased radius per unit RPM

Width
  Example value:	0.1956

  Width of tire

Rim
  Example value:	(0.2074, 850000, 6800, 3.0)

  Rim radius, spring rate, damper rate, minimum velocity to produce sparks

SpringBase
  Example value:	41406

  Base spring rate with no pressure

SpringkPa
  Example value:	640

  Spring rate per unit pressure

Damper
  Example value:	720

  Damping rate of tire

SpeedEffects
  Example value:	(753,-0.5)

  Speed at which grip drops to half (m/s, 0.0 to disable), speed load
  equivalency (see above)

LoadSensLat
  Example value:	( -4.0e-5, 0.51, 17100)

  Load sensitivity for lateral grip (initial slope, final grip multiplier,
  final load)

LoadSensLong
  Example value:	(-2.8e-5, 0.59, 17100)

  Load sensitivity for longitudinal grip (initial slope, final grip multiplier,
  final load)

LatPeak
  Example value:	( 0.137, 0.203, 9250)

  Slip range where lateral peak force occurs depending on load

LongPeak
  Example value:	(0.117, 0.166, 9250)

  Slip range where longitudinal peak force occurs depending on load

LatCurve
  Example value:	"Default"

  Slip angle curve (data uses normalized angle)

BrakingCurve
  Example value:	"Default"

  Slip ratio curve under braking

TractiveCurve
  Example value:	"Default"

  Slip ratio curve under acceleration

CamberLatLong
  Example value:	(3.3, 0.07, 0.41)

  Peak camber angle, lateral gain at peak, longitudinal loss at 90 degrees

RollingResistance
  Example value:	580

  Resistance torque (Nm) per unit deflection (m) on ground

PneumaticTrail
  Example value:	6.0e-6

  Pneumatic trail per unit load (m/N), adjusted based on slip

HeatBasePeak
  Example value:	(0.2, 0.01)

  Base peak slip to compute friction heat, fraction of base to use (0.0=use
  dynamic peak slip only)

Heating
  Example value:	(1.0, 0.0165)

  Heat caused by (rolling, friction)

Transfer
  Example value:	(0.025, 0.0019, 3.50e-4)

  Heat transfer to (road, static air, moving air)

HeatDistrib
  Example value:	(9.5,100)

  (Max camber angle, max off-pressure) that affects heat distribution (higher
  number -> less temperature difference)

AirTreadRate
  Example value:	0.003

  Heat transfer between tread and inside air

WearRate
  Example value:	1.50e-7

  Wear rate constant

WearGrip1
  Example value:	(0.998,0.990,0.985,0.982,0.979,0.976,0.973,0.970)

  Grip at 6/13/19/25/31/38/44/50% wear (defaults to 0.980->0.844), grip is
  1.0 at 0% wear

WearGrip2
  Example value:	(0.967,0.964,0.961,0.956,0.948,0.932,0.860,0.760)

  Grip at 56/63/69/75/81/88/94/100% wear (defaults to 0.824->0.688), tire
  bursts at 100% wear

Softness
  Example value:	0.6

  Softness is now just for AI strategic use

AIGripMult
  Example value:	1.00

  Grip multiplier for AI vehicles (due to tire model simplification)

AIHeatRate
  Example value:	7.5e-6

  Heating rate constant for AI tires (default: 6.6e-6)

AIPitThreshold
  Example value:	0.85

  Remaining grip threshold before AI schedule to stop for fresh tires

Temperatures
  Example value:	(80, 22)

  Optimum operating temperature for peak forces (Celsius), starting
  temperature

OptimumPressure
  Example value:	(190, 0.027)

  Base pressure to remain flat on ground at zero deflection, and multiplier
  by load to stay flat on ground

GripTempPress
  Example value:	(0.85, 0.54, 0.4)

  Grip effects of being below temp, above temp, and off-pressure (higher
  number -> faster grip dropoff

***
TGM
***

The physical tire model (\*.tgm) that is used to define player physics. Some
things from the TBC file are still used to further define player physics.

[QuasiStaticAnalysis]
=====================

NumLayers
  Example value:	2

  Number of layers in the tyre, at present, this must be 2 or ttool will crash

NumSections
  Example value:	132

  Number of layers in the tyre, must be at least 2 or ttool will crash, 3 should provide more accurate behaviour however becomes computationally expensive

RimVolume
  Example value:	0.01589

  Volume of air (m^3) of wheel rim, used to determine actual tire volume

DisplaceBulkMassWithPly
  Example value:	1

  Whether plies displace existing bulk materials when calculating masses

PlyCompressionTensionTransition
  Example value:	(-0.002,0.0001)

  Strain to use compressive or tension modulus. Negative values represent compression.

RealtimeCamberLimit
  Example value:	45

  Angle limit (in degrees) for bristle positioning.  Higher values compromise driving under normal conditions but will provide superior results when driving on 2 wheels for example.  Note this does not effect the QSA model as bristle positions are generated by the real time model.

GaugePressure
  Example value:	0

  Air Pressure in Pascals (Pa) for ttool's QSA tests. In the real time model, this entry is used to identifying results in the lookup table.

  .. code-block::

    GaugePressure=0
    GaugePressure=150000
    GaugePressure=220000
    GaugePressure=270000
    GaugePressure=320000

CarcassTemperature
  Example value:	273.15

  Temperature in Kevlin for QSA tests

  .. code-block::

    CarcassTemperature=273.15
    CarcassTemperature=353.15
    CarcassTemperature=423.15

RotationSquared
  Example value:	0

  Rotation speed (rad^2/sec)

  .. code-block::

     RotationSquared=0
     RotationSquared=18447
     RotationSquared=37080.3333333333
     RotationSquared=55900

NumNodes
  Example value:	49

  Number of nodes defined in the tyre, generated by ttool from the number of
  [node] entries below, again adding more nodes increases the detail and
  accuracy of the tyre. A minimum of 31 is suggested and the recommended
  range of nodes is 41-49 to achieve the accurate results, numbers exceeding
  this are generally not worth due to increasing computational demands along
  with diminishing returns.

TotalMass
  Example value:	9.412522719792774

  tire masses and inertia's below as calculated by ttool

TotalInertiaStandard
  Example value: (0.65716333011079,0.37699329177024093,0.37699329177023894)

  *No description provided*

RingMass
  Example value: 6.755485413509089

  *No description provided*

RingInertiaStandard
  Example value: (0.536511967258675,0.29524779535639917,0.2952477953563986)

  *No description provided*

[Node]
======

Geometry
  Example value:	(0.08899,-0.19015,0.0171)

  Outermost geometrical point (X, Y locations and, Thickness)

BulkMaterial
  Example value:	(273.15,1258,19800000,0.472,1,1340,0.25)

  Bulk material properties (Temperature at which following properties are valid,
  Density, Young's Modulus, Poisson's Ratio, Compressive modulus multiplier,
  Specific Heat, Thermal Conductivity)

  .. code-block::

      BulkMaterial=(273.15,1258,19800000,0.472,1,1340,0.25)
      BulkMaterial=(373.15,1235,16200000,0.472,1,1492,0.24)

AnisoCarcassConductivityMult
  Example value:	(1.1,1,1.5)
  Directional heat conductivity multiplier X, Y and Z

TreadDepth
  Example value:  0.0024
  *No description provided*

TreadMaterial
  Example value: (273.15,1135,2850000,0.48,1,1700,0.21)
  *No description provided*

  .. code-block::

     TreadMaterial=(273.15,1135,2850000,0.48,1,1700,0.21)
     TreadMaterial=(323.15,1130,2600000,0.48,1,1950,0.206)
     TreadMaterial=(373.15,1125,2280000,0.48,1,2100,0.202)
     TreadMaterial=(423.15,1120,2000000,0.48,1,2250,0.198)

RingAndRim
  Example value:	(0,960000000)
  Fraction of node that forms part of the 'rigid' ring, spring rate of nodes' connection to the wheel rim

PlyParams
  Example value:	(1,0.001405,3)

  Ply Angle, Ply Thickness, Connect Flags (1 = previous node, 2 = next node, 3 = both)

PlyMaterial
  Example value:  (273.15,7907,34000000000,0.3,0.1,465,52)

  .. code-block::

      PlyMaterial=(273.15,7907,34000000000,0.3,0.1,465,52)
      PlyMaterial=(373.15,7879,33000000000,0.3,0.1,484,50)
      PlyParams=(74,0.000409,3)
      PlyMaterial=(273.15,1380,3960000000,0.3,0.1,1695,0.25)
      PlyMaterial=(373.15,1360,3400000000,0.3,0.1,1715,0.24)
      PlyParams=(106,0.000409,3)
      PlyMaterial=(273.15,1380,3960000000,0.3,0.1,1695,0.25)
      PlyMaterial=(373.15,1360,3400000000,0.3,0.1,1715,0.24)
      PlyParams=(80.89,0.00042,3)
      PlyMaterial=(273.15,1205,3450000000,0.3,0.09,1695,0.25)
      PlyMaterial=(373.15,1185,3280000000,0.3,0.09,1715,0.24)
      PlyParams=(99.11,0.00042,3)
      PlyMaterial=(273.15,1205,3450000000,0.3,0.09,1695,0.25)
      PlyMaterial=(373.15,1185,3280000000,0.3,0.09,1715,0.24)


[Realtime]
==========

StaticBaseCoefficient
  Example value:	1.985

  base grip coefficient for static friction

SlidingBaseCoefficient
  Example value:	1.34

  base grip coefficient for sliding friction

InclinationExtrapolation
  Example value:	1.0

  0.0=no extrapolation, 1=extrapolate one step, 2=extrapolate two steps, etc.)

AbrasionCurveWLFStartStep
  Example value:	(-8.5,0.5)

  WLF lookup start and step value

AbrasionVolumePerUnitEnergy
  Example value:	(7.02e-10,6.90e-10,6.66e-10,6.36e-10,5.95e-10,5.40e-10,4.25e-10,
  3.16e-10,2.29e-10,1.55e-10,1.20e-10,9.49e-11,7.64e-11,6.55e-11,6.00e-11,
  6.27e-11,6.82e-11,7.75e-11,9.71e-11,1.23e-10,1.64e-10,2.35e-10,3.22e-10,
  3.82e-10,4.31e-10,4.53e-10,4.64e-10,4.73e-10,4.80e-10,4.85e-10,4.88e-10,
  4.89e-10)
  m^3/J volume of rubber sheared per Joule energy, max 32 values

DegradationPerWearFraction
  Example value:	(0.993,1,0.9992,0.998,0.9972,0.9966,0.9961,0.9956,0.9951,0.9946,
  0.9941,0.9937,0.9933,0.9929,0.9925,0.9921,0.9917,0.9913,0.9909,0.9905,0.9901,
  0.9897,0.9893,0.9889,0.9885,0.9881,0.9877,0.9873,0.9869,0.986,0.98,0.88)

  Degradation based on wear fraction, max 32 values

DegradationCurveParameters
  Example value:	(344.15,6000)

  (<activation_temperature_K>,<heat_history_step_Ks>) heat history is a linear
  progression of temperature over activation point multiplied by time

DegradationPerUnitHistory
  Example value:	(1,0.9925,0.9862,0.9809,0.9765,0.9729,0.97,0.9677,0.9659,
  0.9643,0.9628,0.9614,0.96,0.9586,0.9572,0.9558,0.9544,0.953,0.9516,0.9502,
  0.9488,0.9474,0.946,0.9446,0.9432,0.9418,0.9403,0.9386,0.9367,0.9345,0.9322,
  0.93)

  Degradation per heat history step, up to 32 values

MassInertiaMultiplier
  Example value:	(1.0,1.0,1.0,1.0)

  multipliers for mass (m), inertia (p,q,r)

TemporaryRingDamper
  Example value:	(0.085,0.094,0.094,0.17,0.16,0.16)

  tire ring damping for x,y,z,p,q,r

TemporaryBristleSpring
  Example value:	(21700, 14500, 28500)

  bristle spring rate for Lat/Vert/Long

TemporaryBristleDamper
  Example value:(0.95, 0.9, 0.95)

  *No description provided*

MarbleEffectOnEffectiveLoad
  Example value:	-0.06

  fraction of load available for grip when driving on maximum marbles (10% less
  load in this case)

TerrainWeightOnContactTemperature
  Example value:	0.1

  temperature used for WLF is influenced by the track temperature (in this
  case, 90% tire surface, 10% terrain surface)

WLFParameters
  Example value:	(228.15,50,-8.86,51.5)

  glass transition temperature.  Other values pretty much the same for all
  rubbers, except butyl.  Most likely, you won't touch the last three values.

StaticRoughnessEffect
  Example value:	-0.2

  terrain roughness influence on static friction

GrooveEffects
  Example value:	(0.092,0.092,0.076,0.048)

  maximum groove influences grip here for: static friction, sliding adhesion,
  sliding micro-deformation, sliding macro-deformation

DampnessEffects
  Example value:	(-0.075,-0.08,-0.06,-0.03)

  fully damp track (at threshold of standing water or more) influence on grip
  for same things as GrooveEffects

TemporaryGripLossForWetness
  Example value:	0.16

  Temporary hack aquaplaning. Decreases grip due to standing water.

StaticCurve
  Example value:	(153, 0.66, 353, 1.176, 653, 0.65)

  at -100C there's 52% of maximum static grip, at 100C it's maximum, at 400C
  it's back down to 52% of max static grip

SlidingAdhesionCurve
  Example value:	(-9.2, 0.4, -5.2, 1.68, -1.2, 0.2)

  min sliding speed (log(10) aTv), grip multiplier (for min), peak sliding
  speed, grip multiplier (for peak), max sliding speak, grip multiplier (for max)

SlidingMicroDeformationCurve
  Example value:	(-5.2, 0.3, -1.2, 1.8, +2.5, 0.3)

  these values are blended following a cosine rule

SlidingMacroDeformationCurve
  Example value:	(-1.2, 0.2, +2.5, 2, +6.0, 0.4)

  to get the totals the adhesion, micro and macro curves are then multiplied
  by the surface types as defined in the TDF files, the defaults of which are
  0.25 for adhesion, 0.5 microroughness, 0.25 macroroughness

RubberPressureSensitivityPower
  Example value:	(-1.17,4.04e5,5e5,1)
  rubber contact pressure sensivity power, offset, nominal maximum, normalize
  (1=yes,2=no)

IgnitionParameters
  Example value:	(493,0.06,49)
  ignition temperature of rubber in Kelvin, heat power factor, nominal max of
  area\*temperature_over_ignition

SizeMultiplier
  Example value:	(1,1)

  if necessary, an adjustment to the geometrical width and radius; default is
  (1,1)

ThermalDepthAtSurface
  Example value:	0.0001

  the depth of the temperature sample layer used for contact properties (i.e.
  grip and wear); if provisional second layer is disabled, tread will never be
  allowed to get thinner than this value

ThermalDepthBelowSurface
  Example value:	0.0004

  (if provisional code enabled) the depth of the second layer; value should
  be >= surface layer but not too big; tread will never be allowed to get
  thinner than these two layers

BristleLength
  Example value:	0.12

  tuned to aid collision detection, no other physical effects

DampingHeatEnergy
  Example value:	(1.0,0.4,0.8)

  (Fraction of ring damping heat into sidewall (should probably be 1.0),
  fraction of bristle damping heat into carcass, fraction of bristle damping
  heat into tread) the 2nd and 3rd values should generally add up to 1.0

InternalGasHeatTransfer
  Example value:	(10,5,0.6)

  (base, mult, power) - heat transfer coefficients to internal gas cavity =
  base+(mult\*(vel^power)), where vel is linear velocity of tire

ExternalGasHeatTransfer
  Example value:	(8,4,0.6)

  (base, mult, power) - heat transfer coefficients to external air =
  base+(mult\*(vel^power)), where vel is linear velocity of tire

GroundConductance
  Example value:	(1000,0.003,0)

  (base, mult, reserved) - thermal contact conductance coefficient to ground =
  base+(mult\*pressure), where pressure is contact pressure and the reserved
  variable will be used at some later stage.

WetConductance
  Example value:	(710,730,0,0)

  Additional conductance due to (<dampness>, <wetness>,<and reserved for future
  usage 1>,<reserved 2>)

TireRadiationEmissivity
  Example value:	0.936

  thermal radiation emissivity for external tire surface

InternalGasSpecificHeatAtConstantVolume
  Example values:	(250,716)

  (temperature (K), specific heat at constant volume (J/(kg\*K)))

  719 J/(kg\*K) is an approximation for dry air, but value changes slightly
  depending on temperature

  500 is an extreme value, you may have other issues if the internal gas
  reaches 500 degrees Kelvin

.. code-block::

  InternalGasSpecificHeatAtConstantVolume=(250,716)
  InternalGasSpecificHeatAtConstantVolume=(300,718)
  InternalGasSpecificHeatAtConstantVolume=(350,721)
  InternalGasSpecificHeatAtConstantVolume=(400,726)
  InternalGasSpecificHeatAtConstantVolume=(450,733)
  InternalGasSpecificHeatAtConstantVolume=(500,742)

[LookupData]
============

Version
  Example value:	1.103

  *No description provided*

Bin
  Example value:	53b1932d3fe4fe413583c3a63fd816d62c05b4f53fd816d608d85fdc3f068
  b5f85d833ecbe375bd7d54f64143fe12287da50d7413fd2dbe4d1bd98553fd2dbe4

  *No description provided*

Checksum
  Example value:	1100694750

  *No description provided*
