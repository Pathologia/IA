import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

#Ouvre le fichier csv
data = pd.read_csv("./Breast_cancer Dataset/breast_cancer.csv",";", index_col="ID_REF")

#Remplace les classifcation écrite en number
#Intérêt ? Je sais pas
ToReplace = ['breast cancer','non cancer','benign breast disease', 'prostate disease'] 
Values = [0, 1, 2, 3]
data['ETAT'] = data['ETAT'].replace(to_replace=ToReplace, value=Values)

#x prends tout les columns en entrée, y tout les columns en sortie
x=data.drop(columns=["ETAT"])
y=data["ETAT"]
#Récupère des entrées et des sorties d'entrainement et de test
X_train, X_test, y_train, y_test = train_test_split(x, y)

#Paramètre l'algorithme de KNN avec une comparaison de trois voisin
neigh = KNeighborsClassifier(n_neighbors=4)
#Lance KNN avec les entrées et sorties d'entrainement
neigh.fit(X_train, y_train)

#Récupère les sorties prédites avec les entrées de test
y_pred = neigh.predict(X_test)

#Lance les différentes métric pour observer la justesse de l'algorithme
result = confusion_matrix(y_test, y_pred)
print("Confusion Matrix :")
print(result)
result1 = classification_report(y_test, y_pred)
print("Classification Report :")
print(result1)
result2 = accuracy_score(y_test, y_pred)
print("Accuracy:", result2)


