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

from LC709203F_constants import *

# name:        LC709203F
# description: Smart LiB Gauge Battery Fuel Gauge LSI For 1‐Cell Lithium‐ion/Polymer (Li+)
# manuf:       ON Semiconductor
# version:     0.1
# url:         http://www.onsemi.com/pub/Collateral/LC709203F-D.PDF
# date:        2017-12-29


# Derive from this class and implement read and write
class LC709203F_Base:
	"""Smart LiB Gauge Battery Fuel Gauge LSI For 1‐Cell Lithium‐ion/Polymer (Li+)"""
	# Register BEFORE_RSOC
	# Executes RSOC initialization with sampled maximum voltage when 'hAA55 is set. 
	#       This LSI obtains Open Circuit Voltage (OCV) reading
	#       10 ms after Power-on reset to initialize RSOC (See
	#       Figure 7).
	#       Or the LSI can be forced to initialize RSOC by sending the
	#       Before RSOC Command (0×04 = AA55) or the Initial
	#       RSOC Command (0×07 = AA55). The accuracy of the
	#       Initialization requires the OCV reading to be taken with
	#       minimal load or charge, under 0.025C, on the battery. (i.e.
	#       less than 75 mA for 3000 mAh design capacity battery.).
	#       The LSI initializes RSOC by the maximum voltage
	#       between initialize after Power-on reset and setting the
	#       command when the Before RSOC command is written. (See
	#       Figure 8). 
	
	
	def setBEFORE_RSOC(self, val):
		"""Set register BEFORE_RSOC"""
		self.write(REG.BEFORE_RSOC, val, 16)
	
	def getBEFORE_RSOC(self):
		"""Get register BEFORE_RSOC"""
		return self.read(REG.BEFORE_RSOC, 16)
	
	# Bits BEFORE_RSOC
	# Register THERMISTOR_B
	# Sets B−constant of the thermistor to be measured. 
	#       Units: 1K 
	#       Refer to
	#       the specification sheet of the thermistor for the set value to
	#       use. 
	
	
	def setTHERMISTOR_B(self, val):
		"""Set register THERMISTOR_B"""
		self.write(REG.THERMISTOR_B, val, 16)
	
	def getTHERMISTOR_B(self):
		"""Get register THERMISTOR_B"""
		return self.read(REG.THERMISTOR_B, 16)
	
	# Bits THERMISTOR_B
	# Register INITIAL_RSOC
	# Executes RSOC initialization when 0xAA55 is set. 
	#       The LSI can be forced to initialize RSOC by sending the Before RSOC Command (0×04 = AA55) 
	#       or the Initial RSOC Command (0×07 = AA55). 
	#       The LSI initializes RSOC by the measured voltage at that time when the Initial RSOC command 
	#       is written. (See Figure 9). The maximum time to initialize RSOC after the command is 
	#       written is 1.5 ms. 
	
	
	def setINITIAL_RSOC(self, val):
		"""Set register INITIAL_RSOC"""
		self.write(REG.INITIAL_RSOC, val, 16)
	
	def getINITIAL_RSOC(self):
		"""Get register INITIAL_RSOC"""
		return self.read(REG.INITIAL_RSOC, 16)
	
	# Bits INIT_RSOC
	# Register CELL_TEMPERATURE
	# Displays Cell Temperature, 0x0000 to 0xFFFF.
	#       Units: 0.1K (0.0°C = 0x0AAC) 
	#       This register contains the cell temperature from −20_C (0×09E4) to +60_C (0×0D04) measured in 0.1_C units.
	#       In the Thermistor mode (0×16 = 01) the LSI measures the attached thermistor and loads the temperature into the Cell Temperature register. In the Thermistor mode, the thermistor shall be connected to the LSI as shown in Figure 2. The temperature is measured by having TSW pin to provide power into the thermistor and TSENSE pin to sense the output voltage from the thermistor. Temperature measurement timing is controlled by the LSI, and the power to the thermistor is not supplied for other reasons except to measure the temperature. 
	
	
	def setCELL_TEMPERATURE(self, val):
		"""Set register CELL_TEMPERATURE"""
		self.write(REG.CELL_TEMPERATURE, val, 16)
	
	def getCELL_TEMPERATURE(self):
		"""Get register CELL_TEMPERATURE"""
		return self.read(REG.CELL_TEMPERATURE, 16)
	
	# Bits CELL_TEMPERATURE
	# Register CELL_TEMPERATURE
	# Sets Cell Temperature in I2C mode, h09E4 to 'h0D04.
	#       Units: 0.1K (0.0°C = 0x0AAC) 
	#       This register contains the cell temperature from −20_C (0×09E4) to +60_C (0×0D04) measured in 0.1_C units.
	#       In the I2C mode (0×16 = 00) the temperature is provided by the host processor. During discharge/charge the register should be updates when the temperature changes more than 1_C 
	
	
	def setCELL_TEMPERATURE(self, val):
		"""Set register CELL_TEMPERATURE"""
		self.write(REG.CELL_TEMPERATURE, val, 16)
	
	def getCELL_TEMPERATURE(self):
		"""Get register CELL_TEMPERATURE"""
		return self.read(REG.CELL_TEMPERATURE, 16)
	
	# Bits CELL_TEMPERATURE
	# Register CELL_VOLTAGGE
	# Displays Cell Voltage, 'h0000 to 'hFFFF.
	#           Units: 1 mV Displays Cell Voltage 
	#           This register contains the voltage on VDD 1 mV units. 
	
	
	def setCELL_VOLTAGGE(self, val):
		"""Set register CELL_VOLTAGGE"""
		self.write(REG.CELL_VOLTAGGE, val, 8)
	
	def getCELL_VOLTAGGE(self):
		"""Get register CELL_VOLTAGGE"""
		return self.read(REG.CELL_VOLTAGGE, 8)
	
	# Bits CELL_VOLTAGGE
	# Register CURRENT_DIRECTION
	# Selects Auto/Charge/Discharge mode 
	
	def setCURRENT_DIRECTION(self, val):
		"""Set register CURRENT_DIRECTION"""
		self.write(REG.CURRENT_DIRECTION, val, 16)
	
	def getCURRENT_DIRECTION(self):
		"""Get register CURRENT_DIRECTION"""
		return self.read(REG.CURRENT_DIRECTION, 16)
	
	# Bits CURRENT_DIRECTION
	# Register APA
	# Adjustment Pack Application: Sets Parasitic impedance, 'h0000 to 'h00FF.
	#           Units: 1 mΩ 
	#           This register is used to control the reporting of RSOC. In Auto mode the RSOC is reported as it increases or decreases. In Charge mode the RSOC is not permitted to decrease. In Discharge mode the RSOC is not permitted to increase.
	#           With consideration of capacity influence by temperature, we recommend operating in Auto because RSOC is affected by the cell temperature. A warm cell has more capacity than a cold cell. Be sure not to charge in the Discharge mode and discharge in the Charge mode; it will create an error.
	#           An example of RSOC reporting is shown in Figures 10 and 11. 
	
	
	def setAPA(self, val):
		"""Set register APA"""
		self.write(REG.APA, val, 8)
	
	def getAPA(self):
		"""Get register APA"""
		return self.read(REG.APA, 8)
	
	# Bits APA
	# Register APT
	# Adjustment Pack Thermistor: Sets a value to adjust temperature measurement 
	#           delay timing, 'h0000 to 'hFFFF 
	
	
	def setAPT(self, val):
		"""Set register APT"""
		self.write(REG.APT, val, 16)
	
	def getAPT(self):
		"""Get register APT"""
		return self.read(REG.APT, 16)
	
	# Bits APT
	# Register RSOC
	# Displays RSOC value based on a 0−100 scale, 'h0000 to 'h0064.
	#           Units: 1%. 
	
	
	def setRSOC(self, val):
		"""Set register RSOC"""
		self.write(REG.RSOC, val, 8)
	
	def getRSOC(self):
		"""Get register RSOC"""
		return self.read(REG.RSOC, 8)
	
	# Bits RSOC
	# Register ITE
	# Indicator to Empty: 1% Displays RSOC value based on a 0−100 scale, 'h0000 to 'h03E8 .
	#           Units: 0.1%. 
	#           This is the same as RSOC with a resolution of 0.1% over the range 0.0% to 100.0%. 
	
	
	def setITE(self, val):
		"""Set register ITE"""
		self.write(REG.ITE, val, 8)
	
	def getITE(self):
		"""Get register ITE"""
		return self.read(REG.ITE, 8)
	
	# Bits ITE
	# Register IC_VERSION
	# Displays an ID number of an IC, 'h0000 to 'hFFFF. 
	
	def setIC_VERSION(self, val):
		"""Set register IC_VERSION"""
		self.write(REG.IC_VERSION, val, 8)
	
	def getIC_VERSION(self):
		"""Get register IC_VERSION"""
		return self.read(REG.IC_VERSION, 8)
	
	# Bits IC_VERSION
	# Register CHANGE_OF_PARAM
	# Change Of The Parameter Selects a battery profile, 0x0000 or 0x0001 
	#           The LSI contains a data file comprised of two battery profiles. This register is used to select the battery profile to be used. See Table 8. Register Number of the Parameter (0x1A) contains identity of the data file.
	#           The Data file is loaded during final test depending on the part number ordered. 
	#           Most of the time, battery nominal/rated voltage or charging voltage values are used to determine which profile data shall be used. Please contact ON Semiconductor if you cannot identify which profile to select. 
	
	
	def setCHANGE_OF_PARAM(self, val):
		"""Set register CHANGE_OF_PARAM"""
		self.write(REG.CHANGE_OF_PARAM, val, 16)
	
	def getCHANGE_OF_PARAM(self):
		"""Get register CHANGE_OF_PARAM"""
		return self.read(REG.CHANGE_OF_PARAM, 16)
	
	# Bits CHANGE_OF_PARAM
	# Register ALARM_LOW_RSOC
	# Alarm Low RSO: Disable Sets RSOC threshold to generate Alarm signal.
	#           Units: 1% 
	#           The ALARMB pin will be set low when the RSOC value falls below this value, will be released from low when RSOC value rises than this value. Set to Zero to disable. Figure 14. 
	
	
	def setALARM_LOW_RSOC(self, val):
		"""Set register ALARM_LOW_RSOC"""
		self.write(REG.ALARM_LOW_RSOC, val, 16)
	
	def getALARM_LOW_RSOC(self):
		"""Get register ALARM_LOW_RSOC"""
		return self.read(REG.ALARM_LOW_RSOC, 16)
	
	# Bits ALARM_LOW_RSOC
	# Register ALARM_LOW_CELL_VOLTAGE
	# Alarm Low Cell: Disable	1 mV Sets Voltage threshold to generate Alarm signal.
	#           Units: 1mV. 
	#           The ALARMB pin will be set low if VDD falls below this value, will be released from low if VDD rises than this value. Set to Zero to disable. Figure 15. 
	
	
	def setALARM_LOW_CELL_VOLTAGE(self, val):
		"""Set register ALARM_LOW_CELL_VOLTAGE"""
		self.write(REG.ALARM_LOW_CELL_VOLTAGE, val, 16)
	
	def getALARM_LOW_CELL_VOLTAGE(self):
		"""Get register ALARM_LOW_CELL_VOLTAGE"""
		return self.read(REG.ALARM_LOW_CELL_VOLTAGE, 16)
	
	# Bits ALARM_LOW_CELL_VOLTAGE
	# Register IC_POWER_MODE
	# IC Power Mode: Selects Power mode. See note 4. 
	#           The LSI has two power modes. Sleep (0x15 = 02) or Operational mode (0x15 = 01). In the Sleep mode only I2C communication functions. In the Operational mode all functions operate with full calculation and tracking of RSOC during charge and discharge.
	#           If the battery is significantly charged or discharged during sleep mode, the RSOC will not be accurate. Moved charge is counted continuously to measure the RSOC in 
	#           Operational mode. If battery is discharged or charged in the Sleep mode, the count breaks off.
	#           When it is switched from Sleep mode to Operational mode, RSOC calculation is continued by using the data which was measured in the previous Operational mode. 
	
	
	def setIC_POWER_MODE(self, val):
		"""Set register IC_POWER_MODE"""
		self.write(REG.IC_POWER_MODE, val, 16)
	
	def getIC_POWER_MODE(self):
		"""Get register IC_POWER_MODE"""
		return self.read(REG.IC_POWER_MODE, 16)
	
	# Bits IC_POWER_MODE
	# Register STATUS_BIT
	# Status Bit: Selects Temperature obtaining method. 
	#           This selects the Thermistor mode. Thermistor mode (0x16 = 01) the LSI measures the attached thermistor and loads the temperature into the Cell Temperature register.
	#           I2C mode (0x16 = 00) the temperature is provided by the host processor. 
	
	
	def setSTATUS_BIT(self, val):
		"""Set register STATUS_BIT"""
		self.write(REG.STATUS_BIT, val, 16)
	
	def getSTATUS_BIT(self):
		"""Get register STATUS_BIT"""
		return self.read(REG.STATUS_BIT, 16)
	
	# Bits STATUS_BIT
	# Register NUMBER_OF_THE_PARAMETER
	# Number of The	Parameter: Displays Battery profile code 
	#           The LSI contains a data file comprised of two battery profiles. This register contains identity of the data file. Please see register Change of the Parameter (0x12) to select the battery profile to be used. See Table 8.
	#           The Data file is loaded during final test depending on the part number ordered. This file can be loaded in the field if required.
	#           Please contact ON Semiconductor if you cannot identify which profile to select. 
	
	
	def setNUMBER_OF_THE_PARAMETER(self, val):
		"""Set register NUMBER_OF_THE_PARAMETER"""
		self.write(REG.NUMBER_OF_THE_PARAMETER, val, 16)
	
	def getNUMBER_OF_THE_PARAMETER(self):
		"""Get register NUMBER_OF_THE_PARAMETER"""
		return self.read(REG.NUMBER_OF_THE_PARAMETER, 16)
	
	# Bits NUMBER_OF_THE_PARAMETER
