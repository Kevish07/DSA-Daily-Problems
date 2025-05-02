#  Best Solution
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        temp = ''
        
        while dominoes != temp:
            temp = dominoes
            dominoes = dominoes.replace('R.L', 'xxx')       
            dominoes = dominoes.replace('R.', 'RR')        
            dominoes = dominoes.replace('.L', 'LL')         

        return  dominoes.replace('xxx', 'R.L')
    


# Force Approach
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n=len(dominoes)
        forces=[0]*n
        force=0
        for i in range(n):
            if dominoes[i]=='R':
                force=n
            elif dominoes[i]=='L':
                force=0
            else:
                force=max(force-1,0)
            forces[i]+=force
        force=0
        for i in range(n-1,-1,-1):
            if dominoes[i]=='L':
                force=n
            elif dominoes[i]=='R':
                force=0
            else:
                force=max(force-1,0)
            forces[i]-=force
        result=[]
        for i in forces:
            if i==0:
                result.append('.')
            elif i>0:
                result.append('R')
            else:
                result.append('L')
        return ''.join(result)