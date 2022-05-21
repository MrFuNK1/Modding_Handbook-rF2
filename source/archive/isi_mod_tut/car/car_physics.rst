*******
Physics
*******

*Annotations restricted to this tutorial*

GE
   Ground Effects

CG
   Centre of Gravity (In reference to Height)

CF
   Centre of Forces

REF
   Reference Plane

:ref:`archive/isi_mod_tut/car/car_physics:Unit Conversion`

Notes before we begin.
======================

While this tutorial section is designed mainly for beginners, even those
whom consider their skills advanced may learn something new from this
tutorial. Generally, this section describes where to start, gives basic
definitions, and gives more examples. After reading this, we recommend
you visit the physics glossary if you wish to have each variable
described in full.

Before starting to try make a car realistic it's important to gather as
much technical information as you can. I know this is the boring part,
but it will really serve you well. Beginners especially have a tendancy
to overlook this fact. In fact, gathering data will often be nearly as
difficult as altering the actual physics parametres themselves. In
reality, most racing teams know the majority of data that would need to
go into these files. Unfortunately, teams are usually unwilling to
disclose this sensitive information. It would make things comparitively
easy if you could have all this data. Regardless, I would recommend you
try to find as much as possible, because if you find data to the
contrary later, it will usually consume significant time to re-match lap
times and/or performance specs again. To give you a general idea, I
spend approximately one quarter to a third of my time just researching.
Reference photos and other materials can be of great assistance too,
especially if technical data is scarce. Photographs most useful are
particularly those high-resolution non-perspective suspension
photographs. Measuring the photos will give you base values to create
suspension geometry. Even if you can get hard data on anti-dive, camber
change, toe-change, etc. you may find using these pictures useful to
create a base and work from there.

Normally, it would be best if the model has been completed before you
start the physics. Though that might not be possible, at the very least,
the wheels should be in the correct position. If there is any chance of
them moving the suspension geometry may need changing, along with other
variables. If you reposition the supsension arms at a later date (due to
model changes), this will often result in erronous data entries, and at
the least, is not favourable. Once the wheels are in the final position,
take measurements of where the pivot points are (or ask the modeller for
these co-ordinates), it is best to use these co-ordinates for the
suspension file, though often not 100% necessary. Wheelbase and track
should be 100% correct. If the wheel position of the model has not been
positioned as yet and you are aware of the vehicle track and wheelbase
you can plug these values into the HDV, you will find these variables
under the :ref:`archive/isi_mod_tut/car/car_physics_glossary:[SUSPENSION]`
section.

Before creating any physics, I suggest you download `EngNet Converter
<https://www.engnetglobal.com/>`_ . EngNet converter is a tool that will
VERY accurately convert values into other units, such as Horsepower to
KiloWatts, or KPa to PSI. I have created a small list of commonly used
units in terms of car manufacturers specs, and those used in rFactor.
:ref:`archive/isi_mod_tut/car/car_physics:Unit Conversion`.

Another set of useful tools are the Microsoft PowerToys, namely they
include a useful graphing calculator. The best aspect is that is has a
large display and memory. It's not a true graphing calculator in the
sense that it is not as advanced as it could be, but for rFactor you
generally won't need anything more advanced.

Because some people misunderstand the range values, they have been
further explained here.

"All Range values follow this rule (Minimum setting, step size, number
of steps)"

For example let's use Engine RPM. 1st value is minimum RPM setting. 2nd
value is difference per setting increase (i.e. A value of 50 means go up
by 50 each time). 3rd value is how many settings there are. Let's say
for example we have the values (5800,50,5). From this, maximum RPM will
be 6000. This is how it works, 5800 counts as the 1st setting, 5850 is
no.2, 5900 is 3, 5950 is 4, 6000 is 5. Setting the 3rd value to a
numerical value of 1 will mean there is no adjustability, it would be
stuck at 5800rpm.

All the Setting= values create an initial car setup when there is no
setup file (\*.SVM file) to go from. Remember that 0 is actually the
first setting in these cases. The first setting is 0, 2nd is 1, etc.

Introduction - Information Gathering
====================================

Beginning
---------

The first step is to copy the physics files from an original rFactor
file which you think is most similar to the vehicle you are creating
physics parameters for.

Information gathering possibilities will vary according to which vehicle
you are creating physics for. If you are developing physics for a
vehicle you own, or have the availability to take measurements from and
or test, that is a great way to learn. If you own the car, not only do
you know how it drives, but you can make some calculations and take
measurements straight from the source. The best way to develop physics
is to start with the knowns. Always start with the knowns. Mass is the
most obvious thing. It's (generally) easy to find, it's a definate that
won't need changing in the future. Altering mass will provide you with
greater vehicle accuracy and unlike many other values it is not a
subjective opinion. If you can weigh the car yourself that's great. It's
best to try weigh it with driver and fluids but not fuel. If the car has
been weighed with fuel that's ok, just try estimate how much fuel is in
the car. Each litre of fuel weighs approximately 0.75kg, from this you
could conclude within reasonable accuracy, the weight of the car. If the
car weighs 1380kg, with 80 litres of fuel, the real weight should be
around 1320kg (80\*0.75=60kg 1380-60=1320kg). If you can't measure the
weight try to find a reputable source, but make sure you know the method
of weighing used. Generally, weight given is curb weight. Curb weight is
measured as car + engine fluids (oil, coolant, etc.) , no driver, and no
fuel. There are many exceptions to this though, you will also find that
these conventions are not always followed. Dry weight is vehicle weight
without fluids and driver. Formula one vehicles are weighed with fluids,
and driver.

Next is engine power. To calculate power the following formula applies:

Horsepower=Torque(NM)\*RPM/7120.8

Torque(NM)=Horsepower\*7120.8/RPM

The next value I suggest you change are the RPMTorque values. The engine
power curve is located in an engine.ini file (though it could be named
almost anything). I have created an excel power curve approximately
correct for a Nissan Skyline R32 GTS-T. It peaks at around 212hp @
6200rpm. Download. You will need to use a suitable spreadsheet program
that can view Microsoft Excel spreadsheets to open this file. If you
don't have Microsoft Office, I recommend `Open Office
<http://www.openoffice.org/>`_, it's a great open source office style
program, and is free.

Ideally, you should try and get access to a real power curve graph.
Often you will not be able to so. Generally peak power and torque should
be sufficient to reasonably accurately estimate the entire power curve.
Torque should be negative at low end because an engine can not overcome
friction at 0 rpm (with the obvious exception of an electric motor,
which actually produces peak torque near this point). Most engines will
not be able to overcome friction forces until they spin to approximately
250-500rpm. An engine should not produce negative torque at any point
afterwards, however after the Over Rev/ fuel cut out/RPM limiter the
motor should not produce much above 0 NM of torque, going into negative
values here is acceptable. Unless you know better and have tried it for
yourself, the fuel cut/rev limiter is generally about 200-300rpm over
the redline. A Nissan Skyline R32 with a RB20DET for example, engages a
fuel cut (rFactor can't simulate this, RPM limiter is close enough
though) at just under 7800rpm while the redline is only indicated at
7500rpm. Note that the redline in a race car is also usually the rev
limit. Negative power torque should never be greater than engine braking
torque, as throttle application never reduces torque.

Tires, in the HDV file you should change the name of TireBrand= to
something suitable that will be unique to that vehicle or mod. You may
consider making it specific to the brand & type of tires. Copy and paste
the original game vehicle with the most similar tires. You may choose to
use tires from another mod too, but make sure you have permission BEFORE
taking any such actions unless you keep the vehicle for private use. The
first thing you'll want to do with these tires is give them correct
dimensions, Width= & Radius=. To calculate width, simply take the first
value of a specification such as 265/40 R17, then divide the first value
by 1000. This converts to a game ready value of 0.265.

To calculate the radius of tire using these numbers (265/40 R17) we can
determine needed dimensions for rFactor. Firstly use width times profile
265\*0.4 (the 40 part is 40% or 0.4 in multiplication terms) then add
half rim radius 8.5\* (conversion constant, inch to millimeters
convertion = 25.4), giving a value of 321.9 or in metres, 0.3219 (game
ready). The complete formula is (Width\*(
Profile/100)+(0.5\*WheelRadius\*25.4))/1000.

Some times you will see specs more like 27 / 65 x 18 & 30 / 70 x 18. You
will have to make assumptions, in this case they are obvious, the first
value is width in centimeters, the second is diameter in centimeters,
and the rim size is in inches. The front tires are Width=0.27 (27/100),
Radius=0.325 (65/2/100).

Now that you have read this tutorial, feel free to visit the
:ref:`archive/isi_mod_tut/car/car_physics_glossary:Physics Glossary` for more
information on specific variables.

Unit Conversion
===============

You can also visit the `www.engnetglobal.com
<https://www.engnetglobal.com/>`_ homepage for on site unit conversions.
All of these figures are taken from the EngNet Tools (V1.4.5.0).

+-----------------+-------------------------------------------------+--------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Unit Category   | Units                                           | Conversion Factor  | Description (if necessary)                                                                                                                                                                                         |
+-----------------+-------------------------------------------------+--------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Acceleration    | Km/h per second into Meters per second²         | 0.2777778          | Kilometers per hour gained every second, converted to meters per second gained per second. Alternatively, divide by 3.6.                                                                                           |
+-----------------+-------------------------------------------------+--------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Angle           | Degrees into Radians                            | 0.01745329         | Alternatively, divide by 57.29578.                                                                                                                                                                                 |
+-----------------+-------------------------------------------------+--------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Energy (Torque) | Foot-Pounds (FT-LBS) into Kilogram Meters (KgM) | 0.138255           | Alternative, divide by 7.2330114.                                                                                                                                                                                  |
+-----------------+-------------------------------------------------+--------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Energy (Torque) | Foot-Pounds (FT-LBS) into Newton Meters (NM)    | 1.355818           | Alt, div by 0.73756212                                                                                                                                                                                             |
+-----------------+-------------------------------------------------+--------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Energy (Torque) | Kilogram Meters (KgM) into Newton Meters (NM)   | 9.80665            | Alt, div 0.101971621                                                                                                                                                                                               |
+-----------------+-------------------------------------------------+--------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Length          | Meters to Inches                                | 39.37008           | Div 0.0254.                                                                                                                                                                                                        |
+-----------------+-------------------------------------------------+--------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Length          | Feet into Inches                                | 12                 | 0.08333r                                                                                                                                                                                                           |
+-----------------+-------------------------------------------------+--------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Length          | Miles (International) into Kilometers           | 1.609344           | 0.621371192                                                                                                                                                                                                        |
+-----------------+-------------------------------------------------+--------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Linear Velocity | Km/H into Meters per Second                     | 0.2777778          | 3.6                                                                                                                                                                                                                |
+-----------------+-------------------------------------------------+--------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Power           | Horsepower (British) into KiloWatts             | 0.745701           | 1.34102                                                                                                                                                                                                            |
+-----------------+-------------------------------------------------+--------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Pressure        | Bar into KiloPascal                             | 100                | 0.01                                                                                                                                                                                                               |
+-----------------+-------------------------------------------------+--------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Pressure        | Bar into Pound force/Inch² (PSI)                | 14.5038            | .145038 for KPa to PSI. PSI into Bar, 0.0689474                                                                                                                                                                    |
+-----------------+-------------------------------------------------+--------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Temperature     | Celcius to Kelvin                               | K = C + 273.15     | Kelvin is an absolute temperature. Expansion rates of materials are linear using this scale. 0 Kevlin is absolute 0, no lower can be acheived. Atoms stop moving at this temperature.                              |
+-----------------+-------------------------------------------------+--------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Temperature     | Fahrenheit to Celcius                           | C = (F - 32)\* 5/9 | Degrees °C to Deg. °F (F = C \* 9/5 + 32)                                                                                                                                                                          |
+-----------------+-------------------------------------------------+--------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Temperature     | Fahrenheit to Rankine                           | R = F + 459.67     | Rankine is the absolute temperature using the 'fahrenheit scale'.                                                                                                                                                  |
+-----------------+-------------------------------------------------+--------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Volume          | Gallons (US, Liquid) into Liters (decimeters³)  | 3.785412           | Decimeters are 1/10th of a normal meter. A cubic meter will therefore be 1000x larger, 1\*10³. 1 liter is 10x10x10 centimeters, this can be used to determine the fuel tank size (how much room it will occupy).   |
+-----------------+-------------------------------------------------+--------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Weight          | Tons into Kilograms                             | 1000               |                                                                                                                                                                                                                    |
+-----------------+-------------------------------------------------+--------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Weight          | Pounds (avdp) into Kilograms                    | 0.4535929          | AVDP is the widely used pound weight.                                                                                                                                                                              |
+-----------------+-------------------------------------------------+--------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Weight          | Stones to Kilograms                             | 6.350301           | Could be used to determine driver weight.                                                                                                                                                                          |
+-----------------+-------------------------------------------------+--------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Metric Unit Conversions
-----------------------

+--------+--------+---------+
| Factor | Prefix | Symbol  |
+--------+--------+---------+
| 10^6   | Mega   | M       |
+--------+--------+---------+
| 10^3   | Kilo   | K       |
+--------+--------+---------+
| 10^2   | Hecto  | H?      |
+--------+--------+---------+
| 10^1   | Deka   | D?      |
+--------+--------+---------+
| 10^-1  | Deci   | d       |
+--------+--------+---------+
| 10^-2  | Centi  | c       |
+--------+--------+---------+
| 10^-3  | Milli  | m       |
+--------+--------+---------+
| 10^-6  | Micro  | µ       |
+--------+--------+---------+
