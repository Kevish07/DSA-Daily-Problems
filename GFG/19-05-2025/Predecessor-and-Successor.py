class Solution:
    def InOrder(self,root,ans):
        if not root:
            return
        self.InOrder(root.left,ans)
        ans.append(root)
        self.InOrder(root.right,ans)
    def findPreSuc(self, root, key):
        ans=[]
        self.InOrder(root,ans)
        p,n=None,None
        for i,v in enumerate(ans):
            if v.data==key:
                if i-1>=0 and i-1<len(ans):
                    p=ans[i-1]
                if i+1<len(ans) and i+1>=0:
                    n=ans[i+1]
                break
            elif v.data>key:
                n=ans[i]
                if i-1>=0:
                    p=ans[i-1]
                break
        else:
            p=ans[i]
        return [p,n]