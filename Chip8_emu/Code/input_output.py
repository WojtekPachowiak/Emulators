import numpy as np

class InputOutput:
    keys = np.zeros(16, dtype = np.uint8)
    keys_last_frame = np.zeros(16, dtype = np.uint8)

    waiting_for_input = False



io = InputOutput
