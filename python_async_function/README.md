# <p align = "center">🐍 Python - Async Function</p>
## <p align="center">🎓 Holberton School Program - Lille</p>

<img src="https://i.imgur.com/DRPXtkk.jpg" width='100%' />

### Learning Objectives
- `async` and `await` syntax
- How to execute an async program with `asyncio`
- How to run concurrent coroutines
- How to create `asyncio` tasks
- How to use the `random` module

### Tasks
- **0-basic_async_syntax.py** : synchronous coroutine that takes in an integer argument (`max_delay`, with a default value of 10) named `wait_random` that waits for a random delay between 0 and `max_delay` (included and float value) seconds and eventually returns it
- **1-concurrent_coroutines.py** : import `wait_random` from the previous python file and write an async routine called `wait_n` that takes in 2 int arguments (in this order): `n` and `max_delay`. You will spawn `wait_random` `n` times with the specified `max_delay`, `wait_n` should return the list of all the delays (float values)
- **2-measure_runtime.py** : create a `measure_time` function with integers `n` and `max_delay` as arguments that measures the total execution time for `wait_n(n, max_delay)`, and returns `total_time / n`. Your function should return a float
- **3-tasks.py** : function `task_wait_random` that takes an integer `max_delay` and returns a `asyncio.Task`
- **4-tasks.py** : take the code from `wait_n` and alter it into a new function `task_wait_n`. The code is nearly identical to `wait_n` except `task_wait_random` is being called
