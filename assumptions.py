import scipy
ALPHA_LEVEL = 0.05

class AssumptionChecker:
    def __init__(self, data):
        self.is_normal = self.anova_normality_assumption(data)
        self.is_equal_n = self.anova_sample_size_assumption(data)
        self.is_equal_variance = self.anova_variance_assumption(data)
        if self.is_normal and self.is_equal_n and self.is_equal_variance:
            self.is_parametric = True
        else:
            self.is_parametric = False

    def anova_normality_assumption(self, data):
        list_of_data = []
        for lst in data:
            for value in lst:
                list_of_data.append(value)
        shapiro_result = scipy.stats.shapiro(list_of_data)
        if shapiro_result.pvalue > ALPHA_LEVEL:
            #print(f"Normality assumption: p={shapiro_result.pvalue}: PASSED.")
            return True
        else:
            #print(f"Normality assumption: p={shapiro_result.pvalue}: FAILED.")
            return False

    def anova_sample_size_assumption(self, data):
        max = len(data[0])
        min = len(data[0])
        for column in data:
            if len(column) > max:
                max = len(column)
            if len(column) < min:
                min = len(column)
        if max >= 2.5 * min:
            #print(f"Max n: {max}, min n: {min}. Equal n assumption:FAILED.")
            return False
        else:
            #print(f"Max n: {max}, min n: {min}. Equal n assumption:PASSED.")
            return True

    def anova_variance_assumption(self, data):
        levene_result = scipy.stats.levene(*data, center='median')
        if levene_result.pvalue > ALPHA_LEVEL:
            #print(f"Homogeneity of variance assumption: p={levene_result.pvalue}: PASSED.")
            return True
        else:
            #print(f"Homogeneity of variance assumption: p={levene_result.pvalue}: FAILED.")
            return False

    def print_assumptions(self):
        assumption_message = ""
        if self.is_equal_n:
            assumption_message = "Equal n assumption: passed."
        else:
            assumption_message = "Equal n assumption: violated."
        if self.is_equal_variance:
            assumption_message = assumption_message + "\nEqual variance assumption: passed."
        else:
            assumption_message = assumption_message + "\nEqual variance assumption: violated."

        if self.is_normal:
            assumption_message = assumption_message + "\nNormal distribution assumption: passed."
        else:
            assumption_message = assumption_message + "\nNormal distribution assumption: violated."
        print(assumption_message)