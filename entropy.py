import math
import numpy as np
from scipy.stats import entropy as scipy_entropy
import rust_entropy_lib

def compute_entropy_pure_python(data):
    """Compute entropy on byte array `data`."""
    counts = [0] * 256
    entropy = 0.0
    length = len(data)

    for byte in data:
        counts[byte] += 1

    for count in counts:
        if count != 0:
            probability = float(count) / length
            entropy -= probability * math.log(probability, 2)

    return entropy

def compute_entropy_scipy_numpy(data):
    """Compute entropy on byte array `data` with SciPy and NumPy."""
    counts = np.bincount(bytearray(data), minlength=256)
    return scipy_entropy(counts, base=2)

def compute_entropy_rust_from_python(data):
    """Compute entropy on byte array `data` with Rust."""
    return rust_entropy_lib.compute_entropy_cpython(data)

# ### BENCHMARKS ###
# generate some random bytes to test w/ NumPy
NUM = 1000000
VAL = np.random.randint(0, 256, size=(NUM, ), dtype=np.uint8)

def test_pure_python(benchmark):
    """Test pure Python."""
    benchmark(compute_entropy_pure_python, VAL)

def test_python_scipy_numpy(benchmark):
    """Test pure Python with SciPy."""
    benchmark(compute_entropy_scipy_numpy, VAL)

def test_rust(benchmark):
    """Test Rust implementation called from Python."""
    benchmark(compute_entropy_rust_from_python, VAL)