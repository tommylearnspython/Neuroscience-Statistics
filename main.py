###pyscript
ALPHA_LEVEL = 0.05

from stats_executer import StatsExecuter
from data_manager import DataManager
from assumptions import AssumptionChecker
import pandas as pd



file_name = input("What is the path of the excel file you'd like to analyze? ")
raw_data = pd.read_excel(file_name)


data_manager = DataManager(raw_data)
data = data_manager.data
assumption_checker = AssumptionChecker(data)
assumption_checker.print_assumptions()
stats = StatsExecuter(data, assumption_checker.is_parametric, data_manager.num_groups)
stats.print_p_value()





























#### CALCULATE T-TEST

# def get_sum_square_value(nums):
#     total = 0
#     for i in nums:
#         total += i**2
#     return total
#
# def is_p_more_than_005(t, crit):
#     if abs(t) > crit:
#         return True
#     return False
###### T TEST RAW
# sum_1 = sum(nums1)
# sum_2 = sum(nums2)
# n_1 = len(nums1)
# n_2 = len(nums2)
# mean_1 = sum_1/n_1
# mean_2 = sum_2/n_2
# df = (n_1+n_2) - 2
# critical_t = scipy.stats.t.ppf(q=1-0.025, df=df)
# sum_squared_values_1 = get_sum_square_value(nums1)
# sum_squared_values_2 = get_sum_square_value(nums2)
#
#
#
#
# ss_1 = sum_squared_values_1 - ((sum_1**2)/n_1)
# ss_2 = sum_squared_values_2 - ((sum_2**2)/n_2)
#
# variance_pooled = (ss_1 + ss_2)/((n_1-1)+(n_2-1))
# std_pooled = np.sqrt(variance_pooled*((1/n_1)+(1/n_2)))
# t = (mean_1 - mean_2)/std_pooled
#print(is_p_more_than_005(t, critical_t))
