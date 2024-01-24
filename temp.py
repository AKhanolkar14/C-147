print("hello world")
a=100
print(type(a))
city= 'Pune'
print(type(city))
super_heroes= ["Superman", "Spiderman", "Batman"]
print(type(super_heroes))

from tkinter import*
root= Tk()
root.title("Addition")
root.geometry("400x200")
root.mainloop()
from tkinter import *
root= Tk()
root.title("Fibonacci")
root.geometry("400x400")
root.mainloop()

label_series= Label(root,text="Fibonacci Series:")
label_flower= Label(root)
label_spiral= Label(root)

def Fibonacci():
    num=10
    first_no=0
    second_no= 1
    sum= 0
    counter=1
while(counter <= num):
        label_series["text"]+=str(sum)+" "
        counter= counter+1
        first_no= second_no
        second_no= sum
    sum= first_no+ second_no
    label_flower['text']= "Flower is fully bloomed"
    label_spiral['text']= "Spirals in right direction are"+
    str(first_no)+"and spirals in left dirction are"+ str(second_no)+"\n,Total spiral are"+ str(sum)
    btn= button(root,text="Show Fibonacci Series", command= Fibonacci)
    btn.pack()
        label_series.pack()
        label_flower.pack()
        label_spiral.pack()
        root.mainloop
        
        root=tk()
        root.title("Ascii")
        root.geometry("400x400")
        root.configure(background='snow')
        
        enter_word= Entry(root)
        enter_word.place(relx= 0.5, rely= 0.4,anchor= CENTER)
        
        label= Label(root, text= "Namein Ascii:", bg="light yellow", fg="black")
        def asciiConverter():
            input_word= enter_word.get()
            for letter in input_word:
                label["text"]+= str(ord(letter))+""
btn= Button(root, text="Show namein Ascii", command= asciiConverter, bg= 'gold', fg='black')
btn.place(relx= 0.5, rely= 0.5,anchor= CENTER)
label.place(relx= 0.5, rely= 0.6,anchor= CENTER)
        root.mainloop()