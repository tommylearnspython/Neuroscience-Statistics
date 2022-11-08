class DataManager:
    def __init__(self, data):
        self.num_groups = len(data.columns)
        self.data = []
        for column in data.columns:
            self.data.append(data[column].values)

