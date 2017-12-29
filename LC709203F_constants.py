#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""LC709203F: Smart LiB Gauge Battery Fuel Gauge LSI For 1‐Cell Lithium‐ion/Polymer (Li+)"""

__author__     = "ChISL"
__copyright__  = "TBD"
__credits__    = ["ON Semiconductor"]
__license__    = "TBD"
__version__    = "0.1"
__maintainer__ = "https://chisl.io"
__email__      = "info@chisl.io"
__status__     = "Test"

class REG:
	BEFORE_RSOC = 4
	THERMISTOR_B = 6
	INITIAL_RSOC = 7
	CELL_TEMPERATURE = 8
	CELL_TEMPERATURE = 8
	CELL_VOLTAGGE = 9
	CURRENT_DIRECTION = 10
	APA = 11
	APT = 12
	RSOC = 13
	ITE = 15
	IC_VERSION = 17
	CHANGE_OF_PARAM = 18
	ALARM_LOW_RSOC = 19
	ALARM_LOW_CELL_VOLTAGE = 20
	IC_POWER_MODE = 21
	STATUS_BIT = 22
	NUMBER_OF_THE_PARAMETER = 26
