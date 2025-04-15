import pandas as pd
import pingouin

late_shipments = pd.read_csv(r'D:\STUDY\python\Track_Associate_Data_Scientist_Python\29_Course_Hypothesis_Testing_in_Python\datasets\late_shipments.csv')

# Perform a pairwise t-test on pack price, grouped by shipment mode
pairwise_results = pingouin.pairwise_tests(data=late_shipments,
                                           dv='pack_price',
                                           between='shipment_mode',
                                           padjust='none') 

# Print pairwise_results
print(pairwise_results)

# Modify the pairwise t-tests to use Bonferroni p-value adjustment
bonf_pairwise_results = pingouin.pairwise_tests(data=late_shipments, 
                                           dv="pack_price",
                                           between="shipment_mode",
                                           padjust="bonf")

# Print pairwise_results
print(bonf_pairwise_results)

print(0.01 < bonf_pairwise_results['p-unc'])

for p_value in bonf_pairwise_results['p-unc']:
    print(f"{p_value} < 0.01: {p_value < 0.01}")
