"""."""


class ID3:
    """description."""

    def __init__(self):
        """."""
        self.root = None
        self.trainning_set = None

    def mine(self, node, trainning_set):
        """."""
        root = trainning_set.getBestEntropy()
        if trainning_set.hasOnlyOneValue:
            return trainning_set.getMoreFrequentValue()
        else:
            for n in root.getBranches():
                self.mine(n, trainning_set.subSet(n))
        return root
