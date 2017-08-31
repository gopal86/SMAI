import csv;
import numpy as np;
import time;
import sys;

train = sys.argv[1]
test = sys.argv[2]

start_time = time.time()

def File(filename):
    file = open(filename , 'r');
    reader = csv.reader(file);
    rows=[];
    for row in reader:
        rows.append(row);
    file.close();
    rows=np.array(rows, dtype = 'float64');
    return rows;

ans = lambda x: 0 if x < 0 else 1
rate = 0.25;

### This is Part-1 ###

# filename = 'mnist_train.csv';
rows=File(train);
for row in rows[:1]:
    w = np.zeros(len(row) , dtype = 'float64');

x=np.array(rows);
x[:,0]=1;
count = 0;
for i in xrange(20):
    count=0;
    for j,row in enumerate(rows):
        y = row[0];
        val = np.dot(w,x[j]);
        error = y - ans(val);
        w+= rate*error*x[j];
        if(error!=0):
            count+=1
    if(count==0):
        # print i;
        break;

# filenames = 'mnist_test.csv';
rows = File(test)
count=0
total = len(rows);
x=np.array(rows);
# x[:,0]=1;
# print len(x) , len(x[0]);
temp = np.zeros(shape=(len(x),1))
x = np.array(np.hstack((temp,x)))
# print len(x) , len(x[0])
for j,row in enumerate(rows):
    # y = row[0];
    val = np.dot(w,x[j]);
    # error = y - ans(val);
    # if(error == 0):
        # count+=1;
    print ans(val);
# print count , total;
# print (float(count*100))/float(total);
# print "My program took", time.time() - start_time, "to run"

##############################

### This is Part-2 ###

# filename = 'mnist_train.csv';
rows=File(train);
ans = lambda x: 0 if x < 0 else 1
for row in rows[:1]:
    w = np.zeros(len(row) , dtype = 'float64');
x=np.array(rows);
x[:,0]=1;
count = 0;
b=1100000
for i in xrange(25):
    count=0;
    for j,row in enumerate(rows):
        y = row[0];
        # x[0]=1;
        # x=np.array(x, dtype = 'float64');
        # y=np.array(y, dtype = 'float64');
        val = np.dot(w,x[j])-b;
        error = y - ans(val);
        w+= rate*error*x[j];
        if(error!=0):
            count+=1
    # print count
    if(count==0):
        # print i
        break;

# filenames = 'mnist_test.csv';
rows = File(test)
count=0
total = len(rows);
x=np.array(rows);
# x[:,0]=1;
temp = np.zeros(shape=(len(x),1))
x = np.array(np.hstack((temp,x)))
for j,row in enumerate(rows):
    # y = row[0];
    # x[0]=1;
    # x=np.array(x, dtype = 'float64');
    # y=np.array(y, dtype = 'float64');
    val = np.dot(w,x[j]);
    # error = y - ans(val);
    print ans(val)
    # print y , ans(val);
    # if(error == 0):
        # count+=1;
# print count , total;
# print (float(count*100))/float(total);
# print "My program took", time.time() - start_time, "to run"

##########################


########## This is Part-3 ################


# filename = 'train';
rows=File(train);
ans = lambda x: 0 if x < 0 else 1
for row in rows[:1]:
    w = np.zeros(len(row) , dtype = 'float64');
    z = np.zeros(len(row) , dtype = 'float64');
x=np.array(rows);
x[:,0]=1;
count = 1;
i=0;

# for i in xrange(50):
while(count!=0 and i < 70):
    i+=1;
    count=0 ;
    for j,row in enumerate(rows):
        y = row[0];
        # x[0]=1;
        # x=np.array(x, dtype = 'float64');
        # y=np.array(y, dtype = 'float64');
        val = np.dot(w,x[j]);

        error = y - ans(val);
        z+= rate*error*x[j];
        if(error!=0):
            count+=1
    if(count==0):
        break;
    w+=z;
# filenames = 'mnist_test.csv';
rows = File(test)
count=0
total = len(rows);
x=np.array(rows);
# x[:,0]=1;
temp = np.zeros(shape=(len(x),1))
x = np.array(np.hstack((temp,x)))
for j,row in enumerate(rows):
    # y = row[0];
    # x[0]=1;
    # x=np.array(x, dtype = 'float64');
    # y=np.array(y, dtype = 'float64');
    val = np.dot(w,x[j]);
    # error = y - ans(val);
    # print y , ans(val);
    # if(error == 0):
        # count+=1;
    print ans(val);
# print count , total;
# print (float(count*100))/float(total);
# print "My program took", time.time() - start_time, "to run"


##########

################### This is Part-4 ################


# filename = 'mnist_train.csv';
rows=File(train);
ans = lambda x: 0 if x < 0 else 1
for row in rows[:1]:
    w = np.zeros(len(row) , dtype = 'float64');
    z = np.zeros(len(row) , dtype = 'float64');
x=np.array(rows);
x[:,0]=1;
count = 1;
i=0;
b=12000000
# for i in xrange(50):
while(count!=0 and i < 70):
    i+=1;
    count=0 ;
    for j,row in enumerate(rows):
        y = row[0];
        # x[0]=1;
        # x=np.array(x, dtype = 'float64');
        # y=np.array(y, dtype = 'float64');
        val = np.dot(w,x[j])-b;
        error = y - ans(val);
        z+= rate*error*x[j];
        if(error!=0):
            count+=1
    if(count==0):
        break;
    w+=z;

# filenames = 'mnist_test.csv';
rows = File(test)
count=0
total = len(rows);
x=np.array(rows);
# x[:,0]=1;
temp = np.zeros(shape=(len(x),1))
x = np.array(np.hstack((temp,x)))
for j,row in enumerate(rows):
    # y = row[0];
    # x[0]=1;
    # x=np.array(x, dtype = 'float64');
    # y=np.array(y, dtype = 'float64');
    val = np.dot(w,x[j]);
    # error = y - ans(val);
    # print y , ans(val);
    # if(error == 0):
        # count+=1;
    print ans(val)
# print count , total;
# print (float(count*100))/float(total);
# print "My program took", time.time() - start_time, "to run"
