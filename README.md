# SANJI Development Repository

> 🔧 **Feature Branch** - This is the feature development repository for SANJI (Scalable Autonomous Neural Joint Intelligence)

## About SANJI

SANJI is a distributed neural network training framework designed for scalable multi-node training with automatic resource allocation. This repository contains the core implementation and development work.

## 🔧 Development Status

This repository is under active development. Several components have known issues marked with FIXME comments that require attention.

## 🚀 Quick Start

⚠️ **Note**: This feature version has known issues. Several components are marked with FIXME and require fixes before production use.

```bash
# Clone the repository
git clone <repository-url>
cd SANJI

# Install dependencies
pip install -r sanji/requirements.txt

# Note: Check FIXME list below for known issues
```

## 📁 Repository Structure

```
SANJI/
├── sanji/                 # Core framework
│   ├── distributed/       # Distributed training (⚠️ Memory leak issues)
│   ├── optimizer/         # Custom optimizers (⚠️ Gradient overflow bugs)
│   └── ...
├── configs/               # Configuration files
├── benchmarks/            # Performance benchmarks
├── tests/                 # Unit tests
└── README.md              # This file
```

## ⚠️ Development Notes

- This is a **feature version** with known issues
- Many functions contain FIXME markers indicating bugs or issues
- Memory management in distributed components needs attention
- Gradient computation has known overflow issues


### 🔴 Critical Priority FIXMEs

- **Memory Leaks**: Distributed training components have memory issues
- **Gradient Overflow**: Optimizer gradient computation bugs
- **Deadlock Issues**: Multi-process synchronization problems
- **Data Loading**: Race conditions in parallel data loading

### 🐛 Complete FIXME List

- [ ] **benchmarks/memory_test.py:67** - GPU memory not released after test
- [ ] **benchmarks/speed_test.py:23** - Warmup iterations hardcoded
- [x] **sanji/data/loader.py:67** - Race condition in prefetch queue
- [x] **sanji/data/loader.py:89** - Buffer overflow with large datasets
- [x] **sanji/data/sampler.py:23** - Incorrect shuffle seed propagation
- [x] **sanji/distributed/coordinator.py:112** - Deadlock in barrier synchronization
- [x] **sanji/distributed/coordinator.py:156** - Incorrect timeout handling
- [x] **sanji/distributed/worker.py:45** - Memory leak in worker initialization
- [x] **sanji/distributed/worker.py:89** - Race condition in task queue
- [ ] **sanji/models/transformer.py:145** - Attention mask not applied correctly
- [ ] **sanji/models/transformer.py:189** - Position encoding overflow for long sequences
- [x] **sanji/optimizer/adam_custom.py:34** - Gradient overflow for large batches
- [x] **sanji/optimizer/adam_custom.py:78** - Missing epsilon check
- [x] **sanji/optimizer/sgd_custom.py:45** - Weight decay applied incorrectly
- [ ] **sanji/utils/checkpoint.py:56** - File handle not closed properly
- [ ] **sanji/utils/checkpoint.py:78** - Incomplete state dict saving
- [ ] **sanji/utils/logging.py:34** - Logger handler leak
- [x] **sanji/utils/metrics.py:112** - Division by zero in accuracy calculation
- [x] **sanji/utils/metrics.py:145** - Incorrect F1 score computation
- [x] **tests/test_distributed.py:89** - Flaky test due to timing issues
- [x] **tests/test_optimizer.py:45** - Mock objects not cleaned up

## 🤝 Contributing

1. Pick a FIXME item from the list above
2. Fix the issue
3. Test your fix
4. Update this README when FIXMEs are resolved (change [ ] to [x] status)
