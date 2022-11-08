import scipy
from math import log10, floor


class StatsExecuter:
    def __init__(self, data, assumptions, num_groups):
        self.pvalue = None
        self.testPerformed = None
        if assumptions and num_groups == 2:
            self.pvalue= self.t_test(data)
            self.testPerformed = "T-Test"
        elif (not assumptions) and num_groups == 2:
            self.pvalue= self.mann_whitney_test(data)
            self.testPerformed = "Mann Whitney Test"
        elif assumptions and num_groups > 2:
            self.pvalue= self.one_way_anova(data)
            self.testPerformed = "One-way ANOVA"
        elif (not assumptions) and num_groups > 2:
            self.pvalue= self.kruskal_wallis(data)
            self.testPerformed = "Kruskal Wallis Test"
        self.pvalue = self.round_sig(self.pvalue)


    def t_test(self, data):
        result = scipy.stats.ttest_ind(*data)
        print(f"T-test performed. ")
        return result.pvalue

    def mann_whitney_test(self, data):
        result = scipy.stats.mannwhitneyu(*data)
        print(f"Mann-Whitney test performed. ")
        return result.pvalue

    def one_way_anova(self,data):
        result = scipy.stats.f_oneway(*data)
        print(f"One-way ANOVA performed. ")
        return result.pvalue

    def kruskal_wallis(self,data):
        result = scipy.stats.kruskal(*data)
        print(f"Kruskal Wallis Test performed. ")
        return result.pvalue

    def round_sig(self, x, sig=2):
        return round(x, sig - int(floor(log10(abs(x)))) - 1)

    def print_p_value(self):
        print(f"p:value: {self.pvalue}")