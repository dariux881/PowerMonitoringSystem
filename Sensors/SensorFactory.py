import logging
#from Sensors.AmperometerSensor import AmperometerSensor
from Sensors.SensorMock import SensorMock, SensorMockNumber


class SensorFactory:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def create(self, sensor_type, sensor_config):
        match sensor_type:
            case 'amperometer':
                self.logger.info('Creating Amperometer sensor')
                instance = AmperometerSensor()
                if not instance.setup(sensor_config):
                    return None
                return instance
            
            case 'mock_bool':
                self.logger.info('Creating Mocked sensor')
                instance = SensorMock()
                if not instance.setup(sensor_config):
                    return None
                return instance

            case 'mock_number':
                self.logger.info('Creating Mocked sensor for number results')
                instance = SensorMockNumber()
                if not instance.setup(sensor_config):
                    return None
                return instance

            case _:
                self.logger.warning('sensor type: ' + sensor_type + ' is not supported')
                return None 
