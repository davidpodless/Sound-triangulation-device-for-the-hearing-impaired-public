import math

SPEED_OF_SOUND = 343.
D = 0.0457
PI = math.pi
MOD_2_PI = 2*PI
NOISE_CANCELING = 0

SAMPLE_RATE = 48000
CHUNK = 1024
NUM_OF_SNAPSHOTS_FOR_MUSIC = 16
NUM_OF_MICS = 4
RECORD_SECONDS = 10
RECORD_BUFFER_MAX = (SAMPLE_RATE * RECORD_SECONDS) // CHUNK

THRESHOLD_FOR_MODE = (NUM_OF_SNAPSHOTS_FOR_MUSIC // 2) + 1
THRESHOLD_FOR_MUSIC_PEAK = 0
THRESHOLD_FOR_EIGENVALUES = 1

NUM_OF_DIRECTIONS = 72
ANGLE_OF_DIRECTIONS = 360 / NUM_OF_DIRECTIONS

LEN_OF_AVG = 480 * RECORD_SECONDS