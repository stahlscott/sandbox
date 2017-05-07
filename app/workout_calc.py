import math

DEADLIFT_MAX = 200
SQUAT_MAX = 200
BENCH_MAX = 200
CLOSE_GRIP_BENCH_MAX = 200

from collections import namedtuple
LiftTuple = namedtuple('LiftTuple', ['name', 'weight'])

class WorkoutCalculator():
    def __init__(self):
        pass

    def get_deadlift(self, reps):
        weight = DEADLIFT_MAX / reps
        return weight

    def get_squat(self, reps):
        weight = DEADLIFT_MAX / reps
        return weight

    def get_bench(self, reps):
        weight = DEADLIFT_MAX / reps
        return weight

    def get_close_grip_bench(self, reps):
        weight = DEADLIFT_MAX / reps
        return weight

    def get_workout(self, multiplier=1):
        deadlift_weight = math.ceil(DEADLIFT_MAX*multiplier)
        squat_weight = math.ceil(SQUAT_MAX*multiplier)
        bench_weight = math.ceil(BENCH_MAX*multiplier)
        cg_bench_weight = math.ceil(CLOSE_GRIP_BENCH_MAX*multiplier)

        deadlift = LiftTuple(name='Deadlift', weight=deadlift_weight)
        squat = LiftTuple(name='Squat', weight=squat_weight)
        bench = LiftTuple(name='Bench', weight=bench_weight)
        cg_bench = LiftTuple(name='Close Grip Bench', weight=cg_bench_weight)
        return [deadlift, squat, bench, cg_bench]
