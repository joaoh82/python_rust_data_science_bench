Rust and Python - Data Science Benchmark
===
Testing the performance of Rust and Python on a simple data science task.

Tools and Requirements:
* https://github.com/dgrunwald/rust-cpython
* https://github.com/PyO3/setuptools-rust
* https://docs.rs/crate/pyo3/0.13.1
* brew install gnu-time
* virtualenv
* Python 3.7.4


Importante Sources:
* https://gist.github.com/ssokolow/34ce62a0d98054810c488a7f0d3fd4e0


Running the tests:
```
$ virtualenv env
$ source venv/bin/activate
$ pip install
```

Results:

```
# Python invoking pure Rust
$ gtime python entropy_rust.py
3.00user 0.61system 0:02.01elapsed 180%CPU (0avgtext+0avgdata 60240maxresident)k
0inputs+0outputs (5major+15215minor)pagefaults 0swaps

# Python with Data Science Libraries
$ gtime python entropy_python_data_science.py
5.85user 1.28system 0:05.84elapsed 122%CPU (0avgtext+0avgdata 151744maxresident)k
0inputs+0outputs (2133major+35969minor)pagefaults 0swaps

# Pure Python
$ gtime python entropy_pure_python.py
83.88user 0.95system 1:23.82elapsed 101%CPU (0avgtext+0avgdata 60004maxresident)k
0inputs+0outputs (2129major+13035minor)pagefaults 0swaps
```

Benchmark Tests:
```
$ pytest entropy.py
--------------------------------------------------------------------------------------------------- benchmark: 3 tests ---------------------------------------------------------------------------------------------------
Name (time in us)                    Min                     Max                    Mean                StdDev                  Median                   IQR            Outliers         OPS            Rounds  Iterations
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
test_rust                       405.5010 (1.0)        1,275.1050 (1.0)          461.5349 (1.0)         95.0086 (1.0)          421.8365 (1.0)         36.5445 (1.0)       214;289  2,166.6835 (1.0)        1996           1
test_python_scipy_numpy       2,055.4330 (5.07)       7,084.0560 (5.56)       2,844.4945 (6.16)       731.1409 (7.70)       2,717.1220 (6.44)       604.1060 (16.53)        15;5    351.5563 (0.16)        155           1
test_pure_python            104,375.9260 (257.40)   110,629.1110 (86.76)    106,744.7134 (231.28)   2,456.0260 (25.85)    105,233.1660 (249.46)   3,715.2733 (101.66)        2;0      9.3681 (0.00)          9           1
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Legend:
  Outliers: 1 Standard Deviation from Mean; 1.5 IQR (InterQuartile Range) from 1st Quartile and 3rd Quartile.
  OPS: Operations Per Second, computed as 1 / Mean
```