#!/usr/bin/env python3
"""Depth pass, M1 Python: fill in real, hand-checked data_table and
formulae (runnable code) content for the 119 M1 Python lessons not
covered by the earlier breadth-first batch. Brings M1 Python to full
120/120 coverage.

Structure: l1-l100 are unique graduate-level topics spanning CPython
internals, metaprogramming, concurrency, web/data frameworks, and
production engineering practices; l101-l120 are "Worked Analysis"
companions reusing the data_table/formulae of l1-l20 (direct 1:1
mapping). l3 was already completed by an earlier breadth-first batch
(data_table only, no formulae there), so its data_table is
hard-coded here for reuse (it falls within l1-l20, so it is also
reused for l103).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m1_python_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


_L3_SOURCE = table(["Term", "Meaning"], [
    ["Metaclass", "The class of a class; controls how classes themselves are constructed"],
    ["type()", "The default metaclass that creates ordinary Python classes"],
])

CHARTS: dict[str, dict] = {
    "python-m1-l1": {"data_table": table(["Feature", "Purpose"], [
        ["Advanced Python", "Idioms and language features beyond the basics for production-quality code"],
    ]), "formulae": ["x, *rest = [1, 2, 3, 4]\nprint(rest)  # [2, 3, 4]"]},
    "python-m1-l2": {"data_table": table(["Tool", "Purpose"], [
        ["venv / pip", "Isolates project dependencies and packages a distributable project"],
    ]), "formulae": ["python -m venv .venv\nsource .venv/bin/activate\npip install -e ."]},
    "python-m1-l4": {"data_table": table(["Protocol", "Method"], [
        ["Descriptor", "__get__, __set__, __delete__ customize attribute access"],
    ]), "formulae": ["class Positive:\n    def __set_name__(self, owner, name):\n        self.name = '_' + name\n    def __get__(self, obj, type=None):\n        return getattr(obj, self.name)\n    def __set__(self, obj, value):\n        if value < 0:\n            raise ValueError('must be positive')\n        setattr(obj, self.name, value)"]},
    "python-m1-l5": {"data_table": table(["Dunder", "Purpose"], [
        ["__repr__", "Unambiguous developer-facing string representation"],
        ["__eq__", "Defines equality comparison behavior"],
    ]), "formulae": ["class Point:\n    def __init__(self, x, y):\n        self.x, self.y = x, y\n    def __repr__(self):\n        return f'Point({self.x}, {self.y})'"]},
    "python-m1-l6": {"data_table": table(["Term", "Meaning"], [
        ["Reference counting", "CPython frees an object once its reference count reaches zero"],
        ["Generational GC", "Collects cyclic garbage in generations to reduce overhead"],
    ]), "formulae": ["import gc\ngc.collect()"]},
    "python-m1-l7": {"data_table": table(["Term", "Meaning"], [
        ["GIL", "Global Interpreter Lock; ensures only one thread executes Python bytecode at a time"],
    ]), "formulae": ["import sys\nprint(sys.getswitchinterval())"]},
    "python-m1-l8": {"data_table": table(["Tool", "Purpose"], [
        ["Cython / C-API", "Compiles Python-like code or C code into fast native extensions"],
    ]), "formulae": ["// simplified C extension entry point\nstatic PyMethodDef Methods[] = {\n  {\"add\", py_add, METH_VARARGS, \"Add two numbers\"},\n  {NULL, NULL, 0, NULL}\n};"]},
    "python-m1-l9": {"data_table": table(["Term", "Meaning"], [
        ["Generic", "A type parameterized over another type, e.g. list[int]"],
        ["Protocol", "Defines structural typing (duck typing) checked statically"],
    ]), "formulae": ["from typing import Protocol\nclass Sized(Protocol):\n    def __len__(self) -> int: ..."]},
    "python-m1-l10": {"data_table": table(["Term", "Meaning"], [
        ["match/case", "Structural pattern matching introduced in Python 3.10"],
    ]), "formulae": ["match command.split():\n    case ['go', direction]:\n        print(f'going {direction}')\n    case _:\n        print('unknown')"]},
    "python-m1-l11": {"data_table": table(["Term", "Meaning"], [
        ["Event loop", "Schedules and runs asynchronous tasks and callbacks"],
    ]), "formulae": ["import asyncio\nasync def main():\n    await asyncio.sleep(1)\n    print('done')\nasyncio.run(main())"]},
    "python-m1-l12": {"data_table": table(["Term", "Meaning"], [
        ["Plugin architecture", "Dynamically loads extensions without modifying core application code"],
    ]), "formulae": ["import importlib\nplugin = importlib.import_module('myapp.plugins.example')"]},
    "python-m1-l13": {"data_table": table(["Pattern", "Purpose"], [
        ["Singleton", "Ensures only one instance of a class exists"],
        ["Observer", "Notifies subscribed listeners when state changes"],
    ]), "formulae": ["class Singleton:\n    _instance = None\n    def __new__(cls):\n        if cls._instance is None:\n            cls._instance = super().__new__(cls)\n        return cls._instance"]},
    "python-m1-l14": {"data_table": table(["Term", "Meaning"], [
        ["Property-based testing", "Generates many random inputs to test that a property always holds"],
    ]), "formulae": ["from hypothesis import given, strategies as st\n@given(st.integers())\ndef test_abs_nonnegative(n):\n    assert abs(n) >= 0"]},
    "python-m1-l15": {"data_table": table(["Term", "Meaning"], [
        ["Wheel", "A prebuilt binary Python package format for faster installation"],
    ]), "formulae": ["python -m build --wheel"]},
    "python-m1-l16": {"data_table": table(["Tool", "Purpose"], [
        ["cProfile", "Profiles overall function call time"],
        ["line_profiler", "Profiles execution time per line of code"],
    ]), "formulae": ["python -m cProfile -s cumulative script.py"]},
    "python-m1-l17": {"data_table": table(["Term", "Meaning"], [
        ["Pipeline", "Chains preprocessing and model steps into one reusable object"],
    ]), "formulae": ["from sklearn.pipeline import Pipeline\nfrom sklearn.preprocessing import StandardScaler\nfrom sklearn.linear_model import LogisticRegression\npipe = Pipeline([('scale', StandardScaler()), ('clf', LogisticRegression())])"]},
    "python-m1-l18": {"data_table": table(["Term", "Meaning"], [
        ["Docker image", "Packages a Python app with its dependencies into a portable container"],
    ]), "formulae": ["FROM python:3.12-slim\nCOPY . /app\nWORKDIR /app\nRUN pip install -r requirements.txt\nCMD [\"python\", \"main.py\"]"]},
    "python-m1-l19": {"data_table": table(["Practice", "Purpose"], [
        ["Code review", "Catches bugs and spreads knowledge before code merges into the main codebase"],
    ]), "formulae": ["# CI check example\nruff check . && mypy . && pytest"]},
    "python-m1-l20": {"data_table": table(["Component", "Purpose"], [
        ["Production-ready application", "Integrates testing, packaging, deployment, and observability into one project"],
    ]), "formulae": ["# entry point\nif __name__ == '__main__':\n    main()"]},
    "python-m1-l21": {"data_table": table(["Term", "Meaning"], [
        ["Bytecode", "The compiled intermediate instructions the CPython VM executes"],
    ]), "formulae": ["import dis\ndis.dis(lambda x: x + 1)"]},
    "python-m1-l22": {"data_table": table(["Term", "Meaning"], [
        ["Bytecode manipulation", "Rewrites compiled instructions to alter or instrument program behavior"],
    ]), "formulae": ["code = compile('1+1', '<string>', 'eval')\nprint(code.co_code)"]},
    "python-m1-l23": {"data_table": table(["Term", "Meaning"], [
        ["AST", "Abstract Syntax Tree; a structured tree representation of parsed source code"],
    ]), "formulae": ["import ast\ntree = ast.parse('x = 1 + 2')\nprint(ast.dump(tree))"]},
    "python-m1-l24": {"data_table": table(["Term", "Meaning"], [
        ["DSL via ast", "Uses Python's own parser to build a small custom language on top of Python syntax"],
    ]), "formulae": ["import ast\nast.parse('a = 1', mode='exec')"]},
    "python-m1-l25": {"data_table": table(["Term", "Meaning"], [
        ["Class factory", "A function that dynamically constructs and returns a new class"],
    ]), "formulae": ["def make_class(name, **fields):\n    return type(name, (), fields)"]},
    "python-m1-l26": {"data_table": table(["Term", "Meaning"], [
        ["Context manager", "Defines setup/teardown logic used with the 'with' statement"],
    ]), "formulae": ["from contextlib import contextmanager\n@contextmanager\ndef timer():\n    import time; start = time.time()\n    yield\n    print(time.time() - start)"]},
    "python-m1-l27": {"data_table": table(["Term", "Meaning"], [
        ["Generator-based coroutine", "Uses yield to pause and resume execution cooperatively"],
    ]), "formulae": ["def gen():\n    x = yield\n    print('received', x)\ng = gen()\nnext(g)\ng.send(5)"]},
    "python-m1-l28": {"data_table": table(["Term", "Meaning"], [
        ["Protocol (PEP 544)", "Defines structural subtyping: a class satisfies it by shape, not inheritance"],
    ]), "formulae": ["from typing import Protocol\nclass Drawable(Protocol):\n    def draw(self) -> None: ..."]},
    "python-m1-l29": {"data_table": table(["Feature", "Purpose"], [
        ["__slots__", "Restricts instance attributes, saving memory versus a default __dict__"],
    ]), "formulae": ["from dataclasses import dataclass\n@dataclass(slots=True)\nclass Point:\n    x: int\n    y: int"]},
    "python-m1-l30": {"data_table": table(["Term", "Meaning"], [
        ["Weak reference", "References an object without preventing it from being garbage collected"],
    ]), "formulae": ["import weakref\nclass Obj: pass\no = Obj()\nr = weakref.ref(o)"]},
    "python-m1-l31": {"data_table": table(["Term", "Meaning"], [
        ["Lazy evaluation", "Defers computing a value until it's actually needed"],
    ]), "formulae": ["def lazy_range(n):\n    i = 0\n    while i < n:\n        yield i\n        i += 1"]},
    "python-m1-l32": {"data_table": table(["Function", "Purpose"], [
        ["functools.reduce", "Cumulatively applies a function across a sequence"],
        ["itertools.chain", "Lazily concatenates multiple iterables"],
    ]), "formulae": ["from functools import reduce\nreduce(lambda a, b: a + b, [1, 2, 3])"]},
    "python-m1-l33": {"data_table": table(["Term", "Meaning"], [
        ["singledispatch", "Dispatches a function implementation based on the type of its first argument"],
    ]), "formulae": ["from functools import singledispatch\n@singledispatch\ndef process(x): ...\n@process.register\ndef _(x: int): return x * 2"]},
    "python-m1-l34": {"data_table": table(["Term", "Meaning"], [
        ["Exception group (PEP 654)", "Bundles multiple unrelated exceptions raised together"],
    ]), "formulae": ["try:\n    raise ExceptionGroup('errs', [ValueError('a'), TypeError('b')])\nexcept* ValueError as eg:\n    print('caught value errors')"]},
    "python-m1-l35": {"data_table": table(["Term", "Meaning"], [
        ["TaskGroup", "Runs and awaits multiple async tasks together with structured error propagation"],
    ]), "formulae": ["import asyncio\nasync def main():\n    async with asyncio.TaskGroup() as tg:\n        tg.create_task(asyncio.sleep(1))"]},
    "python-m1-l36": {"data_table": table(["Term", "Meaning"], [
        ["Custom event loop", "Implements the scheduling logic that drives asyncio coroutines"],
    ]), "formulae": ["import asyncio\nloop = asyncio.new_event_loop()\nasyncio.set_event_loop(loop)"]},
    "python-m1-l37": {"data_table": table(["Approach", "Trade-off"], [
        ["Threading", "Good for I/O-bound work, limited by the GIL for CPU-bound work"],
        ["Multiprocessing", "True parallelism for CPU-bound work, higher memory overhead"],
    ]), "formulae": ["from multiprocessing import Pool\nwith Pool(4) as p:\n    p.map(str, range(10))"]},
    "python-m1-l38": {"data_table": table(["Term", "Meaning"], [
        ["Shared memory", "Lets separate processes access the same memory block without copying data"],
    ]), "formulae": ["from multiprocessing import shared_memory\nshm = shared_memory.SharedMemory(create=True, size=10)"]},
    "python-m1-l39": {"data_table": table(["Term", "Meaning"], [
        ["Celery", "A distributed task queue for running background jobs asynchronously"],
    ]), "formulae": ["from celery import Celery\napp = Celery('tasks', broker='redis://localhost')\n@app.task\ndef add(x, y):\n    return x + y"]},
    "python-m1-l40": {"data_table": table(["Term", "Meaning"], [
        ["Dask", "Scales pandas-like computation across multiple cores or machines"],
    ]), "formulae": ["import dask.dataframe as dd\ndf = dd.read_csv('data.csv')"]},
    "python-m1-l41": {"data_table": table(["Term", "Meaning"], [
        ["Ray", "A framework for scaling Python workloads across a distributed cluster"],
    ]), "formulae": ["import ray\nray.init()\n@ray.remote\ndef square(x):\n    return x * x"]},
    "python-m1-l42": {"data_table": table(["Term", "Meaning"], [
        ["Stride", "The number of bytes to step to move to the next element along a NumPy array axis"],
    ]), "formulae": ["import numpy as np\na = np.arange(12).reshape(3, 4)\nprint(a.strides)"]},
    "python-m1-l43": {"data_table": table(["Term", "Meaning"], [
        ["ufunc", "A NumPy function that operates element-wise on arrays without explicit loops"],
    ]), "formulae": ["import numpy as np\nadd = np.frompyfunc(lambda a, b: a + b, 2, 1)"]},
    "python-m1-l44": {"data_table": table(["Term", "Meaning"], [
        ["Numba JIT", "Compiles numerical Python functions to fast machine code at call time"],
    ]), "formulae": ["from numba import njit\n@njit\ndef sum_sq(n):\n    total = 0\n    for i in range(n):\n        total += i * i\n    return total"]},
    "python-m1-l45": {"data_table": table(["Term", "Meaning"], [
        ["PyO3", "A Rust library for writing native Python extension modules in Rust"],
    ]), "formulae": ["// Rust\n#[pyfunction]\nfn add(a: i64, b: i64) -> i64 { a + b }"]},
    "python-m1-l46": {"data_table": table(["Term", "Meaning"], [
        ["ctypes", "Calls functions in compiled C libraries directly from Python"],
    ]), "formulae": ["import ctypes\nlibm = ctypes.CDLL('libm.so.6')\nprint(libm.sqrt(4.0))"]},
    "python-m1-l47": {"data_table": table(["Tool", "Purpose"], [
        ["tracemalloc", "Traces memory allocations to find where Python memory is being used"],
    ]), "formulae": ["import tracemalloc\ntracemalloc.start()\nsnapshot = tracemalloc.take_snapshot()"]},
    "python-m1-l48": {"data_table": table(["Term", "Meaning"], [
        ["mypy plugin", "Extends static type checking to understand custom or dynamic library behavior"],
    ]), "formulae": ["# mypy.ini\n[mypy]\nplugins = mypackage.mypy_plugin"]},
    "python-m1-l49": {"data_table": table(["Term", "Meaning"], [
        ["Gradual typing", "Lets a codebase mix typed and untyped code, adding types incrementally"],
    ]), "formulae": ["def f(x: int) -> int:\n    return x + 1"]},
    "python-m1-l50": {"data_table": table(["Term", "Meaning"], [
        ["Dependency injection (FastAPI)", "Declares a request's required resources so the framework provides them automatically"],
    ]), "formulae": ["from fastapi import FastAPI, Depends\napp = FastAPI()\ndef get_db(): ...\n@app.get('/items')\ndef read(db=Depends(get_db)):\n    return db"]},
    "python-m1-l51": {"data_table": table(["Framework", "Purpose"], [
        ["Strawberry / Ariadne", "Python libraries for building GraphQL APIs"],
    ]), "formulae": ["import strawberry\n@strawberry.type\nclass Query:\n    @strawberry.field\n    def hello(self) -> str:\n        return 'world'"]},
    "python-m1-l52": {"data_table": table(["Layer", "Purpose"], [
        ["SQLAlchemy Core", "Lower-level, explicit SQL expression construction"],
        ["SQLAlchemy ORM", "Maps Python classes to database tables"],
    ]), "formulae": ["from sqlalchemy.orm import declarative_base\nBase = declarative_base()"]},
    "python-m1-l53": {"data_table": table(["Term", "Meaning"], [
        ["Connection pooling", "Reuses a limited set of open database connections instead of opening new ones per request"],
    ]), "formulae": ["import asyncpg\npool = await asyncpg.create_pool(dsn='postgresql://...')"]},
    "python-m1-l54": {"data_table": table(["Standard", "Feature"], [
        ["WSGI", "Synchronous interface between Python web apps and servers"],
        ["ASGI", "Asynchronous interface supporting WebSockets and async apps"],
    ]), "formulae": ["def app(environ, start_response):\n    start_response('200 OK', [('Content-Type', 'text/plain')])\n    return [b'Hello']"]},
    "python-m1-l55": {"data_table": table(["Term", "Meaning"], [
        ["Middleware", "Wraps request/response handling with cross-cutting logic like logging or auth"],
    ]), "formulae": ["async def middleware(request, call_next):\n    response = await call_next(request)\n    return response"]},
    "python-m1-l56": {"data_table": table(["Format", "Feature"], [
        ["Protocol Buffers", "Compact, schema-based binary serialization"],
        ["MessagePack", "Compact binary format similar to JSON but smaller"],
    ]), "formulae": ["import msgpack\ndata = msgpack.packb({'a': 1})"]},
    "python-m1-l57": {"data_table": table(["Term", "Meaning"], [
        ["Kafka consumer", "Reads a stream of events published to a Kafka topic"],
    ]), "formulae": ["from kafka import KafkaConsumer\nconsumer = KafkaConsumer('my-topic')"]},
    "python-m1-l58": {"data_table": table(["Term", "Meaning"], [
        ["Structured logging", "Emits logs as structured key-value data rather than plain text"],
    ]), "formulae": ["import structlog\nlog = structlog.get_logger()\nlog.info('event', user_id=42)"]},
    "python-m1-l59": {"data_table": table(["Term", "Meaning"], [
        ["OpenTelemetry", "A standard for collecting traces, metrics, and logs across services"],
    ]), "formulae": ["from opentelemetry import trace\ntracer = trace.get_tracer(__name__)\nwith tracer.start_as_current_span('op'):\n    pass"]},
    "python-m1-l60": {"data_table": table(["Library", "Purpose"], [
        ["Click / Typer", "Build command-line interfaces with argument parsing and help text"],
    ]), "formulae": ["import typer\napp = typer.Typer()\n@app.command()\ndef greet(name: str):\n    print(f'Hello {name}')"]},
    "python-m1-l61": {"data_table": table(["Term", "Meaning"], [
        ["re module internals", "Compiles patterns into a matching state machine executed against input text"],
    ]), "formulae": ["import re\nre.findall(r'\\d+', 'a1 b22 c333')"]},
    "python-m1-l62": {"data_table": table(["Term", "Meaning"], [
        ["Parser combinator", "Builds complex parsers by composing small reusable parsing functions"],
    ]), "formulae": ["def literal(s):\n    def parse(text):\n        return (s, text[len(s):]) if text.startswith(s) else None\n    return parse"]},
    "python-m1-l63": {"data_table": table(["Component", "Role"], [
        ["Lexer", "Splits raw text into a stream of tokens"],
        ["Parser", "Builds a structured tree from the token stream"],
    ]), "formulae": ["import re\ntokens = re.findall(r'\\d+|[+\\-*/]', '1 + 2 * 3'.replace(' ', ''))"]},
    "python-m1-l64": {"data_table": table(["Term", "Meaning"], [
        ["Hypothesis strategies", "Compose custom generators to test more complex input structures"],
    ]), "formulae": ["from hypothesis import given, strategies as st\n@given(st.lists(st.integers()))\ndef test_sorted(xs):\n    assert sorted(xs) == sorted(sorted(xs))"]},
    "python-m1-l65": {"data_table": table(["Term", "Meaning"], [
        ["Mutation testing", "Introduces small code bugs to check whether the test suite catches them"],
    ]), "formulae": ["mutmut run"]},
    "python-m1-l66": {"data_table": table(["Term", "Meaning"], [
        ["Contract testing", "Verifies that a service and its consumers agree on the API's expected behavior"],
    ]), "formulae": ["# pact-python example\npact.given('a user exists').upon_receiving('a request').will_respond_with(200)"]},
    "python-m1-l67": {"data_table": table(["Term", "Meaning"], [
        ["Fuzzing", "Feeds a program random or malformed input to discover crashes or vulnerabilities"],
    ]), "formulae": ["import atheris\ndef fuzz(data):\n    parse(data)\natheris.Setup([], fuzz)\natheris.Fuzz()"]},
    "python-m1-l68": {"data_table": table(["Tool", "Purpose"], [
        ["Bandit / Semgrep", "Static analysis tools that detect common security issues in Python code"],
    ]), "formulae": ["bandit -r ./mypackage"]},
    "python-m1-l69": {"data_table": table(["Practice", "Purpose"], [
        ["Secure coding", "Avoids common vulnerability classes like injection and insecure deserialization"],
    ]), "formulae": ["import subprocess\nsubprocess.run(['ls', path], shell=False)"]},
    "python-m1-l70": {"data_table": table(["Library", "Purpose"], [
        ["cryptography", "Provides audited implementations of encryption and hashing primitives"],
    ]), "formulae": ["from cryptography.fernet import Fernet\nkey = Fernet.generate_key()\nf = Fernet(key)"]},
    "python-m1-l71": {"data_table": table(["Term", "Meaning"], [
        ["Reproducible pipeline", "Ensures a scientific computation produces the same result given the same inputs"],
    ]), "formulae": ["import random\nrandom.seed(42)"]},
    "python-m1-l72": {"data_table": table(["Term", "Meaning"], [
        ["MultiIndex", "A pandas hierarchical index allowing multiple levels of row/column labeling"],
    ]), "formulae": ["import pandas as pd\ndf = pd.DataFrame({'v': [1, 2]}, index=pd.MultiIndex.from_tuples([('a', 1), ('a', 2)]))"]},
    "python-m1-l73": {"data_table": table(["Term", "Meaning"], [
        ["Polars", "A DataFrame library built in Rust offering faster performance than pandas for large data"],
    ]), "formulae": ["import polars as pl\ndf = pl.DataFrame({'a': [1, 2, 3]})"]},
    "python-m1-l74": {"data_table": table(["Term", "Meaning"], [
        ["Custom transformer", "A scikit-learn compatible class implementing fit/transform for a pipeline step"],
    ]), "formulae": ["from sklearn.base import BaseEstimator, TransformerMixin\nclass MyTransform(BaseEstimator, TransformerMixin):\n    def fit(self, X, y=None): return self\n    def transform(self, X): return X"]},
    "python-m1-l75": {"data_table": table(["Term", "Meaning"], [
        ["Custom autograd function", "Defines a manual forward/backward pass for a PyTorch operation"],
    ]), "formulae": ["import torch\nclass Square(torch.autograd.Function):\n    @staticmethod\n    def forward(ctx, x):\n        ctx.save_for_backward(x)\n        return x * x"]},
    "python-m1-l76": {"data_table": table(["Tool", "Purpose"], [
        ["TorchServe / ONNX Runtime", "Serves trained models for production inference"],
    ]), "formulae": ["import onnxruntime as ort\nsess = ort.InferenceSession('model.onnx')"]},
    "python-m1-l77": {"data_table": table(["Term", "Meaning"], [
        ["Pydantic validator", "Enforces custom validation logic on a data model's fields"],
    ]), "formulae": ["from pydantic import BaseModel, field_validator\nclass User(BaseModel):\n    age: int\n    @field_validator('age')\n    def check_age(cls, v):\n        assert v >= 0\n        return v"]},
    "python-m1-l78": {"data_table": table(["Tool", "Purpose"], [
        ["Poetry / PDM", "Manage Python dependencies and packaging with lockfiles for reproducibility"],
    ]), "formulae": ["poetry add requests\npoetry install"]},
    "python-m1-l79": {"data_table": table(["Term", "Meaning"], [
        ["Monorepo", "Manages multiple related Python packages in a single repository"],
    ]), "formulae": ["# pyproject.toml workspace-style layout\n[tool.uv.workspace]\nmembers = [\"packages/*\"]"]},
    "python-m1-l80": {"data_table": table(["Tool", "Purpose"], [
        ["Maturin", "Builds Python packages containing compiled Rust extensions"],
    ]), "formulae": ["maturin build --release"]},
    "python-m1-l81": {"data_table": table(["Tool", "Purpose"], [
        ["pdb / py-spy", "Interactive debugging and low-overhead sampling profiler for running processes"],
    ]), "formulae": ["import pdb; pdb.set_trace()"]},
    "python-m1-l82": {"data_table": table(["Term", "Meaning"], [
        ["Async profiling", "Identifies which awaited coroutines are causing latency bottlenecks"],
    ]), "formulae": ["python -X importtime -m asyncio_profiler script.py"]},
    "python-m1-l83": {"data_table": table(["Term", "Meaning"], [
        ["Caching layer", "Stores computed results in Redis to avoid repeating expensive work"],
    ]), "formulae": ["import redis\nr = redis.Redis()\nr.set('key', 'value', ex=60)"]},
    "python-m1-l84": {"data_table": table(["Term", "Meaning"], [
        ["Snapshot testing", "Compares a function's output against a previously saved 'golden' reference file"],
    ]), "formulae": ["def test_output(snapshot):\n    assert render() == snapshot"]},
    "python-m1-l85": {"data_table": table(["Term", "Meaning"], [
        ["Feature flag", "Toggles a feature on or off without redeploying code"],
    ]), "formulae": ["if flags.is_enabled('new_ui', user):\n    render_new_ui()"]},
    "python-m1-l86": {"data_table": table(["Term", "Meaning"], [
        ["Token bucket", "A common rate-limiting algorithm that refills allowed requests over time"],
    ]), "formulae": ["import time\nclass Bucket:\n    def __init__(self, rate):\n        self.tokens = rate\n        self.rate = rate\n        self.last = time.time()"]},
    "python-m1-l87": {"data_table": table(["Term", "Meaning"], [
        ["Distributed task scheduler", "Coordinates job execution across multiple worker machines"],
    ]), "formulae": ["from celery.schedules import crontab\napp.conf.beat_schedule = {'job': {'task': 'tasks.run', 'schedule': crontab(minute=0)}}"]},
    "python-m1-l88": {"data_table": table(["Term", "Meaning"], [
        ["Actor model", "Isolates state within independent actors that communicate only via messages"],
    ]), "formulae": ["import queue\nmailbox = queue.Queue()"]},
    "python-m1-l89": {"data_table": table(["Term", "Meaning"], [
        ["Entry points", "Lets installed packages register plugins discoverable by other applications"],
    ]), "formulae": ["# pyproject.toml\n[project.entry-points.'myapp.plugins']\nfoo = 'mypackage:foo_plugin'"]},
    "python-m1-l90": {"data_table": table(["Term", "Meaning"], [
        ["Compiled extension wheel", "Bundles precompiled native code so users don't need a compiler to install"],
    ]), "formulae": ["python -m build --wheel"]},
    "python-m1-l91": {"data_table": table(["Term", "Meaning"], [
        ["Code generation", "Programmatically produces source code from a template rather than writing it by hand"],
    ]), "formulae": ["from jinja2 import Template\nTemplate('class {{ name }}: pass').render(name='Foo')"]},
    "python-m1-l92": {"data_table": table(["Tool", "Purpose"], [
        ["Static site generator", "Builds HTML pages from templates and content at build time"],
    ]), "formulae": ["from jinja2 import Environment, FileSystemLoader\nenv = Environment(loader=FileSystemLoader('templates'))"]},
    "python-m1-l93": {"data_table": table(["Term", "Meaning"], [
        ["Airflow DAG", "Defines a scheduled workflow of dependent data pipeline tasks"],
    ]), "formulae": ["from airflow import DAG\nfrom airflow.operators.python import PythonOperator\nwith DAG('etl', schedule='@daily') as dag:\n    pass"]},
    "python-m1-l94": {"data_table": table(["Term", "Meaning"], [
        ["Apache Flink (PyFlink)", "Processes unbounded data streams with low latency and exactly-once guarantees"],
    ]), "formulae": ["from pyflink.datastream import StreamExecutionEnvironment\nenv = StreamExecutionEnvironment.get_execution_environment()"]},
    "python-m1-l95": {"data_table": table(["Term", "Meaning"], [
        ["Custom linter", "Walks a program's AST to flag project-specific code style or correctness issues"],
    ]), "formulae": ["import ast\nclass Visitor(ast.NodeVisitor):\n    def visit_FunctionDef(self, node):\n        print(node.name)"]},
    "python-m1-l96": {"data_table": table(["Term", "Meaning"], [
        ["Security auditing", "Systematically reviews code and dependencies for exploitable vulnerabilities"],
    ]), "formulae": ["pip-audit"]},
    "python-m1-l97": {"data_table": table(["Pattern", "Feature"], [
        ["Hexagonal architecture", "Isolates core business logic behind ports, independent of frameworks"],
    ]), "formulae": ["class OrderService:\n    def __init__(self, repo):\n        self.repo = repo  # port, injected"]},
    "python-m1-l98": {"data_table": table(["Term", "Meaning"], [
        ["sys.settrace", "Registers a callback invoked on every Python interpreter execution event"],
    ]), "formulae": ["import sys\ndef trace(frame, event, arg):\n    print(event)\n    return trace\nsys.settrace(trace)"]},
    "python-m1-l99": {"data_table": table(["Term", "Meaning"], [
        ["Buffer protocol", "Lets objects like bytes and NumPy arrays share memory without copying"],
    ]), "formulae": ["b = bytearray(b'hello')\nmv = memoryview(b)"]},
    "python-m1-l100": {"data_table": table(["Term", "Meaning"], [
        ["Type stub (.pyi)", "A separate file declaring type hints for an untyped library"],
    ]), "formulae": ["# mypackage.pyi\ndef add(a: int, b: int) -> int: ..."]},
}

for worked_n in range(101, 121):
    base_n = worked_n - 100
    base_key = f"python-m1-l{base_n}"
    worked_key = f"python-m1-l{worked_n}"
    if base_n == 3:
        CHARTS[worked_key] = {"data_table": dict(_L3_SOURCE)}
    elif base_key in CHARTS:
        fields = {"data_table": dict(CHARTS[base_key]["data_table"])}
        if "formulae" in CHARTS[base_key]:
            fields["formulae"] = list(CHARTS[base_key]["formulae"])
        CHARTS[worked_key] = fields


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["Python"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_m1.json Python: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} M1 Python lessons (completing 120/120).")


if __name__ == "__main__":
    main()
