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
neigh = KNeighborsClassifier(n_neighbors=3)
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


# =============================================================================
# pd.set_option('display.max_columns', None)
# 
# statN=data.describe()
# statC=data.describe(include=['object'])
# 
# display(data.info())
# display(statN)
# display(statC)
# 
# nrows = data.shape[0]
# rcols = data.shape[1]
# 
# 
# data5898=data.groupby("ETAT")["MIMAT0005898"]
# data5951=data.groupby("ETAT")["MIMAT0005951"]
# data19691=data.groupby("ETAT")["MIMAT0019691"]
# data27623=data.groupby("ETAT")["MIMAT0027623"]
# data27650=data.groupby("ETAT")["MIMAT0027650"]
# 
# display(data5898.describe())
# display(data5951.describe())
# display(data19691.describe())
# display(data27623.describe())
# display(data27650.describe())
# 
# 
# numerical_cols = data.select_dtypes(exclude=['object']).columns
# num_subplot_rows = len(numerical_cols)
# num_subplot_cols = 5
# plt.subplots(figsize=(5*num_subplot_cols, 5*num_subplot_rows))
# for index, col in enumerate(numerical_cols):
#     plt.subplot(num_subplot_rows, num_subplot_cols, num_subplot_cols*index+3, autoscale_on=True)
#     plt.boxplot(data[col].values)
#     plt.title(col)
#     plt.show()
#     
#     
# =============================================================================
    
    
# =============================================================================
# BC5898=[]
# BC5951=[]
# BC19691=[]
# BC27623=[]
# BC27650=[]
# 
# NC5898=[]
# NC5951=[]
# NC19691=[]
# NC27623=[]
# NC27650=[]
# 
# PC5898=[]
# PC5951=[]
# PC19691=[]
# PC27623=[]
# PC27650=[]
# 
# BBD5898=[]
# BBD5951=[]
# BBD19691=[]
# BBD27623=[]
# BBD27650=[]
# 
# boobscancer =np.array([])
# noncancer =np.array([])
# prostatecancer =np.array([])
# bbdcancer =np.array([])
# 
# for i in data.index :
#     if data.ETAT[i] == 'breast cancer' :
#         boobscancer=np.append(boobscancer,[ data.MIMAT0005898[i],
#                               data.MIMAT0005951[i],
#                               data.MIMAT0019691[i],
#                               data.MIMAT0027623[i],
#                               data.MIMAT0027650[i]])
#         
#     elif data.ETAT[i] == 'non-cancer' :
#          noncancer=np.append(noncancer, [data.MIMAT0005898[i],
#                               data.MIMAT0005951[i],
#                               data.MIMAT0019691[i],
#                               data.MIMAT0027623[i],
#                               data.MIMAT0027650[i]])
#     elif data.ETAT[i] == 'prostate disease' :
#         prostatecancer=np.append(prostatecancer,[ data.MIMAT0005898[i],
#                               data.MIMAT0005951[i],
#                               data.MIMAT0019691[i],
#                               data.MIMAT0027623[i],
#                               data.MIMAT0027650[i]])
#     elif data.ETAT[i] == 'benign breast disease' :
#          bbdcancer=np.append(bbdcancer, [data.MIMAT0005898[i],
#                               data.MIMAT0005951[i],
#                               data.MIMAT0019691[i],
#                               data.MIMAT0027623[i],
#                               data.MIMAT0027650[i]])
#         
# print(boobscancer)        
# =============================================================================
# =============================================================================
#         
#         
# for i in data.index :
#     if data.ETAT[i] == 'breast cancer' :
#         BC5898.append(data.MIMAT0005898[i])
#         BC5951.append(data.MIMAT0005951[i])
#         BC19691.append(data.MIMAT0019691[i])
#         BC27623.append(data.MIMAT0027623[i])
#         BC27650.append(data.MIMAT0027650[i])
#         
#     elif data.ETAT[i] == 'non-cancer' :
#         NC5898.append(data.MIMAT0005898[i])
#         NC5951.append(data.MIMAT0005951[i])
#         NC19691.append(data.MIMAT0019691[i])
#         NC27623.append(data.MIMAT0027623[i])
#         NC27650.append(data.MIMAT0027650[i])
#         
#     elif data.ETAT[i] == 'prostate disease' :
#         PC5898.append(data.MIMAT0005898[i])
#         PC5951.append(data.MIMAT0005951[i])
#         PC19691.append(data.MIMAT0019691[i])
#         PC27623.append(data.MIMAT0027623[i])
#         PC27650.append(data.MIMAT0027650[i])
#         
#     elif data.ETAT[i] == 'benign breast disease' :
#         BBD5898.append(data.MIMAT0005898[i])
#         BBD5951.append(data.MIMAT0005951[i])
#         BBD19691.append(data.MIMAT0019691[i])
#         BBD27623.append(data.MIMAT0027623[i])
#         BBD27650.append(data.MIMAT0027650[i])
#         
# #Afficher moyenne
# print("Moyenne miARN 5898 : ")     
# print("Breast Cancer : "+str(s.mean(BC5898)))
# print("Non Cancer : "+str(s.mean(NC5898)))
# print("Prostate Cancer : "+str(s.mean(PC5898)))
# print("Benign Breast Disease : "+str(s.mean(BBD5898))+'\n')
# 
# print("Moyenne miARN 5951 : ")     
# print("Breast Cancer : "+str(s.mean(BC5951)))
# print("Non Cancer : "+str(s.mean(NC5951)))
# print("Prostate Cancer : "+str(s.mean(PC5951)))
# print("Benign Breast Disease : "+str(s.mean(BBD5951))+'\n')
# 
# print("Moyenne miARN 19691 : ")     
# print("Breast Cancer : "+str(s.mean(BC19691)))
# print("Non Cancer : "+str(s.mean(NC19691)))
# print("Prostate Cancer : "+str(s.mean(PC19691)))
# print("Benign Breast Disease : "+str(s.mean(BBD19691))+'\n')
# 
# print("Moyenne miARN 27623 : ")     
# print("Breast Cancer : "+str(s.mean(BC27623)))
# print("Non Cancer : "+str(s.mean(NC27623)))
# print("Prostate Cancer : "+str(s.mean(PC27623)))
# print("Benign Breast Disease : "+str(s.mean(BBD27623))+'\n')
# 
# print("Moyenne miARN 27650 : ")     
# print("Breast Cancer : "+str(s.mean(BC27650)))
# print("Non Cancer : "+str(s.mean(NC27650)))
# print("Prostate Cancer : "+str(s.mean(PC27650)))
# print("Benign Breast Disease : "+str(s.mean(BBD27650))+'\n')
# 
# #Afficher variance
# print("Variance miARN 5898 : ")     
# print("Breast Cancer : "+str(s.variance(BC5898)))
# print("Non Cancer : "+str(s.variance(NC5898)))
# print("Prostate Cancer : "+str(s.variance(PC5898)))
# print("Benign Breast Disease : "+str(s.variance(BBD5898))+'\n')
# 
# print("Variance miARN 5951 : ")     
# print("Breast Cancer : "+str(s.variance(BC5951)))
# print("Non Cancer : "+str(s.variance(NC5951)))
# print("Prostate Cancer : "+str(s.variance(PC5951)))
# print("Benign Breast Disease : "+str(s.variance(BBD5951))+'\n')
# 
# print("Variance miARN 19691 : ")     
# print("Breast Cancer : "+str(s.variance(BC19691)))
# print("Non Cancer : "+str(s.variance(NC19691)))
# print("Prostate Cancer : "+str(s.variance(PC19691)))
# print("Benign Breast Disease : "+str(s.variance(BBD19691))+'\n')
# 
# print("Variance miARN 27623 : ")     
# print("Breast Cancer : "+str(s.variance(BC27623)))
# print("Non Cancer : "+str(s.variance(NC27623)))
# print("Prostate Cancer : "+str(s.variance(PC27623)))
# print("Benign Breast Disease : "+str(s.variance(BBD27623))+'\n')
# 
# print("Variance miARN 27650 : ")     
# print("Breast Cancer : "+str(s.variance(BC27650)))
# print("Non Cancer : "+str(s.variance(NC27650)))
# print("Prostate Cancer : "+str(s.variance(PC27650)))
# print("Benign Breast Disease : "+str(s.variance(BBD27650))+'\n')
# 
# #Afficher variance
# print("Ecart Type miARN 5898 : ")     
# print("Breast Cancer : "+str(s.stdev(BC5898)))
# print("Non Cancer : "+str(s.stdev(NC5898)))
# print("Prostate Cancer : "+str(s.stdev(PC5898)))
# print("Benign Breast Disease : "+str(s.stdev(BBD5898))+'\n')
# 
# print("Ecart Type miARN 5951 : ")     
# print("Breast Cancer : "+str(s.stdev(BC5951)))
# print("Non Cancer : "+str(s.stdev(NC5951)))
# print("Prostate Cancer : "+str(s.stdev(PC5951)))
# print("Benign Breast Disease : "+str(s.stdev(BBD5951))+'\n')
# 
# print("Ecart Type miARN 19691 : ")     
# print("Breast Cancer : "+str(s.stdev(BC19691)))
# print("Non Cancer : "+str(s.stdev(NC19691)))
# print("Prostate Cancer : "+str(s.stdev(PC19691)))
# print("Benign Breast Disease : "+str(s.stdev(BBD19691))+'\n')
# 
# print("Ecart Type miARN 27623 : ")     
# print("Breast Cancer : "+str(s.stdev(BC27623)))
# print("Non Cancer : "+str(s.stdev(NC27623)))
# print("Prostate Cancer : "+str(s.stdev(PC27623)))
# print("Benign Breast Disease : "+str(s.stdev(BBD27623))+'\n')
# 
# print("Ecart Type miARN 27650 : ")     
# print("Breast Cancer : "+str(s.stdev(BC27650)))
# print("Non Cancer : "+str(s.stdev(NC27650)))
# print("Prostate Cancer : "+str(s.stdev(PC27650)))
# print("Benign Breast Disease : "+str(s.stdev(BBD27650))+'\n')
# =============================================================================
