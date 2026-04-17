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

from sklearn.linear_model import LassoCV

# Create and fit the LassoCV model on the training set
lcv = LassoCV()
lcv.fit(X_train, y_train)
print(f'Optimal alpha = {lcv.alpha_:.3f}')

# Calculate R squared on the test set
r_squared = lcv.score(X_test, y_test)
print(f'The model explains {r_squared:.1%} of the test set variance')

# Create a mask for coefficients not equal to zero
lcv_mask = lcv.coef_ != 0
print(f'{sum(lcv_mask)} features out of {len(lcv_mask)} selected')

# Optimal alpha = 0.097
# The model explains 87.4% of the test set variance
# 22 features out of 32 selected
print(lcv_mask)