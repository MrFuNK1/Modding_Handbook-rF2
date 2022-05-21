
########
Overview
########

This is an overview into how rFactor works. This section illustrates the file
structure and describes the uses of the differing file types used in rFactor.

The main priority of this tutorial is to give those learning the modding scene
the best possible start. At the same time we would like to provide experienced
users with an understanding of additional features new to rFactor.

If you are new to modding, please take a few minutes to go through some
:ref:`general tips<archive/isi_mod_tut/overview/overview:Tips>`.

To get started, we will take a look at rFactor from a hierarchical point of
view.

The above diagram shows rFactor from a text file dependancy point of view.

Let's start with the configuration file (config.ini) located in your main
rFactor directory. The config.ini contains entries that define directories
where particular files are stored for the executable file. This file rarely
needs to be changed when creating new mods, however it has been left possible
for you to create own configuration files. The config file allows the use of
different directory structures. Note: Using a different circuits directory is
not recommended in most circumstances. If you do this, you are likely to
consume significantly more HDD space. To help reduce the need for this, new to
rFactor are some extra features which enable more independence with current
folder structures. In turn we hope that this will translate to an increased
number of mods which will now be executable from the main shortcut, thus
increasing convenience for the player, and simultaneously reducing HDD
consumption.

Regarding circuits, we would like new tracks to follow some conventions. As per
ISI Mike D's recommendation the following format should be used. Let's use
Daytona for this example. When building a new track it is best to model the
entire circuit, including all variants in the main folder. As a subfolder we
can then have different layouts and sponsored versions. However, all the track
pieces and textures should be contained in the DAYTONA.MAS and DAYTONAMAP.MAS
files. Now, in the Daytona folder, there would sub-folders. These would
corespond to different events held at the track. See Diagram:

.. code::

    TRACKS
    ___|
    ___|___DAYTONA
    ___|___|
    ___|___|___Daytona500
    ___|___|___BudShootout
    ___|___|___Pepsi400
    ___|___|___Rolex24hrs
    ___|___|___etc.
    ___|___|___etc.

In each of those folders there would be a .scn file, an .aiw file, a .cam file,
and a .gdb file that would call the proper pieces and set up the proper format
for the race listed.

Now, if someone wants to make a new event, they just add a new event folder to
the Daytona Track folder. They could even throw in a new mas file if they wanted
different textures or to add cones or barricades, and just order the .scn file
properly in order for them to override the default textures.

I'd like to see things move away from the whole "I changed the textures lets
call this a new track" concept, because that leads to confusion. rFactor is
designed to be the next step in racing sim/mod platforms...it's probably a good
time to maybe think about advancing some of the concepts that govern the mod
community end as well.

The next file dependency for rFactor is the \*.PLR player file. The player file
maintains records of all player settings/configurations. By default, this file
is located in the UserData folder. Again, this for the most part does not
require alterations when creating mods. Regarding rFactor, we have separated
multiplayer and controller configurations as new multiplayer.ini & controller.ini
files. This should allow users to exchange preferences which they find optimal.
Controller preferences can be used by pasting them into your UserData\\CONTROLLER
folder. These can then be loaded from the menu. rFactor no longer requires
alterations to the player file when increasing field sizes either. The maximum
field size limit is no longer hard-coded into the game. Instead, it is now
adjustable in the \*.RFM file. By default the \*.rFm is located in the rFm
folder.

All mods containing a unique championship will require changes to the \*.RFM
file. For those familiar with older ISI products, you will realise the \*.RFM
file as the replacement for season \*.GDB files in rFactor. The RFM defines the
details of the championship including tracks available, season order of tracks,
vehicles participating and so forth. There are still \*.GDB files in rFactor;
however these are now exclusively used for tracks.

The next file, the SCN file describes the properties of tracks used in rFactor.
These details and properties include locations and useages of MAS files, light
emitters, model files, etc. Everything to do with tracks is described in either
the SCN file, the AIW file, the GDB file, the CAM file, or the terrain.tdf file.

:ref:`Track Creation & Conversion<archive/isi_mod_tut/track/track_creation:Track Creation>`

The SCN (Scenery) file contains;

  - Details to the locations of permitted MAS files
  - References to, and properties of GMT model files
  - Draw distances

The AIW (Artificial Intelligence Waypoint) file contains;

  - AI Waypoints
  - Grid/Pit lane locations
  - AI speed
  - Fuel consumption estimate
  - Track fog air color/density, etc.

GDB (Game DataBase) file contains;

  - Track descriptions and details
  - Pit lane speeds, session times and durations
  - Geographical location, latitude & facing direction, time of year date, start
    line altitude???
  - Lighting levels at night, morning, etc.
  - Default vehicle setup names

CAM (Camera) file contains details of locations and actions of trackside cameras.

Terrain.tdf (Terrain Definition File) contains all of the road surface grip and
bump levels and details for useage of graphic effects such as spray, dust, rain
droplets, etc.

The next file description is of the \*.Veh (Vehicle) file. The veh file is the
main vehicle file. The veh file contains all references to the car and where to
find all the required files. It contains locations to physics, graphics, sounds
file references, and more. This is where to start when creating a new automobile
for the game. Category= is a filter which determines which vehicles will be
useable in the race. Classes is a subcategory of this. Classes permits class
winners for categories. As an example lets look at the BPR 1995 championship.
The category could be considered BPR 1995, the classes inside of this were GT1
& GT2 classes, with their own seperate regulations. Essentially Category= is a
filter to allow only a specific list of cars and tracks when selecting a
particular mod and vehicle. Only if the \*.rFm file Vehicle Filter is equal
to Category = defined in the \*.veh will the car be selectable in that season.
DefaultLivery= Describes which paint scheme is to be used by default. Track
discriminate entries can also be added for championship rounds where different
liveries can be applied. Pit crew liveries can also be defined here.

The first file reference in the VEH file is the physics HDV (High Detail Vehicle)
file. This file can be considered the overlord of physics files; it accepts most
of the physics input variables directly and contains all references to all other
physics files.

Graphics= Next is the GEN (Generate?) file. This file describes where to
retrieve the model files and textures from, it also describes LoD's (Levels
of Detail). In rFactor the upgrade parts can visually change the look of the
vehicle, these GMT files are written in the same \*.gen file. Any head/brake
light illumination is also defined in the Gen file. We now have a different Gen
file just for the spinner, this allows the user to create more independant and
graphically intense model display.

GenString= is used to define the car's model in the \*.gen file. We previously
used this to enable exchange of models between different cars and teams. The
characters here are used as token's by the gen file. Note that you no longer
need to use a different GenString and model files to create team mates, as was
the case in F1C. You can simply change the defaultlivery, thus allowing smaller
\*.MAS file sizes. In fact, GenStrings are really not essential at all. We have
begun phasing out the use of these.

Cameras= A blank entry defaults to default.cam in the \\GameData\\Vehicles\\
directory. You can define all new camera positions/orientations specifically
for each vehicle.

This brings us to the \*.SFX (Sound FX) file. All sounds generated by the car
are obtained from the list in this file. Engine sounds, horns, tyre squeals,
gear shifts, etc.

HeadPhysics= Changes visual head (camera) movement in cockpit view and nothing
else, it does not affect physics. Generally, this file does not require
alterations.

Cockpit= Vehicle cockpit information. Lists onboard camera positions, instrument
details such as display RPM range & temperature range, graphic textures to use,
etc.

Upgrades= The upgrades file allows users to create purchaseable vehicle upgrades.
The possibilities are practically endless; you can change sounds, models,
anything physics related, etc.

AIUpgradeClass= Upgrades that this vehicle has installed by default. The AI
will always use these upgrades and only these upgrades, the player car will
start with these upgrades. The player still has the ability to improve the car
beyond this point by purchasing better parts, assuming they are available. The
upgrade class is defined in the upgrades file, these are used to define
different models of vehicle.

For more information on the \*.Veh file please visit the
:ref:`Vehicle Creation<archive/isi_mod_tut/car/car_creation:Vehicle Creation & Conversion>`
page.

Check out the other sections for some more detailed descriptions depending on
what you wish to mod. As always have fun!

Tips
====

Before you being modding, it would probably be best to read these general
tips first.

1. Use a better text editing program than Notepad.
I recommend downloading NoteTab. This is my personal favourite text editor and
there is a free version available. Other alternatives are available such as
Textpad and Ultra edit, these are great too. Ultra edit 32, is able to edit
hexadecimal documents, thic can be very useful when renaming textures in \*.GMT
files, etc (GMT is the new 3d model file type replacing MTS). This program is
not free though, there are free hex-editing programs out there though. We highly
recommend that you not use Notepad. Notepad is not user friendly when it comes
to modding, and it will cost you time in the long run. It may be useful for
small edits and quick fixes, but not serious modding.

2. Use as many comments as you find useful.
Comments are text written after 2 slashed lines, //. These tell the game to
ignore anything written thereafter, and are VERY useful to make notes to
yourself. Don't worry if it looks messy, if you plan to release it publically
you can delete these comments before you publically release your car(s)/track(s)
/etc. Flooding the page too much is not good either, it's up to the user to
determine how many comments to write. Often I write little variables from
formulas as comments to remind myself what values I used to calculate
variables such as inertia, downforce, old tested values, untested values etc.
They maintain consistency, accuracy, what has been done and needs to be done,
etc.
