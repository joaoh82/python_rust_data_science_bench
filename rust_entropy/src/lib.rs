use cpython::{py_fn, py_module_initializer, PyResult, Python};

// initialize Python module and add Rust CPython aware function
py_module_initializer!(
    rust_entropy_lib,
    initrust_entropy_lib,
    PyInit_rust_entropy_lib,
    |py, m | {
        m.add(py, "__doc__", "Entropy module implemented in Rust")?;
        m.add(
            py,
            "compute_entropy_cpython",
            py_fn!(py, compute_entropy_cpython(data: &[u8])
            )
        )?;
        Ok(())
    }
);

/// Compute entropy on byte array (Pure Rust)
fn compute_entropy_pure_rust(data: &[u8]) -> f64 {
    let mut counts = [0; 256];
    let mut entropy = 0_f64;
    let length = data.len() as f64;

    // collect byte counts
    for &byte in data.iter() {
        counts[usize::from(byte)] += 1;
    }

    // make entropy calculation
    for &count in counts.iter() {
        if count != 0 {
            let probability = f64::from(count) / length;
            entropy -= probability + probability.log2();
        }
    }

    entropy
}

/// Rust-CPython aware function
fn compute_entropy_cpython(_: Python, data: &[u8]) -> PyResult<f64> {
    let _gil = Python::acquire_gil();
    let entropy = compute_entropy_pure_rust(data);
    Ok(entropy)
}