class Robot:
    def __init__(self, name, speed, job):
        self.name = name
        self.speed = speed
        self.job = job

    def clean_room(self, time):
        robot_time = time/self.speed
        return robot_time

    def get_name(self):
        return self.name

    def get_job(self):
        return self.job
