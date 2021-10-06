"""
ExecutionTime
This class is used to get the execution time of a code.
"""

import time
import random

class ExecutionTime:
    def __init__(self):
        self.start_time = time.time()

    def duration(self):
        return time.time() - self.start_time

