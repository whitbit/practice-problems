class TempTracker(object):

    def __init__(self):
        # for mode
        self.mode = None
        self.max_occurrences = 0
        self.occurrences = [0] * (111)

        # for mean
        self.total_numbers = 0
        self.total_sum = 0.0
        self.mean = None

        # for min / max
        self.min_temp = float('inf')
        self.max_temp = float('-inf')

    def __repr__(self):
        return "<Mode {} Mean {} Min {} Max {}>".format(self.mode,
                                                        self.mean,
                                                        self.min_temp,
                                                        self.max_temp)

    def insert(self, new_temp):
        # for mode
        self.occurrences[new_temp] += 1
        if self.occurrences[new_temp] > self.max_occurrences:
            self.mode = new_temp
            self.max_occurrences = self.occurrences[new_temp]

        # for mean
        self.total_numbers += 1
        self.total_sum += new_temp
        self.mean = self.total_sum / self.total_numbers

        # for min and max
        if temperature > self.max_temp:
            self.max_temp = new_temp
        if temperature < self.min_temp:
            self.min_temp = new_temp

    def get_max(self):
        return self.max_temp

    def get_min(self):
        return self.min_temp

    def get_mean(self):
        return self.mean

    def get_mode(self):
        return self.mode