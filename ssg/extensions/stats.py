from ssg import hooks
import time

start_time = None
total_written = 0

@property("start_build")
def start_build():
    global start_time
    