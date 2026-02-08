"""Custom Adam optimizer implementation."""

import math

class CustomAdam:
    """Custom Adam optimizer with improvements."""
    
    def __init__(self, params, lr=0.001, betas=(0.9, 0.999), eps=1e-8):
        self.params = list(params)
        self.lr = lr
        self.beta1, self.beta2 = betas
        self.eps = eps
        self.t = 0
        self.m = [0] * len(self.params)
        self.v = [0] * len(self.params)
    
    def step(self, grads):
        """Perform optimization step."""
        self.t += 1
        
        # Fixed: Added gradient clipping to prevent overflow
        max_grad_norm = 1.0
        total_norm = math.sqrt(sum(g**2 for g in grads))
        clip_coef = max_grad_norm / (total_norm + 1e-6)
        if clip_coef < 1:
            grads = [g * clip_coef for g in grads]
        
        for i, (param, grad) in enumerate(zip(self.params, grads)):
            self.m[i] = self.beta1 * self.m[i] + (1 - self.beta1) * grad
            self.v[i] = self.beta2 * self.v[i] + (1 - self.beta2) * grad**2
            
            m_hat = self.m[i] / (1 - self.beta1**self.t)
            v_hat = self.v[i] / (1 - self.beta2**self.t)
            
            # Fixed: Proper epsilon check for numerical stability
            denom = math.sqrt(v_hat) + self.eps
            if denom < self.eps:
                denom = self.eps
            
            param -= self.lr * m_hat / denom
