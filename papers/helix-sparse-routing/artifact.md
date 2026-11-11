# HELIX: Sparse Routing for Long-Context Transformers

- Record: MRD-2025-0142
- Version: v2 (posted 2025-05-02)
- Authors: Priya Raghunathan, Tomas Eklund, Mei Lin
- Topic: efficient long-context attention
- Review state: approved

## Abstract
HELIX introduces a sparse routing layer that activates only a small subset of context blocks per token. On 128k-token retrieval and reasoning benchmarks it matches dense attention accuracy while cutting context attention cost by roughly two thirds.

## Code
https://github.com/knobbyintens/meridian-code-helix-a91c4

<!-- artifact-key: MRD-2025-0142-v2-473cdb2736 -->
