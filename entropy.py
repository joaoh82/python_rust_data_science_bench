import math
import numpy as np
from scipy.stats import entropy as scipy_entropy
import rust_entropy_lib
import numba
import numexpr as ne

def compute_entropy_pure_python(data):
    """Compute entropy on bytearray `data`."""
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

@numba.njit
def compute_entropy_numpy_numba(data):
    """Compute entropy on bytearray `data`."""
    counts = np.zeros(256, dtype=np.uint64)
    entropy = 0.0
    length = len(data)

    for byte in data:
        counts[byte] += 1

    for count in counts:
        if count != 0:
            probability = float(count) / length
            entropy -= probability * np.log2(probability)

    return entropy

def compute_entropy_scipy_numpy(data):
    """Compute entropy on bytearray `data` with SciPy and NumPy."""
    counts = np.bincount(bytearray(data), minlength=256)
    return scipy_entropy(counts, base=2)


def compute_entropy_numpy(data):
    """Compute entropy on bytearray `data` with SciPy and NumPy."""
    counts = np.bincount(bytearray(data), minlength=256)
    prob = counts[counts != 0].astype(float) / len(data)
    entropy = -np.sum(prob * np.log2(prob))
    return entropy

def compute_entropy_numpy_numexpr(data):
    """Compute entropy on bytearray `data` with SciPy and NumPy."""
    counts = np.bincount(bytearray(data), minlength=256)
    prob = counts[counts != 0].astype(float) / len(data)
    log2 = np.log(2)
    entropy = ne.evaluate("sum(-1*prob * log(prob)/log2, 0)")
    # entropy = ne.evaluate("prob * log(prob)").sum() * -1/np.log(2)
    return entropy

def compute_entropy_rust_from_python(data):
    """Compute entropy on bytearray `data` with Rust."""
    return rust_entropy_lib.compute_entropy_cpython(data)

# ### BENCHMARKS ###
# generate some random bytes to test w/ NumPy
NUM = 1000000
VAL = np.random.randint(0, 256, size=(NUM, ), dtype=np.uint8)

def test_pure_python(benchmark):
    """Test pure Python."""
    benchmark(compute_entropy_pure_python, VAL)

def test_pure_numpy_numba(benchmark):
    """Test pure Python."""
    benchmark(compute_entropy_numpy_numba, VAL)

def test_python_scipy_numpy(benchmark):
    """Test pure Python with SciPy."""
    benchmark(compute_entropy_scipy_numpy, VAL)

def test_python_numpy(benchmark):
    """Test pure Python with SciPy."""
    benchmark(compute_entropy_numpy, VAL)

def test_python_numpy_numexpr(benchmark):
    """Test pure Python with SciPy."""
    benchmark(compute_entropy_numpy_numexpr, VAL)

def test_rust(benchmark):
    """Test Rust implementation called from Python."""
    benchmark(compute_entropy_rust_from_python, VAL)
