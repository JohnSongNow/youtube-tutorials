import unittest
import voting as voting


class TestVotingDemo(unittest.TestCase):


    def test_ftfp(self):
        voters = []
        voters.append([4, 3, 0, 2, 1])
        voters.append([4, 1, 3, 0, 2])
        voters.append([4, 0, 2, 3, 1])
        voters.append([1, 4, 0, 2, 3])
        voters.append([3, 2, 0, 4, 1])
        voters.append([2, 1, 3, 0, 4])
        winner = voting.compute_ftfp(voters)
        self.assertEqual(winner, 1)
        

    def test_borda_count(self):
        voters = []
        voters.append([4, 3, 0, 2, 1])
        voters.append([4, 1, 3, 0, 2])
        voters.append([4, 0, 2, 3, 1])
        voters.append([1, 4, 0, 2, 3])
        voters.append([3, 2, 0, 4, 1])
        voters.append([2, 1, 3, 0, 4])
        winner = voting.compute_borda_count(voters)
        self.assertEqual(winner, 1)


    def test_instant_runoff(self):
        voters = []
        voters.append([3, 2, 1, 0])
        voters.append([3, 0, 2, 1])
        voters.append([0, 3, 2, 1])
        voters.append([0, 3, 1, 2])
        voters.append([0, 1, 2, 3])
        voters.append([1, 0, 2, 3])
        voters.append([1, 2, 0, 3])
        winner = voting.compute_instant_runoff(voters)
        self.assertEqual(winner, 1)


if __name__ == '__main__':
    unittest.main()