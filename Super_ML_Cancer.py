import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn import svm
from sklearn.model_selection import train_test_split,cross_val_score
from sklearn.metrics import classification_report, accuracy_score, recall_score
from sklearn.ensemble import RandomForestClassifier

#Ouvre le fichier csv
data = pd.read_csv("./Breast_cancer Dataset/breast_cancer.csv",";", index_col="ID_REF")

ToReplace = ['breast cancer','non cancer','benign breast disease', 'prostate disease'] 
Values = [1, 2, 3, 4]
data['ETAT'] = data['ETAT'].replace(to_replace=ToReplace, value=Values)

#x prends tout les columns en entrée, y tout les columns en sortie
x=data.drop(columns=["ETAT"])
y=data["ETAT"]
#Récupère des entrées et des sorties d'entrainement et de test
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3)



def printResult(name,model,X_test, y_test,x,y):
    print(" ")
    print(name)
    y_pred = model.predict(X_test)
    result_svm_1  = classification_report(y_test, y_pred,zero_division=0)
    print("Classification Report : ")
    print(result_svm_1)
    result_svm_2  = accuracy_score(y_test, y_pred)
    print("Accuracy: ", result_svm_2)
    result_svm_3 = recall_score(y_test, y_pred, average='macro',zero_division=0)
    print("Recall: ", result_svm_3)
    
    scores = cross_val_score(model, x, y, cv=5)
    print("CrossValidation : ")
    print(scores)
    print(" ")



#Paramètre l'algorithme de KNN avec une comparaison de trois voisin
neigh = KNeighborsClassifier(n_neighbors=3)
neigh.fit(X_train, y_train)
printResult("KNN",neigh,X_test, y_test,x,y)


def svmFunction(name, v_kernel, X_train, y_train, X_test, y_test,x,y) :
    clf = svm.SVC(kernel=v_kernel)
    clf.fit(X_train, y_train)
    printResult(name, clf, X_test, y_test,x,y)
    

svmFunction('SVM - Linear','linear', X_train, y_train, X_test, y_test,x,y)
svmFunction('SVM - Polynomial','poly', X_train, y_train, X_test, y_test,x,y)
svmFunction('SVM - RBF','rbf', X_train, y_train, X_test, y_test,x,y)
svmFunction('SVM - Sigmoid','sigmoid', X_train, y_train, X_test, y_test,x,y)

#Random Forest
forest = RandomForestClassifier()
forest.fit(X_train, y_train)
printResult("Random Forest", forest, X_test, y_test, x, y)