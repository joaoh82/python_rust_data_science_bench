Rust and Python - Data Science Benchmark
===
Testing the performance of Rust and Python on a simple data science task.

Tools and Requirements:
* https://github.com/dgrunwald/rust-cpython
* https://github.com/PyO3/setuptools-rust
* https://docs.rs/crate/pyo3/0.13.1
* brew install gnu-time

Importante Sources:
* https://gist.github.com/ssokolow/34ce62a0d98054810c488a7f0d3fd4e0
* https://www.crowdstrike.com/blog/data-science-test-drive-of-rust-programming-language/


Results:

```
# Python invoking pure Rust
$ gtime python benchmark.py
3.00user 0.61system 0:02.01elapsed 180%CPU (0avgtext+0avgdata 60240maxresident)k
0inputs+0outputs (5major+15215minor)pagefaults 0swaps

# Python with Data Science Libraries
$ gtime python benchmark.py
5.85user 1.28system 0:05.84elapsed 122%CPU (0avgtext+0avgdata 151744maxresident)k
0inputs+0outputs (2133major+35969minor)pagefaults 0swaps

# Pure Python
$ gtime python benchmark.py
83.88user 0.95system 1:23.82elapsed 101%CPU (0avgtext+0avgdata 60004maxresident)k
0inputs+0outputs (2129major+13035minor)pagefaults 0swaps
```