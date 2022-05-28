.. warning::

  This page is WIP.

.. sidebar:: Source

  Source of the information and descriptions herein were extracted from
  "SkipBarber.pm" file of the SkipBarber that comes with the Dev Mode
  of rFactor2 game version v1121. Where necessary and available, information and
  descriptions were amended.

==========
Suspension
==========

.. contents:: Contents
  :depth: 2
  :local:

************
Introduction
************

Introduction text. Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed
do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim
veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo
consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum
dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident,
sunt in culpa qui officia deserunt mollit anim id est laborum.

Conventions
===========

+x = left

+z = rear

+y = up

+pitch = nose up

+yaw = nose right

+roll = right

[BODY]
  Rigid mass with mass and inertial properties.

  These suspension objects have the following parameters:

  name

  mass

  inertia

  pos

  ori

[JOINT]
  Ball joint constraining an offset of one body to an offset of another body
  (eliminates 3 DOF).

[HINGE]
  Constraint restricting the relative rotations of two bodies to be around a
  single axis (eliminates 2 DOF).

[BAR]
  Constraint holding an offset of one body from an offset of  another body at a
  fixed distance (eliminates 1 DOF).

[JOINT&HINGE]
  Both the joint and hinge constraints, forming the conventional definition of
  a hinge (eliminates 5 DOF).

******
Bodies
******

Main Body
=========

Body including all rigidly attached parts (wings, barge boards, etc.):

.. note:: The mass and inertia for the main vehicle "body" are not used because
  it is derived from the HDV file by subtracting out all the wheels, etc.
  For all other bodies (wheels, spindles), they are important!

[BODY]
name=body mass=(0) inertia=(0,0,0)
pos=(0,0,0) ori=(0,0,0)

Front spindles
==============

.. note:: Unsprung masses that do not exhibit any pitch rotation with
  significant relation to the wheel rotation rate.

[BODY]
name=fl_spindle mass=(9.7) inertia=(0.0275,0.026,0.0245)
pos=( 0.605,0,-1.35) ori=(0,0,0)

[BODY]
name=fr_spindle mass=(9.7) inertia=(0.0275,0.026,0.0245)
pos=(-0.605,0,-1.35) ori=(0,0,0)

Front wheels
============

[BODY]
name=fl_wheel mass=(21.9) inertia=(0.859,0.5049,0.5049)
pos=( 0.676,0,-1.35) ori=(0,0,0)

Any unsprung bodies that rotate significantly in proportion to the wheel
rotation rate (i.e. generally tyre+rim+disc/bell+bearing+nuts).

[BODY]
name=fr_wheel mass=(21.9) inertia=(0.859,0.5049,0.5049)
pos=(-0.676,0,-1.35) ori=(0,0,0)

Rear spindles
=============

[BODY]
name=rl_spindle mass=(9.5) inertia=(0.0275,0.026,0.0245)
pos=( 0.56,0,1.11) ori=(0,0,0)

[BODY]
name=rr_spindle mass=(9.5) inertia=(0.0275,0.026,0.0245)
pos=(-0.56,0,1.11) ori=(0,0,0)

Rear wheels
===========

.. note:: These do includes half of driveshaft.

[BODY]
name=rl_wheel mass=(22.427) inertia=(1.14882,0.67382,0.67382)
pos=( 0.658,0,1.11) ori=(0,0,0)

[BODY]
name=rr_wheel mass=(22.427) inertia=(1.14882,0.67382,0.67382)
pos=(-0.658,0,1.11) ori=(0,0,0)

Fuel tank
=========

Fuel in tank is not rigidly attached - it is attached with springs and dampers
to simulate movement.  Properties are defined in the HDV file.

[BODY]
name=fuel_tank mass=(0.5) inertia=(0.3,0.3,0.3)
pos=(0,0,0) ori=(0,0,0)

Defines the minimum mass of remaining fuel in tank.

Driver Head
===========

.. note:: Driver's head is not rigidly attached, and it does NOT affect the
  vehicle physics. Position is from the eyepoint defined in the VEH file, while
  other properties are defined in the head physics file.

[BODY]
name=driver_head mass=(6.6) inertia=(0.047,0.036,0.039)
pos=(0,0,0) ori=(0,0,0)

***********
Constraints
***********

Wheel and spindle connections
=============================

[JOINT&HINGE]
posbody=fl_wheel negbody=fl_spindle pos=fl_wheel axis=( 1,0,0)

[JOINT&HINGE]
posbody=fr_wheel negbody=fr_spindle pos=fr_wheel axis=(-1,0,0)

[JOINT&HINGE]
posbody=rl_wheel negbody=rl_spindle pos=rl_wheel axis=( 1,0,0)

[JOINT&HINGE]
posbody=rr_wheel negbody=rr_spindle pos=rr_wheel axis=(-1,0,0)

Front Suspension
================

Front left suspension (2 A-arms + 1 steering arm = 5 links):

[BAR]
name=fl_fore_upper posbody=body negbody=fl_spindle pos=( 0.352, 0.087945,-1.41) neg=( 0.5817, 0.127,-1.336)

[BAR]
name=fl_rear_upper posbody=body negbody=fl_spindle pos=( 0.352, 0.087945,-1.1) neg=( 0.5817, 0.127,-1.336)

[BAR]
name=fl_fore_lower posbody=body negbody=fl_spindle pos=( 0.262,-0.1317625,-1.44) neg=( 0.622,-0.10175,-1.3556)

[BAR]
name=fl_rear_lower posbody=body negbody=fl_spindle pos=( 0.262,-0.1222375,-1.1) neg=( 0.622,-0.10175,-1.3556)

[BAR]
name=fl_steering posbody=body negbody=fl_spindle pos=( 0.311,-0.0348,-1.46) neg=( 0.611, 0,-1.46)

.. note:: Steering arm (must be named for identification).

Front right suspension (2 A-arms + 1 steering arm = 5 links):

[BAR]
name=fr_fore_upper posbody=body negbody=fr_spindle pos=(-0.352, 0.087945,-1.41) neg=(-0.5817, 0.127,-1.336)

.. note:: Forward upper arm (used in steering lock calculation).

[BAR]
name=fr_rear_upper posbody=body negbody=fr_spindle pos=(-0.352, 0.087945,-1.1) neg=(-0.5817, 0.127,-1.336)

[BAR]
name=fr_fore_lower posbody=body negbody=fr_spindle pos=(-0.262,-0.1317625,-1.44) neg=(-0.622,-0.10175,-1.3556)

[BAR]
name=fr_rear_lower posbody=body negbody=fr_spindle pos=(-0.262,-0.1222375,-1.1) neg=(-0.622,-0.10175,-1.3556)

[BAR]
name=fr_steering posbody=body negbody=fr_spindle pos=(-0.311,-0.0348,-1.46) neg=(-0.611, 0,-1.46)

.. note:: Steering arm (must be named for identification)

Rear Suspension
===============

Rear left suspension (2 A-arms + 1 straight link = 5 links):

[BAR]
name=rl_fore_upper posbody=body negbody=rl_spindle pos=(0.338, 0.0394335,0.388) neg=(0.543,0.1706,1.1)

[BAR]
name=rl_rear_upper posbody=body negbody=rl_spindle pos=(0.338, 0.1100455,1.11) neg=(0.543,0.1706,1.1)

[BAR]
name=rl_fore_lower posbody=body negbody=rl_spindle pos=(0.203,-0.1891665,0.443) neg=(0.56,-0.1706,1.06)

[BAR]
name=rl_rear_lower posbody=body negbody=rl_spindle pos=(0.203,-0.1891665,1.07) neg=(0.56,-0.1706,1.06)

[BAR]
name=rl_toelink posbody=body negbody=rl_spindle pos=(0.203,-0.1891665,1.07) neg=(0.579,-0.1706,1.19)

Rear right suspension (2 A-arms + 1 straight link = 5 links):

[BAR]
name=rr_fore_upper posbody=body negbody=rr_spindle pos=(-0.338, 0.0394335,0.388) neg=(-0.543,0.1706,1.1)

[BAR]
name=rr_rear_upper posbody=body negbody=rr_spindle pos=(-0.338, 0.1100455,1.11) neg=(-0.543,0.1706,1.1)

[BAR]
name=rr_fore_lower posbody=body negbody=rr_spindle pos=(-0.203,-0.1891665,0.443) neg=(-0.56,-0.1706,1.06)

[BAR]
name=rr_rear_lower posbody=body negbody=rr_spindle pos=(-0.203,-0.1891665,1.07) neg=(-0.56,-0.1706,1.06)

[BAR]
name=rr_toelink posbody=body negbody=rr_spindle pos=(-0.203,-0.1891665,1.07) neg=(-0.579,-0.1706,1.19)
