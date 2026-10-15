# Validation

Local verification on Python 3.9.6 using synthetic inputs.

## Tests

```text
test_added_and_removed (test_drift.Tests) ... ok
test_arrays_atomic (test_drift.Tests) ... ok
test_equal (test_drift.Tests) ... ok
test_ignore_does_not_use_prefix (test_drift.Tests) ... ok
test_ignore_subtree (test_drift.Tests) ... ok
test_nested (test_drift.Tests) ... ok
test_pointer_escaping (test_drift.Tests) ... ok
test_types_differ (test_drift.Tests) ... ok

----------------------------------------------------------------------
Ran 8 tests in 0.000s

OK
```

## Example

```sh
python3 drift.py sample.json --ignore /metadata
```

Exit status: 1. A nonzero policy result is expected for the failing example and is not a test failure.

```text
{
  "changes": [
    {
      "path": "/image",
      "change": "modified",
      "expected": "app:1.0",
      "actual": "app:1.1"
    },
    {
      "path": "/replicas",
      "change": "modified",
      "expected": 2,
      "actual": 1
    }
  ],
  "in_sync": false
}
```

These results demonstrate the included fixtures. They do not establish production readiness or performance on real customer data.
