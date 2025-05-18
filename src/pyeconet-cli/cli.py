import typer
from async_typer import AsyncTyper
from typing_extensions import Annotated

from pyeconet import EcoNetApiInterface
from pyeconet.equipment import EquipmentType
from pyeconet.equipment.thermostat import Thermostat
from pyeconet.equipment.water_heater import WaterHeater

import utils



app = AsyncTyper()



# Common arguments and options
emailOption = typer.Option(
    "--email",
    "-e",
    help="Your EcoNet account email.",
    envvar="ECONET_EMAIL",
    show_default=False,
    prompt=True,
)
passwordOption = typer.Option(
    "--password",
    "-p",
    help="Your EcoNet account password.",
    envvar="ECONET_PASSWORD",
    show_default=False,
    prompt=True,
    hide_input=True
)
idArgument = typer.Argument(
    help="The id of the device to inspect. See `list` command.",
    show_default=False
)



# Commands
@app.async_command()
async def list(
    email: Annotated[str, emailOption],
    password: Annotated[str, passwordOption]
):
    """Lists all EcoNet devices that are available to inspect."""

    api = await EcoNetApiInterface.login(email, password)

    all_equipment = await api.get_equipment_by_type(
        [EquipmentType.THERMOSTAT, EquipmentType.WATER_HEATER]
    )
    thermostats = all_equipment.get(EquipmentType.THERMOSTAT)
    water_heaters = all_equipment.get(EquipmentType.WATER_HEATER)
    
    print("Thermostats:")
    if (len(thermostats) == 0):
        print("  NONE")
    for thermostat in thermostats:
        utils.printDeviceNameId(thermostat)

    print("Water Heaters:")
    if (len(water_heaters) == 0):
        print("  NONE")
    for water_heater in water_heaters:
        utils.printDeviceNameId(water_heater)

@app.async_command()
async def device(
    email: Annotated[str, emailOption],
    password: Annotated[str, passwordOption],
    id: Annotated[str, idArgument],
    showInfo: Annotated[bool, typer.Option(
        "--info",
        "-i",
        help="Shows details of the device."
    )] = False,
    showStatus: Annotated[bool, typer.Option(
        "--status",
        "-s",
        help="Shows current status of the device."
    )] = False,
    showTemps: Annotated[bool, typer.Option(
        "--temps",
        "-t",
        help="Shows current temperatures and programming of the device."
    )] = False,
):
    """Prints the status of the specified device. Specifying `-ist` or none of those options will show all the information available."""

    api = await EcoNetApiInterface.login(email, password)
    device = await utils.getDevice(api, id)

    showAll = not (showInfo | showStatus | showTemps)

    if (showAll | showInfo):
        utils.printDeviceInfo(device)
    
    if (showAll | showStatus):
        if (type(device) is Thermostat):
            utils.printThermostatStatus(device)
        elif (type(device) is WaterHeater):
            utils.printWaterHeaterStatus(device)
        else:
            raise TypeError(format("Unsupported Type: %s", type(device)))

    if (showAll | showTemps):
        if (type(device) is Thermostat):
            utils.printThermostatTemps(device)
        elif (type(device) is WaterHeater):
            utils.printWaterHeaterTemps(device)
        else:
            raise TypeError(format("Unsupported Type: %s", type(device)))



if __name__ == '__main__':
    app()

