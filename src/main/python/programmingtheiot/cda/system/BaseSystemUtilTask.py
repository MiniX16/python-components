import programmingtheiot.common.ConfigConst as ConfigConst

class BaseSystemUtilTask:
    """
    Shell implementation representation of class for student implementation.
    """

    def __init__(self, name: str = ConfigConst.NOT_SET, typeID: int = ConfigConst.DEFAULT_SENSOR_TYPE):
        self.name = name
        self.typeID = typeID

    def getName(self) -> str:
        return self.name

    def getTypeID(self) -> int:
        return self.typeID

    def getTelemetryValue(self) -> float:
        pass
