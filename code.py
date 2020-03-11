from tkinter import *
import tkinter.ttk as ttk
import time

i=0
root= Tk()
root.title("Scheduling Simulator")
root.geometry("1020x650+20+20")
root.configure(background="BLACK")

global queue

def InsRead(event):
	global inss
	global arr
	inss = textfield.get(1.0,END).splitlines()
	arr= []
	for i in inss:
		arr.append(i.split(" "))
	print (arr)	

def fcfs(event):
	global arr
	pro=[]
	p=len(arr)
	global names
	global avgtt
	global avgwt
	names=[]
	at=[]
	bt=[]
	rt=[]
	at2=[]
	avgwt=0.0
	avgtt=0.0
	
	for a in arr:
			pro=pro+[a[0]]
			bt=bt+[int(a[2])]
			at=at+[int(a[1])]
			at2=at2+[int(a[1])]
			rt=rt+[int(a[2])]
	remain=p
	t=0
	print(pro)
	print(bt)
	print(at)
	print(rt)
	tat=[0,0,0,0,0,0]
	wt=[0,0,0,0,0,0]
	while(remain!=0):
		x=99999
		#print(remain)
		for i in range(p):
			#print(x)
			if(at2[i]<=t):
				x=rt[i]
		for i in range(p):
			if(rt[i]==x):
				print(t)
				print(pro[i])
				for ad in range(rt[i]):
					names.append(pro[i])
				t=t+rt[i]
				remain=remain-1
				tat[i]=t-at[i]
				wt[i]=t-at[i]-bt[i]
				avgwt=avgwt+t-at[i]-bt[i]
				avgtt=avgtt+t-at[i]
				at2[i]=9999
	print(t)

	print("\n");
	print("***************************************")
	print("Pro\tArTi\tBuTi\tTaTi\tWtTi")
	print("***************************************")
	for i in range(p):
		print(pro[i], end="\t")
		print(at[i], end="\t") 
		print(bt[i] ,end="\t")  
		print(tat[i],end="\t")
		print(wt[i])
	print("***************************************");
	avgwt = avgwt/p;
	avgtt = avgtt/p;
	print("Average Waiting Time : ",end=' ')
	print(avgwt)
	print("Average Turnaround Time : ",end=' ')
	print(avgtt)
	global kk
	kk="In the First come first serve scheduling algorithm, as the name suggests, the process which arrives first, gets executed first."


def sjfnp(event):
	global arr
	pro=[]
	p=len(arr)
	global names
	global avgtt
	global avgwt
	names=[]
	at=[]
	bt=[]
	rt=[]
	at2=[]
	avgwt=0.0
	avgtt=0.0
	
	for a in arr:
			pro=pro+[a[0]]
			bt=bt+[int(a[2])]
			at=at+[int(a[1])]
			at2=at2+[int(a[1])]
			rt=rt+[int(a[2])]
	remain=p
	t=0
	print(pro)
	print(bt)
	print(at)
	print(rt)
	tat=[0,0,0,0,0,0]
	wt=[0,0,0,0,0,0]
	while(remain!=0):
		x=99999
		#print(remain)
		for i in range(p):
			#print(x)
			if(at2[i]<=t and rt[i]<x and rt[i]>0):
				x=rt[i]
		for i in range(p):
			if(rt[i]==x):
				print(t)
				print(pro[i])
				for ad in range(rt[i]):
					names.append(pro[i])
				t=t+rt[i]
				remain=remain-1
				tat[i]=t-at[i]
				wt[i]=t-at[i]-bt[i]
				avgwt=avgwt+t-at[i]-bt[i]
				avgtt=avgtt+t-at[i]
				at2[i]=9999
	print(t)

	print("\n");
	print("***************************************")
	print("Pro\tArTi\tBuTi\tTaTi\tWtTi")
	print("***************************************")
	for i in range(p):
		print(pro[i], end="\t")
		print(at[i], end="\t") 
		print(bt[i] ,end="\t")  
		print(tat[i],end="\t")
		print(wt[i])
	print("***************************************");
	avgwt = avgwt/p;
	avgtt = avgtt/p;
	print("Average Waiting Time : ",end=' ')
	print(avgwt)
	print("Average Turnaround Time : ",end=' ')
	print(avgtt)
	global kk
	kk="Shortest job non premitive is a sheduling algorithm used for decreasing queue filled up with the short processes .So that short jobs get higher priority while execution."

def rr(event):
	global q
	global names
	names=[]
	global arr
	q=4
	#arr=[['p0',2,8],['p1',1,3],['p2',0,5],['p3',3,6]]
	global avgwt
	global avgtt
	avgtt=0.0
	avgwt=0.0
	remain=len(arr)
	p=remain
	pro=[]
	at=[]
	bt=[]
	rt=[]
	tat=[0,0,0,0]
	wt=[0,0,0,0]

	for i in range(p):
		for j in range(i+1,p):
			if(arr[i][1]>arr[j][1]):
				temp=arr[i]
				arr[i]=arr[j]
				arr[j]=temp
	for a in arr:
			pro=pro+[a[0]]
			bt=bt+[int(a[2])]
			at=at+[int(a[1])]
			rt=rt+[int(a[2])]
	#print("AFTER SORT:")
	#print(arr)
	#print(pro)
	#print(at)
	#print(bt)
	#print(rt)
	#print(tat)
	#print(wt)

	print("\n***************************************\n")
	print("Gantt Chart\n")
	print("0")
	time=0
	i=0
	while(remain!=0):
		c=0
		if(int(rt[i])<=q and rt[i]>0):
			time=time+rt[i]
			for c in range(rt[i]):
				names.append(pro[i])
			print(pro[i])
			print(time)
			rt[i]=0
			flag=1
		elif(int(rt[i])>0):
			rt[i]=rt[i]-q;
			time=time+q;
			for c in range(q):
				names.append(pro[i])
			print(pro[i])
			print(time)
		if(int(rt[i])==0 and flag==1):
			remain=remain-1
			tat[i]=time-at[i]
			wt[i]=time-at[i]-bt[i]
			avgwt=avgwt+time-at[i]-bt[i]
			avgtt=avgtt+time-at[i]
			flag=0
		if(i==p-1):
			i=0
		elif(at[i+1]<=time):
			i=i+1
		else:
			i=0

	print("\n");
	print("***************************************")
	print("Pro\tArTi\tBuTi\tTaTi\tWtTi")
	print("***************************************")
	for i in range(p):
		print(pro[i], end="\t")
		print(at[i], end="\t") 
		print(bt[i] ,end="\t")  
		print(tat[i],end="\t")
		print(wt[i])
	print("***************************************");
	avgwt = avgwt/p;
	avgtt = avgtt/p;
	print("Average Waiting Time : ",end=' ')
	print(avgwt)
	print("Average Turnaround Time : ",end=' ')
	print(avgtt)
	print(names)
	global kk
	kk="Round robin can used where every process is of equal priority, so that we give equal quantum of time to each of them each time."


def sjf(event):

	global arr
	p=len(arr)
	global names
	global avgwt
	global avgtt
	names=[]
	pro=[]
	at=[]
	bt=[]
	rt=[]
	at2=[]
	avgwt=0.0
	avgtt=0.0
	tat=[0,0,0,0,0,0]
	wt=[0,0,0,0,0,0]
	for a in arr:
			pro=pro+[a[0]]
			bt=bt+[int(a[2])]
			at=at+[int(a[1])]
			at2=at2+[int(a[1])]
			rt=rt+[int(a[2])]
	remain=p
	t=0
	print(pro)
	print(bt)
	print(at)
	print(rt)
	while(remain!=0):
		x=99999
		#print(remain)
		for i in range(p):
			#print(x)
			if(at2[i]<=t and rt[i]<x):
				x=rt[i]
		for i in range(p):
			if(rt[i]==x):
				print(t)
				print(pro[i])
				names.append(pro[i])
				t=t+1
				rt[i]=rt[i]-1
				if(rt[i]==0):
					remain=remain-1
					tat[i]=t-at[i]
					wt[i]=t-at[i]-bt[i]
					avgwt=avgwt+t-at[i]-bt[i]
					avgtt=avgtt+t-at[i]
					at2[i]=9999
				
				break
			
	print(t)

	print("\n");
	print("***************************************")
	print("Pro\tArTi\tBuTi\tTaTi\tWtTi")
	print("***************************************")
	for i in range(p):
		print(pro[i], end="\t")
		print(at[i], end="\t") 
		print(bt[i] ,end="\t")  
		print(tat[i],end="\t")
		print(wt[i])
	print("***************************************");
	avgwt = avgwt/p;
	avgtt = avgtt/p;
	print("Average Waiting Time : ",end=' ')
	print(avgwt)
	print("Average Turnaround Time : ",end=' ')
	print(avgtt)
	global kk
	kk="Shortest job first non premitive can be used in a situation where there are numbers of program with low burst time, and few are of very high burst time. So to decrease the queue we use this algorithm."






def priority(event):
	global arr
	global names
	names=[]
	global avgwt
	global avgtt
	p=len(arr)
	pro=[]
	at=[]
	bt=[]
	rt=[]
	pt=[]
	at2=[]
	tat=[0,0,0,0]
	wt=[0,0,0,0]
	avgwt=0.0
	avgtt=0.0

	for a in arr:
		pro=pro+[a[0]]
		bt=bt+[int(a[2])]
		at=at+[int(a[1])]
		at2=at2+[int(a[1])]
		rt=rt+[int(a[2])]
		pt=pt+[int(a[3])]
	remain=p
	t=0
	print(pro)
	print(at)
	print(bt)
	print(rt)
	print(pt)
	while(remain!=0):
		pri=99999;
		for i in range(p):
			if(at2[i]<=t and pt[i]<pri):
				pri=pt[i]
		for i in range(p):
			if(pt[i]==pri):
				print(t)
				print(pro[i])
				names.append(pro[i])
				t=t+1
				rt[i]=rt[i]-1
				if(rt[i]==0):
					remain=remain-1
					tat[i]=t-at[i]
					wt[i]=t-at[i]-bt[i]
					avgwt=avgwt+t-at[i]-bt[i]
					avgtt=avgtt+t-at[i]
					at2[i]=99999
				break
	print(t)

	print("\n");
	print("***************************************")
	print("Pro\tArTi\tBuTi\tTaTi\tWtTi")
	print("***************************************")
	for i in range(p):
		print(pro[i], end="\t")
		print(at[i], end="\t") 
		print(bt[i] ,end="\t")  
		print(tat[i],end="\t")
		print(wt[i])
	print("***************************************");
	avgwt = avgwt/p;
	avgtt = avgtt/p;
	print("Average Waiting Time : ",end=' ')
	print(avgwt)
	print("Average Turnaround Time : ",end=' ')
	print(avgtt)
	global kk
	kk="Priority queues tend to crop up in a lot of algorithms as helpers for working with other data structures.Parking lots and garages might be simulated as objects that, at random time intervals, toss a new car out on to the street in front of the lot or garage."


def lrtf(event):
	
	global arr
	p=len(arr)
	global names
	global avgtt
	global avgwt
	names=[]
	pro=[]
	at=[]
	bt=[]
	rt=[]
	avgwt=0.0
	avgtt=0.0
	tat=[0,0,0,0]
	wt=[0,0,0,0]
	for a in arr:
			pro=pro+[a[0]]
			bt=bt+[int(a[2])]
			at=at+[int(a[1])]
			rt=rt+[int(a[2])]
	remain=p
	t=0
	i=0
	print(pro)
	print(bt)
	print(at)
	print(rt)
	while(remain!=0):
		x=-1
		i=0
		#print(remain)
		for i in range(p):
			#print(x)
			if(at[i]<=t and rt[i]>x):
				x=rt[i]
		for i in range(p):
			if(rt[i]==x):
				rt[i]=rt[i]-1
				if(rt[i]==0):
					remain=remain-1
					tat[i]=t-at[i]
					wt[i]=t-at[i]-bt[i]
					avgwt=avgwt+t-at[i]-bt[i]
					avgtt=avgtt+t-at[i]
				print(t)
				print(pro[i])
				names.append(pro[i])
				t=t+1
				break
			
	print(t)

	print("\n");
	print("***************************************")
	print("Pro\tArTi\tBuTi\tTaTi\tWtTi")
	print("***************************************")
	for i in range(p):
		print(pro[i], end="\t")
		print(at[i], end="\t") 
		print(bt[i] ,end="\t")  
		print(tat[i],end="\t")
		print(wt[i])
	print("***************************************");
	avgwt = avgwt/p;
	avgtt = avgtt/p;
	print("Average Waiting Time : ",end=' ')
	print(avgwt)
	print("Average Turnaround Time : ",end=' ')
	print(avgtt)
	global kk
	kk="This technique of scheduling is used where there is a long queue of high burst time process.So we use longest job remaining first to decrease the elongation of our queue processes."





	


def processes(event):
	global names
	global avgtt
	global avgwt
	process=[]
	time=[]
	l=len(names)
	w=0
	str1=names[0]
	for name in names:
		if(str1==name):
			w+=1
			if(w==l):
				process.append(str1)
				time.append(w)
				break

		else:
			print (str1)
			print (l)
			process.append(str1)
			str1=name
			time.append(w)
			w+=1
	print(process)		

	entry = {}
	label = {}
	label1 = {}
	i=0
	j=0
	k=0
	
	for name in process:
		lb = Label(frame1,background="#f4a463", height=10,width=10,text=name)
		lb.place(x=40+(i*55),y=40+(j*58),relwidth=.92, relheight=1.02, height=-580, width=-470)
		label[name] = lb
		lb1 = Label(frame1,background="#cd853f", height=10,width=10,text=time[k])
		lb1.place(x=40+(i*55),y=62+(j*58),relwidth=.92, relheight=1.02, height=-580, width=-470)
		label1[name] = lb1
		k+=1
		i += 1
		if(i==9):
			j=j+1
			i=0
	text = Text(frame1,background="#8080ff")
	text.place(x=12,y=350,relheight=1,relwidth=1,height=-510,width=-20)	
	text.insert(INSERT,"Average waiting time is =   ")
	text.insert(INSERT,avgwt)
	text.insert(INSERT,"\n\nAverage turn around time is =   ")
	text.insert(INSERT,avgtt)
	global kk

	lb1 = Label(frame1,background="#faebd7", height=10,width=10,text="Applications:")
	lb1.place(x=12,y=450,relwidth=.92, relheight=1.02, height=-580, width=-430)
	text1 = Text(frame1,background="#8080ff")
	text1.place(x=12,y=480,relheight=1,relwidth=1,height=-510,width=-20)
	text1.insert(INSERT,kk)	
	w=0


frame1= Frame(root, background="#faebd7", relief=RIDGE, borderwidth=5)
frame1.pack(side = LEFT)
frame2= Frame(root, background="#faebd7", relief=RIDGE, borderwidth=5)
frame2.pack(side = LEFT)

frame1.place(x=15, y=15, relwidth=1, relheight=1, height=-40, width=-440)
frame2.place(x=600, y=15, relwidth=1, relheight=1, height=-40, width=-620)

frame21= Frame(frame2, background="#8080ff", relief=RIDGE, borderwidth=5)
frame21.pack(side = LEFT)
frame22= Frame(frame2, background="#8080ff", relief=RIDGE, borderwidth=5)
frame22.pack()

frame21.place(x=10, y=10, relwidth=1, relheight=1, height=-310, width=-20)
frame22.place(x=10, y=320, relwidth=1, relheight=1, height=-335, width=-20)

b1= Button(frame21, text="First Come First Serve" , height=10 , width=20)
b2= Button(frame21, text="Round Robin Scheduling" , height=10 , width=20 )
b3= Button(frame21, text="Shortest Job First" , height=10 , width=20)
b4= Button(frame21, text="Priority Scheduling" , height=10 , width=20)
b5= Button(frame21, text="Shortest Time  Remaining First" , height=10 , width=20)
b6= Button(frame21, text="Longest Job First (Preemptive)" , height=10 , width=20)
b7= Button(frame21, text="Submit" , height=10 , width=20)
b8= Button(frame21, text="Print" , height=10 , width=20)


b1.bind("<Button-1>", fcfs)
b2.bind("<Button-1>", rr)
b3.bind("<Button-1>", sjfnp)
b4.bind("<Button-1>", priority)
b5.bind("<Button-1>", sjf)
b6.bind("<Button-1>", lrtf)
b7.bind("<Button-1>", InsRead)
b8.bind("<Button-1>", processes)



b1.place(x=18,y=42, relheight=1, relwidth=1,height=-260,width=-35)
b2.place(x=18,y=72, relheight=1, relwidth=1,height=-259,width=-35)
b3.place(x=18,y=102, relheight=1, relwidth=1,height=-258,width=-35)
b4.place(x=18,y=132, relheight=1, relwidth=1,height=-257,width=-35)
b5.place(x=18,y=162, relheight=1, relwidth=1,height=-256,width=-35)
b6.place(x=18,y=192, relheight=1, relwidth=1,height=-255,width=-35)
b7.place(x=30,y=232, relheight=1, relwidth=1,height=-256,width=-295)
b8.place(x=270,y=232, relheight=1, relwidth=1,height=-255,width=-295)


textfield= Text(frame22, height=300, width=250,font='helvetica 14')

textfield.place(x=0, y=0, relheight=1, relwidth=1, height=0)

root.mainloop()
