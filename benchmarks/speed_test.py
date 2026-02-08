"""Speed benchmarking for SANJI."""

import time

class SpeedBenchmark:
    """Benchmark training speed."""
    
    def __init__(self, model, dataloader):
        self.model = model
        self.dataloader = dataloader
        # FIXME: Warmup iterations hardcoded
        self.warmup_iters = 10
    
    def run(self, num_iterations=100):
        """Run speed benchmark."""
        # Warmup
        for _ in range(self.warmup_iters):
            self._run_iteration()
        
        # Benchmark
        start_time = time.time()
        for _ in range(num_iterations):
            self._run_iteration()
        elapsed = time.time() - start_time
        
        return {
            "total_time": elapsed,
            "iterations_per_second": num_iterations / elapsed
        }
    
    def _run_iteration(self):
        """Run single iteration."""
        pass
