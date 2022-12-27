class Telemetry:
    _instance = None

    _RwS: int = 0  # right wheel speed
    _LwS: int = 0  # left wheel speed

    _HaH: int = 90  # head angle horizontal
    _HaV: int = 0  # head angle vertical
    _RaaH: int = 0  # right arm angle horizontal
    _RaaV: int = 0  # right arm angle vertical
    _LaaH: int = 0  # left arm angle horizontal
    _LaaV: int = 0  # left arm angle vertical

    _CoX: int = 0  # compas x
    _CoY: int = 0  # compas y
    _CoZ: int = 0  # compas z

    _GyX: int = 0  # gyroscope x
    _GyY: int = 0  # gyroscope y
    _GyZ: int = 0  # gyroscope z

    _AcX: int = 0  # accelerometer x
    _AcY: int = 0  # accelerometer y
    _AcZ: int = 0  # accelerometer z

    _Tmp: int = 0  # temperature
    _Dist: int = 0  # distance

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Telemetry, cls).__new__(cls)
        return cls._instance

    def get_current_telemetry(self) -> list:
        pass

