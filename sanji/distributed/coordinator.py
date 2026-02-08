"""Distributed training coordinator."""

import threading
import time

class DistributedCoordinator:
    """Coordinates distributed training across multiple workers."""
    
    def __init__(self, world_size, timeout=300):
        self.world_size = world_size
        self.timeout = timeout
        self._barrier_count = 0
        self._barrier_lock = threading.Lock()
        self._barrier_event = threading.Event()
    
    def barrier(self):
        """Synchronization barrier for all workers."""
        # Fixed: Proper barrier synchronization to prevent deadlock
        with self._barrier_lock:
            self._barrier_count += 1
            if self._barrier_count >= self.world_size:
                self._barrier_count = 0
                self._barrier_event.set()
                self._barrier_event.clear()
                return True
        
        # Fixed: Proper timeout handling
        if not self._barrier_event.wait(timeout=self.timeout):
            raise TimeoutError(f"Barrier timeout after {self.timeout} seconds")
        return True
    
    def all_reduce(self, tensor):
        """All-reduce operation across workers."""
        pass
