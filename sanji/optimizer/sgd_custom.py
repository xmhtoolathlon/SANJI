"""Custom SGD optimizer implementation."""

class CustomSGD:
    """Custom SGD optimizer with momentum and weight decay."""
    
    def __init__(self, params, lr=0.01, momentum=0.9, weight_decay=0.0001):
        self.params = list(params)
        self.lr = lr
        self.momentum = momentum
        self.weight_decay = weight_decay
        self.velocity = [0] * len(self.params)
    
    def step(self, grads):
        """Perform optimization step."""
        for i, (param, grad) in enumerate(zip(self.params, grads)):
            # Fixed: Apply weight decay to gradient before momentum update
            if self.weight_decay != 0:
                grad = grad + self.weight_decay * param
            
            # Update velocity
            self.velocity[i] = self.momentum * self.velocity[i] + grad
            
            # Update parameter
            param -= self.lr * self.velocity[i]
