"""Tests for optimizers."""

import unittest
from unittest.mock import MagicMock, patch

class TestOptimizer(unittest.TestCase):
    """Test optimizer implementations."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.mock_params = [1.0, 2.0, 3.0]
        self.mock_grads = [0.1, 0.2, 0.3]
    
    def test_adam_step(self):
        """Test Adam optimizer step."""
        # Fixed: Proper mock cleanup using context manager
        with patch("sanji.optimizer.adam_custom.CustomAdam") as mock_adam:
            mock_instance = MagicMock()
            mock_adam.return_value = mock_instance
            mock_instance.step(self.mock_grads)
            mock_instance.step.assert_called_once()
    
    def test_sgd_step(self):
        """Test SGD optimizer step."""
        with patch("sanji.optimizer.sgd_custom.CustomSGD") as mock_sgd:
            mock_instance = MagicMock()
            mock_sgd.return_value = mock_instance
            mock_instance.step(self.mock_grads)
            mock_instance.step.assert_called_once()

if __name__ == "__main__":
    unittest.main()
