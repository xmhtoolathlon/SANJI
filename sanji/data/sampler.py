"""Data sampler module for SANJI framework."""

import random

class RandomSampler:
    """Random sampler with proper seed propagation."""
    
    def __init__(self, data_source, seed=None):
        self.data_source = data_source
        # Fixed: Properly propagate seed to all workers
        self.seed = seed if seed is not None else random.randint(0, 2**32-1)
        self._rng = random.Random(self.seed)
    
    def __iter__(self):
        indices = list(range(len(self.data_source)))
        self._rng.shuffle(indices)
        return iter(indices)
    
    def __len__(self):
        return len(self.data_source)
