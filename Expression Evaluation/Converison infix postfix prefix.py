def check_precedence(v1,v2):
    precedence={"-":1,"+":1,"/":2,"*":2,"^":3}
    if v2 is '(':
        return True
    '''
    for i in range(len(precedence)):
        if precedence[i] is v1:
            count1=i
        if precedence[i] is v2:
            count2=i
            '''
    count1=precedence[v1]
    count2=precedence[v2]
    if count1 > count2:
        return True
    else:
        return False
class stack:
    def __init__(self):
        self.stlist=[]
        self.top=-1
        self.pk=''
    def push(self,data):
        self.stlist.append(data)
        self.top+=1
    def pop(self):
        self.top-=1
        item=self.stlist.pop()
        return item
    def peak(self):
        return self.stlist[self.top]
    def empty(self):
        count=0
        for y in self.stlist:
            count+=1
        if count is 0:
            return True
        else:
            return False
    def display(self):
        for i in self.stlist:
            print(i,end=' ')
        print()
class infix_to_postfix:
    def __init__(self,expression="0"):
        self.exp=expression
        self.operator=stack()
        self.operand=stack()
        self.postfix=""
    def check_exp(self):
        lenofexp=len(self.exp)
        for i in self.exp:
            lenofexp-=1
            res=i.isalpha()
            if res is False:
                if i is '(':
                    self.operator.push(i)
                elif i is ')':
                    while self.operator.stlist[self.operator.top] is not '(':
                        self.operand.push(self.operator.pop())
                    
                    self.operator.pop()
                else:
                    if self.operator.empty() is True:
                        self.operator.push(i)
                    elif check_precedence(i,self.operator.stlist[self.operator.top]) is True:
                        
                        self.operator.push(i)
                    else:
                        while self.operator.empty() is False and self.operator.stlist[self.operator.top] is not '(' :
                            self.operand.push(self.operator.pop())
                        self.operator.push(i)
            elif res is True:
                self.operand.push(i)
        if lenofexp is 0 and self.operator.empty() is False:
            while self.operator.empty() is False:
                self.operand.push(self.operator.pop())
    def convert(self):
        for x in self.operand.stlist:
            self.postfix+=x
        return self.postfix
    def print_exp(self):
        print("Infix : ",self.exp)
        print("Postfix: ",self.convert())
class infix_to_prefix:
    def __init__(self,expression="0"):
        self.exp=expression
        self.exp1=expression
        self.prefix=""
    def check_exp(self):

        '''
        #Manual method for reversing string with brackets
        for i in range(len(self.exp)):
            if self.exp[i] is '(':
                self.exp=self.exp[:i] + ')' + self.exp[i+1:]
            elif self.exp[i] is ')':
                self.exp=self.exp[:i] + '(' + self.exp[i+1:]
        
        self.exp=self.exp[::-1]
        '''

        
        self.exp=self.exp[::-1]
        self.exp=self.exp.replace("(","&")
        self.exp=self.exp.replace(")","(")
        self.exp=self.exp.replace("&",")")

        
        ex=infix_to_postfix(self.exp)
        ex.check_exp()
        self.prefix=ex.convert()
        self.prefix=self.prefix[::-1]
    def print_exp(self):
        print("Infix : ",self.exp1)
        print("Prefix: ",self.prefix)

def main():
    #expression=input("Enter the expression: ")
    
    expression="(a*(b+c))-(d/e)"
    
    
    print("Conversion into POstfix")
    intopost=infix_to_postfix(expression)
    intopost.check_exp()
    intopost.print_exp()
    print("Conversion into Prefix")
    intopre=infix_to_prefix(expression)
    intopre.check_exp()
    intopre.print_exp()
main()
