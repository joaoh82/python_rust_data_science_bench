import entropy

# test.img is binary file generate with
# dd if=/dev/zero of=test.img bs=1024 count=0 seek=$[1024*10] for 10Mb
# just a set of random bytes generate for testing purposes
with open('test.img', 'rb') as f:
    DATA = f.read()

# Here we just repeat the calculations 100 times, for our Python using Rust
for _ in range(100):
    entropy.compute_entropy_rust_from_python(DATA)