'''
Implementation of Token Bucket traffic shaping algorithm as described in 
"Tanenbaum Computer Networks 5ed" chapter 5.4.2.
'''


class TokenBucket:

    def __init__(self, B:int, R:int) -> None:
        ''' B - Bucket max token capacity
            R - Token refill rate
        '''

        self._B: int = B
        self._R: int = R

        self._current_bucket_tokens: int = self._B
        self._last_update_time: int = 0


    def GetAvailableTokens(self) -> int:
        return self._current_bucket_tokens


    def Update(self, ammount_of_data: int, time: int) -> int:
        
        if  self._last_update_time == 0:
             self._last_update_time = time

        dt = time - self._last_update_time
        
        self._current_bucket_tokens = self._current_bucket_tokens + dt * self._R

        if self._current_bucket_tokens > self._B:
            self._current_bucket_tokens = self._B

        available_tokens: int = self.GetAvailableTokens()

        # Save the timestamp of the last update
        self._last_update_time = time

        if  available_tokens >=  ammount_of_data:
            # There is enough capacity for all the requested data

            self._current_bucket_tokens = self._current_bucket_tokens - ammount_of_data

            return ammount_of_data

        else:
            # There is not enough capacity for all the data

            self._current_bucket_tokens = 0

            return available_tokens