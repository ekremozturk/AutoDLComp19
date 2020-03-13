# Thomas' comment: not needed anymore, just for lookup purpose

UNBALANCE_RATIO = 3

# symbols
UNEVEN = 'uneven'
MIN_CLASS = 'min_class'
MAX_CLASS = 'max_class'
CLASS_NUM = 'class_num'
EACH_CLASS_NUM = 'each_class_num'
NUM = 'num'
INDEX = 'index'
INDICES = 'indices'
CLASS_INFO = 'each_class_info'
SAMPLE_INFO = "sample_info"
ITER_NUM = 'iter_num'
TRAIN_NUM = 'train_num'
TEST_NUM = 'test_num'

# CONSTANT NUMBER
MAX_SAMPLE_NUM = 3000
MIN_SAMPLE_NUM = 1000
MAX_VALID_PERCLASS_SAMPLE = 200
MAX_VALID_SET_SIZE = 500
MIN_VALID_PER_CLASS = 1

# MODEL HYPER PARAMETERS
MODEL_FIRST_MAX_RUN_LOOP = 3
MODEL_MAX_RUN_LOOP = 20

# Modified by qmc
NUM_MFCC = 96  # num of mfcc features, default value is 24
MAX_AUDIO_DURATION = 5  # limited length of audio, like 20s

FIRST_ROUND_DURATION = 10
MIDDLE_DURATION = 15
SECOND_ROUND_DURATION = 30

IS_CUT_AUDIO = True
AUDIO_SAMPLE_RATE = 16000
MAX_FRAME_NUM = 700
FFT_DURATION = 0.1
HOP_DURATION = 0.04