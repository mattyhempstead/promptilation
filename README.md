# Promptilation

What if instead of writing code, you wrote prompts?


If rather than writing code like
```python
for i in range(1,11):
	print(i)
print("Done")
```
you wrote, compiled, and executed files containing prompts like
```
print all the numbers from 1 to 10
print "Done"
```
and you never needed to understand the "complexity" of the actual source code.

Let's call this process promptilation. A compilation-like process that takes a program specified as a list of prompts (or arbitrarily abstract pseudocode) to an LLM, which will translate the prompts into an executable language like Python. The user can then execute the source code file without ever having to understand or even read it.


Promptilation is compilation, declarative programming, and programming languages, all taken to its natural (language) limit.

It's also not very good. More of a idea than any actual product, at least for now.


## Usage
Instructions via `python promptcc --help`

Usage is inspired by C compilers like `gcc`.

Promptilation currently applies only to a single file (`.promptpy`) that is translated into a single Python (`.py`) file. It would not be hard to extend this to multiple files in or multiple files out.


To perform promptilation on a single file, execute `promptcc` and supply an input file of type `.promptpy` via the path specified by `INPUT_FILE_PATH`. This will produce a file at `OUTPUT_DIR_PATH` of type `.py`. If no `OUTPUT_DIR_PATH` is specified, `./build` will be used as a default.

`python promptcc --input-file INPUT_FILE_PATH --output-dir OUTPUT_DIR_PATH`

e.g. `python promptcc --input-file input/prime.promptpy`

You should then be able to execute the file.

`python ./build/prime.py`



## Inspiration

The history of programming languages looks like a long list of increasingly abstract languages. Each language is approximately compiled down to those lower in the hierarchy until we eventually reach machine code for the specific hardware.

The advent of good code generation via LLMs has opened up the possibility for an entirely new layer, which I'll call the prompting layer.

Unless you have been living under a read lock, you would have already tried working at the prompting layer when you asked ChatGPT to generate some code given a natural language description that you wrote.

Promptilation is about wondering what would happen if we viewed this process as a kind of "compilation" step in the same way you might compile C files to a binary, rather than as simply a coding assistant. It's essentially declarative programming with no theoretical limits to how much control flow you choose to abstract. Any details that are missing will simply be filled in with a best-guess.

I suppose the documentation for promptilation would look like something like "Any missing details will be filled in via a best guess. If you want the code to work in a particular way, you should state it."



## Issues

It its current form, promptilation is a mostly useless paradigm. It is not much better (arguably worse) that just asking ChatGPT/Copilot to generate code and storing the prompt alongside as documentation.

But I claim promptilation is more of a perspective for a future theoretical paradigm, than it is a solution. So far, all I have done is build a crappy seed for what could eventually represent an new way of writing programs.

There are numerous issues that need to be resolved before it is of any real use. Some of these are out of our control (LLM accuracy), but many are not (UX).

#### Accuracy
Regarding accuracy, I personally wouldn't trust an LLM to generate much more than 100 lines of code without me validating it. However, assuming LLM performance continues to increase we might soon reach the point where this is no longer a practical issue (in the rare cases an error occurs, you just "debug" the compiled source).

#### Non-determinism
This particular compilation process is also not deterministic, although many LLMs let you provide a seed so determinism can be forced if one desires. This probably won't hold over new releases of LLMs.

#### UX
In my opinion, the primary limitation stopping real use cases is UX.

I see no fundamental reason why we can't write and read code for codebases at the level of prompts, particularly when accuracy is of no real concern relative to the provided specificity of the prompt. Even still, a really high quality prompt debugger (perhaps using LLM summarisation) should resolve this.

Ideally, the programmer should only need to specify the details that matter. One encompassing perspective of a code base is just a large collection of nested interfaces communicating with eachother. Once the interface requirements have been specified, the programmer does not really care how it works.

The risk here is that the user does not specify the requirements correctly. In that case, perhaps the compiler could throw a kind of specificity warning. Maybe like "On line 22 you asked for x to be a random integer, what kind of range were you hoping for?". The response could then be stored for future use, possibly by updating the source prompt.

This iterative feedback loop appears quite important for generating code with ChatGPT, so you would need solve this for promptilation.



### Actual short term use cases?

There is some potential for promptilation as an educational tool.

Rather than needing to learn syntax, people learning to program can just start by writing prompts which are compiled and executed directly.

If something went wrong, they would be encouraged the fundamental lesson of programming; that you need to tell the computer exactly what to do.

I asked a friend who hadn't programmed before if they could guess what a given promptiled program would do, and then what the original prompt file looks like. They only understood the prompt file, although some forgivably some explanation regarding.




## Examples

The following are some real examples of promptilation outputs.

See `./examples/input`

### Simple Code

```
do this a random number of times between 1 and 10 (uniformly distributed)
    print "Hello, World!"
```

promptiles to

```python
import random

# Generate a random number between 1 and 10
num_times = random.randint(1, 10)

# Print "Hello, World!" a random number of times
for _ in range(num_times):
    print("Hello, World!")
```


### Function Calling

```
lets call the following code "hello"
    print all the numbers from 1 to 10 on a single line
    (make sure you have a newline at the end of the above instruction)

run the hello code 10 times
```

promptiles to

```python
# Define a function to print numbers from 1 to 10 on a single line with a newline at the end
def hello():
    print(*range(1, 11), sep=' ', end='\n')

# Run the hello code 10 times
for _ in range(10):
    hello()
```


### Harder Function Calling

```
read a number as the first argument (call the variable "N")

function is_prime(n): bool
    return whether n is prime

for all the numbers up to and including N:
    if that number is_prime then print it
```

promptiles to

```python
from math import isqrt

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

N = int(input("Enter a number: "))

for num in range(2, N + 1):
    if is_prime(num):
        print(num)
```


## Tech

A GPT wrapper so thin it's practically transparent.

Just single iteration prompting (see `pcc/prompt.py`) that tells the LLM to convert pseudocode into working python code.
