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
        0: {"name": "head_H", "is_inverted": False},
        1: {"name": "right_arm", "is_inverted": False},
        2: {"name": "left_arm", "is_inverted": True}
    }
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379
    REDIS_TIMEOUT = 3000
    REDIS_CMD_KEY = "cmd"
    REDIS_TELEMETRY_KEY = "telemetry"

    WINDOW_WIDTH = 1920
    WINDOW_HEIGHT = 1080
    WINDOW_FPS = 60
