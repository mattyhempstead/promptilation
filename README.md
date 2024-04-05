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

Usage is similar to regular compilers like `gcc`.

`python promptcc --input-file INPUT_FILE_PATH --output-dir OUTPUT_DIR_PATH`


Promptilation currently applies only to a single file (`.promptpy`) that is translated into a single Python (`.py`) file. It would not be hard to extend this to multiple files in or multiple files out.


To perform promptilation on a single file, execute `promptcc` and supply an input file of type `.promptpy` via the path specified by `INPUT_FILE_PATH`. This will produce a file at `OUTPUT_DIR_PATH` of type `.py`. If no `OUTPUT_DIR_PATH` is specified, `./build` will be used as a default.


**Example**

`python promptcc --input-file prime.promptpy --output-dir build`

You should then be able to execute the file.

`python ./build/prime.py`


## How it works

A GPT wrapper so thin it's practically transparent.

Currently just single iteration prompting (see `promptcc/prompt.py`) that tells the LLM to convert pseudocode into working python code.



## Inspiration

The history of programming languages looks like a long list of increasingly abstract languages. Each language is approximately compiled down to those lower in the hierarchy until we eventually reach machine code for the specific hardware.

The advent of good code generation via LLMs has opened up the possibility for an entirely new layer, which I'll call the prompting layer.

Unless you have been living under a read lock, you would have already tried working at the prompting layer when you asked ChatGPT to generate some code given a natural language description that you wrote.

Promptilation is about wondering what would happen if we viewed this process as a kind of "compilation" step in the same way you might compile C files to a binary, rather than as simply a coding assistant.
It's essentially declarative programming with no theoretical limits to how much control flow you choose to abstract.
Any details that are missing will simply be filled in with a best-guess.
If you want the code to work in a particular way, you should state it.

Promptilation also means all libraries exist and are dynamically generated on an as-need basis.
Ultimately, the programmer should only need to specify the details that matter and at the abstraction layer that matters. No more. No less.

One encompassing perspective of a code base is just a large collection of nested interfaces communicating with eachother.
Once the interface requirements have been specified with a prompt, the programmer does not and should not really care how it works.

Are LLMs the solution to all of this? I think it's very possible.


## Issues

It its current form, promptilation is mostly useless. It is arguably worse that just asking ChatGPT/Copilot to generate code and storing the prompt alongside as documentation.

But I claim promptilation is more of a direction for a future theoretical programming paradigm. So far, all I have done is build a crappy seed for what could eventually represent a new way of writing programs.

There are numerous issues that need to be resolved before it is of any real use. Some of these are out of our control (LLM accuracy), but imo can be addressed with a good enough UX wrapper.



### Accuracy
Regarding accuracy, I personally wouldn't trust an LLM to generate much more than 100 lines of code without me validating it.
However, assuming LLM performance continues to increase we might soon reach the point where this is no longer a practical issue.

The primary factor here is how abstract you make your prompts.
If your prompts translate to only a few lines of source code each, accuracy is not likely to be an issue.

In the cases an error does occur, a nice UX wrapper to "debug" the compiled source would address this problem.
The debugger might also itself exist at the level of natural language using some LLM-powered code understanding / natural language summarisation.

Further wrappers could be used to automatically generate unit tests (e.g. in isolation from the generated source code) to assist with validating correctness.


### Non-determinism
This particular compilation process is also not deterministic, which is an issue as it could cause different outputs on different runs.
Many LLMs let you provide a seed so determinism can be forced if one desires, however this likely won't hold over new releases of LLMs or updated weights.

Assuming the generated code is technically correct according to the prompt, the primary cause of non-determinism would likely be the user not sufficiently specifying the requirements, causing the LLM to fill in missing details.

One possibility to address this is by having the compiler throw a kind of specificity warning. Something like "On line 22 you asked for x to be a random integer, what kind of range were you hoping for?". The response could then be stored for future use, possibly by updating the source prompt. This iterative feedback loop appears quite important for generating code with ChatGPT, so you would probably need solve this for promptilation.

We could also look into reusing the same results from previous promptilations (and we probably should for efficiency reasons), but ideally we force the determinism inside the prompts themselves.


### UX
In my opinion, the primary limitation stopping promptilation from being usable is UX.

I see no fundamental reason why we can't write and read code for entire codebases at the level of prompts, particularly if problems like accuracy and non-determinism are practically resolved.

In its current form, promptilation is only single file in, single file out.
What would really improve usability is working out a good UX for OOP, particularly one that allows for reliable classes and dependencies across multiple prompt files.

A good next step would be figuring out UX for building a simple OOP multi-file game with prompts.



## Examples

The following are some real examples of promptilation outputs.

See `examples/`

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

### Classes

*TODO*

