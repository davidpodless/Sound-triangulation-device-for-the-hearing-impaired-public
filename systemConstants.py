import math

SPEED_OF_SOUND = 343.
D = 0.0457
PI = math.pi
MOD_2_PI = 2*PI
NOISE_CANCELING = 0

SAMPLE_RATE = 48000
CHUNK = 512
NUM_OF_SNAPSHOTS_FOR_MUSIC = 16
NUM_OF_MICS = 4
RECORD_SECONDS = 5
RECORD_BUFFER_MAX = (SAMPLE_RATE * RECORD_SECONDS) // CHUNK

RATE_OF_AVERAGING = RECORD_SECONDS / (CHUNK * NUM_OF_SNAPSHOTS_FOR_MUSIC / (SAMPLE_RATE ))

THRESHOLD_FOR_MODE = (NUM_OF_SNAPSHOTS_FOR_MUSIC // 2) + 2

NUM_OF_DIRECTIONS = 360
ANGLE_OF_DIRECTIONS = 360 / NUM_OF_DIRECTIONS
