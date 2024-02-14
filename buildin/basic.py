from buildin.chrome import ChromeList

class Trash_Parce:
    
    @staticmethod
    def check_if_any_in_str(lis: list, st: str):
        
        for i in lis:
            if i in st:
                return True
        return False
    
    @staticmethod
    def check_if_all_in_str(lis: list, st: str):
        for i in lis:
            if type(i) is list:
                if not Trash_Parce.check_if_any_in_str(i, st):
                    return False
                else:
                    if i not in st:
                        return False  
            return True
        
def chrome_code(query):
    for _, lists in ChromeList.items():
        A = Trash_Parce.check_if_all_in_str(lists, query)
        if A:
            return _
    return False