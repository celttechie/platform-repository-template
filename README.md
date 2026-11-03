# Platform Repository Template (`platform-repository-template`)

[![CI Status](https://img.shields.io/badge/CI-Passing-brightgreen.svg)](#)
[![Security Scan](https://img.shields.io/badge/Security-Gitleaks%20Active-blue.svg)](#)
[![Architecture](https://img.shields.io/badge/Pattern-Decoupled%20Monorepo-orange.svg)](#)
[![Multi-Cloud](https://img.shields.io/badge/Target-KVM%20%7C%20AWS%20%7C%20GCP-teal.svg)](#)

A standardized, enterprise-grade repository blueprint for **Platform Engineering**, **Site Reliability Engineering (SRE)**, and **Multi-Cloud Kubernetes Platforms**.

Built to deliver **clonable, deterministic deployments** with strict shift-left security, zero secret leakage, and living Architecture Decision Records (ADRs).

---

## 🏛️ Architecture Overview

This template enforces a strict **Three-Tier Decoupled Monorepo** architecture:

```
platform-repository-template/
├── infra/                  # TIER 1: Infrastructure as Code (OpenTofu / Terraform)
│   ├── modules/            # Reusable modules (VPC, NodePools, IAM OIDC)
│   └── environments/       # Environment roots (local-kvm, aws, gcp)
│
├── platform/               # TIER 2: Kubernetes Platform Services (Helm / Kustomize)
│   ├── ingress/            # Ingress Controllers & Gateways (Envoy / Cilium)
│   ├── autoscaling/        # Event-driven autoscaling (KEDA + Metrics-Server)
│   ├── storage/            # Distributed CSI / Operators (Longhorn, CloudNative-PG)
│   └── observability/      # Telemetry & Monitoring (Prometheus + Grafana)
│
├── workloads/              # TIER 3: Applications & Resilience Harness
│   ├── demo-app/           # Multi-replica microservices with Anti-Affinity & PDB
│   ├── load-tests/         # Synthetic traffic generation (k6 / Locust)
│   └── chaos-drills/       # Automated node/network failure injection scripts
│
├── docs/                   # Living Documentation Architecture
│   ├── IMPLEMENTATION_PLAN.md # Real-time project roadmap & checklist
│   ├── adr/                # Architecture Decision Records (ADR 0001, 0002...)
│   ├── security/           # Threat model & zero-leakage security posture
│   └── operations/         # Demonstration runbooks & media recording guides
│
├── scripts/                # SRE Automation Tooling (doctor.py, capture scripts)
└── Makefile                # Unified Developer & CI/CD Interface
```

---

## ⚡ Quick Start

### 1. Initialize Python Tooling & Linters
Create an isolated virtual environment and install linters and testing tools (`yamllint`, `flake8`, `pre-commit`, `pytest`) defined in `pyproject.toml` (accelerated with `uv` if present):
```bash
make venv
```

### 2. Pre-Flight Environment Audit
Verify your workstation has the required CLI binaries, virtualization flags, and cloud tooling:
```bash
make doctor
```

### 3. Run Local Quality & Security Gates
Run code formatters, YAML linters, secret detection, and unit tests:
```bash
make ci
```

### 4. Deploy Stack to Target Environment
```bash
# Target: Local KVM Hypervisor ($0 cost)
make deploy TARGET=local-kvm

# Target: Ephemeral AWS EKS (Spot NodeGroup with cost guardrails)
make deploy TARGET=aws

# Target: Ephemeral GCP GKE (Zonal free tier with Spot NodePool)
make deploy TARGET=gcp
```

### 5. Run Automated Demo & Chaos Resilience Drill
```bash
make demo
```

---

## 🚀 Using This Template

### Via GitHub Web UI
Click the green **"Use this template"** button at the top of this repository on GitHub to generate a new clean repository.

### Via GitHub CLI (`gh`)
```bash
gh repo create my-platform-project \
  --template celttechie/platform-repository-template \
  --public \
  --clone
```

---

## 🛡️ Security Posture

* **Zero Secret Leakage:** Integrated `gitleaks` pre-commit hooks and GitHub Actions workflows block private keys, tokens, and cloud credentials before they touch git history.
* **Identity Federation:** Pods authenticate to cloud APIs via **EKS Pod Identity** or **GCP Workload Identity**—never long-lived static API keys.
* **Restricted Workloads:** Containers run as non-root with read-only root filesystems and dropped capabilities.

---

## 📚 Documentation Reference

* **[Implementation Plan & Roadmap](docs/IMPLEMENTATION_PLAN.md)**
* **[Architecture Decision Records (ADRs)](docs/adr/0001-record-architecture-decisions.md)**
* **[Security Architecture Model](docs/security/security-model.md)**
* **[Demonstration & Media Recording Runbook](docs/operations/demonstration-runbook.md)**
* **[Homelab & Cross-Project Master Index](file:///home/bjarrett/Projects/lab-docs/PROJECT_INDEX.md)**
