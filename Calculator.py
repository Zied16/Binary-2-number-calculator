from tkinter import*

def binaryAddition(A,B):
    while(len(A)>len(B)):
        B='0'+B
    while(len(A)<len(B)):
        A='0'+A
    A=list(A[::-1])
    B=list(B[::-1])
    A=[int(x) for x in A]
    B=[int(x) for x in B]
    C=''
    D=[0 for i in range(len(A))]
    for i in range(len(A)):
        if (A[i]+B[i]+D[i])>1:
            if (A[i]+B[i]+D[i])==2:
                D[i]=0
                m=1
            if (A[i]+B[i]+D[i])>2:
                D[i]=1
                m=1
        elif (A[i]+B[i]+D[i])==1:
            D[i]=1
            m=0
        else:
            D[i]=0
            m=0
        if i+1 in range(len(D)):
                D[i+1]=m+D[i+1]
        elif m!=0:
            D.append(m)
    D=D[::-1]
    for i in range(len(D)):
        C+=str(D[i])
    
    return C

def binarySubstraction(a,b):
    while(len(a)>len(b)):
        b='0'+b
    while(len(a)<len(b)):
        a='0'+a
    a=list(a)
    a=[int(x) for x in a]
    for i in range(len(a)):
        if a[i]==0:
            a[i]=1
        elif a[i]==1:
            a[i]=0
    a=a[::-1]
    s7=''
    s8=[0 for i in range(len(a))]
    s5='1'
    while(len(s5)<len(a)):
        s5='0'+s5
    s5=list(s5)
    s5=[int(x) for x in s5]          
    for i in range(len(a)):
        if a[i]+s5[i]+s8[i]>1:
            if (a[i]+s5[i]+s8[i])==2:
                s8[i]=0
                k=1
            if (a[i]+s5[i]+s8[i])>2:
                s8[i]=1
                k=1
        elif (a[i]+s5[i]+s8[i])==1:
            s8[i]=1
            k=0
        else:
            s8[i]=0
            k=0
        if i+1 in range(len(s8)):
                s8[i+1]=k+s8[i+1]
        elif k!=0:
            s8.append(k)
    s8=s8[::-1]
    for i in range(len(s8)):
        s7+=str(s8[i])
    print(s7)
    return(binaryAddition(s7,b))
    
    
def iCalc(source, side):
    storeObj = Frame(source, borderwidth=4, bd=4,bg="powder blue")
    storeObj.pack(side=side, expand=YES, fill=BOTH)
    return storeObj

def button(source, side, text, command=None):
    storeObj = Button(source, text=text, command=command)
    storeObj.pack(side=side, expand=YES, fill=BOTH)
    return storeObj

class app(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.option_add('*Font','arial 20 bold')
        self.pack(expand=YES, fill=BOTH)
        self.master.title('Binary Calculator')


        display = StringVar()
        Entry(self, relief=RIDGE,
              textvariable=display,justify='right',
              bd=30,bg="powderblue").pack(side=TOP,expand=YES,fill=BOTH)
        for clearBut in (["CE"],["C"]):
            erase = iCalc(self,TOP)
            for ichar in clearBut:
                button(erase, LEFT, ichar,
                       lambda storeObj=display, q=ichar: storeObj.set(''))
        for NumBut in ("01", "-+"):
            FunctionNum = iCalc(self, TOP)
            for char in NumBut:
                button(FunctionNum, LEFT, char,
                       lambda storeObj=display,q=char:storeObj.set(storeObj.get()+q))
        EqualsButton = iCalc(self,TOP)
        for iEquals in "=":
            if iEquals== "=":
                btniEquals = button(EqualsButton , LEFT , iEquals)
                btniEquals.bind('<ButtonRelease-1>',
                                lambda e,s=self,
                                storeObj=display: s.calc(storeObj), '+')
            else:
                btniEquals= button(EqualsButton, LEFT, iEquals,
                                   lambda storeObj=display,
                                   s=' %s '%iEquals:storeObj.set(storeObj.get()+s))
    def calc(self,display):
        try:
            ch=display.get()
            if '+' in ch:
                s1=ch[0:ch.find('+')]
                s2=ch[(ch.find('+')+1):]
                display.set(binaryAddition(s1,s2))
            elif '-' in ch:
                s1=ch[0:ch.find('-')]
                s2=ch[0:ch.find('-')]
                display.set(binarySubstraction(s1,s2))
        except:
            display.set("ERROR")

if __name__=='__main__':
    app().mainloop()
