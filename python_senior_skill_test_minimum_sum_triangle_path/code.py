
def MinimumSumPathTriangle(triangle):
      for length in range(len(triangle)-2,-1,-1):
        for index in range(len(triangle[length])):
          triangle[length][index] += min(triangle[length+1][index],triangle[length+1][index+1])
          
      print(triangle)
      return triangle[0][0]

