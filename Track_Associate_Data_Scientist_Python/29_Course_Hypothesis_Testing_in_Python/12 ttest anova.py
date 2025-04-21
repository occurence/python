import pandas as pd
import pingouin

late_shipments = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\29_Course_Hypothesis_Testing_in_Python\datasets\late_shipments.csv')

# Run an ANOVA for pack_price across shipment_mode
anova_results = pingouin.anova(data=late_shipments,
                               dv='pack_price',
                               between='shipment_mode')

# Print anova_results
print(anova_results)