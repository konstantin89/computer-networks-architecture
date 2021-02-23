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

        # Fill the bucket to the max camapicy
        data_used = bucket.Update(ammount_of_data=10, time=1)
        self.assertEqual(data_used, 10)
        self.assertEqual(bucket.GetBucketAvailableCapacity(), 0)

        # Make sure the after one time unit, exactly R data run out of the bucket.
        data_used = bucket.Update(ammount_of_data=0, time=2)
        self.assertEqual(data_used, 0)
        self.assertEqual(bucket.GetBucketAvailableCapacity(), 1)

        # Make sure the long period, the bucket is empty.
        data_used = bucket.Update(ammount_of_data=0, time=100)
        self.assertEqual(data_used, 0)
        self.assertEqual(bucket.GetBucketAvailableCapacity(), 10)


    def test_use_more_than_max_camacity(self):

        bucket = LeakyBucket(B=10, R=1)

        # Make sure that we can't fill the bucket more than B.
        data_used = bucket.Update(ammount_of_data=100, time=1)
        self.assertEqual(data_used, 10)
        self.assertEqual(bucket.GetBucketAvailableCapacity(), 0)


    def test_fill_bucket_with_rate_smaller_than_R(self):

        bucket = LeakyBucket(B=10, R=2)
        
        # We fill bucket in rate 1 data per second, 
        for i in range(1, 100):
            data_used = bucket.Update(ammount_of_data=1, time=i)
            self.assertEqual(data_used, 1)


    def test_fill_bucket_with_rate_larger_than_R(self):

        bucket = LeakyBucket(B=10, R=1)
        data_used_sum: int = 0

        # Start with full bucket
        data_used = bucket.Update(ammount_of_data=100, time=1)
        self.assertEqual(data_used, 10)
        self.assertEqual(bucket.GetBucketAvailableCapacity(), 0)

        # We fill bucket in rate 2 data per second, while R is 1 data per second
        for i in range(2, 12):
            data_used_sum += bucket.Update(ammount_of_data=2, time=i)

        # total data used: dt * R = 10 * 1  = 10
        self.assertEqual(data_used_sum, 10)


if __name__ == '__main__':
    unittest.main()