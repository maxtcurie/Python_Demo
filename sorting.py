#From:https://leetcode.com/problems/reorder-data-in-log-files/
logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]

class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        let_count=0
        dig_count=0
        output=['']*len(logs)
        for i in range(len(logs)):
            list_TEMP=logs[i].split(' ')
            try:
                int(list_TEMP[-1])
                output[len(logs)-1-dig_count]=logs[i]
                dig_count=dig_count+1
            except:
                output[let_count]=logs[i]
                let_count=let_count+1
        def sort_fun(e):
            list_TEMP=e.split(' ')
            output=e[len(list_TEMP[0]):]
            return output
        let_list=output[:let_count]
        let_list.sort(key=sort_fun)
        output[:let_count]=let_list

        dig_list=output[len(logs)-dig_count:]
        dig_list.sort(key=sort_fun)
        output[len(logs)-dig_count:]=dig_list
        
        output.sort(key=sort_fun)
        return output

a=Solution()
output=a.reorderLogFiles(logs)
print(output)