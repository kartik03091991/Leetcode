class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        #length = 1000 
        #width = 35 
        #height = 700 
        #mass = 300
        
        #length = 200 
        #width = 50 
        #height = 800 
        #mass = 50
        
        # box is bulky
        volume = (length * width * height)
        lst1 = []
        a = 10**4
        b = 10**9
        
        lst2 = []
        
        if length >= a or width >= a or height >= a :
            lst2.append(True)
        else:
            lst2.append(False)
        
        
        if any(lst2) or (volume >= b):
            lst1.append("Bulky")
            
        # if box is Heavy
        
        if mass >= 100:
            lst1.append('Heavy')
            
        # check if box is bulky , heavy , both , neither
        
        if ('Bulky' in lst1) and ('Heavy' in lst1):
            return('Both')
        elif ('Bulky' not in lst1) and ('Heavy' not  in lst1):
            return('Neither')
        elif ('Bulky' in lst1) and ('Heavy' not in lst1):
            return('Bulky')
        elif ('Bulky' not  in lst1) and ('Heavy' in lst1):
            return('Heavy')
        else:
            pass
            
            
            