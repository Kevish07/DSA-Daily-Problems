class Solution:
    def colorTheGrid(self, m: int, n: int) -> int:
        
        def encode(colors):
            result = 0
            for i in range(len(colors)):
                result += colors[i] * (3 ** i)
            return result
        
        def decode(value):
            result = []
            while value > 0:
                result.append(value % 3)
                value //= 3
            while len(result) < m:
                result.append(0)
            return result
   
        def isValid(color1, color2):
            if color1 == color2:
                return False
            color1_list = decode(color1)
            color2_list = decode(color2)
            
            for i in range(len(color1_list)):
                if color1_list[i] == color2_list[i]:
                    return False
            return True  

        def isValidColor(color):
            color_list = decode(color)
            for i in range(len(color_list) - 1):
                if color_list[i] == color_list[i + 1]:
                    return False
            return True

        max_color = 3 ** m
        dp = [[0] * max_color for _ in range(n)]
       
      
        # Precompute the valid colors for mapping
        valid_colors = []
        for color in range(max_color):
            if isValidColor(color):
                valid_colors.append(color)
        
        # Precompute the valid colors for each color
        valid_colors_map = {vc: [] for vc in valid_colors}
        for i in range(len(valid_colors)):
            color1 = valid_colors[i]
            for j in range(i + 1, len(valid_colors)):
                color2 = valid_colors[j]
                if isValid(color1, color2):
                    valid_colors_map[color1].append(color2)
                    valid_colors_map[color2].append(color1)
        
      
        # Initialize the first row of the dp array with 1
        for color in valid_colors:
            dp[0][color] = 1

        # Fill the dp array
        for i in range(1, n):
            for color in valid_colors:
                for next_color in valid_colors_map[color]:
                    dp[i][next_color] = (dp[i][next_color] + dp[i - 1][color]) % (10 ** 9 + 7)

        return sum(dp[n - 1][color] for color in valid_colors) % (10 ** 9 + 7)