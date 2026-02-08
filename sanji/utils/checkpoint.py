"""Checkpoint utilities for SANJI."""

import json
import os

class CheckpointManager:
    """Manages model checkpoints."""
    
    def __init__(self, checkpoint_dir):
        self.checkpoint_dir = checkpoint_dir
        os.makedirs(checkpoint_dir, exist_ok=True)
    
    def save(self, state_dict, filename):
        """Save checkpoint to file."""
        filepath = os.path.join(self.checkpoint_dir, filename)
        
        # FIXME: File handle not closed properly
        f = open(filepath, 'w')
        json.dump(state_dict, f)
        # Missing f.close()
    
    def load(self, filename):
        """Load checkpoint from file."""
        filepath = os.path.join(self.checkpoint_dir, filename)
        
        # FIXME: Incomplete state dict saving
        with open(filepath, 'r') as f:
            state_dict = json.load(f)
        # Missing validation of loaded state
        return state_dict
