# Issues Found in `bike_share_stations.py`

Line numbers refer to the **original** file (before fixes). Reports are in `before/` and `after/`.

| Issue | Type | Line(s) | Description | Fix Approach |
| ----- | ---- | ------- | ----------- | ------------ |
| SQL injection (Bandit B608) | Security (Medium) | 9 | `addStation` builds the INSERT by string concatenation, so a station name such as `x'); DROP TABLE stations;--` would be run as SQL | Use a parameterised query: `VALUES (?, ?, ?)` with a tuple of values |
| Weak random generator (Bandit B311) | Security (Low) | 20 | `random.randint` is predictable and is used to create an unlock PIN | Use `secrets.randbelow(9000) + 1000` (same 1000-9999 range) |
| Try/except/pass (Bandit B110) and broad exception (Pylint W0718) | Security (Low) / Bug | 28-31 | `resetStation` catches every `Exception` and ignores it, so database failures are hidden | Catch `sqlite3.Error` only and log the error with `logging.error` |
| Mutable default argument (Pylint W0102) | Bug | 8 | `log=[]` is created once and shared across all calls, so logs leak between calls | Default to `None` and create a new list inside the function |
| Inconsistent return (Pylint R1710) | Bug | 13-17 | `rentBike` returns `True` on success but implicitly returns `None` on failure | Add an explicit `return False`; update the demo that checked `is None` |
| Crash on unknown station (found by manual review) | Bug | 34-37 | `hasBikes` reads `row[0]` when `row` is `None` for a missing station, raising `TypeError` | Check `row is None` before indexing |
| Comparison to None (Pylint C0121, Flake8 E711) | Style | 35 | `row[0] == None` should use identity comparison | Use `is None` |
| Unused variable (Pylint W0612, Flake8 F841) | Quality | 24 | `summary = len(stations)` is assigned but never used | Remove the line |
| Function naming (Pylint C0103) | Style | 8, 13, 19, 22, 27, 33 | camelCase function names violate PEP 8 | Rename to snake_case; rename `conn` to `CONN` (module-level constant) |
| Missing docstrings (Pylint C0114, C0116) | Style | 1 and every function | No module or function docstrings | Add a one-line docstring to the module and each function |
| Line too long (Pylint C0301, Flake8 E501) | Style | 6, 9, 14, 16, 23, 29, 34 | Lines run to 91-131 characters, over the 79 limit | Wrap long SQL strings and calls across lines |
| Blank lines (Flake8 E302, E305) | Style | 8, 13, 19, 22, 27, 33, 39, 46 | Only one blank line between top-level definitions | Use two blank lines before and after functions |
| `main()` runs on import | Quality | 46 | The demo runs whenever the module is imported | Wrap in `if __name__ == "__main__":` |

## Summary of results

| Tool | Before | After |
| ---- | ------ | ----- |
| Pylint | 4.17 / 10 | 10.00 / 10 |
| Bandit | 3 issues (1 Medium, 2 Low) | 0 issues |
| Flake8 | 17 warnings | 0 warnings |

## Commits

1. Bandit fixes: parameterised SQL, `secrets`, specific exception handling
2. Pylint fixes: naming, docstrings, mutable default, return consistency, unused variable
3. Flake8 fixes: line length, blank lines, `__main__` guard
