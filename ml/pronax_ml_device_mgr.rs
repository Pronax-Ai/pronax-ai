//! ProNax AI - Device Manager
//! Hardware abstraction layer for 3D spatial AI engine

use std::collections::HashSet;
use std::fmt::Display;
use std::sync::atomic::{AtomicBool, AtomicU64, AtomicUsize, Ordering};
use std::sync::{Arc, Mutex, RwLock};

use crate::pronax_ml_backend_trait::{DeviceType, ExecutionCoord3D, FlashAttentionMode};

/// Device manager for 3D spatial AI operations
pub struct DeviceManager {
    devices: HashSet<Device>,
    default_device: Option<Device>,
}

impl DeviceManager {
    pub fn new() -> Self {
        Self {
            devices: HashSet::new(),
            default_device: None,
        }
    }

    pub fn add_device(&mut self, device: Device) {
        self.devices.insert(device);
    }

    pub fn get_default_device(&self) -> Option<&Device> {
        self.default_device.as_ref()
    }
}

/// Hardware device representation
#[derive(Debug, Clone, PartialEq, Eq, Hash)]
pub struct Device {
    pub device_type: DeviceType,
    pub device_id: String,
    pub memory_size: u64,
}

impl Display for Device {
    fn fmt(&self, f: &mut std::fmt::Formatter<'_>) -> std::fmt::Result {
        write!(f, "{} ({})", self.device_id, self.device_type)
    }
}

/// Device capabilities for 3D spatial operations
#[derive(Debug, Clone)]
pub struct DeviceCapabilities {
    pub supports_3d_spatial: bool,
    pub flash_attention_mode: FlashAttentionMode,
    pub max_tensor_size: u64,
}

impl Default for DeviceCapabilities {
    fn default() -> Self {
        Self {
            supports_3d_spatial: true,
            flash_attention_mode: FlashAttentionMode::Standard,
            max_tensor_size: 1024 * 1024 * 1024, // 1GB
        }
    }
}