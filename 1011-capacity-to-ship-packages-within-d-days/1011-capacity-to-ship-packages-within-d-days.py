class Solution:
    def shipWithinDays(self, weights: List[int], days: int):

        def daysToLoadShip(shipCapacity):
            shipCapacityRemaining = shipCapacity
            daysToLoad = 1
            for w in weights:
                if shipCapacityRemaining - w < 0:
                    shipCapacityRemaining = shipCapacity
                    daysToLoad +=1
                    if daysToLoad > days:
                        return sys.maxsize
                shipCapacityRemaining -= w
            return daysToLoad

        l = max(weights)
        r = sum(weights)
        res = sys.maxsize
        while l <= r:
            shipWeight = l + (r-l) //2
            daysToLoad = daysToLoadShip(shipWeight)
            if daysToLoad <= days:
                res = min(res,shipWeight)
                r = shipWeight -1
            else:
                l = shipWeight +1
        return res

        