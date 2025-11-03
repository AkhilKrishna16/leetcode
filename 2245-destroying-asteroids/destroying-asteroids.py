class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        # grab all the smallest possible values first by sorting 
        # then add the sum and if mass is there, take it 

        asteroids = sorted(asteroids)
        for asteroid in asteroids:
            if asteroid <= mass:
                mass += asteroid
            else:
                return False
        return True