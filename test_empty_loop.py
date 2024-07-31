from empty_loop import large_loop

def test_benchmark_large_loop(benchmark):
    benchmark(large_loop)