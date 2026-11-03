# OpenTofu Root: Local KVM Hypervisor (Libvirt / Talos)
# Architecture: 3 Control Plane (HA etcd) + 3 Worker Nodes

terraform {
  required_version = ">= 1.8.0"
  required_providers {
    libvirt = {
      source  = "dmacvicar/libvirt"
      version = "~> 0.8.0"
    }
  }
}

# Environment-specific variables and module calls will be defined here
