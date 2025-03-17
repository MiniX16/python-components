#####
# 
# This class is part of the Programming the Internet of Things project.
# 
# It is provided as a simple shell to guide the student and assist with
# implementation for the Programming the Internet of Things exercises,
# and designed to be modified by the student as needed.
#

from programmingtheiot.data.SensorData import SensorData
import programmingtheiot.common.ConfigConst as ConfigConst
from programmingtheiot.common.ConfigUtil import ConfigUtil
from programmingtheiot.cda.sim.BaseSensorSimTask import BaseSensorSimTask

from pisense import SenseHAT

class PressureSensorEmulatorTask(BaseSensorSimTask):
    def __init__(self):
        super().__init__(
            name=ConfigConst.PRESSURE_SENSOR_NAME,
            typeID=ConfigConst.PRESSURE_SENSOR_TYPE
        )

        enable_emulation = ConfigUtil().getBoolean(
            ConfigConst.CONSTRAINED_DEVICE, ConfigConst.ENABLE_EMULATOR_KEY
        )

        self.sh = SenseHAT(emulate=enable_emulation)

    def generateTelemetry(self) -> SensorData:
        sensor_data = SensorData(name=self.getName(), typeID=self.getTypeID())
        sensor_val = self.sh.environ.pressure

        sensor_data.setValue(sensor_val)
        self.latestSensorData = sensor_data

        return sensor_data

