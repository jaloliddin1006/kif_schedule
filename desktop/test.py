# class Solution:
#     def letterCombinations(self, digits: str):
#         self.source={
#                 '2':['a', 'b', 'c'],
#                 '3':['d', 'e', 'f'],
#                 '4':['g', 'h', 'i'],
#                 '5':['j', 'k', 'l'],
#                 '6':['m', 'n', 'o'],
#                 '7':['p', 'q', 'r', 's'],
#                 '8':['t', 'u', 'v'],
#                 '9':['w', 'x', 'y', 'z']
#             }
        
#         res = self.letters(nums=list(digits))
#         return res
        
#     def letters(self, nums, res=[]):
#         print(nums, res)
#         res = res
#         if not nums:
#             return res
        
#         if not res:
#             res = self.source[nums[0]]
#         else:
        
#             temp = []
#             for i in self.source[nums[0]]:
#                 for j in res:
#                     temp.append(j+i)
#             res = temp   
       
        
#         nums.pop(0)
#         return self.letters(nums, res)
        
            


# s = '234'
# program = Solution()

# print(program.letterCombinations(s))
# # c = ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# # b = ["adg","adh","adi","aeg","aeh","aei","afg","afh","afi","bdg","bdh","bdi","beg","beh","bei","bfg","bfh","bfi","cdg","cdh","cdi","ceg","ceh","cei","cfg","cfh","cfi"]
# # a = ["adp","adq","adr","ads","aep","aeq","aer","aes","afp","afq","afr","afs","bdp","bdq","bdr","bds","bep","beq","ber","bes","bfp","bfq","bfr","bfs","cdp","cdq","cdr","cds","cep","ceq","cer","ces","cfp","cfq","cfr","cfs"]
# # e = ["jpw","jpx","jpy","jpz","jqw","jqx","jqy","jqz","jrw","jrx","jry","jrz","jsw","jsx","jsy","jsz","kpw","kpx","kpy","kpz","kqw","kqx","kqy","kqz","krw","krx","kry","krz","ksw","ksx","ksy","ksz","lpw","lpx","lpy","lpz","lqw","lqx","lqy","lqz","lrw","lrx","lry","lrz","lsw","lsx","lsy","lsz"]
# # print(len(a)) # 237
# # print(len(b)) # 234
# # print(len(c)) # 23
# # print(len(e)) # 579
# # a.sort()
# # print(a)

