# <p align = "center">🐍 Python - Async Comprehension</p>
## <p align="center">🎓 Holberton School Program - Lille</p>

<img src="https://i.imgur.com/DRPXtkk.jpg" width='100%' />

### Learning Objectives
- How to write an asynchronous generator
- How to use async comprehensions
- How to type-annotate generators

### Tasks
- **0-async_generator.py** : coroutine called `async_generator` that takes no arguments
- **1-async_comprehension.py** : Import `async_generator` from the previous task and then write a coroutine called `async_comprehension` that takes no arguments. The coroutine will collect 10 random numbers using an async comprehensing over `async_generator`, then return the 10 random numbers.
- **2-measure_runtime.py** : Import `async_comprehension` from the previous file and write a `measure_runtime` coroutine that will execute `async_comprehension` four times in parallel using `asyncio.gather`. `measure_runtime` should measure the total runtime and return it.


