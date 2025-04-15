import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

ansur_df = pd.read_csv(r'D:\STUDY\python\Track_Machine_Learning_Scientist_in_Python\10_Course_Dimensionality_Reduction_in_Python\datasets\ansur_filter.csv')
ansur_df = ansur_df.drop(['Branch','Component','Gender','abdominalextensiondepthsitting','acromionradialelength','anklecircumference','balloffootcircumference','balloffootlength','biacromialbreadth','bicristalbreadth','bimalleolarbreadth','bitragionchinarc','bitragionsubmandibulararc','bizygomaticbreadth','buttockdepth','buttockheight','calfcircumference','chestbreadth','chestdepth','crotchheight','crotchlengthomphalion','crotchlengthposterioromphalion','earbreadth','earlength','elbowrestheight','eyeheightsitting','footlength','forearmcenterofgriplength','forearmforearmbreadth','forearmhandlength','functionalleglength','handbreadth','handcircumference','headcircumference','headlength','heelanklecircumference','hipbreadthsitting','interpupillarybreadth','interscyei','kneeheightmidpatella','kneeheightsitting','lowerthighcircumference','mentonsellionlength','neckcircumference','overheadfingertipreachsitting','palmlength','poplitealheight','shoulderlength','sittingheight','sleevelengthspinewrist','span','suprasternaleheight','tenthribheight','thumbtipreach','tibialheight','tragiontopofhead','trochanterionheight','waistbacklength','waistbreadth','waistfrontlengthsitting','waistheightomphalion','wristcircumference','weight_kg','stature_m','BMI_class','Height_class'], axis=1)
X = ansur_df.drop('bicepscircumferenceflexed', axis=1).iloc[:1000]
y = ansur_df.loc[:999, 'bicepscircumferenceflexed']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

from sklearn.feature_selection import RFE
from sklearn.ensemble import GradientBoostingRegressor

# Select 10 features with RFE on a GradientBoostingRegressor, drop 3 features on each step
rfe_gb = RFE(estimator=GradientBoostingRegressor(), 
             n_features_to_select=10, step=3, verbose=1)
rfe_gb.fit(X_train, y_train)

# Calculate the R squared on the test set
r_squared = rfe_gb.score(X_test, y_test)
print(f'The model can explain {r_squared:.1%} of the variance in the test set')

# Assign the support array to gb_mask
gb_mask = rfe_gb.support_

# Fitting estimator with 32 features.
# Fitting estimator with 29 features.
# Fitting estimator with 26 features.
# Fitting estimator with 23 features.
# Fitting estimator with 20 features.
# Fitting estimator with 17 features.
# Fitting estimator with 14 features.
# Fitting estimator with 11 features.
# The model can explain 85.8% of the variance in the test set
print(gb_mask)