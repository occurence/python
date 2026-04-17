import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

ansur_df = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\10_Course_Dimensionality_Reduction_in_Python\datasets\ansur_filter.csv')
ansur_df = ansur_df.drop(['Branch','Component','Gender','abdominalextensiondepthsitting','acromionradialelength','anklecircumference','balloffootcircumference','balloffootlength','biacromialbreadth','bicristalbreadth','bimalleolarbreadth','bitragionchinarc','bitragionsubmandibulararc','bizygomaticbreadth','buttockdepth','buttockheight','calfcircumference','chestbreadth','chestdepth','crotchheight','crotchlengthomphalion','crotchlengthposterioromphalion','earbreadth','earlength','elbowrestheight','eyeheightsitting','footlength','forearmcenterofgriplength','forearmforearmbreadth','forearmhandlength','functionalleglength','handbreadth','handcircumference','headcircumference','headlength','heelanklecircumference','hipbreadthsitting','interpupillarybreadth','interscyei','kneeheightmidpatella','kneeheightsitting','lowerthighcircumference','mentonsellionlength','neckcircumference','overheadfingertipreachsitting','palmlength','poplitealheight','shoulderlength','sittingheight','sleevelengthspinewrist','span','suprasternaleheight','tenthribheight','thumbtipreach','tibialheight','tragiontopofhead','trochanterionheight','waistbacklength','waistbreadth','waistfrontlengthsitting','waistheightomphalion','wristcircumference','weight_kg','stature_m','BMI_class','Height_class'], axis=1)
X = ansur_df.drop('bicepscircumferenceflexed', axis=1).iloc[:1000]
y = ansur_df.loc[:999, 'bicepscircumferenceflexed']


lcv_mask = [False, False,  True,  True, False,  True, False,  True,  True, False,  True,  True,  True,  True, False, False, False,  True, True,  True,  True,  True,  True,  True,  True,  True,  True, True, False,  True, False,  True]
gb_mask = [False, False,  True,  True, False, False, False,  True, False, False, False,  True, False, False, False, False,  True,  True, False, False, False, False,  True, False, False,  True, False, False,  True, False, False,  True]
rf_mask = [False, False,  True,  True, False, False, False,  True, False, False, False,  True, False, False, False, False, False, False, False, False, False, False,  True,  True, False,  True,  True, False, False, False,  True,  True]

# Sum of the votes of LassoCV, GradientBoosting, RandomForest
votes = np.sum([lcv_mask, gb_mask, rf_mask], axis=0)
print(votes)

# Mask for feature selected from votes
meta_mask = votes == 3

# Apply the dimensionality reduction on X
X_reduced = X.loc[:, meta_mask]

lm = LinearRegression()
scaler = StandardScaler()

# Reduced dataset into a linear regression pipeline
X_train, X_test, y_train, y_test = train_test_split(X_reduced, y, test_size=0.3, random_state=0)

lm.fit(scaler.fit_transform(X_train), y_train)
r_squared = lm.score(scaler.transform(X_test), y_test)
print(f'The model can explain {r_squared:.1%} of the variance in the test set using {lm.n_features_in_} features.')