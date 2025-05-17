from pyeconet.equipment import EquipmentType

async def getDevice(api, id: str):
    all_equipment = await api.get_equipment_by_type(
        [EquipmentType.THERMOSTAT, EquipmentType.WATER_HEATER]
    )
    for equip_list in all_equipment.values():
        for equipment in equip_list:
            if(equipment.device_id == id):
                return equipment
    
    raise Exception(format("Could not find device with id: %s", id))

def printDeviceNameId(device: any):
    print(f"  - {device.device_name}: {device.device_id}")

def printDeviceInfo(device: any):
    print(f"  Id:               {device.device_id}")
    print(f"  Name:             {device.device_name}")
    print(f"  Serial Number:    {device.serial_number}")
    print(f"  Type:             {device.type}")
    print(f"  Generic Type:     {device.generic_type}")

def printThermostatStatus(thermostat: any):
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
    print(f"  Supports Humidifier: {thermostat.supports_humidifier}")

def printThermostatConditions(thermostat: any):
    print(f"  Temperature:      {thermostat.set_point} [{thermostat.set_point_limits[0]}-{thermostat.set_point_limits[1]}]")
    print(f"  Humidity:         {thermostat.humidity}")
    print(f"  Mode*:            {thermostat.mode} [{thermostat.modes}]")
    print(f"  Fan Mode*:        {thermostat.fan_mode} [{thermostat.fan_modes}]")
    print(f"  Cool To*:         {thermostat.cool_set_point} [{thermostat.cool_set_point_limits[0]}-{thermostat.cool_set_point_limits[1]}]")
    print(f"  Heat To*:         {thermostat.heat_set_point} [{thermostat.heat_set_point_limits[0]}-{thermostat.heat_set_point_limits[1]}]")
    print(f"  Dehumidifier Enabled: {thermostat.dehumidifier_enabled}")
    print(f"  Dehumidify To:    {thermostat.dehumidifier_set_point} [{thermostat.dehumidifier_set_point_limits[0]}-{thermostat.dehumidifier_set_point_limits[1]}]")
    print(f"  Dead Band:        {thermostat.deadband} [{thermostat.deadband_set_point_limits[0]}-{thermostat.deadband_set_point_limits[1]}]")
    print(f"  Away*:            {thermostat.away}")
    print(f"  Vacation:         {thermostat.vacation}")