class Solution:
	def sortArray(self, arr, A, B, C):
		
		def calulate(x,A,B,C):
			fx = (A*(x**2)) + (B*(x)) + (C)
			return fx
		
		ans = []
		for i in range(len(arr)):
			response = calulate(arr[i],A,B,C)
			ans.append(response)
		  
		new = sorted(ans)
		return new