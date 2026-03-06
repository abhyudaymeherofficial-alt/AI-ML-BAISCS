import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import RandomOverSampler #pip install imblearn

data=pd.read_csv("D:/pythontrail1/Machine learning/magic04.data")
print(data)
data.columns=["fLength","fWidth","fSize","fConc","fConc1","fAsym","fM3Long","fM3Trans"
              ,"fAlpha","fDist","class"]
print(data.head())
print(data["class"].unique())

data["class"] = (data["class"] == 'g').astype(int)
print(data)
'''
for label in data.columns[:-1]: # Exclude last column (class) You exclude the last column because the last column is your target variable (class), not a feature.
    plt.hist(data[data["class"]==1][label],color="blue",label="gamma",alpha=0.7,density=True)
    plt.hist(data[data["class"]==0][label],color="red",label="hydron",alpha=0.7,density=True)
    plt.title(label)
    plt.ylabel("Probability")
    plt.xlabel(label)
    plt.legend()
    plt.show()
'''

print("====Train Validation Test dataset====")

train,valid,test=np.split(data.sample(frac=1),[int(0.6*len(data)),int(0.8*len(data))])
print(train)
print(valid)
print(test)

print(len(train[train["class"]==1])) #gamma
print(len(train[train["class"]==0]))#hydron

shuffled = data.sample(frac=1, random_state=42).reset_index(drop=True)
train, valid, test = (
    shuffled[:int(0.6*len(shuffled))],
    shuffled[int(0.6*len(shuffled)):int(0.8*len(shuffled))],
    shuffled[int(0.8*len(shuffled)):]
)
print(train)
print(valid)
print(test)

print(len(train[train["class"]==1])) #gamma
print(len(train[train["class"]==0]))#hydron

def scale_dataset(dataframe,oversample=False):
    x=dataframe[dataframe.columns[:-1]].values
    y=dataframe[dataframe.columns[-1]].values

    scalar=StandardScaler()
    x=scalar.fit_transform(x)

    if oversample:
        ros=RandomOverSampler()
        x,y=ros.fit_resample(x,y)

    dt=np.hstack((x,np.reshape(y,(-1,1))))

    return dt,x,y

train,x_train,y_train=scale_dataset(train,oversample=True)
print(len(y_train[y_train==1]))
print(len(y_train[y_train==0]))

valid,x_valid,y_valid=scale_dataset(valid,oversample=False)
print(len(y_valid[y_valid==1]))
print(len(y_valid[y_valid==0]))

test,x_test,y_test=scale_dataset(test,oversample=False)
print(len(y_test[y_test==1]))
print(len(y_test[y_test==0]))

from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
knn_model=KNeighborsClassifier(n_neighbors=1)
knn_model.fit(x_train,y_train)
y_pred=knn_model.predict(x_test)
print(y_pred)
print(y_test)
print(classification_report(y_test,y_pred))

print("====Naive Bayes Theo====")
from sklearn.naive_bayes import GaussianNB
nb_model=GaussianNB()
nb_model.fit(x_train,y_train)
y_pred=nb_model.predict(x_test)
print(y_pred)
print(y_test)
print(classification_report(y_test,y_pred))

print("====Logistic regression====")
from sklearn.linear_model import LogisticRegression
lg_model=LogisticRegression()
lg_model.fit(x_train,y_train)
y_pred=lg_model.predict(x_test)
print(y_pred)
print(y_test)
print(classification_report(y_test,y_pred))

print("====SVM====")
from sklearn.svm import SVC
svm_model=SVC()
svm_model.fit(x_train,y_train)
y_pred=svm_model.predict(x_test)
print(y_pred)
print(y_test)
print(classification_report(y_test,y_pred))

print("=======Neural networks========")
import tensorflow as tf # pip install tensorflow

def plot_history(history):
    fig ,(ax1,ax2)=plt.subplots(1,2,figsize=(10,4))

    ax1.plot(history.history['accuracy'], label='Train Accuracy')
    ax1.plot(history.history['val_accuracy'], label='Val Accuracy')
    ax1.set_xlabel('Epoch')
    ax1.set_ylabel('Accuracy')
    ax1.grid(True)

    ax2.plot(history.history['loss'], label='Train Loss')
    ax2.plot(history.history['val_loss'], label='Val Loss')
    ax2.set_xlabel('Epoch')
    ax2.set_ylabel('Binary cross entropy')
    ax2.grid(True)

    plt.show()


def train_model(x_train,y_train,num_nodes,dropout_prob,lr,batch_size,epochs):
    nn_model=tf.keras.Sequential([
        tf.keras.layers.Dense(num_nodes,activation="relu",input_shape=(10,)),
        tf.keras.layers.Dropout(dropout_prob),
        tf.keras.layers.Dense(num_nodes,activation="relu"),
        tf.keras.layers.Dropout(dropout_prob),
        tf.keras.layers.Dense(1,activation="sigmoid")
    ])

    nn_model.compile(optimizer=tf.keras.optimizers.Adam(lr)
                 ,loss="binary_crossentropy",metrics=["accuracy"])

    history=nn_model.fit(x_train,y_train,epochs=epochs,batch_size=batch_size,
                     validation_split=0.2,verbose=0)

    return nn_model,history

least_val_loss=float("inf")
least_loss_model=None
epochs=100
for num_nodes in [16,32,64]:
    for dropout_prob in [0,0.2]:
        for lr in [0.01,0.005,0.001]:
            for batch_size in [32,64,128]:
                model,history=train_model(x_train,y_train,num_nodes,dropout_prob,lr,batch_size,epochs)
                #plot_history(history)
                val_loss,val_accuracy=model.evaluate(x_valid,y_valid)
                if val_loss<least_val_loss:
                    least_val_loss=val_loss
                    least_loss_model=model

print("Best validation loss:", least_val_loss)

y_pred=least_loss_model.predict(x_test)
y_pred=(y_pred>0.5).astype(int).reshape(-1,)

print(classification_report(y_test,y_pred))
