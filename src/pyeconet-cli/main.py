import typer
from async_typer import AsyncTyper
from typing_extensions import Annotated

from pyeconet import EcoNetApiInterface
from pyeconet.equipment import EquipmentType
from pyeconet.equipment.thermostat import Thermostat

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
async def info(
    email: Annotated[str, emailOption],
    password: Annotated[str, passwordOption],
    id: Annotated[str, idArgument],
):
    """Prints metadata about the specified device."""

    api = await EcoNetApiInterface.login(email, password)
    device = await utils.getDevice(api, id)
    utils.printDeviceInfo(device)

@app.async_command()
async def status(
    email: Annotated[str, emailOption],
    password: Annotated[str, passwordOption],
    id: Annotated[str, idArgument],
):
    """Prints status and configuration of the specified device."""

    api = await EcoNetApiInterface.login(email, password)
    device = await utils.getDevice(api, id)
    utils.printThermostatStatus(device)

@app.async_command()
async def conditions(
    email: Annotated[str, emailOption],
    password: Annotated[str, passwordOption],
    id: Annotated[str, idArgument],
):
    """Prints current conditions and programming for the specified device."""

    api = await EcoNetApiInterface.login(email, password)
    device = await utils.getDevice(api, id)
    utils.printThermostatConditions(device)



if __name__ == '__main__':
    app()

