class Solution:

    def nthRowOfPascalTriangle(self, n):
        if n == 1:
            return [1]

        prev_row = self.nthRowOfPascalTriangle(n - 1)
        
        row = [1]
        for i in range(1, len(prev_row)):
            row.append(prev_row[i - 1] + prev_row[i])
        row.append(1)
        
        return row
    