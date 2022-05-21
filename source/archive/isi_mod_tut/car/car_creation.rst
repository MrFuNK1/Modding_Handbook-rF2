*****************************
Vehicle Creation & Conversion
*****************************

*Converting vehicles from older ISI products to rFactor*

Tools required

    - `ZModeler <http://www.zmodeler2.com/>`_
    - ?? - Mas tools for older ISI products.
    - rFactor Downloads - Mas Tools.
    - nVidia - nVidia tools and plugins.

.. note:: Please note that most of the official downloads are not available
  anymore. There are still other tools providing the same functionality.

The tools you require will vary on the quality of the conversion you are
attempting. A quick conversion, or an optimal quality conversion.

An optimised quality conversion will, as the name implies, require numerous
optimisations and will thus consume more time. For now, we will examine the
"quick converting" concept.

Quick Conversions
=================

If for whatever reason you just wish to get the vehicle ingame as fast as
possible with few optimisations as possible, here is a step by step process
you can follow. Tools may soon be available which can automatically do most
of this, regardless, this will be left here for your reference.

Note: Quick conversions are recommended if you wish to alter the \*.GMT model
files of the vehicle to match rFactor standards, or the vehicle has no plans
for any upgrades, such as private use. If you plan to make optimisations
outlined in a "High Quality" conversion we recommend undergoing that process,
as it will save time overall. We would rather any quick conversions not be
released publically as the quality will not be up to the standards of the
new gMotor 2 engine.

In creating a conversion you will need to find all the vehicle specific files
from your older ISI product and have them handy. First thing to do is copy and
paste your vehicle folder into rFactor. There 3 basic elements, sound, graphics,
physics.

Sounds
------

Sounds can simply be taken straight from F1 Challenge, along with some other
older products and used in rFactor. However, rFactor has many new and improved
sound effects since F1 Challenge, during a 'quick conversion', you will only
need to change the directory structure in the SFX file. To find out needed
sound files, check the original Veh file for the vehicle copy the SFX file
over to rFactor, and make appropriate changes. We would suggest you copy car
specific sounds (such as engine sounds) to a new sub-directory under the sounds
folder, as to avoid possible conflicts. You will also have to make some changes
if you plan on using sounds from rFactor, such as tyre squeal sounds.

The sounds file structure in rFactor is as follows (These sound reference
suggestions can be found as sounds.txt under your \\rFactor\\GameData\\Sounds\\
folder);

\\Sounds\\Default - General purpose sounds, to be used as placeholder for new
vehicles awaiting vehicle specific sounds.

\\Sounds\\Ambient - Ambient sounds not made by the vehicle and not specific
to any make of vehicle. Ex. crowd, pit, airhorns.

\\Sounds\\Secondary - Sounds that the vehicle makes but are not necessarily
specific to that make of vehicle. Ex. collisions, rumble, wind, stones.

\\Sounds\\"TireMake" - Sounds associated with the tires. Ex. road, rolling,
skidding, grass, gravel.

\\Sounds\\"EngineMake" - All engine sounds for this make of engine. Ex.
engine_int, engine_ext.

\\Sounds\\"VehicleMake" - Sounds that the vehicle produces while racing specific
to that make of vehicle. Ex. trans, gearbox, backfire, brakes.

**Notes:**

  - There may be situations where the secondary sounds can be moved into
    specific vehicle directories.
  - Use the suffix "_ex" or "_in" for extenal sounds and no suffix or "_int"
    or "_out" for internal sounds.
  - For sounds that have upgrades or multiple versions, use a number after the
    rootname and before any other identifying works. Ex. ABCEngine3_onhigh_ex,
    Backfire2_low_in.
  - TV Cockpit view uses internal sounds.
  - To conserve memory, some vehicles share sounds for other vehicles. The
    Rhez sounds are widely cross referenced.

Graphics
---------

This is the longest aspect of the quick conversion. You will need to extract
existing mas files using MASTools for F1 Challenge, then import the MTS files
using ZModeler and export them as 3DS files, then to re-import these into 3DS
and export those files as GMT files. Keep in mind that there may be tools
available to help you short-cut this process. Using rF MAS Tools, you will
then need to compress all the files back in to your new GM2 MAS file. Please
note that to successfully "convert" the MTS file to GMT you will need to have
EVERY last used texture the vehicle uses (including any CMAPS.MAS files)
located in your ZModeller editing folder. If this is not done, ZModeler will
not include emaps and various similarly used textures, the automobile will
probably look very unusual in the game. This occurs unless you have the
original Z3D files. If you have the original Z3D files, use those. We would
also like to mention that it is not ethical to convert cars for public use
made by other authors without their permission. If you wish to do so, please
obtain their permission first.

Inside the .gen file you will need to make sure that all MTS file references
are now replaced with GMT.

Creating Physics
----------------

Perhaps one of the great aspects of rFactor is that physics are fully
compatible with older ISI games; NASCAR Thunder 2003?, F1 Challenge
99-02, and NASCAR Thunder 2004. You don't need to change them! Just copy
all the physics files you need, ensuring that every file referenced to
from the HDV is copied to rFactor. You should be done.

You will probably have hitches and issues, but generally if you follow
these steps, your conversion should have been succesful. If there are
game crashes please try adding trace=5 to the target line of your rF
shortcut.

Optimised Conversion
====================

Again there are 3 basic aspects to converting an automobile to rFactor
with an optimised conversion.

Sounds If you want to have better sounds you will need to include some
sound upgrades included stock in rFactor. Generally copying the most
similar existing car's sound file in rFactor and overwriting some
variables with sounds from the older vehicle. Such as using all rFactor
sounds with the exception of engine sounds.

Graphics Probably still the longest process for most people. You'll want
to make use of new vehicle headlights that use pixel shaders, convert
textures to DDS and perhaps enhance them. You may also wish to map some
rFactor textures to your vehicle. You will need a modelling program that
can export GMT files.

Physics It can be very time consuming to implement optimised physics.
Depending on your skill, just how accurate you want the car to drive,
and your spare time, this can take as little as a few hours to several
weeks for just 1 car. While physics are technically compatible with
older products, the game interprets them differently and more
accurately. For example tyre heating may be thrown off a little bit when
just using F1 C values. Also we continue to learn more with newer games,
our understanding of what is realistic changes, and thus older default
values used as a base by modders could be inaccurate.
