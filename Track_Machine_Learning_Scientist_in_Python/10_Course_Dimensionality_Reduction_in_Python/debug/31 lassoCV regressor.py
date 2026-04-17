import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

ansur_df = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\10_Course_Dimensionality_Reduction_in_Python\datasets\ansur_filter.csv')
ansur_df = ansur_df.drop(['Branch','Component','Gender','abdominalextensiondepthsitting','acromionradialelength','anklecircumference','balloffootcircumference','balloffootlength','biacromialbreadth','bicristalbreadth','bimalleolarbreadth','bitragionchinarc','bitragionsubmandibulararc','bizygomaticbreadth','buttockdepth','buttockheight','calfcircumference','chestbreadth','chestdepth','crotchheight','crotchlengthomphalion','crotchlengthposterioromphalion','earbreadth','earlength','elbowrestheight','eyeheightsitting','footlength','forearmcenterofgriplength','forearmforearmbreadth','forearmhandlength','functionalleglength','handbreadth','handcircumference','headcircumference','headlength','heelanklecircumference','hipbreadthsitting','interpupillarybreadth','interscyei','kneeheightmidpatella','kneeheightsitting','lowerthighcircumference','mentonsellionlength','neckcircumference','overheadfingertipreachsitting','palmlength','poplitealheight','shoulderlength','sittingheight','sleevelengthspinewrist','span','suprasternaleheight','tenthribheight','thumbtipreach','tibialheight','tragiontopofhead','trochanterionheight','waistbacklength','waistbreadth','waistfrontlengthsitting','waistheightomphalion','wristcircumference','weight_kg','stature_m','BMI_class','Height_class'], axis=1)
# X = ansur_df.drop('bicepscircumferenceflexed', axis=1)
X = ansur_df.drop('bicepscircumferenceflexed', axis=1).iloc[:1000]
y = ansur_df.loc[:999, 'bicepscircumferenceflexed']
# y = ansur_df['bicepscircumferenceflexed']
# y = y[:1000]

# X = ansur_df.iloc[:, :-1]
# y = ansur_df.iloc[:, -1]

# X_train = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\10_Course_Dimensionality_Reduction_in_Python\datasets\diabetes_X_train.csv')
# y_train = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\10_Course_Dimensionality_Reduction_in_Python\datasets\diabetes_y_train.csv', header=None)
# X_test = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\10_Course_Dimensionality_Reduction_in_Python\datasets\diabetes_X_test.csv')
# y_test = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\10_Course_Dimensionality_Reduction_in_Python\datasets\diabetes_y_test.csv', header=None)

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)
# print(ansur_df.info())

# for key in ansur_df.columns:
#     print(f'{key}')
print(X)