
# Solution - Dynamic Programming Tabulation

class GraduationAttendanceCalculator:
    max_consective_miss = 4

    # n - no. of days
    def __init__(self, n):
        self.n = n
        

    def calculate(self):
        """
        Dynamic Progamming Tabulation
        """

        if self.n < self.max_consective_miss or self.n < 0 or self.max_consective_miss < 0:
            raise Exception("Incorrect Inputs")


        n, m = self.n, self.max_consective_miss
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(m):
            dp[0][i] = 1

        for i in range(1, n + 1):
            for j in range(m - 1, -1, -1):
                dp[i][j] = dp[i - 1][0] + dp[i - 1][j + 1]

        no_of_ways_to_attend = dp[n][0]  # correct way to attend classes
        no_of_ways_to_miss = dp[n - 1][1]  # ways to miss last day

        return f"{no_of_ways_to_miss}/{no_of_ways_to_attend}"


if __name__ == "__main__":
    no_of_days = input('No. of days: ')
    calculator = GraduationAttendanceCalculator(int(no_of_days))
    print(calculator.calculate())
    

