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

### 📝 Complete FIXME List

- [ ] **benchmarks/memory_test.py:22** - GPU memory not released after test
- [ ] **benchmarks/speed_test.py:11** - Warmup iterations hardcoded
- [ ] **sanji/models/transformer.py:19** - Attention mask not applied correctly
- [ ] **sanji/models/transformer.py:32** - Position encoding overflow for long sequences
- [ ] **sanji/utils/checkpoint.py:17** - File handle not closed properly
- [ ] **sanji/utils/checkpoint.py:26** - Incomplete state dict saving
- [ ] **sanji/utils/logging.py:14** - Logger handler leak

## 🤝 Contributing

1. Pick a FIXME item from the list above
2. Fix the issue
3. Test your fix
4. Update this README when FIXMEs are resolved (change [ ] to [x] status)
