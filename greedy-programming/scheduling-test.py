import unittest
import scheduling as scheduling

class SchedulingDemo(unittest.TestCase):


    def test_job_scheduling(self):
        jobs = [[0, 3, 50], [1, 5, 50], [2, 5, 90], [3, 5, 50], 
            [4, 4, 80], [5, 3, 40], [6, 1, 30], [7, 3, 40], [8, 4, 40], 
            [9, 3, 30], [10, 3, 60], [11, 4, 60], [12, 5, 60], 
            [13, 4, 60], [14, 4, 20]]

        schedule = scheduling.schedule_jobs(jobs, 6)
        answer = [[1, 5, 50], [14, 4, 20], [9, 3, 30], [5, 3, 40], [6, 1, 30]]

        self.assertEqual(schedule, answer)


    def test_interval_scheduling(self):
        intervals = [[10, 1, 1], [2, 1, 2], [11, 1, 2], [1, 5, 1], 
            [4, 3, 3], [9, 4, 2], [6, 6, 2], [12, 7, 1], 
            [3, 7, 2], [13, 7, 30], [7, 13, 25], [8, 12, 35], 
            [5, 15, 3], [0, 17, 2]]

        schedule = scheduling.schedule_intervals(intervals, 20)
        answer = [[10, 1, 1, 2], [11, 1, 2, 3], [1, 5, 1, 6], [9, 4, 2, 6], 
            [6, 6, 2, 8], [3, 7, 2, 9], [5, 15, 3, 18]]

        self.assertEqual(schedule, answer)

        
if __name__ == '__main__':
    unittest.main()