
.. sidebar:: Credits

  Original author Mike DiPonio. The text below is an edited version of JPS's
  postings giving an introduction to Track Editing. It appears with JPS's
  permission. This tutorial has been extensively edited to rF track editing and
  was originally made for SCGT and F1C.

##############
Track Creation
##############

**************
Tools required
**************

-  3DS Max
-  rFactor Downloads - GMotor2 Mas Tools
-  nVidia - nVidia tools and plugins.

Firstly, you’ll need to be using 3D Studio MAX because Zmodeler won't
cut it in this case. Unfortunately 3D Studio is commercial software and
is not available to download legally on the net so you'll need to find
another, hopefully, inexpensive source.

***********************
rF Track Building Guide
***********************

Section 1
=========

Lofting a basic layout
----------------------

To start with, get your units set to meters in Customize - Unit setup.
Getting the scale correct is pretty much a lot of guesswork unless you know
for a fact that, say, the front straight is exactly 1200m long. Get a good
map of the track that is to correct scale and set it as a diffuse map on a
material.

Create a flat plane roughly the size of the track(top view, obviously). It
will be used as a template for tracing the tracks path. Assign the track
map material to the plane and lower it 10 meters down so it’ll be out of the
way of your work.

UV map the plane using the “fit” and “bitmap fit” functions to get it mapped
proportionally correct to the plane. Then you can uniform scale it to whatever
size you need, without worrying about messing up proportions.

Start creating a standard line (spline) and set the vertex type to "smooth".
Draw the line down the centre of the pavement. Click to create a vertex only
when necessary, create the minimum number of vertices you can get away with.
Since all the vertices will be of type "smooth" you'll notice the line will
sometimes bulge out as if it wants to go in another direction - ignore this for
now and just keep plotting along down the center of tarmac. Just to give you
some idea, a typical horseshoe shaped hairpin will typically require only 3
vertices to make (one placed just before the start of the turn and one just
after the exit of the turn). Again, at this point don't be concerned if the
line is bulging out in places; just make sure your vertices are in the center
of the tarmac. When you end the line click the last vertex on top of the
first vertex to complete the circuit. It then asks you if you want to
close the spline, answer yes. At this point you'll have a pretty
roughed-in line following the center of the pavement.

For corners that need to be touched-up you can change the vertex type from
"smooth" to "bezier" or when you're in a really tough situation choose
"bezier-corner". DO NOT USE "corner" type vertices. I try to set the
starting line right at the world center (0,0,0) that way when I first
test, it will be easy to set the aiw up. Move the vertices around and
tug-and-pull on the bezier handles until your line follows the center of
the pavement all the way around the track as perfectly as you can. In
some cases you might have to go back and actually add some additional
vertices in order to achieve the perfect curvature to follow the center
of the tarmac; you do this by clicking the "refine" button then click
where you want the new vertex to be created (make sure you created the
right type of vertex for the situation at hand--either smooth, bezier or
bezier-corner). Be careful to not go overboard and add too many vertices
there should typically be a vertex every 20 meters on the tight spots
and every 80 meters on a long straightaway. Most turns can be achieved
with only 2-3 vertices, and I have never run across a turn so
complicated as to require more than 4 vertices. Use the minimum amount
you can get away with - you'll see why in the lofting step.

Now go back and raise/lower individual vertices on the line to add the
elevation changes. Again, to achieve the correct and smooth elevation changes
feel free to use "refine" to add an additional vertex if you have to. You
don't want any knife-edge elevation changes. Pay close attention to your
measurements here, it's easy to over do it and end up with huge heights
or really steep hills. I’ve noticed that if you rise or lower a point by
1 meter it will make a gradual hill and 2 meters per point will make a
fairly steep hill. It’s a good idea to make the 2 points at either end
of the hill half the height difference of the rest to make a gradual
transition. Don't worry about getting this line too perfect first-try,
you will be able to go back and adjust this line as much as you need to
later.

.. note::

  Do NOT attach this line to any dummy or to the "hierarchy".

It should remain a free-floating object in the "schematics view". Also,
never delete this line (the "path"), it can come in very handy even much
later in the track development process. To keep it from being exported
into your .3DS all you have to do is hide it.

I've been asked if the grass and such are also lofted. Well, you can loft the
polygons for the rumble strips and berms pretty well and also at least have the
loft generate the spare polys that you can then pull on and stretch to form
the grass and gravel traps. An alternative is to just "extrude" the
polys for the rumble strips/berms/grass from the edges of the lofted
tarmac when it's finished. You can push/pull on these new polys to form
whatever you need. The good thing about doing it this way is that it is
incredibly easy and fast, the drawback is that you will have to manually
map those polys (if you loft them they can be automatically mapped to
follow the curves and hills - cool stuff when it works!).

With your "path" line selected, over on the command panel in the "modify" tab
you will see a "General" section. In there are settings for "Interpolation"
and a check-box for "Adaptive". I turn on "Adaptive"; it seems to result
in smoother lofts and better polygon arrangement in some situations. You
can turn this setting on/off at will at any time later if you want to
compare how your resulting loft is affected. Another way is to set
Interpolation to “steps” and set it equal to the number of steps in
you’re loft, then it will match up perfectly.

OK then, on to the next step, which unfortunately takes a lot of words to
explain but is remarkably easy and quick. Everything I say here is based on
3D Studio MAX 3.0, the locations and perhaps even the names of some of these
functions may be different in other versions of MAX and I really can't
help you there. If you've gone through any lofting tutorials then you
understand that lofting is the process of pulling one or more "shapes"
along a "path" to form a 3D object. For example: Hmmmm... that squiggly
line looks kind of like a part of a race track. What if, instead of that
stupid star "shape" we substituted a simple straight line? Pulling that
along the squiggly "path" would probably yield something like a road,
eh? So, somewhere out of harms way create a line (spline) that is
perfectly straight and flat with only two vertices (the start point and
the end point) and make them both "corner" type vertices. What I do is
just splash down a rough line then go into vertex edit mode and snap the
vertexes to the grid, with the grid set to 1 meter (the snap and grid
settings are in Customize – Grid and snap settings). The width of this
line will be the width of the lofted pavement. I find widths between
8m-16m to be good for racing.

Now then, you've got your "shape" and your "path" so you're ready to loft
your track. Select your "path" line (the line that looks like your track).
The "loft" function is rather hard to find in 3D Studio MAX:

- In the command panel go to the "create" tab (the one with the little white
  arrow pointer on it).

- Directly under that select the "geometry" button (looks like a gray sphere).

- In the pull-down list select "Compound Objects".

- In the arrangement of buttons below will appear a button that says "Loft".

Somewhere in the fancy modeling icons list there is a "loft" icon that does
the same thing, but that's just as hard to find. It's also located on the tab
panel, in the compounds tab. It's the snake looking icon.

In the lower part of the command panel will now appear a whole set of loft
settings and functions. In the "Path Parameters" section you will see selections
for Percentage, Distance or Path Steps - choose "Path Steps".

In the "Creation Method" section make sure "Instance" is selected, then click
the "Get Shape" button. Click on your straight little "shape" line. As
soon as you click the loft will be generated.

Now go back and click the "Get Shape" button again to exit that mode. "Well,
ummmm.... Jeeezzz, it created something but it doesn't look too much like a
road...what gives???" It will look a lot better as soon as we apply the right
settings.

If the loft is facing upright like a wall, you need to select the shape line and
go to the modify panel find “Line segment mode” and use the transform type-in
window to rotate the line on its Z axis 90 degrees, until its flat like a road,
then turn off line segment mode. Take a look at it in the side and front view
ports to make sure its level.

Go all the way down to the bottom of the command panel to the "Skin Parameters"
section (you might have to click it to make it roll-out). Use the following
settings At this point your loft should start looking more like a drivable road.
If you were to apply a tarmac bitmap to it you could instantly make it look
like tarmac. Let's go ahead and do that....

Making gMotor2 Materials First thing you need is a Multi/Sub-Object material,
so open the material editor and click on a slot.

- Then click on the button where it says Standard in the top right (this is the
  material type);
- Pick Multi/Sub-Object;
- Click yes to the prompt to keep old material;

Now you have 10 material inside to work with, which can be increased to up to
100. All materials that will be used on the track mesh need to be in the
material, or you’ll run into problems later with material ID assignments.

Click on the first material in the list and name it ROAD(something) Then click
on the material type button (Standard –in the top right) Pick gMotor Material
from the list.

The first thing to setup is the shader, so pick one, most likely T1 for
DX7 and Bump Specular Map T1 for DX 8. All shader levels between DX7 and
9 need to be setup for it to work correctly. If you’re just lazy then
setup DX7 and 8 because the upper levels are auto generated from the
lower if left at default type.

Now assign a texture to it by clicking the first slot in the Texture section.
For complex multi-shaders materials like Bump Specular Map T1, you will need to
assign 3 textures, for each shader.

So set you’re main road texture to the Color slot; a specular map (use one from
the original tracks, they have a (ROAD)_S.DDS type name. And set a normal map to
the Bump slot (use one from the original tracks, they have a (ROAD)_B.DDS type
name.

Bump and specular maps need to use a different pixel ratio than the main texture.
To set them up; go into the texture level of each of the shaders, in the
Coordinates section set the U and V tiling for specular to 6 and the
Bump to 12. This number is based on track width, with my example being
12 meter wide. After creating your material, apply it to the loft object.

Look at it in the view port you'll notice that the material is probably
heavily stretched along the length of the track (blechhhiieee!!). Let's
fix it up nice and pretty....

The Length Repeat setting is critical to get right in order to make the tarmac
look believable in-game. Length Repeat is exactly what it sounds like: how many
times your road surface bitmap is repeated along the entire length of the loft.
The correct setting depends entirely upon the length of your track and, frankly,
comes down to a sort of guessing game to find the number that looks best
for you. We've started with 40 and will increase/decrease that number
until the road surface looks good.

Set the view port to "Smooth + Highlights" so you can see the materials in
real-time; if your display system is incapable of this you will just have to
resort to rendering it each time. Zoom in to a piece of the track close enough
so you can see what the surface is going to look like. Using a bitmap that
doesn’t tile very well (just for testing purposes) is the best way to find the
right repeat length, its best to have it a little less than square though or
else it’ll look jagged at high speed. Try making it 2 long.

Similarly, width Repeat is how many times the bitmap is repeated across the
width of the loft. Almost always you want this set to 1, but there are some
rare situations where you would want it repeated multiple times; this
setting allows you to achieve that.
Notice also that you are allowed to specify fractional numbers like 1.5 or 3.25
to get just the effect you might need for those unusual situations. If the track
uses multiple line segments on its shape line, its best to set width repeat to
its number of segments and turn off “normalize” on the surface parameters.
You can the select each line segment and scroll down the modify panel to the
surface parameters and give each segment a unique material ID. This will
be helpful when you convert the loft to a mesh because each polygon
going out from the track will already have a material ID and will be
easy to assign materials to.

At this point you should definitely save your work.

Let's switch back to wire frame viewing mode for this next part. Remember
above in the "Skin Parameters" section I mentioned there would be more about
the "Shape Steps" and "Path Steps"? Well, here you go: Shape Steps is
essentially how many times across the width of your road polygons will be
generated.

A setting of 0 = 1 quad across, 1 = 2 quads across, 2 = 3 quads across, etc.
Go ahead and play with that number and you will be see what I mean.
You can see how playing with this number can instantly cause you to have a
high-poly track that could be very FPS- unfriendly for everyone. A setting of
0 works best in almost all cases. There are some cases where increasing the
polycount across the width of the road is desirable in order to make the road
smoother in areas where the pavement twists or banks to a significant
degree and makes the road too bumpy in-game, but you would really only
want to increase the number of polygons in those specific areas that
need it, not the entire track - that would be a wasteful excess of polys.
You could always loft those troublesome sections with a separate loft
using the same "path" and "shape" as your original track loft, and
increase the Shape Steps for that second loft. Then just use the
higher-poly track parts in the areas that need it and stick with the
original loft for the rest of the track.

Note that "Shape Steps" has no effect on the "Width Repeat" for the bitmap
mapping across the width of the track, which is something totally independent
regardless of how many polys you have across the width of the track.

Also note that it does not change the width of the track, it only increases
the polygon density across the width.

Path Steps controls how many polygons are generated down the length of your
road. Finding the best number for this setting comes down to "best feel" and
"what looks best" and it is also greatly effected by how many vertices you have
on your "path" line. You will notice that around curves and where hills start
/end you need to increase the polycount in order to make it smooth.
Each time you change the Path Steps setting it will warn you that doing so will
change the locations of "shapes". This is actually a pretty important thing to
be concerned about and you will see why when we get into adding additional "shapes"
to change the road width, add camber, banking, etc. Try not to get into
the habit of mindlessly just clicking YES to this warning.

For right now, however, we have a very basic loft with only one shape on it, so
go ahead and adjust this number up/down and look closely at how it affects
your track. Notice that if you increase it too much the track will
actually start to fold over itself in tight turns and this becomes a
royal mess to try and fix later. You want your final settings to yield a
track that is smooth around corners and hills/dips but also very
low-poly along straights. It will quickly become clear to you that this
setting alone is not going to give us what we need for F1C. The other
thing that greatly affects the poly density is the placement of the
vertices on your "path" line.

Remember plotting out all those "smooth", "bezier" and "bezier-corner" vertices?
Notice how the loft increases the poly density based on those vertices. Notice
also that how much you pushed/pulled on the bezier handles of those vertices
also affects the ultimate density and arrangement of your track's polys. Let's
see this in-action....

Un-select your loft and select your "path" line - since it is underneath your
loft it might be easiest to use the select-by-name feature (Edit - Select By -
Name). Go into vertex .edit mode and move a vertex. Notice how the loft is
effected in real-time and adjusts the poly arrangement accordingly. Notice also
how pushing/pulling on the bezier handles of a bezier vertex has a profound
effect on the smoothness of your loft. Now go ahead and use refine to add a
vertex somewhere. Pretty powerful stuff, eh? Since the whole goal is to end up
with a track that is smooth where it needs to be smooth, it is important
to find the right balance between the "Path Steps" setting and the
amount and placement of vertices.

Yet you might not be able to make major changes to the vertices without
changing the shape of your track too much. You also do not want to end up
with sections where the polygons overlap each other. You can also experiment
with changing some vertices from "smooth" to "bezier" or visa-versa. It
shouldn't take too long to strike a good balance. For rF the poly density is
pretty uniform and cant be too low on the straightaways, or it’ll be noticeable
in the specular detailing. For this reason I try to keep the polys fairly
square, and not let them get too long. For corners you can increase the
poly count as much as needed though, to make a smooth corner.

Let's get this thing into the game and drive on it.

What we'll do is cut the track into a couple of giant chunks and make up some
really rough track files just for the sake of testing what it's like to
actually drive on it. After driving on it you will have a better sense of what
changes you should make to your loft to improve the track. Just a quick-and-dirty
test here.

Small but important divergence from the topic: Before we go further, make sure
the material you are using for your road surface is named so it matches up to
a valid road entry in the TERRAIN.tdf file. Road surfaces typically start with
the letters; road, conc, rdcem, rdrd, rdgr. If the name of your material does
not match a valid road terrain type in the TERRAIN.tdf file then rename it now
so it does match. Texture names don’t require special naming, and they don’t
need to match the material name. It is important that you understand that the
names of material are critical when it comes to tracks. Any surface that you
intend to drive on, crash into, or scrape against, must use a material
that is named to correspond with a terrain entry defined in the
TERRAIN.tdf file. If the material name does not match any type of
defined terrain the game will give it a really horrible default
response, which just so happens to be a surface you cannot drive on.
Notice in the TERRAIN.tdf file there are different types of terrain for
pavement, guardrails, tire barriers, concrete walls, rumble strips, etc.
Make your material names match the appropriate entries and your surfaces
will give the correct responses, sounds, sparks, dust, damage levels,
etc., in the game. Materials you use on objects that will not constitute
terrain (such as the outfield and outfield buildings and decorations) do
not need to match the terrain file.

Select your loft and make a clone of it; you will do the rest of your editing
from this clone, leaving the original loft untouched and safe so you will be
able to call it up again later when you need to make alterations to it. Hide
the original loft, path line and shape line so they are out of the way and
you don't accidentally mess them up. Let's take a minute to find the co-ordinates
of the point on the track where you will want the car to start in the
game. Anywhere on the track pavement will do; near the start/finish line
is great. Find the (x,y,z) co-ordinates of a point in the middle of the
road, and at the same height as the pavement (z would be the height).
Pay careful attention to whether each number is positive or negative and
write them down in (x,y,z) format. You'll be using these co-ordinates in
your waypoint file very soon.

Advanced lofting (unfinished)
-----------------------------

This section is for after you have the path worked out pretty nice and you want
to start adding in details alike curbing, and walls. The Lofts shape spline
is the cross section of the track, so whatever shape it’s in, the loft
will follow. Say you twist it from end to end, the track will tilt
sideways. Modeling the spline Select you’re shape spline and copy it.
Now snap the copy to the grid and in vertex mode; stretch the points so
they are 26 meters apart, also make sure the object center stays
centered or the loft will be offset from the path. Now hot the refine
button and make a point 6 meters from each end of the spline, and then a
pint 1 meter from each end. Now move the far end points 1 meter up and
in so they form a wall. Now you have a 12 meter center section which is
the road, twp 6 meter sections which are the grass sides, and two 1
meter sections which are the walls. Assigning IDs In segment mode;
select the center section and make it material ID 1 (the material we
made earlier.

Section 2
=========

Setting up the game files folders
---------------------------------

The first thing you need to do is decide on a track name and make a folder
in the Locations directory of the same. Then make a GMT and MAP directory
inside. If you plan on having multiple layouts, then make a sub-directory
for each of them too. Go to one of the original tracks and copy the aiw, cam,
gdb, and mas, and scn files, paste them into your track, if you have multiple
layouts put them in their sub-directories instead. Rename them all to your
track’s name with exception to the (track’s name)map.mas, which needs to
have that part preserved. For multiple layouts do the naming distinctly;
like TrackLong, and TrackShort for the sub-directories and file names.

The Scene and GDB files All files in for a track revolve around these 2,
so they need to be made carefully.

GDB file
--------

Open the sample GDB and fill in all the data for it the top entry needs to be
the name of the track in capital letters.

**Filter Properties** needs to match up with the series or mod you want it to show
up in. The track info section is all pretty self explanatory; just make sure
the event name is the track’s name.

**Special settings** You can define unique terrain settings for you’re track by
making a TDF.

**SCORETOWER DATA** can wait for later, when you create a
score board.

The **track lighting** section has all the variables for time
of day behavior.

**Setups** should be named to match you’re track.

Scene file
----------

The scene file is also going to be very simple. What I do is start out with a copy
of a scene file from an original F1C track (I suggest using the Sample
track’s scn, because its setup very simple and organized. Delete all of
the Instances at the bottom of the file. The Instances can be made in
the GMT converter, but for the heard and stuff its easier to just hand
write it if you’re working on more than one project. So copy the
Directory, Mas, View, and Lighting lines from the sample and paste them
in to yours, and then rename the directories and mas sections.

Converting you’re assets to GMT format The tools for rF require a bit of
setup to actually convert a file, don’t worry though, this only needs to
be setup once. First thing to do; on the command panel go to utilities –
configure buttons; scroll down to the bottom, and drag the GMT Converter
listing and drop in on top of a button you don’t plan on using, the
click OK.

Now click on the new button and in the firsts section set the
mesh Directory; I set it to
C:\\Program Files\\rFactor\\GameData\\Locations\\SampleTrack\\GMT
so that I can simply hit the button and instantly have the meshes ready to test.

Then select the loft and go down to the instance section and hit the “Get
Selected” button. Check these boxes:

- Collidable
- Hat
- Use gMotor Normals
- Smooth
- Receiver
- Omni

Hit the “Do Mesh” button to make the GMT file.

Now you can go down to the Scene File Output section and set the Current Scene
File to
C:\\Program Files\\rFactor\\GameData\\Locations\\SampleTrack\\ST_Long\\NEW.SCN

The scn file used for the converter will be written to a temporary file, so
that it wont mess up the header we just wrote. Skip the Fog and Views
part, and only check objects and selected. Paths can also be ignored.
Select the loft, hit the Do Scene button and open the new.scn; copy out
the instance lines for the loft out of it and copy it into you’re
track’s scn file.

You won’t need MAS files yet, we will be using open folders instead to make
working with files easier. Later, when you're about finished building the track
(if ever), you can make them, and add the line into the scn file.

Now it's time to create an A.I. Waypoint File (.AIW file) for your track:
Leave everything from the old track’s AIW alone except the grid positions, the
pit slots should also be left alone at this point.

.. code-block::

  [GRID]
  GridIndex=0
  Pos=(-3.865,0.050,-2.316) // (X,Z,Y) the values are equal to 3s max generic units)
  Ori=(0.000,-1.569,-0.001) // pitch, rotatation (0=south, 11=east, 22=north, 33= west), and roll

The Pos= line is where you put starting the co-ordinates. You can figure this
out easily by plotting a “point” helper in 3DS where you want a starting slot.
One thing though; there's a little conversion you have to do to those numbers
because the co-ordinate system inside rF is different than MAX. If the MAX
co-ordinates you wrote down were (-150,220,2) then the numbers for the
Pos line would need to be changed to (-150,2,220). Notice that Y and Z
are swapped around. You also want to increase the second number in Pos
by perhaps 0.2 meters (make the Y value more positive to go up higher in
elevation). This will make the car start out about 0.2m above the
surface of the pavement, so when rF drops the car onto the track it will
probably land on the tarmac rather than fall through it because of
differences in car heights and centre points..

The second value of the orient determines which direction the car will be
facing when it appears on the track. You can play around with this number
until it’s the right way. In max, X is facing south. That's all you need for
the waypoint file for this test drive. At the bottom add in the instance
definitions for your two track MTS's. It typically looks like this:

.. code-block::

  Instance=track01
  { MeshFile=track01.mts CollTarget=True HATTarget=True ShadowReceiver=True
  Response=VEHICLE,TERRAIN }

Make sure you close off the "{}" braces sets correctly, otherwise wacky stuff
can start to happen.

Let's see.... You've got your track converted into MTS's Directories for
everything to go into the MTS's and textures are in their respective folders,
the AIW file exists and is in-place, the SCN file exists and is in-place, the
GDB file exists and is in-place. Sounds like it's time to drive:

- go into rF,
- set the opponents to zero (remember there's only one starting grid position),
- turn off flags in the rules section,
- select your track,
- set the game to "Race" mode (no practice or qualify sessions),
- and start the race.

If your car does not start out on the pavement then fix your Pos co-ordinates
in the AIW file.

If you car is facing the wrong way then play with the second value of the Ori
line. Ignore any "Wrong Way" or Black Flag warnings that might pop up; since you
don't have a valid waypoint file or any checkpoint barriers the game has no
way of telling if you're going the right direction or not. Also note that the
lap time and lap counter cannot work yet.

What if my car falls into the blue? One thing that you need to keep in mind
when the car starts falling through the ground is the material names for you’re
road, grass, sand etc.

Then the HAT file for the track.
--------------------------------

It is basically a collision model of the track
that is generated the first time you load it in-game and is used as the
collision model there after. This file causes a problem with track
testing because it retains the same HAT file even if you make modeling
changes. Usually it doesn't even accept the old HAT and simply acts as
if there is no track at all. I had this error for 2 months with my first
F1 2002 track before I finally pinned down the problem. I noticed that
if I put the track into a bran new installation of the game it would
work fine until I made any further changes, then back to the bottomless
pit. The solution is to go into the LOG/HAT folder and delete the HAT
file with you’re track's name on it - or just delete them all if you
like, they'll automatically rebuild the next time you load them anyways.

The second step is to open you're PLR file and do a word search for;
Always Rebuild HAT, then change the value to "0". This will make the HAT
file refresh every time a track is loaded and save you the task of
deleting the HAT file every time.

Fine tuning the loft
--------------------

What you want to look for first is whether the track is smooth enough to drive
on at high speed, with no lethal bumps or sudden angles in the surface. Also
check out the elevation changes, do they seem realistic? Are the turns
relatively round and not choppy and angular? Is the pavement wide enough
or too wide? Try to drive the entire track surface. Do you run into any
polygons where the game will not allow you to drive?

If you need to smooth out the loft or make other changes to it remember to make
those changes to the original loft that you have hidden. Un-hide it, and make
your changes, then clone it. Hide the original again for safe keeping
and convert only the clone into an editable mesh. The idea is to keep
one "master loft" under development - as opposed to generating a new
loft in each edit session.

When it's time to export you make a clone of it and convert that to editable
mesh (which can be exported). The "master loft" remains as a loft with all the
changes up-to-date as you continue to refine and tweak it. This only goes on
for short time as you will soon reach a point where you are happy with the loft
and declare the road surface is now "good enough". You will then clone it one
last time, convert that clone to an editable mesh and start doing the next
phase of track development directly to those polygons, such as extruding
grass, walls, curbing, etc. Always keep that finalized loft (and the
lines you used to generate it) tucked away somewhere because you may
find yourself in a situation later down the road where you say to
yourself "Damn! I wish I still had that finished version of the loft
because it would come in handy for what I'm trying to do right now."

If the track seems to be too wide, use the "Tape Measure" tool in 3D Studio
Max to measure the width. If the "shape" line measures 12 then the road
width should also have turned out to be 12. If it is not the same then
you may have scaled the path line up to make it the right size for the
track. This creates some serious problems because the resulting loft is
further effected by any scaling you did to the original path line, thus
the pavement will be the wrong size, and even the mapping values will be
thrown off. In fact, all units of measure are now thrown off when you
later try to work with those polygons; for example, try to extrude one 1
meter and it may end up only 0.273 meters in reality, so you have to
figure a "conversion factor" to adjust for the scaling.

It can quickly become very aggravating. This is why it is important to zoom
your view port so that the grid matches up to the scale of the background image
correctly before you even start. I have not found a way to tell 3D
Studio MAX that I want the path line to be considered to be un-scaled
without it shrinking back to its original smaller size. Unfortunately,
the easiest and safest thing to do is to make a new path line,
considering the fact that you probably now have your view port zoomed
out to the proper size to trace the track map. Stay away from scaling
anything used in your lofts, it causes some tricky issues.

If you already know the length of the track you can do a measured lap around
your track at 30 Kmh\\Mph and divide the lap time by 2 to find the
actual track distance in Km or Miles. You can then use cross
multiplication to find out how much the track needs to be enlarged or
reduced in size. To reduce the size of the loft create a “measuring
tape” helper, go to “move mode” and move the triangle part of it to be
on the west side of the track and the box shaped part is on the west
side. Then go to the modify panel and click the specify length box and
increase the length until the green line reaches the east side of the
track (where the box is). Multiply the measuring tapes length to the
number you got from the measured lap and type in the new length. Then
select the path line in “line segment mode” and reduce\\increase its
size to match the measuring tape using uniform scale. You may need to
move the line around a bit to match it up to the measuring tape.

Here is an example: The track real world length is: 3 miles You take a lap
around the track at approximately 30 Mph and it take 8 minutes. The 8
minutes divided by 2 = 4 miles, the 3 miles divided by 4 = 0.75. The
measuring tape length is 500 meters. Multiply the 500 meters by .75 and
it = 375. Type this into the measuring tape length and reduce make the
path line match the green line’s length.
