# Convert Unix seconds to UTC: implementation

## What the example does

Use an explicit UTC timezone to avoid machine-local interpretation. Unix seconds do not model leap seconds; fractional seconds may round to microseconds.

The public function is `solve(value)`. The JSON input contract can be seen in this concrete example:

```json
0
```

Expected result:

```json
"1970-01-01T00:00:00+00:00"
```

Run `python3 example.py` for the Python representation of the result. `solution.py` contains the full implementation and can also be imported by another script.

## Scope

The function implements exactly the behavior described above. It does not perform network or filesystem access. Python exceptions indicate unsupported input; the next lesson turns them into a command-line error response. Review the limitations before reusing it in an application.
