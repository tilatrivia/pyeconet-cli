from enum import Enum
from typing import List
from pyeconet.equipment import Equipment
from pyeconet.equipment import EquipmentType
from pyeconet.equipment.thermostat import Thermostat
from pyeconet.equipment.water_heater import WaterHeater

async def getDevice(api, id: str):
    all_equipment = await api.get_equipment_by_type(
        [EquipmentType.THERMOSTAT, EquipmentType.WATER_HEATER]
    )
    for equip_list in all_equipment.values():
        for equipment in equip_list:
            if(equipment.device_id == id):
                return equipment
    
    raise Exception(format("Could not find device with id: %s", id))

def printDeviceNameId(device: Equipment):
    print(f"  - {device.device_name}: {device.device_id}")

def printDeviceInfo(device: Equipment):
    print("Information:")
    print(f"  Id:               {device.device_id}")
    print(f"  Name:             {device.device_name}")
    print(f"  Serial Number:    {device.serial_number}")
    print(f"  Type:             {device.type.name}")
    print(f"  Generic Type:     {device.generic_type}")

def printThermostatStatus(thermostat: Thermostat):
    print("Status:")
    print(f"  Active            {thermostat.active}")
    print(f"  Running:          {thermostat.running}")
    print(f"  Running State:    {thermostat.running_state}")
    print(f"  Screen Locked:    {thermostat.screen_locked}")
    print(f"  Connected:        {thermostat.connected}")
    print(f"  WiFi Signal:      {thermostat.wifi_signal}")
    print(f"  Zone Id:          {thermostat.zone_id}")
    print(f"  Alert Count:      {thermostat.alert_count}")
    print(f"  Beep Enabled:     {thermostat.beep_enabled}")
    print(f"  Away Supported:   {thermostat.supports_away}")
    print(f"  Supports Humid.:  {thermostat.supports_humidifier}")

def printThermostatTemps(thermostat: Thermostat):
    print("Temperatures:")
    print(f"  Temperature:      {thermostat.set_point} [{thermostat.set_point_limits[0]}-{thermostat.set_point_limits[1]}]")
    print(f"  Humidity:         {thermostat.humidity}")
    print(f"  Mode*:            {thermostat.mode.name} {[mode.name for mode in thermostat.modes]}")
    print(f"  Fan Mode*:        {thermostat.fan_mode.name} {[fan_mode.name for fan_mode in thermostat.fan_modes]}")
    print(f"  Cool To*:         {thermostat.cool_set_point} [{thermostat.cool_set_point_limits[0]}-{thermostat.cool_set_point_limits[1]}]")
    print(f"  Heat To*:         {thermostat.heat_set_point} [{thermostat.heat_set_point_limits[0]}-{thermostat.heat_set_point_limits[1]}]")
    print(f"  Dehumid. Enabled: {thermostat.dehumidifier_enabled}")
    print(f"  Dehumidify To:    {thermostat.dehumidifier_set_point} [{thermostat.dehumidifier_set_point_limits[0]}-{thermostat.dehumidifier_set_point_limits[1]}]")
    print(f"  Dead Band:        {thermostat.deadband} [{thermostat.deadband_set_point_limits[0]}-{thermostat.deadband_set_point_limits[1]}]")
    print(f"  Away*:            {thermostat.away}")
    print(f"  Vacation:         {thermostat.vacation}")

def printWaterHeaterStatus(water_heater: WaterHeater):
    print("Status:")
    print(f"  Active            {water_heater.active}")
    print(f"  Running:          {water_heater.running}")
    print(f"  Running State:    {water_heater.running_state}")
    print(f"  Connected:        {water_heater.connected}")
    print(f"  WiFi Signal:      {water_heater.wifi_signal}")
    print(f"  Alert Count:      {water_heater.alert_count}")
    print(f"  Alert Override:   {water_heater.override_status}")
    print(f"  Away Supported:   {water_heater.supports_away}")
    print(f"  Leak Detection:   {water_heater.leak_installed}")
    print(f"  Has Shutoff:      {water_heater.has_shutoff_valve}")
    print(f"  Shutoff Open:     {water_heater.shutoff_valve_open}")
    print(f"  Tank Health:      {water_heater.tank_health} [0-100]")
    print(f"  Compressor Health:{water_heater.tank_health} [0-100]")
    print(f"  Demand Response:  {water_heater.demand_response_over}")
    print(f"  Today's Energy:   {water_heater.todays_energy_usage}")
    print(f"  Today's Water:    {water_heater.todays_water_usage}")

def printWaterHeaterTemps(water_heater: WaterHeater):
    print("Temperatures:")
    print(f"  Temperature*:     {water_heater.set_point} [{water_heater.set_point_limits[0]}-{water_heater.set_point_limits[1]}]")
    print(f"  Water Available:  {water_heater.tank_hot_water_availability} [100, 40, 10, 0, None]")
    print(f"  Mode*:            {water_heater.mode} {[mode.name for mode in water_heater.modes]}")
    print(f"  Enabled:          {water_heater.enabled}")
    print(f"  Away:             {water_heater.away}")
    print(f"  Vacation:         {water_heater.vacation}")

# TODO: Add energy usage readout for water heaters (energy_usage, historical_energy_usage, energy_type, todays_energy_usage)