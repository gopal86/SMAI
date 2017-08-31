import csv;
import numpy as np;
import time;
import math;
start_time = time.time()

def File(filename):
    file = open(filename , 'r');
    reader = csv.reader(file);
    rows=[];
    for i,row in enumerate(reader):
        if(i!=0):
            if(row[-1]=='low'):
                row[-1]=0;

            if(row[-1]=='medium'):
                row[-1]=1;

            if(row[-1]=='high'):
                row[-1]=2;

            if(row[-2]=='IT'):
                row[-2]=0;

            if(row[-2]=='RandD'):
                row[-2]=1;

            if(row[-2]=='accounting'):
                row[-2]=2;

            if(row[-2]=='hr'):
                row[-2]=3;

            if(row[-2]=='management'):
                row[-2]=4;

            if(row[-2]=='marketing'):
                row[-2]=5;

            if(row[-2]=='product_mng'):
                row[-2]=6;

            if(row[-2]=='sales'):
                row[-2]=7;

            if(row[-2]=='support'):
                row[-2]=8;

            if(row[-2]=='technical'):
                row[-2]=9;

            rows.append(row);
    file.close();
    rows=np.array(rows, dtype = 'float64');
    return rows;


filename = 'decision_tree_train.csv';
rows=File(filename);

x=np.array(rows[:9000]);
train = np.array(rows[9000:]);


class Node:
    def __init__(self, val,num,ans):
        self.l = None
        self.r = None
        self.val = val
        self.num = num
        self.ans = ans

class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, val,num,ans):
        if(self.root == None):
            self.root = Node(val,num,ans)
        else:
            self._add(val, num ,ans , self.root)

    def _add(self, val, num ,ans , node):
        if(val < node.val):
            if(node.l != None):
                self._add(val, num , ans , node.l)
            else:
                node.l = Node(val,num , ans)
        else:
            if(node.r != None):
                self._add(val,num, ans , node.r)
            else:
                node.r = Node(val,num ,ans)

    def find(self, data):
        if(self.root != None):
            return self._find(data, self.root)
        else:
            return None

            # print node.ans;
    def _find(self, data , node ):
        # print type(node.ans)
        if( node.ans == 0.0 or node.ans == 1.0):
            # print node.ans
            # print "am i acoming in ??"
            return float(node.ans);
        elif(data[node.num] > node.val and node.r !=None):
            self._find(data , node.r)
        elif(data[node.num] <node.val and node.l !=None):
            self._find(data , node.l);

    def printTree(self):
        if(self.root != None):
            self._printTree(self.root)

    def _printTree(self, node):
        if(node != None):
            self._printTree(node.l)
            # print node.val , node.num , node.ans ;
            # print;
            self._printTree(node.r)

def entropy(data):

    flag1 = 1.1; #to find the minimum entroy . A flag variable .
    for attr_no in xrange(10):
        # print attr_no;
        if(attr_no !=6):
            if(len(data)==0):
                continue;
            temp = np.unique(data[:,attr_no]); #taking temporary variable to calculate the best check/split in the data.
            # print len(temp)
            for var in temp: #will run the number of times there is a unique value

                class1=0;class2=0;class3=0;class4=0;
                for i in data:# will traverse through whole data
                    if (i[attr_no] > var):
                        if i[6]==0 :
                            class1+=1;
                        else:
                            class2+=1;

                    else:
                        if(i[6]==0):
                            class3+=1;
                        else:
                            class4+=1;

                prob_to_left = float((float(class1)+float(class2))/float(len(data)));
                if(prob_to_left > 0.0):
                    prob_positive_left = float( float(class1)/float(class1+class2));
                    prob_negative_left = float( float(class2)/float(class1+class2))

                    ent_positive_left = 0.0;
                    ent_negative_left = 0.0

                    if(prob_positive_left > 0.0):
                        ent_positive_left = prob_positive_left * np.log2(prob_positive_left)
                    if(prob_negative_left > 0.0):
                        ent_negative_left = prob_negative_left * np.log2(prob_negative_left)

                    ent_towards_left = ent_negative_left + ent_positive_left;
                else:
                    prob_to_left=1.0;
                    ent_towards_left = -1.0

                prob_to_right = float((float(class3)+float(class4))/float(len(data)));

                if(prob_to_right > 0.0):
                    prob_positive_right = float( float(class3)/float(class3+class4));
                    prob_negative_right = float( float(class4)/float(class3+class4))

                    ent_positive_right = 0.0;
                    ent_negative_right = 0.0

                    if(prob_positive_right > 0.0):
                        ent_positive_right = prob_positive_right * np.log2(prob_positive_right)
                    if(prob_negative_right > 0.0):
                        ent_negative_right = prob_negative_right * np.log2(prob_negative_right)
                    ent_towards_right = ent_positive_right + ent_negative_right;
                else:
                    prob_to_right = 1.0;
                    ent_towards_right=-1.0

                flag2 = -1*prob_to_left*ent_towards_left - 1*prob_to_right*ent_towards_right;

                if(flag1>flag2):
                    flag1=flag2;
                    divi_line=var;
                    feature = attr_no;
    row1=[];
    row2=[];
    for i in data:
        if(i[feature]>divi_line):
            row1.append(i);
        else:
            row2.append(i);

    return flag1 , divi_line , np.array(row1) , np.array(row2) ,feature;

tree=Tree()

def create_tree(data,stop):
    vals,divide,data1,data2,att = entropy(data);
    # print divide , att,stop;

    if(vals==0):
        for i in data[:1]:
            ans = i[6];
        # print ans;
        tree.add(divide , att,ans);
    else:
        tree.add(divide , att,None);

    stop+=1;
    if(stop==6):
        return;

    if(vals==0):
        return;
    create_tree(data2,stop);
    create_tree(data1,stop);

create_tree(x,0);
# tree.printTree()

count=0;
for i in train:
    ans = tree.find(i);
    print ans;
    # if(ans!=None):
        # print ans , i[6]

    if(ans == i[6]):
        print "coming in"
        count+=1;
print "Accuracy :- %s" %(count)
# print count , len(train);

print "My program took", time.time() - start_time, "to run";
