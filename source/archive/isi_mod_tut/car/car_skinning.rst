************
Car Skinning
************

In this tutorial we assume readers have some prior painting skills. If not,
visit the :ref:`links<isi-mod-tut-links>` page. From there you should find links to help with
those skills.

First note that rFactor uses \*.DDS textures. A file type that is rarely
supported in "out of the box" products. Therefore a plugin is usually required
to view and edit these files. These are obtainable from nVidia and are fully
compatible with Abode Photoshop, Jasc Paint Shop Pro and more. When creating
skins for rFactor we recommend using Adobe Photoshop, though Jasc Paint Shop
is a much more affordable solution which is comparable in features. Microsoft
paint is definitely not an option.

You will find that you may want to download MAS Tools for rFactor too. These
can be obtained from here.

.. note::

	The original download of the MAS Tools is not available anymore.

When skinning, it's a good idea to preview your new textures with
`ZModeler1or2? or other program? <http://www.zmodeler2.com/>`_. It will often
save you a large amount of time when aligning your new textures.

In order to skin a vehicle you will need to either create a new team or add
another car to an existing team.

The first step is to direct yourself to the ..\\rFactor\\GameData\\Vehicles\\
\*VehicleType\*\\\*Team folder\\\*. ..\\rFactor\\GameData\\Vehicles\\ZR\\SRGP
for example.

To create a new team Simply copy and paste a team folder and then rename it
to your preference. From here you can go into the directory, rename the VEH
file, the TXT file and the DDS file. You will then need to open the veh file
in a suitable text editor, change the DefaultLivery="" texture to your newly
renamed DDS file. Change all other appropriate details and especially remember
to change the "Number=" value to match your new DDS number. Make sure that if
you plan to release this publically you do not use an already taken number.
You should be able to verify this on the rFactor community forum at RSC. If
you have entered a new driver name, you will have to create a new RCD in the
..\\rFactor\\GameData\\Talent folder or rF will roll back to "default driver"
parameters. For rFactor to correctly use your new driver ensure that the first
line in the RCD file exactly matches the Driver="" name in the VEH file. For
example, if "Driver="Buster Timms"" in the VEH file then the first line in the
RCD file must be "Buster Timms" (without quotations). You may alter the TXT
file as you wish.

Depending on whether you wish to partially re-skin the vehicle, or wish to
change more than just the body decal will determine whether or not you need to
extract the MAS file. Whatever is not in the team folder will be located in
either a [Vehicle].MAS file 2 folders up, or 3 folders up in the CMAPS.MAS. The
files located in the [Vehicle].MAS for example, are the files specifically for
that type of vehicle. For example the ZR.MAS contains all the files specifically
required for the ZR vehicle. It contains all the models and all specific
textures to this vehicle. The CMAPS.MAS file contains textures that are common
to all or more than 1 vehicle. Things such as environment maps, skid marks,
sparks, raindrops, etc. Remember that they also include some actual car textures
that are common among several vehicles, such as tire textures, exhaust textures,
dials, etc. If you place a texture from either the [vehicle].mas or cmaps.mas
into a team folder, it will appear only on that vehicle without altering this
texture on any other teams (Note that this will not work on textures that appear
on the track itself, such as tyre marks). We highly recommend you don't alter
the [Vehicle].MAS or the CMAPS.MAS themselves otherwise this will replace the
original textures, which may be undesireable for some users. If you insist on
changing any textures within these files, it would probably be wise to place
these textures inside the team folder. If you expect that the folder size will
be rather large it would probably be best placing the textures inside a TEAM.MAS
file inside the team folder, to do this you would have to include a new gen file
(which is pointed to by the veh file) in the team folder.

When changing the gen file, simply add the following section of text under the
SearchPath=Vehdir section.

.. code::

    //----------------------------------------

    SearchPath=

    MASFile=team.mas

    //----------------------------------------

If you extract a file from a MAS file, edit it and place it in the same
directory, this will allow you to view the skin or model in the game without
physically overwriting the file. Once you have finalised the model or texture,
you can compress it inside the mas file.

To open a model in Zmodeler select file, import, select type as GMT (or it will
not open), then select the GMT file you wish to edit. Remember not to
save/export the vehicle if all the skins are not in the directory, ZModeler
will remove the missing textures. Unfortunately you still have to reload the
GMT file in ZModeler to view texture changes that you have made.

C:\\Games\\rFactor MP Test\\GameData\\Vehicles\\ZR\\SRGP\\Team_Green
