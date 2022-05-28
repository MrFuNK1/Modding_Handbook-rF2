.. warning::

  This page is WIP.

.. sidebar:: Source

  Source of the information and descriptions herein were extracted from
  "skipbarber_engine.ini" file of the SkipBarber that comes with the Dev Mode
  of rFactor2 game version v1121. Where necessary and available, information and
  descriptions were amended.

######
Engine
######

Every car needs an engine, no matter if its a common combustion engine with or
without turbos, or even an electric engine. In rFactor2 you can have all, however
you need to set it up properly and - of course - need some data to get it right.
Hopefully the information and descriptions provided will help you to get your data
into the right format and bring the engine to life!

.. contents:: Contents
  :depth: 2
  :local:

***************************************
Structure of the engine definition file
***************************************

The engine definition file does not include any clear sections. However, it can
still be separated into the following logical sections:

  1. Setting of reference conditions.

  2. Definition of engine performance data (curves).

  3. Parameters to define fuel and air characteristics.

  4. Parameters to define engine mechanics.

  5. Parameters to define a turbo (if any).

********************
Reference Conditions
********************

The presence of reference conditions activates the new engine model of rFactor2.

ReferenceConditions
  Example value:	(101325,1.225,0.073)

  pressure (pascals), density (kg/m^3), fuel/air mass ratio, the presence of this
  line activates the new engine model

****************
Performance Data
****************

.. note::

  The SkipBarber's engine is a 2.0-liter, SOHC, with 133hp @ 6000 rpm, 175nm @
  5000 rpm, Max 6500 rpm, and 4.5s 0-96km/h.

RPMBase
  Example value:	(0, -17.5, -17.5, 0.082, 1.207)

  The individual values are, seperated with a comma: RPM, coast torque, reference
  max torque (assuming VolumeFract=1.0 & MixtureFract=1.0), idle function
  (throttle opening to maintain idle RPM), pressure ^ power (power increase above
  reference air pressure relative to coast torque)

VolumeFract
  Example value:	(0, 1.000, 1.000, 1.000, 1.000, 1.000, 1.000, 1.000, 1.000,
  1.000, 1.000, 1.000, 1.000, 1.000, 1.000, 1.000)

  Maps accelerator position to fraction of combustion chamber filled with air,
  you can define a maximum resolution of 16 steps which are interpolated and
  distributed evenly

MixtureFract
  Example value:	(0.93,0.9335,0.9355,0.9375)

  Maps accelerator position to fraction of reference fuel/air mixture ratio

And this is what the whole section from the "SkipBarber_engine.ini" file looks like:

.. code-block::

    RPMBase=(    0, -17.5, -17.5, 0.082, 1.207)
    VolumeFract=(0, 1.000, 1.000, 1.000, 1.000, 1.000, 1.000, 1.000, 1.000, 1.000, 1.000, 1.000, 1.000, 1.000, 1.000, 1.000)
    MixtureFract=(0.93,0.9335,0.9355,0.9375)
    RPMBase=(  250, -15.9, -3.3, 0.082, 1.747)
    VolumeFract=(0, 0.975, 0.994, 1.000, 1.000, 1.000, 1.000, 1.000, 1.000, 1.000, 1.000, 1.000, 1.000, 1.000, 1.000, 1.000)
    MixtureFract=(0.931,0.944,0.95,0.955)
    RPMBase=(  500, -15.5, 55, 0.082, 0.983)
    VolumeFract=(0, 0.820, 0.890, 0.940, 0.958, 0.977, 0.995, 0.996, 0.998, 0.999, 0.999, 1.000, 1.000, 1.000, 1.000, 1.000)
    MixtureFract=(0.932,0.953,0.968,0.97)
    RPMBase=(  750, -16.2, 105, 0.063, 0.984)
    VolumeFract=(0, 0.530, 0.750, 0.870, 0.907, 0.944, 0.980, 0.986, 0.991, 0.997, 0.998, 0.999, 1.000, 1.000, 1.000, 1.000)
    MixtureFract=(0.933,0.961,0.975,0.98)
    RPMBase=( 1000, -17.0, 135, 0.025, 0.982)
    VolumeFract=(0, 0.340, 0.595, 0.790, 0.848, 0.906, 0.963, 0.973, 0.982, 0.992, 0.995, 0.997, 1.000, 1.000, 1.000, 1.000)
    MixtureFract=(0.934,0.968,0.985,0.99)
    RPMBase=( 1250, -17.9, 147, 0.016, 0.978)
    VolumeFract=(0, 0.230, 0.420, 0.600, 0.709, 0.817, 0.924, 0.943, 0.962, 0.980, 0.986, 0.993, 0.999, 0.999, 1.000, 1.000)
    MixtureFract=(0.935,0.974,0.99,0.995)
    RPMBase=( 1500, -18.8, 159, 0.012, 0.975)
    VolumeFract=(0, 0.160, 0.310, 0.460, 0.601, 0.741, 0.880, 0.910, 0.940, 0.970, 0.979, 0.989, 0.998, 0.999, 0.999, 1.000)
    MixtureFract=(0.936,0.98,0.995,0.997)
    RPMBase=( 1750, -19.8, 168, 0.009, 0.971)
    VolumeFract=(0, 0.134, 0.268, 0.400, 0.549, 0.699, 0.846, 0.885, 0.924, 0.963, 0.974, 0.985, 0.996, 0.997, 0.999, 1.000)
    MixtureFract=(0.937,0.986,0.997,0.998)
    RPMBase=( 2000, -20.8, 173, 0.006, 0.966)
    VolumeFract=(0, 0.122, 0.245, 0.365, 0.515, 0.664, 0.812, 0.860, 0.908, 0.956, 0.969, 0.981, 0.994, 0.996, 0.998, 1.000)
    MixtureFract=(0.938,0.991,0.998,0.999)
    RPMBase=( 2250, -21.8, 174, 0.004, 0.961)
    VolumeFract=(0, 0.114, 0.228, 0.340, 0.487, 0.633, 0.778, 0.836, 0.893, 0.950, 0.964, 0.977, 0.991, 0.994, 0.997, 1.000)
    MixtureFract=(0.939,0.995,0.999,1)
    RPMBase=( 2500, -22.9, 176, 0.003, 0.956)
    VolumeFract=(0, 0.105, 0.210, 0.313, 0.458, 0.602, 0.745, 0.813, 0.881, 0.948, 0.961, 0.974, 0.987, 0.991, 0.996, 1.000)
    MixtureFract=(0.94,0.997,1,1)
    RPMBase=( 2750, -24.0, 179, 0.002, 0.951)
    VolumeFract=(0, 0.097, 0.195, 0.291, 0.431, 0.572, 0.710, 0.785, 0.860, 0.934, 0.951, 0.968, 0.984, 0.989, 0.995, 1.000)
    MixtureFract=(0.941,0.998,1,1)
    RPMBase=( 3000, -25.1, 181.2, 0.001, 0.946)
    VolumeFract=(0, 0.090, 0.181, 0.270, 0.406, 0.543, 0.677, 0.758, 0.840, 0.920, 0.940, 0.961, 0.981, 0.987, 0.994, 1.000)
    MixtureFract=(0.942,0.999,1,1)
    RPMBase=( 3250, -26.3, 181, 0, 0.941)
    VolumeFract=(0, 0.084, 0.168, 0.250, 0.381, 0.511, 0.640, 0.727, 0.814, 0.900, 0.926, 0.952, 0.978, 0.985, 0.993, 1.000)
    MixtureFract=(0.943,1,1,1)
    RPMBase=( 3500, -27.5, 179, 0, 0.934)
    VolumeFract=(0, 0.077, 0.155, 0.231, 0.358, 0.484, 0.609, 0.700, 0.791, 0.880, 0.912, 0.944, 0.975, 0.983, 0.992, 1.000)
    MixtureFract=(0.944,1,1,1)
    RPMBase=( 3750, -28.7, 181, 0, 0.929)
    VolumeFract=(0, 0.072, 0.143, 0.214, 0.337, 0.460, 0.581, 0.674, 0.768, 0.860, 0.897, 0.934, 0.971, 0.981, 0.990, 1.000)
    MixtureFract=(0.945,1,1,1)
    RPMBase=( 4000, -29.9, 188, 0, 0.926)
    VolumeFract=(0, 0.067, 0.134, 0.200, 0.321, 0.441, 0.560, 0.654, 0.748, 0.840, 0.883, 0.925, 0.967, 0.978, 0.989, 1.000)
    MixtureFract=(0.946,1,1,1)
    RPMBase=( 4250, -31.2, 190.5, 0, 0.921)
    VolumeFract=(0, 0.063, 0.125, 0.187, 0.307, 0.427, 0.545, 0.640, 0.736, 0.830, 0.875, 0.919, 0.963, 0.975, 0.988, 1.000)
    MixtureFract=(0.947,1,1,1)
    RPMBase=( 4500, -32.5, 191.4, 0, 0.916)
    VolumeFract=(0, 0.059, 0.117, 0.175, 0.294, 0.412, 0.529, 0.626, 0.724, 0.820, 0.868, 0.916, 0.964, 0.976, 0.988, 1.000)
    MixtureFract=(0.948,1,1,1)
    RPMBase=( 4750, -33.8, 192, 0, 0.911)
    VolumeFract=(0, 0.056, 0.113, 0.168, 0.284, 0.400, 0.514, 0.613, 0.712, 0.810, 0.860, 0.910, 0.959, 0.973, 0.986, 1.000)
    MixtureFract=(0.949,1,1,1)
    RPMBase=( 5000, -35.1, 192.4, 0, 0.905)
    VolumeFract=(0, 0.055, 0.109, 0.163, 0.275, 0.387, 0.498, 0.599, 0.700, 0.800, 0.852, 0.903, 0.954, 0.969, 0.985, 1.000)
    MixtureFract=(0.95,1,1,1)
    RPMBase=( 5250, -36.5, 190.2, 0, 0.899)
    VolumeFract=(0, 0.053, 0.107, 0.159, 0.270, 0.381, 0.490, 0.591, 0.691, 0.790, 0.843, 0.897, 0.949, 0.966, 0.983, 1.000)
    MixtureFract=(0.951,1,1,1)
    RPMBase=( 5500, -37.9, 187.2, 0, 0.891)
    VolumeFract=(0, 0.052, 0.105, 0.156, 0.265, 0.373, 0.480, 0.581, 0.681, 0.780, 0.835, 0.889, 0.943, 0.962, 0.981, 1.000)
    MixtureFract=(0.952,1,1,1)
    RPMBase=( 5750, -39.3, 180.4, 0, 0.882)
    VolumeFract=(0, 0.051, 0.103, 0.153, 0.259, 0.365, 0.470, 0.571, 0.671, 0.770, 0.826, 0.882, 0.937, 0.958, 0.979, 1.000)
    MixtureFract=(0.953,1,1,1)
    RPMBase=( 6000, -40.7, 173.3, 0, 0.871)
    VolumeFract=(0, 0.050, 0.101, 0.150, 0.254, 0.358, 0.460, 0.561, 0.661, 0.760, 0.818, 0.876, 0.933, 0.955, 0.978, 1.000)
    MixtureFract=(0.954,1,1,1)
    RPMBase=( 6250, -42.1, 165.9, 0, 0.86)
    VolumeFract=(0, 0.049, 0.098, 0.147, 0.250, 0.353, 0.454, 0.554, 0.654, 0.753, 0.812, 0.870, 0.928, 0.952, 0.976, 1.000)
    MixtureFract=(0.955,1,1,1)
    RPMBase=( 6500, -43.6, 157.7, 0, 0.847)
    VolumeFract=(0, 0.048, 0.096, 0.144, 0.247, 0.350, 0.452, 0.551, 0.651, 0.749, 0.808, 0.868, 0.926, 0.951, 0.976, 1.000)
    MixtureFract=(0.956,1,1,1)
    RPMBase=( 6750, -45.0, 149, 0, 0.833)
    VolumeFract=(0, 0.048, 0.095, 0.142, 0.245, 0.348, 0.449, 0.548, 0.647, 0.745, 0.805, 0.865, 0.924, 0.949, 0.975, 1.000)
    MixtureFract=(0.957,1,1,1)
    RPMBase=( 7000, -46.5, 142.5, 0, 0.82)
    VolumeFract=(0, 0.047, 0.094, 0.140, 0.243, 0.345, 0.446, 0.545, 0.644, 0.741, 0.802, 0.862, 0.922, 0.948, 0.974, 0.999)
    MixtureFract=(0.958,1,1,1)
    RPMBase=( 7250, -48.0, 136.5, 0, 0.806)
    VolumeFract=(0, 0.046, 0.092, 0.138, 0.240, 0.342, 0.443, 0.541, 0.640, 0.737, 0.798, 0.860, 0.920, 0.946, 0.972, 0.998)
    MixtureFract=(0.959,1,1,1)
    RPMBase=( 7500, -49.5, 126, 0, 0.786)
    VolumeFract=(0, 0.046, 0.091, 0.136, 0.238, 0.340, 0.440, 0.538, 0.636, 0.733, 0.795, 0.857, 0.918, 0.944, 0.971, 0.997)
    MixtureFract=(0.96,1,1,1)
    RPMBase=( 7750, -51.1, 111.6, 0, 0.757)
    VolumeFract=(0, 0.045, 0.090, 0.134, 0.236, 0.337, 0.437, 0.535, 0.633, 0.729, 0.792, 0.854, 0.916, 0.942, 0.969, 0.995)
    MixtureFract=(0.961,1,1,1)
    RPMBase=( 8000, -52.6, 96.8, 0, 0.722)
    VolumeFract=(0, 0.044, 0.088, 0.132, 0.233, 0.334, 0.434, 0.531, 0.629, 0.725, 0.788, 0.852, 0.914, 0.940, 0.966, 0.991)
    MixtureFract=(0.962,1,1,1)
    RPMBase=( 8250, -54.2, 81.4, 0, 0.677)
    VolumeFract=(0, 0.044, 0.087, 0.130, 0.231, 0.332, 0.431, 0.528, 0.625, 0.721, 0.785, 0.849, 0.91, 0.936, 0.960, 0.985)
    MixtureFract=(0.963,1,1,1)
    RPMBase=( 8500, -55.7, 66, 0, 0.62)
    VolumeFract=(0, 0.043, 0.086, 0.128, 0.229, 0.329, 0.428, 0.525, 0.622, 0.717, 0.782, 0.846, 0.9, 0.919, 0.949, 0.974)
    MixtureFract=(0.964,1,1,1)
    RPMBase=( 8750, -57.3, 49.5, 0, 0.541)
    VolumeFract=(0, 0.042, 0.084, 0.126, 0.226, 0.326, 0.425, 0.521, 0.618, 0.713, 0.778, 0.844, 0.878, 0.897, 0.927, 0.946)
    MixtureFract=(0.965,1,1,1)
    RPMBase=( 9000, -58.9, 33, 0, 0.431)
    VolumeFract=(0, 0.042, 0.083, 0.124, 0.224, 0.324, 0.422, 0.518, 0.614, 0.709, 0.775, 0.841, 0.866, 0.895, 0.88, 0.902)
    MixtureFract=(0.966,1,1,1)
    RPMBase=( 9250, -60.5, 11, 0, 0.196)
    VolumeFract=(0, 0.041, 0.082, 0.122, 0.221, 0.321, 0.419, 0.515, 0.611, 0.705, 0.75, 0.77, 0.78, 0.79, 0.801, 0.824)
    MixtureFract=(0.967,1,1,1)

****************************
Fuel and Air Characteristics
****************************

FuelConsumption
  Example value:	2.9e-5

  Affected by throttle position, engine rotation, and air density

FuelEstimate
  Example value:	1.0

  Fudge factor for differences between vehicle types (used for lap estimates
  and AI pit scheduling)

FuelDensity
  Example value:	0.74

  Unit: kg/liter

FuelAirMixtureTable
  Example value:	(0.0, 0.1)

  Start and step size of fuel/air ratio (normalized relative to reference
  mixture) for following table:

FuelAirMixtureEffects
  Example value:	(0.00, 0.00)

  Torque multiplier, exhaust gas temperature multiplier

And this is what the whole section from the "SkipBarber_engine.ini" file looks like:

.. code-block::

  FuelConsumption=2.9e-5
  FuelEstimate=1.0
  FuelDensity=0.74
  FuelAirMixtureTable=(0.0, 0.1)
  FuelAirMixtureEffects=(0.00, 0.00)
  FuelAirMixtureEffects=(0.10, 0.11)
  FuelAirMixtureEffects=(0.20, 0.22)
  FuelAirMixtureEffects=(0.30, 0.33)
  FuelAirMixtureEffects=(0.40, 0.44)
  FuelAirMixtureEffects=(0.50, 0.55)
  FuelAirMixtureEffects=(0.60, 0.66)
  FuelAirMixtureEffects=(0.70, 0.77)
  FuelAirMixtureEffects=(0.80, 0.88)
  FuelAirMixtureEffects=(0.89, 0.99)
  FuelAirMixtureEffects=(0.98, 1.00)
  FuelAirMixtureEffects=(1.00, 0.97)
  FuelAirMixtureEffects=(0.97, 0.90)
  FuelAirMixtureEffects=(0.85, 0.80)
  FuelAirMixtureEffects=(0.65, 0.60)
  FuelAirMixtureEffects=(0.40, 0.40)
  FuelAirMixtureEffects=(0.10, 0.10)
  FuelAirMixtureEffects=(0.00, 0.00)

****************
Engine Mechanics
****************

EngineInertia
  Example value:	0.092

  Rotational inertia of engine components

IdleRPMLogic
  Example value:	(800, 980)

  Anti-stall clutch logic, values should be slightly lower than actual idle RPM

LaunchEfficiency
  Example value:	0

  Efficiency (0.0-1.0) of launch control, or 0.0 if N/A

LaunchRPMLogic
  Example value:	(5030, 6370)

  holds RPM in this range before launch (used for AI even if launch control
  is N/A!)

LaunchVariables
  Example value:	0

  Level of traction control used (0-3) and whether auto-upshifting is enabled
  (add 4); default=7

RevLimitRange
  Example value:	(6500, 50, 1)

  Target RPM for limiter to engage

RevLimitSpecial
  Example value:	(0,,,"")

  Gear specific offset rev limits can be enabled via special instructions
  (gr=,gn=,g1=...g9=) which represent reverse, neutral and gears 1 through
  9. For example g3=-500 would decrease the maximum RPM in 3rd gear by 500 RPM.

RevLimitSetting
  Example value: 0

  *no description provided*

RevLimitAvailable
  Example value:	1

  Whether to use a rev limit (if 0, you still must have a "rev limit", just
  make it 40000 or so, and make sure to change [CONTROLS]->UpshiftAlgorithm
  to fix shifting points)

RevLimitLogic
  Example value:	0

  RPM range around current setting where *soft* rev limiter operates (either
  this or RevLimitTime should probably be zero)

RevLimitHardTime
  Example value:	0.1

  Hard rev-limiter ignition cut time (either this or RevLimitLogic should
  probably be zero)

EngineMapRange
  Example value:	(0, 1, 1)

  0 = most driveable, max = most power (low gears only) (unimplemented)

EngineMapSetting
  Example value: 0

  *no description provided*

EngineBrakingParams
  Example value:	(0,1800)

  0=old-style RPM based throttle increase, 1=throttle-based, 2=torque-based;
  then RPM step size for "Limit" tables below

EngineBrakingLimit
  Example value:	( -15, -16, -17, -18, -19, -20, -21, -22, -23, -24, -25)

  Throttle or goal torque at 100%, has up to 11 entries, intended as the limit
  for engine braking (the maximum engine throttle or minimum negative torque)
  when coasting

EngineBrakingGear0Limit
  Example value:	(-999,-999,-999,-999,-999,-999,-999,-999,-999,-999,-999)

  Limit overrides can be applied per gear, in this case basically requesting
  full engine braking no matter what, again up to 11 entries

EngineBrakingMapRange
  Example value:	(0, 0.0005, 1)

  If RPM based, input throttle is ranged from minimum to 100%, with the
  minimum = setting * step * RPM. If using the throttle or torque-based
  method, you are specifying the fraction of the "limit" values above

EngineBrakingMapSetting
  Example value:	0

  Default is 0 * 0.0005 * 6000 RPM = 0.0% applied throttle at zero input
  throttle, note that with the throttle of torque methods values of (0, 0.1,
  11) would correspond to 0-100% in 10% steps

EngineBoostRange
  Example value:	(0, 0, 1)

  Number of possible boost settings, this can be used in conjunction with
  BoostTurboPressure to alter turbo boost pressures

EngineBoostSetting
  Example value: 0

  *no description provided*

BoostEffects
  Example value:	(0.0, 0.01, 0.02)

  RPM change per setting, fuel increase per setting, engine wear rate per
  setting

OptimumOilTemp
  Example value:	98.0

  Degrees Celsius at which engine operates optimally

CombustionHeat
  Example value:	29.5

  Degrees Celsius added per liter of fuel burned

EngineSpeedHeat
  Example value:	7.78e-04

  Heat added linearly with engine speed

OilMinimumCooling
  Example value:	7.0e-3

  Heat dissipated without oil/water transfer

OilWaterHeatTransfer
  Example value:	(0.014, 8.1e-5)

  Heat transfer from oil to water (base, w/ engine speed)

WaterMinimumCooling
  Example value:	4.5e-3

  Base heat dissipated without velocity

RadiatorCooling
  Example value:	(4.0e-6, 8.0e-5)

  Cooling rate with velocity (base, per setting)

LifetimeEngineRPM
  Example value:	(6200, 250)

  (base engine speed for lifetime, range where lifetime is halved)

LifetimeOilTemp
  Example value:	(109.5, 4.1)

  (base oil temp for lifetime, range where lifetime is halved)

LifetimeAvg
  Example value:	14000

  Average lifetime in seconds

LifetimeVar
  Example value:	4650

  Lifetime random variance

EngineEmission
  Example value:	(0.0, 0.55,-0.27)

  Where flames and smoke are emitted (relative to ref frame at rear axle)

EngineSound
  Example value:	( 0.0, 0.50,-0.40)

  Where engine sound is emitted (relative to ref frame at rear axle)

SpeedLimiter
  Example value:	0

  Whether there is a pitlane speed limiter

OnboardStarter
  Example value:	1

  Whether vehicle restarts when stalled

StarterTiming
  Example value:	(0.1, 0.1, 3.4)

  Average and variable cranking time, then blend with starting sound

RamCenter
  Example value:	(0.0, 0.60,-0.72)

  Location of ram air intake

RamDraftMult
  Example value:	6.0

  Multiplier for effect that draft has on ram air velocity

RamPressure
  Example value:	(0.0,3.5e-6)

  Speed (m/s) to ambient pressure mult, speed squared (m/s)^2 to ambient
  pressure mult

And this is what the whole section from the "SkipBarber_engine.ini" file looks like:

.. code-block::

  EngineInertia=0.092
  IdleRPMLogic=(800, 980)
  LaunchEfficiency=0
  LaunchRPMLogic=(5030, 6370)
  LaunchVariables=0
  RevLimitRange=(6500, 50, 1)
  RevLimitSpecial=(0,,,"")
  RevLimitSetting=0
  RevLimitAvailable=1
  RevLimitLogic=0
  RevLimitHardTime=0.1
  EngineMapRange=(0, 1, 1)
  EngineMapSetting=0
  EngineBrakingParams=(0,1800)
  EngineBrakingLimit=(      -15, -16, -17, -18, -19, -20, -21, -22, -23, -24, -25)
  EngineBrakingGear0Limit=(-999,-999,-999,-999,-999,-999,-999,-999,-999,-999,-999)
  EngineBrakingMapRange=(0, 0.0005, 1)
  EngineBrakingMapSetting=0
  EngineBoostRange=(0, 0, 1)
  EngineBoostSetting=0
  BoostEffects=(0.0, 0.01, 0.02)
  OptimumOilTemp=98.0
  CombustionHeat=29.5
  EngineSpeedHeat=7.78e-04
  OilMinimumCooling=7.0e-3
  OilWaterHeatTransfer=(0.014, 8.1e-5)
  WaterMinimumCooling=4.5e-3
  RadiatorCooling=(4.0e-6, 8.0e-5)
  LifetimeEngineRPM=(6200, 250)
  LifetimeOilTemp=(109.5, 4.1)
  LifetimeAvg=14000
  LifetimeVar=4650
  EngineEmission=(0.0, 0.55,-0.27)
  EngineSound=( 0.0, 0.50,-0.40)
  SpeedLimiter=0
  OnboardStarter=1
  StarterTiming=(0.1, 0.1, 3.4)
  RamCenter=(0.0, 0.60,-0.72)
  RamDraftMult=6.0
  RamPressure=(0.0,3.5e-6)

*****************
Turbos (optional)
*****************

The whole section can be repeated multiple times to create multiple turbos for your
engine. However, it needs confirmation whether there is any limit (maybe only two
turbos are possible).

TurboInertia
  Example value:	0.000115

  You can actually have two turbos, each one starts with this line.

TurboFriction
  Example value:	(0.002,2.5)

  Torque (Nm, constant at any speed), power (W, ramps up linearly with speed)

TurboStaticFrictionWatts
  Example value:	100

  static friction prevents numerical problems at low spool speeds

TurbineFlowTable
  Example value:	(0,0.00756)

  Corrected flow (kg/s corrected to standard temperature and pressure)

TurbineFlowEffects
  Example value:	(1,0.52)

  Pressure ratio, efficiency

TurbineFlowEffects
  Example value:	(1.1, 0.711)

  Etc... eventually basically reaches a peak PR while the efficiency drops back
  down

IntakeVolumePerRevolution
  Example value:	0.9

  Basically the displacement divided by two for a normal four-stroke engine

ExhaustBaseProperties
  Example value:	(1175,1180,0.187,0.222,-0.0000335)

  Kelvin, specific heat at constant pressure, delta per unit Kelvin, (k-1)/k
  (where k is the ratio between specific heats for constant pressure and
  constant temperature), delta per unit Kelvin

CompressorTable
  Example value:	(25000,0.0302)

  Spool RPM step, corrected flow step (kg/s corrected to standard temperature
  and pressure)

Turbo compressor data is defined along RPM steps. In the SkipBarber example,
there are steps from 0 - 150.000 RPM. The explanation and comments below are for
the definition example of first step at 0 RPM and second step at 25.000 RPM. The
full example for all steps can be found below.

Data along 0 RPM compressor map speed line:

CompressorPressRatio
  Example value:	(1)

  nothing going on at 0 RPM

CompressorEfficiency
  Example value:	(0)

  probably not much efficiency at 0 RPM either

CompressorSurgeLineFlow
  Example value:	0

  defining this is optional (and surge effects aren't currently implemented)

Data along 25,000 RPM compressor map speed line:

CompressorPressRatio
  Example value:	(1.116, 1.115, 1.095, 1.066, 1.035, 1.001, 1, 1, 1, 1, 1, 1,
  1, 1, 1, 1, 1)

  per corrected flow

CompressorEfficiency
  Example value:	(0.25, 0.45, 0.59, 0.45, 0.40, 0.35, 0.30, 0.25, 0.20, 0.15,
  0.10, 0.05, 0.00, 0.00, 0.00, 0.00)

  per corrected flow

CompressorSurgeLineFlow
  Example value: 0.019

  *no description provided*

TurboTestSpeedMult
  Example value:	12.0

  Dev-only test variable sets turbo speed to the given multiple of the current
  engine speed at all times

BoostTurboPressure
  Example value:	(250000,50000)

  Base desired boost pressure, multiplier by EngineBoost setting

WastegateBoostMeasurement
  Example value:	1

  0=intake manifold, 1=pre-throttle (this is the default), no other choices at
  this time

Wastegate
  Example value:	(-1500,0.0,1500,1.0)

  Minimum relative boost pressure (to desired), minimum wastegate opening, max
  relative pressure, max opening

IntakeLeak
  Example value:	1e-7

  Minimum mass flow

DumpValve
  Example value:	(150000,120000,0.000001)

  Throttle body pressure drop to fully open dump valve, same for fully closed,
  dump mass flow per Pascal

And this is what the whole section from the "SkipBarber_engine.ini" file looks like:

.. code-block::

  TurboInertia=0.000115
  TurboFriction=(0.002,2.5)
  TurboStaticFrictionWatts=100
  TurbineFlowTable=(0,0.00756)
  TurbineFlowEffects=(1,0.52)
  TurbineFlowEffects=(1.005,0.53)
  TurbineFlowEffects=(1.01,0.55)
  TurbineFlowEffects=(1.016, 0.58)
  TurbineFlowEffects=(1.023, 0.6)
  TurbineFlowEffects=(1.031, 0.63)
  TurbineFlowEffects=(1.04, 0.65)
  TurbineFlowEffects=(1.05, 0.67)
  TurbineFlowEffects=(1.061, 0.685)
  TurbineFlowEffects=(1.073, 0.697)
  TurbineFlowEffects=(1.086, 0.706)
  TurbineFlowEffects=(1.1, 0.711)
  IntakeVolumePerRevolution=0.9
  ExhaustBaseProperties=(1175,1180,0.187,0.222,-0.0000335)
  CompressorTable=(25000,0.0302)
  // data along 0 RPM compressor map speed line:
  CompressorPressRatio=(1)
  CompressorEfficiency=(0)
  CompressorSurgeLineFlow=0
  // data along 25,000 RPM compressor map speed line:
  CompressorPressRatio=(1.116, 1.115, 1.095, 1.066, 1.035, 1.001, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) // per corrected flow
  CompressorEfficiency=(0.25, 0.45, 0.59, 0.45, 0.40, 0.35, 0.30, 0.25, 0.20, 0.15, 0.10, 0.05, 0.00, 0.00, 0.00, 0.00) // per corrected flow
  CompressorSurgeLineFlow=0.019
  // data along 50,000 RPM compressor map speed line:
  CompressorPressRatio=(1.31, 1.325, 1.325, 1.31, 1.275, 1.23, 1.17, 1.1, 1.015, 1, 1, 1, 1, 1, 1, 1, 1)
  CompressorEfficiency=(0.28, 0.5, 0.61, 0.71, 0.74, 0.68, 0.58, 0.47, 0.4, 0.35, 0.25, 0.15, 0.05, 0, 0, 0, 0)
  CompressorSurgeLineFlow=0.037
  // data along 75,000 RPM compressor map speed line:
  CompressorPressRatio=(1.68, 1.705, 1.72, 1.73, 1.73, 1.71, 1.66, 1.6, 1.495, 1.35, 1.14, 1, 1, 1, 1, 1, 1)
  CompressorEfficiency=(0.26, 0.45, 0.55, 0.65, 0.7, 0.75, 0.775, 0.765, 0.68, 0.6, 0.45, 0.3, 0.2, 0.1, 0, 0, 0)
  CompressorSurgeLineFlow=0.058
  // data along 100,000 RPM compressor map speed line:
  CompressorPressRatio=(2.17, 2.2, 2.23, 2.27, 2.31, 2.34, 2.36, 2.36, 2.33, 2.25, 2.12, 1.91, 1.53, 1.05, 1, 1, 1)
  CompressorEfficiency=(0.25, 0.33, 0.38, 0.46, 0.53, 0.605, 0.69, 0.75, 0.765, 0.775, 0.75, 0.65, 0.45, 0.23, 0.11, 0, 0)
  CompressorSurgeLineFlow=0.08
  // data along 125,000 RPM compressor map speed line:
  CompressorPressRatio=(3.26, 3.28, 3.31, 3.33, 3.34, 3.35, 3.36, 3.35, 3.33, 3.3, 3.25, 3.17, 2.97, 2.5, 1.58, 1.01, 1)
  CompressorEfficiency=(0.24, 0.3, 0.36, 0.55, 0.58, 0.61, 0.63, 0.65, 0.665, 0.68, 0.7, 0.715, 0.68, 0.6, 0.49, 0.25, 0)
  CompressorSurgeLineFlow=0.104
  // data along 150,000 RPM compressor map speed line:
  CompressorPressRatio=(4.22, 4.24, 4.26, 4.29, 4.32, 4.34, 4.36, 4.36, 4.35, 4.33, 4.28, 4.23, 4.1, 3.81, 3.16, 2.05, 1)
  CompressorEfficiency=(0.23, 0.29, 0.35, 0.47, 0.49, 0.51, 0.53, 0.55, 0.56, 0.57, 0.58, 0.59, 0.6, 0.58, 0.5, 0.33, 0)
  CompressorSurgeLineFlow=0.13
  //TurboTestSpeedMult=12.0
  BoostTurboPressure=(250000,50000)
  WastegateBoostMeasurement=1
  Wastegate=(-1500,0.0,1500,1.0)
  IntakeLeak=1e-7
  DumpValve=(150000,120000,0.000001)
