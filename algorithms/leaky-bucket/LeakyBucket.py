'''
Implementation of Leaky Bucket traffic shaping algorithm as described in 
"Tanenbaum Computer Networks 5ed" chapter 5.4.2.
'''


class LeakyBucket:

    def __init__(self, B:int, R:int) -> None:
        ''' B - Bucket max capacity
            R - Bucket flow rate
        '''

        self._B: int = B
        self._R: int = R

        self._current_bucket_level: int = 0
        self._last_update_time: int = 0


    def GetCurrentBucketLevel(self) -> int:
        return self._current_bucket_level


    def GetBucketAvailableCapacity(self) -> int:
        return self._B - self._current_bucket_level


    def Update(self, ammount_of_data: int, time: int) -> int:
        
        if  self._last_update_time == 0:
             self._last_update_time = time

        dt = time - self._last_update_time
        
        self._current_bucket_level = self._current_bucket_level - dt * self._R

        if self._current_bucket_level < 0:
            self._current_bucket_level = 0

        available_capacity: int = self.GetBucketAvailableCapacity()

        if  available_capacity >=  ammount_of_data:
            # There is enough capacity for all the requested data

            self._current_bucket_level = self._current_bucket_level + ammount_of_data

            return ammount_of_data

        else:
            # There is not enough capacity for all the data

            self._current_bucket_level = self._B

            return available_capacity