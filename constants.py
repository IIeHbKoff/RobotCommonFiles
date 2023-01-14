class Constants:
    MAX_WHEEL_VALUE: int = 100
    MIN_WHEEL_VALUE: int = -100
    WHEEL_ACCELERATION = 0  # points in second
    MAX_SERVO_ANGLE: int = 180
    MIN_SERVO_ANGLE: int = 0
    SERVO_ACCELERATION = 0  # point in seconds

    MOVEMENT_SKILL_TAG = "mws"
    FACE_VIEWER_SKILL_TAG = "fvs"
    SERVO_SKILL_TAG = "sds"
    SERVOS_CHANNELS = {
        0: {"name": "sch0", "is_inverted": False},
        1: {"name": "sch1", "is_inverted": False},
        2: {"name": "sch2", "is_inverted": True}
    }
    REDIS_HOST = "192.168.0.110"
    REDIS_PORT = 6379
    REDIS_TIMEOUT = 3000
    REDIS_CMD_KEY = "cmd"
    REDIS_TELEMETRY_KEY = "telemetry"

    WINDOW_WIDTH = 1920
    WINDOW_HEIGHT = 1080
    WINDOW_FPS = 60

    WIFI_SSID = 'A1-28-84_2.4Ghz'
    WIFI_PASSWORD = '80736338'
