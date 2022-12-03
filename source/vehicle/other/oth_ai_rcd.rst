.. warning::

  This page is WIP.

.. sidebar:: Source

  Source of the information and descriptions herein were extracted from
  "Skip_Barber.rcd" file of the SkipBarber that comes with the Dev Mode of
  rFactor2 game version v1121. Where necessary and available, information
  and descriptions were amended.

#####################
RCD - AI Talent Files
#####################

The file defines the talent of AI drivers.

.. contents:: Contents
  :depth: 2
  :local:

*****************
RCD File Contents
*****************

[vehicle_class]
  Example value:  Skip_Barber

  This is the first reference in the RCD file and refers to a vehicle class
  as defined in the VEH file under "Classes="

[default]
  Example value:  default

  This is the default talent definition for the vehicle class specified above.

StepDistance
	Example value:	5.0

  *no description provided*

StepSpeed1
	Example value:	25.0

  *no description provided*

StepSpeed2
	Example value:	32.0

  *no description provided*

StepSpeed3
	Example value:	40.0

  *no description provided*

StepSpeed4
	Example value:	55.0

  *no description provided*

StepSpeed5
	Example value:	75.0

  *no description provided*

StepSpeed6
	Example value:	95.0

  *no description provided*

StepSpeed7
	Example value:	115.0

  *no description provided*

StepSpeed8
	Example value:	175.0

  *no description provided*

DrivingLine
	Example value:	OW3_FAST, rTrainer_Fast

  Fast driving line to use as racing line, first in list has priority (max of 3 can be specified).  Falls back to FASTEST if no specified paths exist

CorneringCaution
	Example value:	60

  *no description provided*

UnderSteerEffectOnThrottleMulti
	Example value:	125

  *no description provided*

UnderSteerEffectOnLineMulti
	Example value:	55

  *no description provided*

Driver Name
  Example value:  Eric Elliott

  This is the name of the AI driver. The following talent information is
  specific to this driver. Driver name needs to be equal to the driver name as
  specified in a VEH file of the mod.

Nationality
	Example value:	American

  *no description provided*

DateofBirth
	Example value:	26-2-1984

  *no description provided*

Starts
	Example value:	0

  *no description provided*

Poles
	Example value:	0

  *no description provided*

Wins
	Example value:	0

  *no description provided*

DriversChampionships
	Example value:	0

  *no description provided*

Aggression
	Example value:	90.0

  *no description provided*

Reputation
	Example value:	100.0

  *no description provided*

Courtesy
	Example value:	95.0

  *no description provided*

Composure
	Example value:	97.0

  *no description provided*

Speed
	Example value:	100.0

  *no description provided*

QualifySpeed
	Example value:	90.0

  *no description provided*

WetSpeed
	Example value:	90.0

  *no description provided*

StartSkill
	Example value:	115.0

  *no description provided*

Crash
	Example value:	0.7

  *no description provided*

Recovery
	Example value:	100.0

  *no description provided*

CompletedLaps
	Example value:	100.0

  *no description provided*

MinRacingSkill
	Example value:	90.0

  *no description provided*

******************
SkipBarber Example
******************

.. code-block::

  Skip_Barber
  {
    default
    {
      StepDistance = 5.0
      StepSpeed1 = 25.0
      StepSpeed2 = 32.0
      StepSpeed3 = 40.0
      StepSpeed4 = 55.0
      StepSpeed5 = 75.0
      StepSpeed6 = 95.0
      StepSpeed7 = 115.0
      StepSpeed8 = 175.0
      DrivingLine = OW3_FAST, rTrainer_Fast
      CorneringCaution = 60
      UnderSteerEffectOnThrottleMulti = 125
      UnderSteerEffectOnLineMulti = 55
    }
    Eric Elliott
    {
      Nationality = American
      DateofBirth = 26-2-1984
      Starts = 0
      Poles = 0
      Wins = 0
      DriversChampionships = 0
      Aggression = 90.0
      Reputation = 100.0
      Courtesy = 95.0
      Composure = 97.0
      Speed = 100.0
      QualifySpeed = 90.0
      WetSpeed = 90.0
      StartSkill = 115.0
      Crash = 0.7
      Recovery = 100.0
      CompletedLaps = 100.0
      MinRacingSkill = 90.0
    }
    Richard Chmielewski
    {
      Nationality = American
      DateofBirth = 26-2-1984
      Starts = 0
      Poles = 0
      Wins = 0
      DriversChampionships = 0
      Aggression = 90.0
      Reputation = 100.0
      Courtesy = 95.0
      Composure = 95.0
      Speed = 99.0
      QualifySpeed = 93.0
      WetSpeed = 95.0
      StartSkill = 115.0
      Crash = 0.2
      Recovery = 98.0
      CompletedLaps = 100.0
      MinRacingSkill = 95.0
    }
  }
