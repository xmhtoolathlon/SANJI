"""Metrics utilities for SANJI."""

class MetricsCalculator:
    """Calculate various training metrics."""
    
    def __init__(self):
        self.total_correct = 0
        self.total_samples = 0
        self.true_positives = 0
        self.false_positives = 0
        self.false_negatives = 0
    
    def update(self, predictions, labels):
        """Update metrics with new batch."""
        for pred, label in zip(predictions, labels):
            self.total_samples += 1
            if pred == label:
                self.total_correct += 1
                if label == 1:
                    self.true_positives += 1
            else:
                if pred == 1:
                    self.false_positives += 1
                else:
                    self.false_negatives += 1
    
    def accuracy(self):
        """Calculate accuracy."""
        # Fixed: Handle division by zero
        if self.total_samples == 0:
            return 0.0
        return self.total_correct / self.total_samples
    
    def f1_score(self):
        """Calculate F1 score."""
        # Fixed: Correct F1 score computation
        precision = self._precision()
        recall = self._recall()
        if precision + recall == 0:
            return 0.0
        return 2 * (precision * recall) / (precision + recall)
    
    def _precision(self):
        if self.true_positives + self.false_positives == 0:
            return 0.0
        return self.true_positives / (self.true_positives + self.false_positives)
    
    def _recall(self):
        if self.true_positives + self.false_negatives == 0:
            return 0.0
        return self.true_positives / (self.true_positives + self.false_negatives)
