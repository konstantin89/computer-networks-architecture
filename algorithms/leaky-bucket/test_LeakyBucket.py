import unittest
from LeakyBucket import LeakyBucket

class TestLeakyBucket(unittest.TestCase):

    def test_basic(self):

        bucket = LeakyBucket(B=10, R=1)
        self.assertEqual(bucket.GetBucketAvailableCapacity(), 10)

        data_used = bucket.Update(ammount_of_data=1, time=0)
        self.assertEqual(data_used, 1)
        self.assertEqual(bucket.GetBucketAvailableCapacity(), 9)


    def test_basic_leak_rate(self):

        bucket = LeakyBucket(B=10, R=1)

        data_used = bucket.Update(ammount_of_data=10, time=0)
        self.assertEqual(data_used, 10)
        self.assertEqual(bucket.GetBucketAvailableCapacity(), 0)

        data_used = bucket.Update(ammount_of_data=0, time=1)
        self.assertEqual(data_used, 0)
        self.assertEqual(bucket.GetBucketAvailableCapacity(), 1)




if __name__ == '__main__':
    unittest.main()