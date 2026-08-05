class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False
        elif len(matrix) == 1:
            row_number: int = 0
        else:
            up, down = 0, len(matrix) - 1
            while up < down:
                middle: int = (up + down)//2
                if down - up <= 1:
                    if matrix[up][-1] == target:
                        return True
                    elif matrix[up][-1] > target:
                        row_number = up
                        break
                    else:
                        row_number = down
                        break
                else:
                    if matrix[middle][-1] == target:
                        return True
                    elif matrix[middle][-1] < target:
                        up = middle
                    else:
                        down = middle
        row = matrix[row_number]
        left, right = 0, len(row) - 1
        while left <= right:
            middle: int = (left + right)//2
            if row[middle] == target:
                return True
            elif row[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        return False