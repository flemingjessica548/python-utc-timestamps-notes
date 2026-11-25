# Ordered batch processing for Convert Unix seconds to UTC

`batch.py` accepts an outer JSON array containing separate inputs. This is an extra level of nesting when `solve` itself accepts a list. It produces one result envelope per item, preserving input order and zero-based position.

```sh
python3 batch.py < samples/batch.json
```

The batch covers these three input/output pairs:

## Case 1

Input:
```json
0
```

Result:
```json
"1970-01-01T00:00:00+00:00"
```

## Case 2

Input:
```json
1704067200
```

Result:
```json
"2024-01-01T00:00:00+00:00"
```

## Case 3

Input:
```json
-1
```

Result:
```json
"1969-12-31T23:59:59+00:00"
```

## Partial failures

Each successful item has `ok: true` and `result`. A failed item has `ok: false` and an exception type; later items still run. Exit status 1 means at least one item failed, while status 2 means the batch envelope itself was invalid. An empty outer array is a valid empty batch.

Use an explicit UTC timezone to avoid machine-local interpretation. Unix seconds do not model leap seconds; fractional seconds may round to microseconds.

The implementation processes sequentially, avoiding shared-state concurrency and keeping output order predictable. Input is limited to one MiB and 1000 items; this version materializes all results in memory. The next lesson removes that whole-batch memory requirement with line-oriented processing.
