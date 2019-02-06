from sklearn.neural_network import MLPClassifier
import pickle

#clf = MLPClassifier(solver='lbfgs', alpha=1e-5,
#                    hidden_layer_sizes=(6, 2), random_state=1)

filename = 'NNdata.sav'
clf = pickle.load(open(filename, 'rb'))
########################################3
def checkwn(st,us):
    a= int(st[0])
    b= int(st[1])
    c= int(st[2])
    if len(us) >= 3:
        if a in us:
            if b in us:
                if c in us:
                    return 1
                else:
                    return 0
            else:
                return 0
        else:
            return 0
    else:
        return 0

##################
###### INIT VAR #####
done=[]
us=[]
winz=0
ns=[]
X=[]
count = 0 
end = 0 ### enable/disable

#####################

while end == 0: 
    if count % 2 == 0:
        uc= input("enter choice  ")
        if uc > 9 or uc < 0 :
            print " cant allow take 0-9"
        elif uc in done:
            print "already taken"
        elif uc in ns:
            print "taken by comp"
        else:
            done.append(uc)
            us.append(uc)
        ts = us[:]
        if len(ts) < 5:
            while len(ts) < 5:
                ts.append(0)
        X.append(ts)
        
    else:
        NN= input(" teach the NN place correct Move ")
        if NN in us:
            print "already taken by User"
        else:
            ns.append(NN)
               
        
    if len(X) == len(ns) and len(X) != 0:
        clf.fit(X,ns)
        print "reached"
        print clf.predict([X[0]])
        print len(X)
    print X
    print ns
        
    ws= ["123","456","789","147","159","258","369","357"]
    for chc in ws:
        if checkwn(chc,us)== 1:
            winz=1
            print "STOP WE HAVE A WINNER"
            break
        
        if checkwn(chc,ns)== 1:
            winz=1
            print "STOP WE HAVE A WINNER NS!!"
            break
    if winz == 1:
        break
    count = count + 1
    if count >= 9:
        print "=========================DRAW==========================="
        break

pickle.dump(clf, open(filename, 'wb'))
        
    

