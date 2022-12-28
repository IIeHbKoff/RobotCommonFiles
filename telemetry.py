class Telemetry:
    instance = None
    _params_list = ['rwS', 'lwS', 'sch0', 'sch1', 'sch2', 'sch3', 'sch4', 'sch5', 'sch6', 'sch7', 'sch8',
                    'sch9', 'coX', 'coY', 'coZ', 'gyX', 'gyY', 'gyZ', 'acX', 'acY', 'acZ', 'tmp', 'dist',
                    'battery', 'mood', 'errors']

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super(Telemetry, cls).__new__(cls)
        return cls.instance

    def __init__(self):
        self._rwS: int = 0  # right wheel speed
        self._lwS: int = 0  # left wheel speed

        self._sch0: int = 0  # servo channel 0
        self._sch1: int = 0  # servo channel 1
        self._sch2: int = 0  # servo channel 2
        self._sch3: int = 0  # servo channel 3
        self._sch4: int = 0  # servo channel 4
        self._sch5: int = 0  # servo channel 5
        self._sch6: int = 0  # servo channel 6
        self._sch7: int = 0  # servo channel 7
        self._sch8: int = 0  # servo channel 8
        self._sch9: int = 0  # servo channel 9

        self._coX: int = 0  # compas x
        self._coY: int = 0  # compas y
        self._coZ: int = 0  # compas z

        self._gyX: int = 0  # gyroscope x
        self._gyY: int = 0  # gyroscope y
        self._gyZ: int = 0  # gyroscope z

        self._acX: int = 0  # accelerometer x
        self._acY: int = 0  # accelerometer y
        self._acZ: int = 0  # accelerometer z

        self._tmp: int = 0  # temperature
        self._dist: int = 0  # distance
        self._battery: int = 0  # battery level

        self._mood: str = "void"

        self._errors: list = []

    def get_current_telemetry(self) -> list:
        return [f"{param}:{getattr(self, param)}" for param in self._params_list]

    @property
    def rwS(self):
        return self._rwS

    @rwS.setter
    def rwS(self, value):
        self._rwS = value

    @property
    def lwS(self):
        return self._lwS

    @lwS.setter
    def lwS(self, value):
        self._lwS = value

    @property
    def sch0(self):
        return self._sch0

    @sch0.setter
    def sch0(self, value):
        self._sch0 = value

    @property
    def sch1(self):
        return self._sch1

    @sch1.setter
    def sch1(self, value):
        self._sch1 = value

    @property
    def sch2(self):
        return self._sch2

    @sch2.setter
    def sch2(self, value):
        self._sch2 = value

    @property
    def sch3(self):
        return self._sch3

    @sch3.setter
    def sch3(self, value):
        self._sch3 = value

    @property
    def sch4(self):
        return self._sch4

    @sch4.setter
    def sch4(self, value):
        self._sch4 = value

    @property
    def sch5(self):
        return self._sch5

    @sch5.setter
    def sch5(self, value):
        self._sch5 = value

    @property
    def sch6(self):
        return self._sch6

    @sch6.setter
    def sch6(self, value):
        self._sch6 = value

    @property
    def sch7(self):
        return self._sch7

    @sch7.setter
    def sch7(self, value):
        self._sch7 = value

    @property
    def sch8(self):
        return self._sch8

    @sch8.setter
    def sch8(self, value):
        self._sch8 = value

    @property
    def sch9(self):
        return self._sch9

    @sch9.setter
    def sch9(self, value):
        self._sch9 = value

    @property
    def coX(self):
        return self._coX

    @coX.setter
    def coX(self, value):
        self._coX = value

    @property
    def coY(self):
        return self._coY

    @coY.setter
    def coY(self, value):
        self._coY = value

    @property
    def coZ(self):
        return self._coZ

    @coZ.setter
    def coZ(self, value):
        self._coZ = value

    @property
    def gyX(self):
        return self._gyX

    @gyX.setter
    def gyX(self, value):
        self._gyX = value

    @property
    def gyY(self):
        return self._gyY

    @gyY.setter
    def gyY(self, value):
        self._gyY = value

    @property
    def gyZ(self):
        return self._gyZ

    @gyZ.setter
    def gyZ(self, value):
        self._gyZ = value

    @property
    def acX(self):
        return self._acX

    @acX.setter
    def acX(self, value):
        self._acX = value

    @property
    def acY(self):
        return self._acY

    @acY.setter
    def acY(self, value):
        self._acY = value

    @property
    def acZ(self):
        return self._acZ

    @acZ.setter
    def acZ(self, value):
        self._acZ = value

    @property
    def tmp(self):
        return self._tmp

    @tmp.setter
    def tmp(self, value):
        self._tmp = value

    @property
    def dist(self):
        return self._dist

    @dist.setter
    def dist(self, value):
        self._dist = value

    @property
    def battery(self):
        return self._battery

    @battery.setter
    def battery(self, value):
        self._battery = value

    @property
    def mood(self):
        return self._mood

    @mood.setter
    def mood(self, value):
        self._mood = value

    @property
    def errors(self):
        return self._errors

    @errors.setter
    def errors(self, value):
        self._errors.append(value)

    @errors.deleter
    def errors(self):
        self._errors.clear()
