class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1,n+1):
            fizz = '' if i % 3 else 'Fizz'
            buzz = '' if i % 5 else 'Buzz'
            if fizz or buzz:
                res.append(''.join((fizz,buzz)))
            else:
                res.append(str(i))
        return res
        