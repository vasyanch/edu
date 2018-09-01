class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        busy = [1] * len(people)
        result = [0] * len(people)
        people.sort() #4,4 5,0 5,2 6,1 7,0, 7,1 
        for i in people:
           disp = i[1]
           print(result)
           for ind in range(len(busy)):
               if disp > 0 or busy[ind] != 1:
                   disp -= busy[ind]
               else:
                   
                   break
           busy[ind] = 0
           result[ind] = i 
           
        return result
