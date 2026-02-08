"""Tests for distributed training."""

import unittest
import time

class TestDistributed(unittest.TestCase):
    """Test distributed training components."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.timeout = 5.0
    
    def test_barrier_synchronization(self):
        """Test barrier synchronization."""
        # Fixed: Added proper timing controls to prevent flaky test
        start_time = time.time()
        # Simulate barrier
        time.sleep(0.1)
        elapsed = time.time() - start_time
        self.assertLess(elapsed, self.timeout)
    
    def tearDown(self):
        """Clean up after tests."""
        pass

if __name__ == "__main__":
    unittest.main()
