DEADLIFT_MAX = 200
SQUAT_MAX = 200
BENCH_MAX = 200
CLOSE_GRIP_BENCH_MAX = 200


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

