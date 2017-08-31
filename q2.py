import csv;
import numpy as np;
import time;
import sys

train = sys.argv[1]
test = sys.argv[2]
start_time = time.time()

def File(filename):
    file = open(filename , 'r');
    reader = csv.reader(file);
    rows=[];
    for row in reader:
        if '?' not in row:
            rows.append(row);
    file.close();
    # print rows[:2];
    rows=np.array(rows, dtype = 'float64');
    return rows;

ans = lambda x: 2 if x < 0 else 4
rate = 2.25;

### This is Part-1 ###

# filename = 'q2_breast_cancer.train';
rows=File(train);
for row in rows[:1]:
    w = np.zeros(len(row)-1 , dtype = 'float64');
x=np.array(rows);

x=x[:,:-1];
x[:,0]=1;
# for j,row in enumerate(rows):
    # y=row[-1];
    # if(y==2):
        # x[j]=x[j]*-1;
total = len(rows)

b=100;
count = 0;

for i in xrange(100):
    count=0;
    for j,row in enumerate(rows):
        y = row[-1];
        val = np.dot(w,x[j]);
        temp = np.dot(x[j],x[j]);
        error = float(float((float(y) - float(ans(val-b))))/float(2));
        # if(val < b):
            # flag = ((b-val)/temp)*rate;
            # w+= flag*x[j];
        if(error!=0):
            flag = ((b-val)/temp);
            w+= flag*x[j]*rate;

        if(error==0):
        # else:
            count+=1
    # print float(count)/float(total);

# print "My program took", time.time() - start_time, "to run"

# filenames = 'test.csv';
rows = File(test)
count=0
total = len(rows);
x=np.array(rows);
# x=x[:,:-1];
x[:,0]=1;
# for j,row in enumerate(rows):
    # y=row[-1];
    # if(y==2):
        # x[j]=x[j]*-1;
b=100;
count = 0;

for j,row in enumerate(rows):
    # y = row[-1];
    val = np.dot(w,x[j]);
    # if(val > 0 and y==4):
        # count+=1;
    # if(val < 0 and y == 2):
        # count+=1;
    # error = float(float((float(y) - float(ans(val-b))))/float(2));
    # if(error == 0):
        # count+=1;
    print ans(val-b)
# print count , total;
# print (float(count*100))/float(total);
# print "My program took", time.time() - start_time, "to run"



############This is part-2#



rows=File(train);
for row in rows[:1]:
    w = np.zeros(len(row)-1 , dtype = 'float64');
x=np.array(rows);

x=x[:,:-1];
x[:,0]=1;
# for j,row in enumerate(rows):
    # y=row[-1];
    # if(y==2):
        # x[j]=x[j]*-1;
total = len(rows)

b=100;
count = 0;

for i in xrange(100):
    count=0;
    for j,row in enumerate(rows):
        y = row[-1];
        val = np.dot(w,x[j]);
        temp = np.dot(x[j],x[j]);
        error = float(float((float(y) - float(ans(val-b))))/float(2));

        # if(val < b):
            # flag = ((b-val)/temp)*rate;
            # w+= flag*x[j];
        if(error!=0):
            flag = ((b-val)/temp);
            w+= flag*x[j]*rate;

        if(error==0):
        # else:
            count+=1
    rate-=0.02
    # print float(count)/float(total);

# print "My program took", time.time() - start_time, "to run"

# filenames = 'test.csv';
rows = File(test)
count=0
total = len(rows);
x=np.array(rows);
# x=x[:,:-1];
x[:,0]=1;
# for j,row in enumerate(rows):
    # y=row[-1];
    # if(y==2):
        # x[j]=x[j]*-1;
b=100;
count = 0;

for j,row in enumerate(rows):
    # y = row[-1];
    val = np.dot(w,x[j]);
    # if(val > 0 and y==4):
        # count+=1;
    # if(val < 0 and y == 2):
        # count+=1;
    # error = float(float((float(y) - float(ans(val-b))))/float(2));
    # if(error == 0):
        # count+=1;
    print ans(val-b)
