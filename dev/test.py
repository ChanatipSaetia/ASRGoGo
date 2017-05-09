import pickle
from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score

#-----------------------read model------------------------------
model = pickle.load(open("clf.sav","rb"))
countT = pickle.load(open("countT.sav","rb"))

Y = [] #list of label
df = [] #dataset of words each row
#----------------------------------get data from dev set time.txt----------------------------------
texts = open("test_set.txt",'r', encoding='utf-8')
for text in texts :
    df.append(text.replace('\n',''))
    Y.append(0)

#----------------------------------get data from dev what time.txt----------------------------------
texts = open("test_time.txt",'r', encoding='utf-8')
for text in texts :
    df.append(text.replace('\n',''))
    Y.append(1)

#----------------------------------get data from dev postpone .txt----------------------------------
texts = open("test_postpone.txt",'r', encoding='utf-8')
for text in texts :
    df.append(text.replace('\n',''))
    Y.append(2)

#----------------------------------get data from dev postpone .txt----------------------------------
texts = open("test_task.txt",'r', encoding='utf-8')
for text in texts :
    df.append(text.replace('\n',''))
    Y.append(3)

#-----------------------------------apply transform------------------------------------------------
count = countT.transform(df)

#-----------------------------------apply model------------------------------------------------
y_pred = model.predict(count)
f1 = f1_score(Y, y_pred, average='macro')
print("label: " + str(Y))
print("predicted label: " + str(y_pred))
print("number of dev: " + str(len(y_pred)))
print("f1 score: " + str(f1))
score = accuracy_score(Y, y_pred)
print("accuracy score: " + str(score))
