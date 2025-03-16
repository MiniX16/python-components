#####
# 
# This class is part of the Programming the Internet of Things project.
# 
# It is provided as a simple shell to guide the student and assist with
# implementation for the Programming the Internet of Things exercises,
# and designed to be modified by the student as needed.
#

import logging
import random

import programmingtheiot.common.ConfigConst as ConfigConst
from programmingtheiot.data.ActuatorData import ActuatorData

class BaseActuatorSimTask:
    """
    Shell representation of class for student implementation.
    """

    def __init__(self, name: str = ConfigConst.NOT_SET, typeID: int = ConfigConst.DEFAULT_ACTUATOR_TYPE, simpleName: str = "Actuator"):
        self.latestActuatorResponse = ActuatorData(typeID=typeID, name=name)
        self.latestActuatorResponse.setAsResponse()

        self.name = name
        self.typeID = typeID
        self.simpleName = simpleName
        self.lastKnownCommand = ConfigConst.DEFAULT_COMMAND
        self.lastKnownValue = ConfigConst.DEFAULT_VAL

    def getLatestActuatorResponse(self) -> ActuatorData:
        """
        This can return the current ActuatorData response instance or a copy.
        """
        return self.latestActuatorResponse

    def getSimpleName(self) -> str:
        return self.simpleName

    def updateActuator(self, data: ActuatorData) -> ActuatorData:
        if data and self.typeID == data.getTypeID():
            statusCode = ConfigConst.DEFAULT_STATUS
            curCommand = data.getCommand()
            curVal = data.getValue()

            # Check if the command or value is a repeat from previous
            if curCommand == self.lastKnownCommand and curVal == self.lastKnownValue:
                logging.debug("New actuator command and value is a repeat. Ignoring: %s %s", str(curCommand), str(curVal))
            else:
                logging.debug("New actuator command and value to be applied: %s %s", str(curCommand), str(curVal))

                if curCommand == ConfigConst.COMMAND_ON:
                    logging.info("Activating actuator...")
                    statusCode = self._activateActuator(val=data.getValue(), stateData=data.getStateData())
                elif curCommand == ConfigConst.COMMAND_OFF:
                    logging.info("Deactivating actuator...")
                    statusCode = self._deactivateActuator(val=data.getValue(), stateData=data.getStateData())
                else:
                    logging.warning("ActuatorData command is unknown. Ignoring: %s", str(curCommand))
                    statusCode = -1

                # Update the last known actuator command and value
                self.lastKnownCommand = curCommand
                self.lastKnownValue = curVal

                # Create the ActuatorData response from the original command
                actuatorResponse = ActuatorData()
                actuatorResponse.updateData(data)
                actuatorResponse.setStatusCode(statusCode)
                actuatorResponse.setAsResponse()

                self.latestActuatorResponse.updateData(actuatorResponse)

                return actuatorResponse

        return None

    def _activateActuator(self, val: float = ConfigConst.DEFAULT_VAL, stateData: str = None) -> int:
        msg = "\n*******\n*  ON  *\n*******"
        msg += f"\n{self.name} VALUE -> {val}\n======="

        logging.info("Simulating %s actuator ON: %s", self.name, msg)

        return 0

    def _deactivateActuator(self, val: float = ConfigConst.DEFAULT_VAL, stateData: str = None) -> int:
        msg = "\n*******\n* OFF *\n*******"
        logging.info("Simulating %s actuator OFF: %s", self.name, msg)

        return 0
