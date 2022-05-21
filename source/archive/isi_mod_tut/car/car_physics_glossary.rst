****************
Physics Glossary
****************

*Annotations restricted to this tutorial*

GE
   Ground Effects

CG
   Centre of Gravity (In reference to Height)

CF
   Centre of Forces

REF
   Reference Plane

Note that I continually use examples from many different types of
automobiles, this is to illustrate just how certain vehicles may
contrast. Also note that this tutorial is by no means complete. As more
questions are asked I will continue to expand this tutorial, and to
clarify difficult to understand explanations. Indeed, this tutorial will
also need updating as the game expands.

.. contents:: Contents
  :depth: 1
  :local:

Section 1 - \*.HDV
==================

*Sub-sections*

-  General
-  Left Fender
-  Right Fender
-  Front Wing
-  Rear Wing
-  Body Aero
-  Diffuser
-  Suspension
-  Controls
-  Engine
-  Driveline
-  Front Left
-  Front Right
-  Rear Left
-  Rear Right

[General]
---------

General details on the vehicle.

Rules= 0 for no setup rules, 1 for stock cars. This is basically a
NASCAR thing. NASCAR's are not allowed to adjust left to right ride
heights and things like that. You could thus only alter front-rear ride
heights. You should have Symmetric=1 when you have this on, due to the
differing menu systems.

GarageDisplayFlags= How settings are displayed in garage (Add): 1=Rear
Wing, 2=Radiator, 4=More Gear Info.

Mass= The entire mass of vehicle inclusive of driver and all fluids with
the exception of fuel. You should attempt to determine whether the
vehicle weight is dry/curb weight, or with driver. Generally weight
given in official factory figures is curb weight, which is includes
fluids and but does not include driver. Fluids generally add about
8-15kg, the driver adds about another 70-85kg. The original Mini Cooper
for example, with it's sump mounted gearbox lubricated by engine oil,
would be closer to 6 kg. Air cooled engines, despite not having a water
filled radiatior, aren't nessecarily lighter as their oil capacity is
often double that of a water cooled unit.

Inertia= Total inertia of the vehicle, different components have
differing inertial values. These can be found inside the suspension
geometry file. (See section 3 for more details on the PM file)

Inertia essentially has two components, mass and mass distribution. The
second of which is known as polar moment. You require a certain amount
of energy to rotate a body of mass in any orientation. A vehicle with
exactly double the mass will have exactly double this inertia force. As
I mentioned, mass is not the only component, you must also consider mass
distribution. Polar moment describes the distances that mass is spread
away from the center of a body's center of gravity. Because F1's have
their mass very centralised, developing physics for a sedan which has
say exactly double the mass will mean that the inertia of the vehicle
will be far greater than double. This is due to mass distribution being
further from the vehicle's centre.

To calculate the inertia of a rectangular object the following formula
can be applied; Pitch = (Mass/12)\*(Length\*Length+Height\*Height) In
short the formulae is (M/12)\*(Y²+Z²) or (M/12)\*(L²+H²) Yaw =
(M/12)\*(Length²+Width²) Roll = (M/12)\*(Height²+Width²)

The above formula assumes a perfect rectangular prism, which has equally
distributed mass across the entire object. Note that automobiles are not
like this. In most cases, the mass is more centralised than the vehicle
dimensions (especially true for open wheelers). So you'll probably have
to make an educated guess as to what the distribution is.

For Spheres the following formula applies; Inertia=2/(5\*Mass\*Radius²)

The first value of inertia is the pitch. Second value is the yaw. Third
value is roll. These values are measured in kgm/m. Inertia is the force
required to rotate the car, and the same force is required to stop the
rotation. Pitch is the rotation that occurs under braking and
accelerating, and going up and down hills, you could consider it to be
in use when you flip a car front to back or vice versa. A higher first
value will result in reduced response in terms of dive (under braking)
and squat (under acceleration). Yaw is force required to start and stop
the car from turning, a high value will reduce the steering response and
may cause temporary understeer in changes of direction (value should
always be greater than pitch, except maybe some trucks/buses?). High
values will also reduce the cars' sensitivity to bumps and make it
easier to drive. Roll is rotation of the car as it leans into a corner.
A low value will make the car lean into a corner more aggressively. A
high value will result in a slower and more stable lean. In any car,
roll inertia will always be lower than the pitch, and yaw.

Let's take a look at an F1 C 2002 Williams, Mass=601.8 Inertia=(506.7,
577.4, 117.3). One of the possible measurement combinations (all
possibilities are extremely similar!) is as follows, Length=3.1047m
Width=1.369m Height=0.682m. The car is actually much larger
dimensionally in all aspects. You should note that, an empty F1 chassis
weighs an amazing 30-35kg. The majority of the mass is made up by the
engine (about 95kg), driver (about 75kg), and ballast (75-90kgs), all of
which, are close to the centre of gravity. The result is that despite
the vehicle being 1.8m wide, under 1m tall and around 4.5m long, the
inertia contributions are far less. A GT1 would also have a very low
height, though it would still be slightly greater than an F1, but length
and width would increase significantly. I expect width would probably
increase the most as a percentage, followed by length, and finally
height.

Looking at the drastically higher NASCAR Thunder 2004 inertia values
makes it apparent:

Mass=1571.1 Inertia=(2507.7, 2778.2, 474.6), the car is 2.61x heavier
than an F1, but on average the inertia values are 4.79x greater! This
kind of ratio would be appropriate for most road cars and drag cars too,
but not advanced race cars. NASCAR's have large (and hence heavy)
protection bars and roll cages, are largely responsible for its high
inertia, combined with steel body construction. Mid engine cars should
always have less inertia because the engine is usually a heavy part of
the car (266kg on a road going McLaren F1), being in the centre of the
car it helps lower the polar moment. Please note that engine mounting
position will minimally affect the 3rd inertia value, roll. This is
because roll does not have a length component.

Possible dimensions for these NASCAR values are Length=4.2865m,
Width=1.6869m, Height=0.8829m.

FuelTankPos= Location of fuel tank CG in relation to the center of the
rear axle at the bottom of the chassis (at the reference plane). 1st
value is lateral offset. 2nd value is height. In normal sedans the third
value is often positive and almost always has a very low value (whether
it be positive or negative). Highly tuned mid and rear engine race cars
often have the fuel tank over 1 metre in front of the rear axle (behind
driver, infront of engine). Sometimes, though rare, it can be further
than 2 metres infront. An example of this is the 1996 Porsche 911 GT1,
which has the fuel tank CG approximately 2.5m infront of the rear axle.

FuelTankMotion= This simulates fuel 'slushiness' in the fuel tank. The
first value, spring rate, will define how far the fuel weight moves
(dependant on G-Forces). Critical damping is used to reduce rapid fuel
movement, this works much the same as any suspension damper. It can be
very difficult to know what values to use. Many standard vehicle fuel
tanks have nothing to stop fuel splashing. Think of it like a glass of
water, damping is very low and the water is free to move around quite a
lot. Race cars often have fuel bladders\\ tanks with baffles in place.
Fuel tank baffles can not change the liquid density of fuel, therefore
damping will remain very similar (if not identical) to a vehicle without
these. On the other hand baffles reduce overall fuel movement, this is
simulated using a high spring rate variable. The spring rate variable is
not dependant on fuel load, the fuel CG will move by the same distance
regardless of fuel load. To calculate movement of the CG, we take
acceleration of the vehicle body (in any given direction), and we divide
this by the spring rate. Acceleration/Spring Rate=Distance moved. Let's
say we take 1G of acceleration, 9.8ms/560=0.0175m, for every G of
acceleration acting on the fuel tank, we recieve 1.75cm of movement.
This assumes the force has been applied long enough to move the fuel to
this position.

Notes= You can add notes about the vehicle or default setup here, these
will appear in the vehicle setup menu.

Symmetric= 1 translates to vehicle settings are copied from left to
right. This is changeable while actually running the game though. It's
important this is set to 1 if you have rules set to 1, due to the rules
applied with stock cars.

DamageFile= Name of the damage file (Damage file aspects covered in
Section 7)

CGHeight= 1 dimensional value - Vertical centre of gravity above bottom
of chassis. Realistically, possibly as high as 0.4 for sedans and maybe
even greater. For racing sedan cars however, I expect about 0.32 or so,
GT style cars possibly a little lower. Formula type cars around
0.20-0.28. Cars may have a tendancy bounce a little when you increase
this value, so make sure to increase damper of the tires (\*.TBC file,
Section 2) a little as you increase this value. In order to be able to
use very high or very low CG values you will definately need to change
roll centre of the suspension, otherwise the car will never feel right.
(See \*.PM file, Section 3).

CGRearRange= Percent of weight on rear wheels. Around "0.47" for front
engine sedans. Usually, weight distribution is not adjustable for sedans
and other front engine - rear drive cars because they aim for the
furthest rear weight bias possible (with the exception of some oval
racing vehicles), so the 3rd value usually would be set to 1 (remember 1
really means 0 adjustments). Generally only MR race cars have some
adjustability. If the category requires a relatively high weight limit,
teams are free to position balast as they wish, hence increasing the
amount of available adjustment. Regarding front engine, rear drive cars,
while sometimes they are technically permitted to move their ballast
freely, they will generally only have 1 mounting position, as far back
as possible (except for oval racers).

Note: Remember the following values are VERY sketchy. 1st initial is
engine position, 2nd initial is driven wheels. I.e. FR would represent a
front engine, rear wheel drive car. M4, mid-mounted engine with 4WD
drive.

Fraction of Mass on rear wheels. FF cars have about 0.4, F4 cars have
about 0.46, FR wheel drive cars have about 0.47, M4 cars have about
0.53, MR cars about 0.55, R4 about 0.57, RR have about 0.59 (Note that I
have seen highly tuned FR cars with up to 0.53 rear weight bias! This
demonstrates how different vehicles may contrast enormously). Indeed,
some cars can be surprising. A 1997 to current Jeep Wrangler for example
has a 0.49 rear weight bias in soft top form, and 0.5+ for a hard top
equipped vehicle, a shock considering the four litre iron lump of an
engine in the front and the nothingness of the rear.

CGRightRange= Fraction of mass on right wheels. (0.5 is equal to 50%)
Usually very close to 0.5 on all cars. Can depend on a particular hand
drive car. I.e. Left hand drive car may have a value like 0.49. Race
categories with very restricted weight regulations (cars with a lot of
ballast) even with the driver off centre will probably have 50%. In
those categories it may even be possible to change right-left weight
bias by moving ballast. Remember one side can be more adjustable than
the other though, depending on driving position.

In order to determine the left-right weight bias you'll need to know the
weight of the car, the driver weight and what the left-right weight
distribution is without driver. You will also need to know the front and
rear track of the vehicle. If you know the bias with driver, you won't
need to read this paragraph, though you may yet find this interesting.
To simplify things, all we are going to use the average of the front and
rear track. Most vehicles have close to a 50% weight distribution offset
front to rear anyway. Let's take a look at the 2005 Jaguar XJ. This
vehicle has a mass of 1742kg vehicle and we will assume the driver
weighs 80kg. Let's assume that the middle of the driver seat is exactly
450mm (guess) away from the center of the vehicle. The Jaguar XJ has a
front track of 1557mm, a rear track of 1547mm, and so the average is
1552mm. In actual fact, it is best to get the exact distance between
center of the tires. Regardless, with these numbers we can calculate (to
within reasonable accuracy) what the weight distribution is in lateral
terms. As I don't actually have any figures on the Jag's empty lateral
weight distribution we'll just assumer that it's 50%. For beginners
especially, it's much easier to grab a piece of paper and draw a diagram
to help.

Because we want to know the right weight bias, we will start
calculations from the left.

Mass\*distance from left+Mass\*distance from left=Upward force from
right tire\*track.

((Mass\*DistfromL)+(Mass\*DistfromL))/track=Right weight.

((1742\*.776)+(80\*(0.776+0.45))/1.552=934.196 kgs.

Vehicle Weight+Driver Weight=Total Weight

1742+80=1822

934.196/1822=0.5127, 51.27% right weight distribution. Keep in mind that
this is a very heavy vehicle too. In a lightweight sports car the
difference will only be greater (unless you sit in the middle, like a
McLaren F1).

Many race cars have their batteries, ecu's and accessories placed on the
other side to combat lateral off-center weight bias. However, these
compensations will rarely be enough to fully compensate for the
off-center weight bias. A road car usually does not have any of these
'countermeasures', indeed the battery seems to usually sit on the
driver's side.

Note these are old descriptions, need to be re-written.

The following are locations for points where the car will bottom out.
These are the older values. Later we will show you new and more useful
rFactor undertray values.

FLUndertray= The first value is width. This defines the flat part of the
bottom of the chassis. Firstly find the total width of the bottom of the
chassis then divide it by 2. Then subtract the rear tire width from it
(just 1 of them)(Value must be positive). The second value is usually 0,
you can change this though. The 3rd value is how far ahead the car is
from the front axle. Take a couple cm away depending on if the front is
curved even as much as 7cm(0.07). (Third Value is negative. Except for
Open wheelers)

FRUndertray=All values the same as 1st (FL) except 1st value is
negative.

RLUndertray=All values the same as 1st (FL) but the third value is not.
It usually is between 0 & 0.3. Before kick up at the back (Diffuser).

RRUndertray=All values the same as 3rd (RL) but 1st value is negative.

Instead of the previous variables we recommend using these new
variables. They allow more accurate points where the chassis can bottom
out, as points are more numerous.

.. code::

   Undertray00=(0.20, 0.0, -1.00) // corner offset from center of wheels in
     reference plane
   Undertray01=(-0.20, 0.0, -1.00) // corner offset from center of wheels in
     reference plane
   Undertray02=(0.20, 0.0, 1.30) // corner offset from center of wheels in
     reference plane
   Undertray03=(-0.20, 0.0, 1.30) // corner offset from center of wheels in
     reference plane
   Undertray04=(0.58, 0.0, -0.50)
   Undertray05=(-0.58, 0.0, -0.50)
   Undertray06=(0.58, 0.0, 0.80)
   Undertray07=(-0.58, 0.0, 0.80)
   Undertray08=(0.58, 0.0, 0.0)
   Undertray09=(0.0, 0.0, 0.0)
   Undertray10=(-0.58, 0.0, 0.0)

WedgeRange= Ignore this for now. Rounds of wedge.

WedgeSetting=40

WedgePushrod=0.0 Each round of wedge changes rear-left jacking screw by
this amount (0.0 to disable, use Rules to allow FR ride height)

TireBrand= Name of tire file without the extension. (example, if the
file name is Dunlop.tbc, this value should be set to "Dunlop". Tires
covered in Section 2)

FuelRange= i.e.(1,1,65) Amount of fuel storage in fuel tank. The 1st and
2nd values should probably be left at 1 because it's easier to work with
and provides greater adjustability. The third value defines the maximum
amount of fuel in liters (assuming other 2 values are left at 1). If you
are working in gallons, one gallon is equivalent to 3.785412 liters.

AIAimSpeedsPerWP=(15,25,35,42,50,100,100,100) Speeds at which to look
ahead X. ---- Not sure what this really does ----

AICornerReductionBase=80.0

AIMinPassesPerTick=3 Minimum passes per tick, lower values provide lower
CPU useage, and can increase game performance. Higher values allow more
realistic AI suspension settings, at the cost of CPU useage.

AIRotationThreshold= Rotation threshold in radians per second to
temporarily increment passes per tick to improve accuracy and stability
of AI in corners. 1 radian per second is equivilant to 57.29578 degrees
per second.

AIEvenSuspension= Averages out spring and damper rates to improve
stability (Range: 0 - 1)

AISpringRate= Spring rate adjustment for AI physics, used to soften or
stiffen suspension for AI vehicles. Decrease this to soften spring rates
to keep the AI stable. 1 is equivalent to the setup file or default
setup.

AIDamperSlow= Contribution of average slow damper into simple AI damper.
This simplifies dampers when used for AI.

AIDamperFast= Contribution of average fast damper into simple AI damper.

AIDownforceZArm= Hard-coded center-of-pressure offset from vehicle CG.

AIDownforceBias= Bias between setup and hard-coded downforce value
(Range: 0-1). 0 is most realistic, 1 is least realistic. A value of 0
will ensure the AI do not have more downforce than the player? This can
be useful to improve AI stability though, especially if they have
problems at high speeds.

AITorqueStab= 1st value - AI Resistance to acceleration/brake/hill
spinning? 2nd value - AI Resistance to corner spinning? 3rd value - AI
Resistance to rolling? Trade off is that these slow AI response.

FeelerFlags= How collision feelers are generated (Add): 1=Box Influence
2=Reduce Wall-Jumping 4=Allow Adjustment Hack 8=Top Directions

FeelerOffset= Offset from CG to use when generating feelers.

FeelersAtCGHeight= Whether corner and side feelers are automatically
adjusted to CG height

.. code::

   FeelerFrontLeft=(0.750,0.384,-1.850) // front-left corner collision feeler
   FeelerFrontRight=(-0.750,0.384,-1.850) // front-right corner collision feeler
   FeelerRearLeft=(0.800,0.384,1.510) // rear-left corner collision feeler
   FeelerRearRight=(-0.800,0.384,1.510) // rear-right corner collision feeler
   FeelerFront=(0.0,0.384,-2.040) // front side collision feeler
   FeelerRear=(0.0,0.384,1.510) // rear side collision feeler
   FeelerRight=(-0.800,0.384,-0.247) // right side collision feeler
   FeelerLeft=(0.800,0.384,-0.247) // left side collision feeler
   FeelerTopFrontLeft=(-0.1,0.900,0.160) // top front-left collision feeler
   FeelerTopFrontRight=(0.1,0.900,0.160) // top front-right collision feeler
   FeelerTopRearLeft=(-0.500,0.850,1.600) // top rear-left collision feeler
   FeelerTopRearRight=(0.500,0.850,1.600) // top rear-right collision feeler
   FeelerBottom=(0.064,0.249,-0.10) // bottom feeler The feelers defined here
     are for the source vehicle, which touch the target vehicle on the
     collision GMT. In other words, vehicle-to-vehicle collisions are
     actually line-to-triangle collisions.

[LEFTFENDER]
------------

Left fender details. This is an optional part in rFactor, these are
primarily used in NASCAR. Other categories use them occasionally. The
McLaren F1 GTR Longtail used fender flares at Helsinki in 1997 for
example.

Because these entries are optional, we have left some standard NASCAR
settings to show you how the values are accepted by the game. Of course,
at the bottom of this page there is an example file showing every last
possible variable that rFactor will accept.

FenderFlareRange=(0, 0.00635, 7) // Front left fender flare range in
meters of extra flare over base.

FenderFlareSetting=3

FenderCenter=(0.80, 0.15, -0.32) // Center of fender aero forces. As
with the FRONT WING aero forces are offset from the center of front axle
at the reference plane.

FenderDragParams=(0, 0.2965, 0) // Base drag, 1st order, and 2nd order
drag per meter flare. For more detailed information on Drag/LiftParams,
please check the front wing section.

FenderLiftParams=(0, -1.0306, 3.782) // Base lift, 1st order, and 2nd
order lift per meter flare

FenderSideways=(0.1) // Dropoff in downforce with yaw (0 = none, 1 =
max)

[RIGHTFENDER]
-------------

Right fender details. This is an optional part in rFactor, these are
primarily used in NASCAR. Other categories use them occasionally.

FenderFlareRange=(0, 0.00635, 7) // Front right fender flare

FenderFlareSetting=3

FenderCenter=(-0.80, 0.15, -0.32) // Center of fender forces (offset
from center of front axle in ref plane)

FenderDragParams=(0, 0.2965, 0) // Base, 1st, and 2nd order drag per
meter flare

FenderLiftParams=(0, -1.0306, 3.782) // Base, 1st, and 2nd order lift
per meter flare

FenderSideways=(0.1) // Dropoff in downforce with yaw (0 = none, 1 =
max)

[FRONTWING]
-----------

Front Wing details. Optional part in rFactor, cars with front wings will
require these details. These can still be used even if the car does not
have a front wing.

FWRange= This is the adjustability of the front wing or air dam. Again
1st value is minimum setting. 2nd is Each step (Leave both these at 1,
unless the wing is adjustable in degrees and it's adjustability differs
from these values). The third value is how many settings you can have or
how precisely you can adjust the car. Depending on the car a value of
between 1 & 10 can be accurate. Only Formula One's have more
adjustability (40 with stock rF physics), they are however, almost
beyond this world in terms of technology. 1 for a road car, about 1-3
for most touring cars, about 10-20 for Cart. These settings must be
accounted for in the Drag/Lift.

FWSetting= What the front wing is set to initially. Usually this should
just be set a little over half of the medium setting. You should always
attempt to make default setting values a decent setup for most tracks,
an average if you will.

FWMaxHeight= From this height onward the front wing will not lose more
downforce from an increase in ride height. With a high value the car can
flip when the car leaves the car jumps, value should be around 0.2 for
race cars.

FWDragParams= This is the most complicated part. First value is initial
(and hence minimal) drag at the base setting. The second value is drag
increase per wing setting. Third value changes the the drop off in
efficiency as wing is increased.

The formula for calculating drag in real terms;

Initial Drag + Drag Increase \* (Wing Setting) + Efficiency drop off \*
(Wing Setting) ^ 2

In other words. 1stValue + 2ndValue\*(Setting) + 3rdValue\*(Setting)^2

Wing setting is the same as setting found in the SVM file. Meaning that
the minimum is 0, not 1. A value of 1 in the menu is actually 0 in terms
of setting.

Here is an example.

If Front Wing is set to 3 in the Menu, and FWDragParams=(0.06, 0.01,
0.00003)

Then to get downforce produced we plug the numbers in the formula
0.06+.01\*2 +0.00003\*2^2, the total drag at setting 2 (or 3 in the
menu) is 0.08012.

In a non-open wheeler vehicle it can be acceptable to have negative
front wing drag at the base setting, so long as this is factored in the
BodyDragBase= variable. Doing this will mean as you damage and lose your
front bumper, you actually lose top speed (because it was producing
negative drag). If you lose your front bumper/air dam/spoiler, air flow
becomes rough and flows over the newly exposed wheels, creating extra
drag. Obviously, in a race car you are likely to lose less speed,
because the standard front bar is producing downforce and has more drag,
a normal road car front bar is generally designed for minimal drag.

FWLiftParams= First value is base lift, ie. lift at minimum wing
setting. Note that negative lift is downforce. Second value is the lift
increase per wing setting. These parameters are essentially the same as
FWDragParams= but these variables apply to lift instead.

FWLiftHeight= Higher values make it more sensitive to increases in ride
height. Touring cars are not very sensitive to this and a value of about
0.3 is expected. This is because the front wing can only produce so much
ground effects. F1 and Indy/Cart vehicles are very sensitive to this, a
value of about 1 is appropriate as they have specially design the wings
to produce ground effects. A DTM should probably be around 0.5.
Reduction is easy to calculate. Take your base lift, add fwliftheight
multiplied by front wing ground clearance (measured in meters).
Lift+(LiftHeight\*Ground Clearance). Say lift is -0.2, lift height is
0.3 and current ground clearance is 0.1m. Then -0.2+(0.3\*0.1)=-0.17, at
20cm the lift is -0.14. In other words, this follows a linear
progression. This is not accurate but it is probably not worth the CPU
use of adding extra 2nd order variables, as the diffuser can be used to
complement this.

FWLiftSideways= Drop-off in downforce when wind direction is at 45
degrees to the wing. 0.5 would halve the downforce/lift @ 45 degrees. 1
will mean the wing no longer produces and downforce/lift at 45 degrees
of slide. If you use peakyaw this value will become overwritten? Values
close to 0.5 are considered to be accurate. When a wing is angled to
it's heading direction, it's angle at 45 degrees, and assuming it's flat
in it's X axis,

FWPeakYaw= First value is the angle in degrees, at which maximum
downforce occurs. The second value is used to multiply downforce at this
point. Generally, without end plates, optimum downforce can only occur
at an angle of 0 degrees to the air flow. Wing endplates are generally
not present on the front wing of vehicles, with the exception of winged
formula vehicles. End plates can increase downforce with yaw because
they allow extra air flow to cover the downforce producing plane of the
wing. This diagram (Not here yet) demonstrates how end plates increase
downforce with yaw, the effective increase is not much, but when you
consider vehicles do slide through corners a little bit, they can make a
big difference. Insteady of losing downforce as the car drives through a
corner (as would happen without endplates) downforce is actually
slightly increased. Accurate values for open wheelers are around (2,
1.02). Open wheelers also produce ground effects using their front
wings, yaw reduces the benefits of this by supplying more air under the
diffuser and thus making it work less efficiently.

FWLeft= Aero forces generated by moving left. The first value is the X
axis resistance. Meaning that this should always be negative for left
movements. Second value is Z axis resistance (vertical), 3rd value is Y
axis resistance, forward or backwards.

FWRight=(0,0,0) Aero forces from moving right

FWUp=( 0,0,0) Aero forces from moving up

FWDown=(0,0,0) Aero forces from moving down

FWAft=( 0,0,0) Aero forces from moving rearwards

FWFore=(0,0,0) Aero forces generated from moving forwards, this is
recomputed from settings. Left over from SCGT?????, it's basically it's
an old value and that does nothing (unless you delete the FWRange=,
FWDragParams= & FWLiftParams=).??????

FWRot=( 0,0,0) Aero torque from rotating

FWCenter= Centre of forces acting on the wing in reference to the centre
of front wheels at the reference plane.

[REARWING]
----------

Rear Wing details. Optional value in rFactor, cars with rear wings will
have these details. Do not add this section if the vehicle does not have
a rear wing.

Use explanations from above settings. RWRange= Third value is usually
between 5 & 25 on racing sedans and GT cars. Some road cars have more
than 1 setting like the Nissan Skyline R34 GT-R, which is adjustable
between 3 settings. Many other optional/after market wings for road cars
offer 2-5 adjustments. A DTM probably has about 15 settings, a modern
Cart about 20-30.

[BODYAERO]
----------

Body aerodynamic details.

BodyDragBase= I don't know the exact method used to calculate this value
in the game but you must include frontal area with drag coefficient.
(Someone??) This will reduce or increase the cars top speed, low values
will take longer to acheive absolute top speed. It will also increase
acceleration, but obviously has a greater effect at higher speeds. Every
time a car doubles it's velocity or speed, the drag will increase by
four times. Open wheelers have a poor Co-efficiency of Drag however,
they usually have a small frontal area which can almost compensate. A
modern road car despite having a greater frontal area will probably be
more aerodynamic than an F1.

BodyDragHeightAvg= Drag increase or reduction as ride height is
increased. Should be low value and possibly even negative for most road
cars because this allows clean air to flow under the car. If the car has
a flat full length under tray and purely race style, this value will
probably be positive and greater than 0.1+. This is as a result of
exposing suspension parts and tires.

BodyDragHeightDiff= Increase in Drag when the car has different front to
rear ride heights. Most cars have quite a high value, most race cars
should be higher than 0.5, aerodynamically precise automobiles such as a
Formula type car maybe be even greater than this. Anything wedge shape,
like an old CanAm will be more sensitive to this.

BodyMaxHeight= Max height game calculates drag/lift losses/gains from
ride height. Remember that too high can cause unrealistic flipping. The
diffuser should never produce lift when travelling forwards. See
Diffuser, try to ensure diffuser never reaches less than about 5% of
it's base downforce by altering BodyMaxHeight=.

BodyLeft=(-0.7, 0.03, 0) Drag resistance when car is moving leftward.
Notice the air resistance is in the opposite direction. All cars will
have lift as an effect of moving sideward, with the possible exception
of a sprint car, which when moving left? may produce some downward
force. On the otherhand, a rightward movement of spring cars will result
in high lift. On a normal car, I would expect a second value of around
0.03.

BodyRight=(0.7, 0.03, 0) Aero forces due to rightward movement.

BodyUp=(0.0, -1.5, 0.0) Aero forces from moving up

BodyDown=(0.0, 1.5, 0.0) Aero forces from moving down

BodyAft=(0.0, 0.10, -0.7) Aero forces from moving rearwards, drag should
increase when moving rearward in comparison to forward movement, though
it probably shouldn't be too much worse, on the other hand, lift should
be significantly higher than driving forward. I don't think there is an
automobile that would produce downforce when moving rearward. Reasonable
range for a street car, 0.08-0.3, with most having around 0.2 lift
value.

BodyFore=(0.0, -0.045, 0.200) Aero forces from moving forwards. The
second value, which affects lift, is important. 3rd value drag is
overwritten by BodyDragBase. The second value, lift, is an important
variable to get correct. This affects the cars high speed stability and
can affect lap times enormously. Let's take a look at the 2000
Volkswagen Beetle. According to Internet Auto Guide the beetle has a
wheelbase of 2512mm. Mulsannes Corner has the lift at 742 lbs @ 124 mph
with the front having 332 lbs of lift and the rear having a lift of 411
lbs. A value 742 lbs is equivalent to a value of 336.5kg. 124mph is
roughly 200km/h. From these variables we can conclude that the lift
value should be approximately 0.69 for a 2000 volkswagen beetle. Very,
very few vehicles will produce more lift at speed than the beetle, so
you could consider this to be an upper threshold. The wheelbase will
tell us where the BodyCenter should be placed on the Y-axis (3rd value,
front to back). If you do the math, 2512\*(332/742)=1124mm in front of
the rear axle. So BodyCenter value 3 should be -1.124. Read BodyCenter=
for more details.

BodyRot=(4.0, 3.0, 2.0) Aero torque caused by rotation. When a vehicle
moves through the air it forces air particles to flow around the moving
body. As this occurs the air particles that bombard the vehicle are
moved from their original position, some of these particles are forced
to follow the vehicle as it corners. The vehicle slows the air and
redirects these particles to follow it's own orientation. As this occurs
these particles add what could be considered extra inertia to the
vehicle. Essentially this effect causes the vehicle to feel as though it
has greater inertia in the form of pitch, yaw and roll. The difference
is that it does not add to the vehicles mass itself and occurs with
greater force at higher speeds. At high speeds the vehicle will feel as
though it has more inertia to overcome, the response of the vehicle will
not be as great.

BodyCenter= Center of aerodynamic forces acting on the body. The first
value should, almost always equate to 0. As usual, there are exceptions
though, some vehicles which are not symmetrical left to right, such as a
vehicle with an off-centre cockpit. Cars with a single external mirror,
or with 1 window open will have very slightly off-center aero forces.
Furthermore, some vehicles such as the Toyota TS-020, may have 2
mirrors, but they are not symmetrically aligned. I expect this would
only off-center the average flow by a couple hundred micrometers though
(in other words, a negligible off-set). It is important to note some
mirrors can actually reduce the aerodrag on some cars. The Ford Falcon
AU for example is reported to have less drag while the mirrors are on
the vehicle, (even with the windows closed) as they reduce air pressure
around doors and windows. Formula Renault's and some prototypes may
experience comparitively high off-center aero forces. The 2nd value
defines the height of the center of aero forces from the bottom of the
chassis. I would expect a value roughly in between 0.4 and 0.6 for
GT/Sedans. The third value is distance infront of the rear axle where
the center of aero forces occurs. Generally between 1 & 2 meters.

RadiatorRange=(100, -5, 1) Radiator range. Most vehicles can simply use
front grille tape to reduce the radiators' air intake. This decreases
drag and also (generally) helps decrease lift. The cost is that the
vehicles' radiator will be unable dissipate heat as efficiently and may
cause the engine to overheat. Generally, grille tape is used mostly
during qualifying to help give you that slight aerodynamic edge over
your opponents. More advanced vehicles may work differently, employing a
more expensive and time consuming system of changing over panels (such
as in F1), or adding "plates" of preset sizes, which prohibit the air
flow. Note that lower values will provide higher engine temperatures.
When changing this you may also need to alter your "RadiatorCooling="
value defined in the engine file (\*.INI).

RadiatorSetting=0 Default radiator setting

RadiatorDrag=(0) Effect of radiator setting on drag

RadiatorLift=(0) Effect of radiator setting on lift

BrakeDuctRange=(0,1,1) Brake duct range

BrakeDuctSetting=0 Brake duct setting

BrakeDuctDrag=(0) Effect of brake duct setting on drag

BrakeDuctLift=(0) Effect of brake duct setting on lift

[DIFFUSER]
----------

Diffuser details. Optional value in rFactor, only used for automobiles
with diffusers.

DiffuserBase=(-0.295, -1.5, 15.0) 1st Value defines the base lift of the
diffuser. 2nd value is the 1st order with rear ride height by default
produces a gain in downforce. 3rd Value is 2nd order with rear ride
height. 3rd is square value of drop off.

(DiffuserBase 1st Value)+((DiffuserBase 2nd Value)\*Rear Ride Height (in
metres))+(DiffuserBase 3rd Value\*Rear Ride Height^2) = downforce
Remember that there are many more values which determine downforce, such
as DiffuserRake and DiffuserLimits. A complete formula will be provided
at the end of this [DIFFUSER] section.

DiffuserFrontHeight=(0.275) 1st order of downforce loss when increasing
front ride height.

DiffuserRake=(0.05, 0.01, 0) Optimal rake (rear - front ride height),
1st order with current difference from opt, 2nd order

DiffuserLimits=(0.05, 0.20, 0.05) Minimum ride height before stalling
begins (0=disabled), max rear ride height for computations, max rake
difference for computations.

DiffuserStall=(0.5, 0.5) Function to compute stall ride height
(0=minimum, 1=average), downforce lost when bottoming out (0=none,
1=complete stall). Essentially the first value dictates whether to blend
the ride height (1) when calculating stalling or whether to use real
time calculations (0).

DiffuserSideways=(0.50) Dropoff with yaw (0 = none, 1 = max) Drop-off in
downforce when wind direction is at 45 degrees to the wing. 0.5 Is half
of the downforce/lift.

DiffuserPeakYaw=(0,1) 1st value is angle in Degrees where peak downforce
is generated. Second value is how much to multiply downforce by, at the
peak angle.

DiffuserCenter=(0,-0.05,-1.25) Centre of Forces produced by Diffuser.
(offset from center of rear axle at ref plane)

In order to determine the actual downforce produced by the diffuser the
following 'omni' formula applies (all ride height values must be
calculated in meters, also formula is split up to make it easier to read
and use); (((DiffuserBase 1st Value)+((DiffuserBase 2nd Value)\*Rear
Ride Height)+(DiffuserBase 3rd Value\*Rear Ride
Height^2))+(DiffuserFrontHeight\*Front Ride Height))=Total DownForce1.
Total Downforce1\*(DiffuserRake Value 1-())

To make this easier, I am planning to create an excel spreadsheet.

DiffuserLimits=(0.05, 0.20, 0.05) (Rear ride height - Front ride
height)=.06m (Rear ride height - Front ride height)=.04m (DiffuserRake
2nd Value\*(DiffuserRake 1st Value-(Rear ride height - Front ride
height))) (DiffuserRake 3rd Value\*(DiffuserRake 1st Value-(Rear ride
height - Front ride height)^2))

[SUSPENSION]
------------

Suspension details.

PhysicalModelFile= High detail suspension geometry file. File name
including extension. Ie. "f1susp.pm" See section 3.

CorrectedInnerSuspHeight= Instead of moving inner susp height relative
with ride height, use this offset. Setting this to -1 will use original
behavior.

ApplySlowToFastDampers= Most basic road cars should have this set to 1,
race cars usually have separate fast and slow damper speeds. This is
because having different fast and slow bump/rebound damper designs will
be more expensive. A brand new road going Mercedes S-Class on the other
hand will have different fast and slow dampers, but they are not
adjustable. This links the settings, not the values, I believe all new
decent quality dampers will have different fast to slow damper speeds,
but most will not be able adjust them independantly, you change one, you
change the other.

AdjustSuspRates= Adjust suspension rates due to motion ratio. Whether to
adjust spring rates or wheel rates? A value of 1 adjusts wheel rates, a
value of 0 spring rates? (Gjon take a look)

AlignWheels=1 Should probably leave this at 1. It aligns the wheels to
physics.

CenterWheelsOnBodyX=1 Corrects minor unintentional graphical offsets on
the X-Axis. Ensures that left wheels are exactly the same distance from
the center of the car as the right wheels are.

FrontAntiSwayRange= Same basic principle as other range values. Though
you can override the first setting with in rFactor.

FrontToeInRange=(-1.5, 0.1, 31)

FrontToeInSetting=14

RearToeInRange=(-1.5, 0.1, 31)

RearToeInSetting=17

LeftCasterRange= Caster acting on the left front wheel. Defines the
backward lean of the front left top hub suspension joint compared with
the lower arm. The effect of changing this is that the vehicle will want
to straighten the steering more. It also has the desired effect of
adding negative camber to the outside tire when steering, it also adds
positive camber to the inside tire which can increase grip. With a live
axle front suspension vehicle, caster is generally be very high, perhaps
up to 10 degrees. It is rarely possibly for a live axle setup to have
any negative camber.

RightCasterRange= Same thing as above, only regarding the right wheel,
should have the same adjustability, generally.

LeftTrackBarRange=(0.1778, 0.003175, 65) Rear-left track bar, Value can
be removed if vehicle does not have Track Bar. Track bar adjusts roll
center with a live axle setup.

RightTrackBarRange=(0.1778, 0.003175, 65) // Rear-right track bar, Value
can be removed if vehicle does not have Track Bar.

Do not include 3rd value in under this section if you are sure the
vehicle does not have 3rd springs/dampers. Trophy trucks can use these
values and other advanced off road trucks and probably some very high
downforce race cars. Generally though, these are not present. Note:
Formula one introduced this technology in 1997. (Bristow, 2004)

Because these are not present by default, and typing it out is long and
boring process, the formula has these optional 3rd springs. Feel free to
copy these into rFactor if you wish.

.. code::

   Front3rdBumpTravel=-0.005 // travel to bumpstop with zero packers and zero ride height (5mm compression)
   Front3rdReboundTravel=-0.065 // prevents rebound travel (for example, when upside down), 55mm max front ride height plus 10mm leeway
   Front3rdBumpStopSpring=150000.0 // initial spring rate of bumpstop
   Front3rdBumpStopRisingSpring=7.00e6 // rising spring rate of bumpstop (multiplied by deflection squared)
   Front3rdBumpStopDamper=2500.0 // initial damping rate of bumpstop
   Front3rdBumpStopRisingDamper=7.00e5 // rising damper rate of bumpstop (multiplied by deflection squared)
   Front3rdBumpStage2=0.060 // speed where damper bump moves from slow to fast
   Front3rdReboundStage2=-0.060 // speed where damper rebound moves from slow to fast
   Front3rdPackerRange=(0.000, 0.001, 41)
   Front3rdPackerSetting=5
   Front3rdSpringRange=(0.0, 10000.0, 21)
   Front3rdSpringSetting=7
   Front3rdSlowBumpRange=(0.0, 250.0, 13)
   Front3rdSlowBumpSetting=3
   Front3rdFastBumpRange=(0.0, 250.0, 11)
   Front3rdFastBumpSetting=1
   Front3rdSlowReboundRange=(0.0, 500.0, 17)
   Front3rdSlowReboundSetting=2
   Front3rdFastReboundRange=(0.0, 500.0, 15)
   Front3rdFastReboundSetting=1
   Rear3rdBumpTravel=-0.010 Travel to bumpstop with zero packers and zero ride height (10mm compression)
   Rear3rdReboundTravel=-0.090 Prevents rebound travel (for example, when upside-down), 80mm max rear ride height plus 10mm leeway
   Rear3rdBumpStopSpring=150000.0 Initial spring rate of bumpstop
   Rear3rdBumpStopRisingSpring=7.00e6 Rising spring rate of bumpstop (multiplied by deflection squared)
   Rear3rdBumpStopDamper=2200.0 Initial damping rate of bumpstop
   Rear3rdBumpStopRisingDamper=7.00e5 Rising damper rate of bumpstop (multiplied by deflection squared)
   Rear3rdBumpStage2=0.060 Speed at which damper bump moves from slow to fast
   Rear3rdReboundStage2=-0.060 Speed at which damper rebound moves from slow to fast
   Rear3rdPackerRange=(0.000, 0.001, 61)
   Rear3rdPackerSetting=10
   Rear3rdSpringRange=(0.0, 10000.0, 21)
   Rear3rdSpringSetting=8
   Rear3rdSlowBumpRange=(0.0, 250.0, 13)
   Rear3rdSlowBumpSetting=3
   Rear3rdFastBumpRange=(0.0, 250.0, 11)
   Rear3rdFastBumpSetting=1
   Rear3rdSlowReboundRange=(0.0, 500.0, 17)
   Rear3rdSlowReboundSetting=3
   Rear3rdFastReboundRange=(0.0, 500.0, 15)
   Rear3rdFastReboundSetting=1

[CONTROLS]
----------

Control details.

SteeringFFBMult=1.1 Vehicle-specific steering force feedback multiplier,
useful if the car has heavy or light steering.

SteerLockRange=(6,0.5,73) Steering lock of the car in degrees. Due to
the fact that all controllers have different precision this should be
highly adjustable. If you are developing physics for a race car, a max
lock of about 32 degrees should be sufficient. If it's a road/rally car
you should allow up to about 40 degrees so that users who own Driving
Force Pro steering wheel's and other similar wheels are able to use
realistic steering turn ratios, due to the ability to maintain precision
even with large steering lock. It will make their lives easier, and
allows them to compete in online races when they wish to use large
steering lock.

RearBrakeRange=(0.25,0.005,101) Rear brake bias, shouldn't have extreme
adjustability. Unless you know the real life adjustments, leave them as
stock in the HDV, this does not really matter. If you feel that it is
difficult to adjust brake bias while driving you could reduce the gap
between settings, in doing so you will have greater precision in the
adjustability.

RearBrakeSetting=15

BrakePressureRange=(0.75, 0.05, 6) Shouldn't have much adjustability
either. Maximum should NOT exceed 1. Road cars shouldn't have the luxury
of this adjustment, but seeing as this is still a game, you may want to
leave some slight adjustability. Certainly, I would doubt that there
should be a need to have any more adjustability than the above example.

HandbrakePressRange=(0.00, 0.05, 1) Change First value to a setting of 1
to enable handbrake. Of course if the car has a pathetic or hard to use
handbrake you can lower the value a little. Or you can change the 3rd
value and have users choose their own handbrake pressure.

HandbrakePressSetting=0 Default handbrake pressure setting.

UpshiftAlgorithm=(0.975,0.0) Fraction of rev limit to auto-upshift, or
rpm to shift at (if 0.0, uses rev limit algorithm).

DownshiftAlgorithm=(0.91,0.70,0.60) High gear downshift point (% of max
revs), low gear downshift point, oval adjustment

AutoUpshiftGripThresh=0.63

AutoDownshiftGripThresh=0.63

TractionControlGrip=(1, 0) I prefer a no grip advantage gained by using
aids only easier control performance gains. If the vehicle has traction
control in real life, you can permit small gains.

TractionControlLevel=(0.4, 0.8) Second traction control value should
generally be near worst case senario traction control levels, such as
intermediate tires on a full monsoon track with controllable amounts of
wheelspin. Remember that most real TC devices used in racing wouldn't be
able cope with slicks in the rain either. Road cars, generally, are more
conservative and biased towards circumstances such as driving on ice in
Sweden. The TC's effectiveness is dependant on whether it's biased
towards 'safety' or 'performance', and whether the system uses only ABS
sensors or incorporates accelerometers or is part of a complete vehicle
stability system.

ABSGrip=(1, 0) Again, if the vehicle does not have an ABS system in real
life, I recommend using a no-grip advantage setting, such as in this
example.

ABSLevel=(0.30, 0.90)

OnboardBrakeBias=0 Whether brake bias is adjustable from the cockpit of
the car. A value of 1 allows you to change brake bias as you drive. A
value of 0 will force any brake bias changes to be done in the pit
garage, assuming they are possible at all.

[ENGINE]
--------

Engine details.

SpeedLimiter= Whether or not the car has a speed limiter designed for
the pitlane.

Normal= File name of the engine file.

RestrictorPlate= If there is an entry in the GDB track file that
specifies a particular round uses the restricted engine
("RestrictorPlate=true") the game uses this lower powered engine file
instead. If there is only a single version of the engine, both variable
inputs should refer to the exact same file.

[DRIVELINE]
-----------

Driveline details.

ClutchInertia=0.00472 Inertia of the clutch. Heavy clutches, as used in
a road going Dodge Viper for example, could have as much inertia as
0.02+.

ClutchTorque=1009.5

ClutchWear=0

ClutchFriction=7.206 Friction produced by the drivetrain? Light clutches
also generally have less friction.

ClutchEngageRate=0.4 How quickly clutch is engaged with auto-clutch
driving aid.

BaulkTorque=360 How much torque clutch can handle before slipping.
Should roughly equal max engine torque, and probably always greater,
except possibly some modified road cars without upgraded clutches...

AllowManualOverride=0 Whether manual shifting temporarily overrides the
auto shifting aid.

SemiAutomatic=0 Whether throttle and clutch are operated automatically
without any driver aids enabled. Clutch must be used for launches and in
spins (At any time the car is stationary, such as an F1 car).

UpshiftDelay=0.160 Delay in seconds when selecting a higher gear (low
for semi-automatic vehicles, higher for manual)

UpshiftClutchTime=0.125 Time to ease auto-clutch in AFTER upshift (0 for
F1 cars) Usually should be quite low.

UpshiftLiftThrottle=0.00 Lift to this throttle fraction while upshifting
(if controlled by game not player))

DownshiftDelay=0.160 Delay in seconds when selecting lower gear (low for
semi-automatic, higher for manual)

DownshiftClutchTime=0.225 Time to ease auto-clutch in AFTER AFTER
downshift (used to be SemiAutoClutchTime) Downshift should generally
take longer.

DownshiftBlipThrottle=0.70 Percentage of throttle used to blip if
controlled by game AI (instead of player). Also used for Auto gearboxes
and clutches.

WheelDrive=REAR Which wheels are driven: REAR, FOUR (even torque split),
or FRONT

GearFile=ZR_gears.ini Ratio file name, Must come before
final/reverse/gear settings!

AllowGearingChanges=0 Stops changing of stock ratios until one buys a
tranny upgrade. If you wish for the transmittion to be adjustable as
stock, you can remove this entire variable.

AllowFinalDriveChanges=0 Similar to above, except it leaves the final
drive ratio stock until a diff upgrade is purchased.

FinalDriveSetting=1 Indexed into GearFile list

ReverseSetting=0

ForwardGears=5

Gear1Setting=2

Gear2Setting=9

Gear3Setting=14

Gear4Setting=18

Gear5Setting=20

DiffPumpTorque=250 At 100% pump diff setting, the torque redirected per
wheelspeed difference in radians/sec (roughly 1.2kph)

DiffPumpRange=(0.0,0.10,1) // Differential acting on all driven wheels

DiffPumpSetting=0

DiffPowerRange=(0.75,0.25,1) // Fraction of power-side input torque
transferred through diff

DiffPowerSetting=0 // (not implemented for four-wheel drive)

DiffCoastRange=(0.25,0.25,1) // Fraction of coast-side input torque
transferred through diff

DiffCoastSetting=0 // (not implemented for four-wheel drive)

DiffPreloadRange=(10.0, 5.0, 1) // Preload torque that must be overcome
to have wheelspeed difference

DiffPreloadSetting=0 // (not implemented for four-wheel drive)

[FRONTLEFT]
-----------

Some front left suspension, wheel, and brake details. The \*.PM contains
any remaining details.

BumpTravel=-0.010 Maximum permitted upward suspension travel

ReboundTravel=-0.12 Maximum permitted downward suspension travel

BumpStopSpring=160000 Initial spring rate of bumpstop

BumpStopRisingSpring=1.20e7 Rising spring rate of bumpstop (multiplied
by deflection squared)

BumpStopDamper=2000 Initial damping rate of bumpstop

BumpStopRisingDamper=9.00e5 Rising damper rate of same (multiplied by
deflection squared)

BumpStage2=0.090 Speed where damper bump moves from slow to fast

ReboundStage2=-0.090 Speed where damper rebound moves from slow to fast

FrictionTorque=7.81 Newton-meters of friction produced between spindle
and wheel

SpinInertia=1.633 Inertia in pitch direction including any axle but not
brake disc.

CGOffsetX=0.000 X-offset from graphical center to physical center (NOT
IMPLEMENTED)

PushrodSpindle=(-.15,-.1,0) Spring/damper connection to spindle or axle
(relative to wheel center).

PushrodBody=(-.25,0.300, 0) Spring/damper connection to body (relative
to wheel center).

CamberRange=(-2.0, 0.5, 1) Camber in degrees.

CamberSetting=0

PressureRange=(100, 1, 301) KPa of tire pressure, at the base/starting
tire temperature.

PressureSetting=70

PackerRange=(0, 0.001, 1)

PackerSetting=0

SpringMult=1.00 Take into account suspension motion if spring is not
attached to spindle (affects physics but not garage display)

SpringRange=(80000.0, 5000.0, 1) Spring rate of the suspension, measured
in Newtons per millimeter.

SpringSetting=0

RideHeightRange=(0.1250, 0.005, 1) Ride height in meters.

RideHeightSetting=0

DamperMult=1.00 Take into account suspension motion if damper is not
attached to spindle (affects physics but not garage display)

SlowBumpRange=(4500.0, 250.0, 1)

SlowBumpSetting=0

FastBumpRange=(3000.0, 250.0, 1)

FastBumpSetting=0

SlowReboundRange=(6000.0, 500.0, 1)

SlowReboundSetting=0

FastReboundRange=(4000.0, 500.0, 1)

FastReboundSetting=0

BrakeDiscRange=(0.025, 0.000, 1) Brake disc thickness in meters

BrakeDiscSetting=0

BrakePadRange=(0, 1, 5) Brake pad type (Currently not implemented)

BrakePadSetting=2

BrakeDiscInertia=0.750 Brake disc inertia per meter of thickness.

BrakeOptimumTemp=250 Optimum brake temperature in Celsius where peak
brake grip occurs.

BrakeFadeRange=400 Temperature outside of optimum that brake grip drops
to half (too hot or too cold).

BrakeWearRate=1.20e-13 Meters of wear per second at optimum temperature
with 100% brake application.

BrakeFailure=(1.4e-2,7.5e-4) Average and variation in disc thickness at
which point the brakes will fail.

BrakeTorque=1850 Maximum brake torque with no wear and at optimumal
temperature.

BrakeHeating=0.00100 Heat added linearly with brake torque times wheel
speed (at max disc thickness)

BrakeCooling=(3.60e-2,4.60e-4) Minimum brake cooling rate (base and per
unit velocity)(at max disc thickness)

BrakeDuctCooling=1.18e-004 Brake cooling rate per brake duct setting
increase per unit of velocity, at max disc thickness. In other words,
increasing brake duct by a value of 1 will increase cooling rate per
unit of velocity by this much. Velocity is measured in meters per
second.

[FRONTRIGHT]

[REARLEFT]

[REARRIGHT]

Section 2 - \*.TBC Tire File
============================

Tires are probably the single most important component when developing
physics. Despite the fact that there are considerably more input
variables in the other physics files, about 70% of my time is devoted to
creating accurate tire physics. They connect the car to the road and
they are very complex devices in terms of actual physics behind them.
`<________REFERENCE________>`.

*Sub-sections*

-  Slip Curve
-  Compound

The [SLIPCURVE] section
-----------------------

Name= Name of the slip curve

Step= Increment in the slip step, no longer serves any purpose???
---------- Is THIS TRUE? ------------

DropoffFunction= This describes how the slip curve dropoff is affected
when the peak of the slip curve changes. The peak of the slip curve may
move to a smaller or larger slip when load or speed changes. When this
happens, the slip curve is stretched or shrunk to match. The
DropoffFunction parameter allows you to affect the behavior beyond the
peak when this happens: -1.0 = dropoff occurs faster as peak increases.
The higher the peak (greater the load), the more precise car control is
required. 0.0 = dropoff curve does NOT change shape when the peak
changes 1.0 = dropoff curve is stretched or shrunk with the rest of the
curve, which means the dropoff may feel more gradual as the peak
increases. This is the default (and was the original behavior for NT03
and F1C). Note that you can pick in-between values for a blend of
behaviors.

`______REVISE ! ___` When DropoffFunction is set to 1, the entire slip
curve is multiplied according to the Long/LatPeak values. In other
words, if one of these peak slips is set to (0.1,0.3,15000) then the
peak of the slip curve at 0 load will now be at 0.1, or Sin-1(.1)=5.74
degrees. The entire slip curve will be moved according to this value. If
peak grip is acheived at 0.18 (10.37 degs) according to the slip curve,
this will mean the entire slip curve slip step is multiplied by 0.555r.
Disregarding aerodynamics, you will now be able to slide approximately,
0.555x as much as the slip curve would normally allow. Using a value of
0 would simply shift the entire curve after the peak, removing a value
of 0.08 from each slip step after the peak. The initial slope is still
multiplied by the peak slip though, therefore anything before the
normalized value of 1 in the data section is multiplied by 0.555. Grip
that was of acheived at 1.00 will now be shifted to 0.92. A value of 1
will multiply the entire slip curve. This is why generally having a
value of 1 is considered unrealistic. Because this is a confusing topic,
the following diagram has been created to help you understand.

-------------Note to self: Insert diagram showing an example of -1
dropoff, 0 dropoff, & 1 dropoff.-----------------

Data: This is the actual hard data slip curve. In order to get a true
slip curve you must remember these values will have to be processed by
the DropoffFunction, Long/LatPeak and SpeedEffects. Essentially, this is
the base slip curve of the tire, LatPeak for example is intended to
alter the peak of this curve in at high loads. As the tire has
increasing loads applied to it, it will inevitably stretch and slide
around more. Due to this effect, the whole car will find a peak slide at
a higher angle than originally at the lower loads. Good news is that
unless you are creating a gravel road tire, this probably won't need too
many alterations.

Creating a rally mod would be a huge challenge to anyone, mainly in
terms of physics. Rally cars need significantly more slip to achieve
proper grip levels. They need to move the loose particles away and 'dig'
down to some more firmly in place gravel. rFactor game engine is not
really designed to deal with this, huge CPU processing power is required
to create realistic rally physics, rF is designed to run smoothly with
many opponents on a moderately fast computer. That doesn't mean rally is
hopeless and beyond this game though. We can compromise by skipping the
cause and attempting to get the effect in a similar fashion to all other
games. This means some SLIGHT accuracy is lost when not applying the
maximum performance limit. A rally tire is designed to dig deep into the
surface and grip as much as possible. At low slip angles (and loads)
there is only loose dirt and very low grip levels, therefore, the
initial slip curve has to be much flatter. Unlike a road surface you
actually slide around more at lower loads.

The [COMPOUND] section
----------------------

DryLatLong= Grip coefficients. First is lateral grip (cornering), second
is longitudinal grip (acceleration and deceleration) in DRY weather.
Usually both should use the same value, perhaps with the exception of
rally and drag cars, which may have more slightly more longitudinal
grip.

WetLatLong= Same as above, but on a 100% wet track.

Radius= Radius of Tire. If you have numbers such as these 265/40 R17 we
can determine needed dimensions for rFactor. Firstly use 265\*0.4 (the
40 part is 40% or 0.4 in multiplication terms) then add half rim radius
8.5\*(conversion constant, inch to millimeters convertion = 25.4),
giving a value of 321.9 or in metres, 0.3219 (game ready). The complete
formula is (Width\*(Profile/100)+(0.5\*WheelRadius\*25.4))/1000.

RadiusRPM= Increase in the radius per RPM of wheel spin. Usually less
than 2e-6. Wider and higher radius Tires should have a fairly high value
for this. Older cars would have much larger values, such as 1970's
lemans cars. I estimate the most extreme value could be closer to 1e-5.

Width= Tire width in metres. So if your tire size is 265/40 R17, then
it's simply the first value divided by 1000. 0.265 game ready.

SpringBase= Impact absorption of the Tire. How much the Tire will deform
as weight is applied. Weight on the changes on the tire over bumps or
under braking/acceleration/cornering. If you look at the tire and the
rim is graphically touching the ground over bumps or in cornering, this
value is much to low (unless the car fell from a height of 50m, or you
have a puncture). Generally with modern race vehicles it's very hard to
see ANY deformation. Low profile tires should have a larger value than
normal/high profile Tires.

SpringkPa= Similar to base but this is multiplied by air pressure. I
think that the stock rFactor value of ~1396 is about right for anything,
either way this value should definitely have little variation, much less
than the value above.

Damper= Like spring dampers but this value acts upon the tires. This
value usually needs to be increased when CG is increased. Values of over
2000 should be common with race slicks. F1's should have this quite low.

SpeedEffects= First value is the velocity at which the tire has half
it's stationary grip, due to expansion of the tire at high speeds.
Velocity is measured in metres per Second, which when multiplied by 3.6
is converted into Km/h. Alternatively, you could multiply meters per
second by 2.237 to get a MPH equivalent. Second value is speed load
equivalency at this speed. 1st Value, has a reasonable range of around
350-500. This is probably accurate for most vehicles, possibly for some
70's cars it may be accurate to go down as low as 300m/s. A modern low
profile racing slick would experience a lesser drop off with speed, so a
value of around 500 would be probably be accurate.

The peak of the slip curve is dynamically adjusted to higher or lower
slip values based on current load and speed. The second value of
"SpeedEffects" is an equivalency value for load and speed. To calculate
the slip peak, we use the following input which is a combination of load
and speed:

= + ( \* )

Obviously a larger equivalency value will make speed a more dominant
factor in the calculation of the peak.

LoadSensLat= Grip reduction of the tire (in a lateral sense) when load
is applied. 1st Value is initial slope of the drop off caused by
increasing load (weight) on the tire. 2nd Value is the grip multiplier
when the tire is at the 3rd values load rating. Load is measured in
Newtons. (2e-5, 0.5, 25000), these values, would mean at 25000 newtons
the tire has 0.5x (half) the grip it would normally have. 1 Kilogram =
9.80665 Newtons, so 25000 newtons is about 2550kg or if you prefer about
5620lbs. (1 Pound = 4.4482 Newtons)

LoadSensLong= Similar to above, except longitudinally. If you wish to
keep LoadSens the same laterally and longitudinally, you can replace
these values with LoadSens=.

LatPeak= Peak tire slip. The effect of altering this is a change to the
feel of precision. First value is the peak of slip @ 0 load, in sine-1
(Sin-1(value)=Degrees). Second value is the peak SAE of slip/slide at
the third value, which is maximum load that makes a difference to the
flex of the rubber of the tire. At 0 load, you will not have any grip.

LongPeak= Similar to above, just in a longitudinal aspect.

LatCurve= Lateral slip curve data.

BrakingCurve= Decelerative slip curve data.

TractiveCurve= Accelerative slip curve data.

CamberLatLong= The first value represents peak camber in degrees. Second
value is lateral grip increase at peak camber. The final value is
longitudinal grip decrease at peak camber. (Peak Camber, Lateral
increase at peak, Longitudinal decrease at peak).

HeatBasePeak=(0.15, 0.02) Base peak slip to compute friction heat,
fraction of base to use (0.0=use dynamic peak slip only)

RollingResistance= Friction created by the tire rolling against the
ground. Heavier cars will lose more performance because of this, the
physics engine will take load into consideration and thus this value
does NOT have to be increased simply because a vehicle is heavier.
Rather, this value should reflect width of the tire, compound of tire
and to a lesser extent radius. Narrow, hard, large radius tires
generally have the least rolling resistance.

Heating= (#A, #B) Heat generated by the tires. First value A is
generated heat when driving in a straight line, second value B is heat
generated when the tires are slipping.

Transfer=(#A, #B, #C) Heat transfer to (road, static air, moving air).
The first value A, defines how much heat is transferred when the tire is
in contact with the road surface. Second value B, is the heat transferred
to static air. Finally C, the transfer of tire temperature when the
vehicle and it's tires are moving through the air.

HeatDistrib=(#A, #B) (A = Max camber angle, B = max off-pressure) that
affects heat distribution (higher number -> less temperature
difference). The first value

AirTreadRate=0.013 Heat transfer between the average tire tread
temperature and the air inside the tire.

WearRate= How quickly the tire wears, I believe wear follows a linear
progression ----True?----.

Softness= Used to determine when AI pit for different tires depending on
weather conditions. Also determines the starting compound for AI.??
Untested theory.---?????----

AISens= Simplified load sensitivity for use by AI drivers. Linear rather
than exponential as the player car. Reduces CPU use. Because this is
linear it would probably be wise to set this to lower drop-off than
player car, this is because most time is spent at mid-range of the loads
rather than max loads. This can be used to improve stability of AI cars.

AIGripMult= Grip multiplier for the AI. If AI is too slow, or are
spinning these values can be altered to give them speed, and/or
stability.

AIPeakSlip= Peak AI Tire slip, similar to LatPeak/LongPeak only for the
AI. This does not change dependent on load, if AI slides around a lot
and are unstable as a result reduce this value, especially at the rear.
Otherwise, if you have no such issues, try find the player peak average
slip and use those values.

AIWear= AI Tire wear rate. AI will need to have a much lower wear rate
than the player.

Temperatures= Optimum operating temperature for peak grip (Celsius),
starting temperature. First value is peak operating temperature of the
tires. Most race tires peak at 90-105 degrees Celsius. For Road cars
(I'm guessing here) about 70-85. Wet race tires should peak at low
temperatures, I'm guessing an F1 monsoon tire should peak at about 75.
Second value is starting temperature of the tires, a fresh set of rubber
starts with this temp.

OptimumPressure=(154.0, 0.0170) Base pressure to remain flat on ground
at zero deflection, and multiplier by load to stay flat on ground. You
will never ever want to have less tire pressure than the base setting.
On top of this a vehicle has a mass, which exerts a weight force on the
tires. This load (measured in newtons) is multiplied by the second value
to obtain a .

GripTempPress=(1.6, 0.9, 0.50) // Grip effects of being below temp,
above temp, and off-pressure (higher number -> faster grip dropoff)

Section 3 - \*.PM File
======================

*Sub-sections*

-  Body
-  Bar

[BODY]
------

name=body mass=(522.0) inertia=(388.0,423.0,25.0)

Mass= Weight of the vehicle without rigidly attached parts. Rigidly
attached refers to everything that remains stationary (in regards to the
vehicle main body) when the vehicle is in motion. These are things such
as wheels, Tires, and suspension, which weigh between approximately 150
and 200kgs. All other objects should not be deducted from this value.

Inertia= Firstly if the car mass is double. You should double all
inertia values then you must take into consideration whether or not the
mass is spread further out than an F1. Which it always is (except things
like Go-Karts, and RC cars). This is known as polar moment. When mass is
twice as far away from the central point it will double inertia in that
dimension. (Section 1See for best explanation). These values are
recalculated from the HDV Inertia and Mass values based on the
suspension mass and inertia values below.

Ok now for the good stuff. Roll Centres, Camber Change, Anti-Dive,
Anti-Squat, etc. Will be described in greater detail at a later stage.

Roll Centre: This will probably be the most important and crucial aspect
of suspension geometry. This is especially true if you're making physics
for a truck or a go-kart (something with a very high CG, or very low
CG). Roll centre is basically the point where cornering forces are
positioned. If roll centre matches centre of gravity the car will have
no body roll! As in real life however, this is not optimal, there are
trade offs involved. Generally you want the rear to have a higher roll
centre than the front, and I can't see any exceptions, as this maintains
vehicle stability. The best way to lift roll centre and reduce body roll
is to lower the Upper inside A-arms (lifting them will have the opposite
effect).

Camber Change: This defines how much camber is gained as the suspension
is "lowered". The desired effect is that the outside tires will gain
more negative camber in a corner. Undesired effect is that under power,
under brakes, over bumps, and at high speed the car losses excessive
longitudinal grip by running too much camber in those particular
circumstances (when suspension drops). Too much camber gain can even
reduce lateral grip. A compromise has to be found.

Anti-Dive: is when suspension is angled to distribute some brake force
to an unmovable component of the suspension thus increasing resistance
to the cars brake angle. How it works is that you rotate the front
suspension, in a pitch sense. Front arms should be moved downward and
the rear arms upward to see the desired effect. The problem with this is
that it introduces a terrible trade-off known as bump steer. Bump steer
causes the suspension to steer when you drive over a bump, reducing grip
and causing instability to some degree. Very few race cars actually use
Anti-dive. Anti-squat is similar but reduces the accelerative downward
movement of the rear suspension, this is more frequently used, but still
has similar trade off.

Anti-Squat: Ie.

[BAR]
-----

[BAR] // forward upper arm Posbody=body Negbody=rr_spindle
Pos=(-0.185,0.095,1.16) Neg=(-0.67,0.14,1.42)

Posbody defines what the inside suspension arm is connecting to, in this
case the suspension joins to the "body". Negbody defines to what the
other end of the suspension arm joins to, in this case "rr_spindle" or
the right rear spindle/hub. We would prefer keeping to standard
conventions, i.e. Pos defines the inside connection to the vehicle
body/chassis. Neg should thus be the outer joint, where the arm joins to
the spindle/hub which connects to the wheel. The first value for both
Pos, and Neg is the X axis location (width). Second value is height (Z
axis) in reference to wheel center. Third values are distances from the
arm to centre of the model in a longitudinal (Y axis) sense.

To reduce body roll, we would like to increase the roll center closer to
the CG. To achieve this reduce the second value in Pos for both upper
A-Arms. Make sure to do this for front and rear arms and straight links
or steering arms, and both left and right sides. You should have changed
6 values just for the rear suspension. Another 6 for the front. Front
should all be very similar to each other and same with the rear, however
front and rear values can differ quite a lot.

Live axle suspension

rFactor now supports live axle at the front as well as the rear.

Section 4 - Engine.ini File
===========================

RPMTorque= The first value is RPM. Second value is engine braking
torque (In Newton Meters). Third value is torque (In Newton Meters).
Engine Braking Torque is essentially speed reduction whilst in gear with
no throttle. Formula to get power from Torque & RPM: Horsepower =
Torque(NM)\*RPM/7120.8 Torque(NM) = Horsepower\*7120.8/RPM

FuelConsumption= Fuel consumption of the engine, this is affected by
throttle and engine speed as in real life. This variable defines the
maximum possible fuel consumption rate of the engine. This value should
have a strong correlation to max horsepower and torque.

FuelEstimate= // fudge factor for differences between vehicle types
(used for lap estimates and AI pit scheduling)

EngineInertia= Using the engine capacity is usually a good way to
estimate this value. It is best if you know the engine mass and size but
that information can be hard to find. The value should increase as the
engine size increases. A value of around 0.1-0.2 is about right for 4
Litre race engine. For a road going 8 Litre V10 Viper I'd guess 0.3 or
more would be accurate. This value should increase slightly for turbo
charged engines, especially high boost or high lag turbos, but only
alter the values slightly for Turbos! To simulate lag the best is to
reduce low end power and reduce high end engine braking.

IdleThrottle=1.0 // throttle multiplier to help maintain idle speed

IdleRPMLogic= 1st value is the lowest idle of the engine. 2nd is the max
idle. Should be close to each other.

LaunchEfficiency= Used for launch control. Defines how fast you get off
the line using it. A value of 1 is theoretically perfect acceleration.
Try about 0.95 for an Enzo as nothing is perfect. New Formula 1 vehicles
would come very close, especially Renault. I guess about 0.98 or higher?
You may delete this entire value if the car doesn't have LC in real
life.

LaunchRPMLogic= (NOT EXPLAINED PROPERLY YET) Minimum RPM when launching
and Normal Launch RPM. Set the second value a fair bit higher about
600-2000rpm higher. AI uses this value to determine launch RPM, so don't
delete it if the car doesn't have launch control, or the AI may have
some very slow starts.

RevLimitRange= Rev limits on most cars are not adjustable. If the
vehicle you are creating has a programmable ECU then this should be
adjustable.

RevLimitSetting=5

RevLimitLogic=150.0 // RPM range around current setting where rev
limiter operates

RevLimitAvailable=1 Whether to use an engine rev limiter. If you choose
to disable this setting, you still must have a "rev limit", just make it
40000 or so, and be sure to change [CONTROLS]->UpshiftAlgorithm to fix
shifting points. Otherwise the AI (also the auto gearbox) will never
shift gear.

EngineMapRange=(0, 1, 5) 0 = most drivable, max = most power (low gears
only) Currently is unimplemented and can not be used.

EngineMapSetting=2

EngineBrakingMapRange=(0.0, 0.000133, 5) Input throttle is ranged from
minimum to 100%, with the minimum = setting \* step \* RPM.

EngineBrakingMapSetting=2 The default is 1 \* 0.000133 \* 15000 RPM = 2%
applied throttle at zero input throttle

OptimumOilTemp= Engine oil temperature in Celsius where engine is
producing its peak performance. Usually less than 100. Use around 90 for
road cars, unless you have more accurate information. A few more degrees
above this value the engine will remain at practically optimum
temperature, this is the temperature the driver should aim for when
driving in the game.

CombustionHeat= This depends on how efficient your car engine is.
Generally the more efficient the higher this value is (not the major
factor though). This is because the fuel is completely burned hence
creating more heat (only because it is relative to fuel burned). Usually
between about 35 and 45. Smaller engines generally gain more heat per
liter of fuel burned.

EngineSpeedHeat= Usually the lower the max RPM of the car the higher
this value. Between 6e-4 And 1.2e-3.

OilMinimumCooling= Minimum cooling of oil through the engine block
itself.

OilWaterHeatTransfer=(5.500e-003,9.050e-005) // heat transfer from oil
to water (base, w/ engine speed)

WaterMinimumCooling= When car is stationary this defines amount of
cooling the engine receives. Depending on whether the radiator has a fan
to cool it or not can vary this largely. If it does then value should be
set so that the car can stay stationary without overheating (if the
temperature rises slightly that's ok). If it doesn't have an engine fan
the engine should start to overheat after about 3 minutes and possibly
retire in about 20mins. However this depends on the car, and it's very
hard to determine..

RadiatorCooling= 1st setting. Defines how much cooling the radiator
provides as the car is moving. 2nd setting the increase in cooling as
you increase the radiator duct.

LifetimeEngineRPM= 1st setting determines after which point the engine
starts increasing its wear rate beyond the Lifetime already
predetermined. This value should be set below the minimum RPM rev limit.
The 2nd value determines how many RPM after this the engines life time
is cut in half. Usually between 100-300 RPM. If it's set to 150 and you
over rev by the first value by 300 for 1 second you will remove 4
seconds of engine "lifetime".

LifetimeOilTemp= Similar story to the setting above. The temperature
(1st setting) is set maybe about 5-10 degrees above the Optimum Water
Temperature. The second value is usually about 3, this defines the point
at which the engines lifetime is halved. Lower values result in earlier
retirement from overheating..

LifetimeAvg= Average lifetime of the engine in seconds. Depends on how
long a race is. For highly tuned and stressed race engines, this value
should usually be around 1.3-1.6x the length of races. This setting
assumes that the 2 previous Lifetime variables are never far exceeded,
which is why it must be higher than race lengths (if the car can finish
the race under normal circumstances). This is the base engine life.

LifetimeVar= Random variation in engine lifetime. About 30% of lifetime
average however it can probably be as low as 10%. Depends on the
similarity of the reliability is. If a car constantly retires at very
similar stages of the race, then this value will be low. If it has very
good reliability, it will be difficult to guess. Generally speaking
though, reliable engines have lower life time variation.

EngineEmission=(0.0, 0.50, 0.0) Where flames and smoke are emitted
(relative to ref frame at rear axle)

EngineSound=(0.0, 0.50, 0.0) Where engine sound is played (relative to
ref frame at rear axle)

SpeedLimiter=1 Whether vehicle has a pitlane speed limiter

OnboardStarter=1 Whether vehicle has an onboard starter system.

StarterTiming=(1.4, 0.4, 2.5) Average and variable cranking time, then
time to blend with starting sound

Section 5 - Terrain.tdf File
============================

*Sub-sections*

-  Track Variables
-  Feedback
-  Loose

[TRACKVARS]
-----------

Track variables are simply variables you can refer to from the
[FEEDBACK] section. Generally these are used to change 'bumpiness' or
grip levels of surfaces. Therefore, you can add as many of these track
variables as you wish. To refer to these you simply must replace the
input variable of a feedback property with a name that will uniquely
identify it. Here's an example;

// Gravel

[FEEDBACK]

Dry=0.52

Wet=0.50

Resistance=5000.00

BumpAmp=0.052

BumpWavelen=4.0

Legal=false

Spring=0.0

Damper=0.0

CollFrict=0.8

Sparks=0

Scraping=0

Sink=0.017

Sound=gravel

We could replace Dry=0.52 with GravelDryGrip, this must then be refered
to from the [TRACKVARS] section as GravelDryGrip=0.52. With any value.
The advantage of doing this is that you can now edit these variables on
a per track basis.

For example, let's use the Mills_Long circuit,

If underneath

Track Record = Brad Shuber, 53.669

We Add

RoadDryGrip=0.96

So that it looks like

.. code::

   Track Record = Brad Shuber, 53.669
   RoadDryGrip=0.96

This will reduce the road surface grip at only this track, this can be
used for street circuits or other circuits with a lower surface grip.
Generally 1 should not be exceeded, we like to use it as completely 100%
optimal grip surface.

It's now possible to use an entirely new terrain file per track. In
order to do so you will need to add a TerrainDataFile= entry into your
\*.GDB file. The file should be given the same name as the track as to
avoid any possible conflicts.

These are the default [TrackVars] used in rFactor.

.. code::

   RoadDryGrip=1.00 Multiplier of grip on dry tarmac roads, or if you prefer, the main track itself.
   RoadWetGrip=0.75 Multiplier of grip on wet tarmac roads.
   RoadmetalGrip=0.80
   RoadDustGrip=0.90
   RoadBumpAmp=0.006 Bump Amplitude of the road surface. This has the effect of changing severity of the bumps on the main road.
   RoadBumpLen=8 Bump "wavelength" of the road surface. This has the effect of changing the speeds at which the bumps become most noticeable.
   RumbleDryGrip= Grip Multiplier to slightly reduce dry grip on ripple/rumble strips versus normal ashpalt.
   RumbleWetGrip= Grip multiplier to considerably reduce wet grip on ripple/rumble strips versus normal ashpalt and dry conditions.
   RumbleBumpAmp= Bump amplitute of ripple/rumble strips.
   RumbleBumpLen=1
   MiscBumpAmp=0.08
   MiscBumpLen=4.0

[FEEDBACK]
----------

// Gravel

Dry=0.52 Basic dry weather grip multiplier

Wet=0.50 Basic wet weather grip multiplier

Resistance=5000.00

BumpAmp=0.052 Bump Amplitude of the surface. Basically, this alters the
apparent severity of the surface bumpiness.

BumpWavelen=4.0 Wavelength of the bumps. Changing this will make the
bumps more apparent at different speeds.

Legal=false Whether it is legal to use this surface. Basically tells the
AIW editor whether to classify this as a potential terrain type the
could be classified as cheating.

Spring=0.0 Spring rate of the terrain.

Damper=0.0

CollFrict=0.8

Sparks=0 Whether sparks are generated with collisions to this surface.

Scraping=0 Whether sounds are generated?

Sink=0.017 How far the tires will 'sink' into this surface.

Sound=gravel The sound used when travelling on this surface type.

[LOOSE]
-------

Section 6 - Gear_ratios.ini File
================================

*Sub-sections*

-  Gear Ratios
-  Final Drive

[GEAR_RATIOS]
-------------

ratio=(16, 40) These represent the gear ratios used by the vehicle, if
you vehicle is a road car with a 5-speed transmittion generally you will
need 6 gear ratios. You will need to remember to set reverse to the
lowest (unless the real vehicle has a higher reverse than 1st gear, very
uncommon). In order to determine the ratio we divide the second variable
with the first. In this case we have a ratio of 2.5.

Going backwards with a numerical ratio value to number of teeth on gears
is much more difficult, generally if you don't know these values, it is
easiest to just divide by 1000. If the ratio of first gear is 3.555 for
example, simply add a value ratio=(1000, 3555) to the file. If the
numerical value is 0.855 then ratio would equal (1000, 855).

[FINAL_DRIVE]
-------------

bevel=( 1, 1) // 1.000

ratio=(10, 36) // 3.600

Section 7 - Damage.ini
======================

*Sub-sections*

-  Physical

-  Vertex

[PHYSICAL]
----------

RadiusAdd= Base radius to apply damage to vehicle.

RadiusMult= Radius multiplier by collision impulse to increase radius.

Impluse is used to measure the collision force. The formula for impluse
is (mass\*velocity)/time.

RadiusMax= Maximum radius to apply damage, no matter how much impluse.

Engine= Impulse required to seize engine, at this point, you will be
unable to restart the engine.

AeroDiv= Multiplied by impulse to affect aerodynamics and vertices.

AeroMin= Minimum impulse to damage aero and verts (unlike everything
else, computed BEFORE damage multiplier)

VertMult= Multiplied by aero damage to get vert damage

RadiatorCoverInstance= Name of the radiator cover. If the radiator cover
is knocked off, engine recieves extra cooling but aerodynamics will
suffer.

DeactivateInstance= LowDetailEngine, deactivate this instance if any
parts get knocked off. While all parts are attached, the game will only
render this low detail engine to help frame rates.

ActivateInstance= HighDetailEngine, activate this instance if any parts
get knocked off.

WallSkidThresh= Minimum impulse to generate wall skid (ignores damage
setting and multiplier)

FrontWingDetach= Minimum impulse to detach front wing (doesn't apply to
WC cars)

FrontWingRandom= Fraction of time the wing actually breaks off at the
detach impluse. Note considerablely large impluse will always result in
detachment of wing.

FrontWingPos=(0,0,0) // If zero, automatically finds position of wing
from graphics to check for damage

FrontWingMassInertia=(10, 1, 0.5, 1.5) Mass and inertia (Pitch, Yaw,
Roll) of the front wing.

FrontWingCollParams=(3600,65, 0.6) // Spring rate, Damper rate,
Friction.

RearWingDetach=1900 // Minimum impulse to detach rear wing (doesn't
apply to WC cars)

RearWingRandom=1.0 // Fraction of time wing breaks off

RearWingPos=(0,0,0) // If zero, automatically finds position of wing
from graphics to check for damage

RearWingMassInertia=(10, 1, 0.5, 1.5) // Mass and inertia

RearWingCollParams=(3600,65, 0.60) // Spring/damper/friction

TireCutDull=(6000, 0.25) Impulse and fraction of incidents to cut tire
with dull object. Hitting blunt objects such as brick walls with a high
impulse may puncture one of more tires.

TireCutSharp=(500, 0.65) Impulse and fraction of incidents to cut tire
with sharp object. A sharp object can be classified as any body panel or
wing.

WheelBend= Minimum impulse to bend suspension arms.

WheelDetach= Impluse threshold to detach wheel from vehicle.

WheelRandom=0.35 Fraction of incidents where wheel actually breaks off

Wheel0MassInertia=(30.0, 1.5, 1.0, 1.0) // Mass and inertia

Wheel0CollParams=(11100.0, 105.0, 1.00) // Spring/damper/friction

Wheel1MassInertia=(30.0, 1.5, 1.0, 1.0) // Mass and inertia

Wheel1CollParams=(11100.0, 105.0, 1.00) // Spring/damper/friction

Wheel2MassInertia=(30.0, 1.5, 1.0, 1.0) // Mass and inertia

Wheel2CollParams=(11100.0, 105.0, 1.00) // Spring/damper/friction

Wheel3MassInertia=(30.0, 1.5, 1.0, 1.0) // Mass and inertia

Wheel3CollParams=(11100.0, 105.0, 1.00) // Spring/damper/friction

Part0Detach= Impulse to make part become debris (see .gen file)

Part0Random= Fraction of time part breaks off

Part0Pos=(0.0,0.0,0.0) // If zero, automatically finds position of part
from graphics to check for damage

Part0MassInertia=(20.0, 2.0, 4.0, 2.0) // Mass and inertia

Part0CollParams=(7200.0, 100.0, 0.60) // Spring/damper/friction

[VERTEX]
--------

DefaultLimit= Limits the maximum movement of vertex damage.

Section 8 - Upgrades File
=========================

UpgradeType="" Name of the upgrade type, for example Rear Wing. This
would enable you to purchase different rear wings.

{

Instance="DEBRIS0"

UpgradeLevel="" Name of the upgraded part, for example Adjustable Carbon
Fibre Rear Wing.

{

Picture=""Type_A_F_end.tga Menu picture of the upgrade part.

Description="STOCK Front End" Description of the upgrade part.

GEN==ZR_fbumper_lvl1.gmt Gen file entry of the upgraded part. Visual
model upgrade.

}

UpgradeLevel="Type M Front End"

{

Picture=Type_M_F_end.tga Picture of the upgrade option for menu display.

Description="Upgraded front end package offers better aerodynamics"
Description of particular upgrade part.

GEN==ZR_fbumper_lvl2.gmt Change to the Gen file. In this case, this is
changing the model of the front bumper to that of a better version.

Price=150 Cost of this part.

HDV=[GENERAL] When making changes to the HDV file, the category must be
defined before you can make changes to variables within.

HDV=Mass+=3 In order to change variables by certain amounts, you must
define lists like this. += will increase the amount by this much. You
can Multiply \*, Divide /, Add +, and subtract -,

HDV=

HDV=[FRONTWING]

HDV=FWRange=(0, 1, 1) // only one setting allowed on this wing

HDV=FWSetting=0

HDV=FWMaxHeight=(0.40)

HDV=FWDragParams=( 0.005, 0.0, 0.0) // 1st & 2nd order not needed unless
there

HDV=FWLiftParams=(-0.080, 0.0, 0.0) // is more than one setting

HDV=FWLiftHeight=(0.180)

HDV=FWLiftSideways=(0.50)

HDV=FWPeakYaw=(0.0, 1.0)

HDV=FWLeft=(-0.03, 0.0, 0.0)

HDV=FWRight=(0.03, 0.0, 0.0)

HDV=FWUp=(0.0, -0.04, 0.0)

HDV=FWDown=(0.0, 0.04, 0.0)

HDV=FWAft=(0.0, 0.01, -0.01)

HDV=FWFore=(0.0, 0.0, 0.0) // recomputed from other settings

HDV=FWRot=(0.02, 0.01, 0.03)

HDV=FWCenter=(0.00, -0.10, -0.55) // center of front wing forces (offset
from center of front axle in ref plane)

}
