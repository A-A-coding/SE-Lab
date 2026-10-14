# Reflection

## 1. Which issues were the easiest and hardest to fix?

The easiest were the mechanical ones: renaming functions to snake_case, adding docstrings, replacing `== None` with `is None`, deleting the unused `summary` variable, and fixing blank lines and line length. Each was a small, local edit and the tools told me exactly where it was.

The hardest were the ones that needed a decision rather than an edit. Fixing the SQL injection meant rewriting the INSERT as a parameterised query. Fixing `rentBike` meant changing its return value from `None` to `False` on failure, which also changed the demo's output, so I had to update the `main()` line that tested `is None`. Replacing `except Exception: pass` required deciding what should happen when a reset fails (I log the error instead of hiding it).

## 2. Did the tools report any false positives?

Not clear-cut ones. The Bandit warning about `random.randint` (B311) is only Low severity, and a bike-share PIN is not a high-value secret, but a PIN that unlocks a bike should not be predictable, so I treated it as a real finding and switched to `secrets`.

The one real inconsistency was between the tools themselves: Pylint allows 100 characters per line while Flake8 allows 79, so lines that satisfied Pylint still failed Flake8. Some findings also overlap (Pylint W0612 and Flake8 F841 are the same unused variable), which makes the combined report look longer than the number of real problems. In a real project I would configure both tools to share one line length.

## 3. How would I integrate static analysis into a real workflow?

I would run Flake8 and Pylint in a pre-commit hook so style and quality problems are caught before code is committed, and run all three tools in a CI pipeline (for example GitHub Actions) on every pull request, failing the build on any Bandit Medium or High finding or when the Pylint score drops below a threshold. I would also commit a shared configuration file (line length, disabled checks) so everyone and the CI see the same results, and keep the reports as build artifacts so trends are visible over time.

## 4. What improvements did I see in quality, readability and robustness?

The Pylint score went from 4.17 to 10.00, Bandit went from 3 findings to 0, and Flake8 went from 17 warnings to 0. More importantly, the code is safer and more correct: a user-supplied station name can no longer alter the SQL, the shared `log=[]` list no longer leaks data between calls, PINs come from a cryptographically secure source, and database errors are reported rather than silently ignored. `has_bikes` also no longer crashes for a station that does not exist, a bug none of the tools flagged and that I only found by reading the code. The code is easier to read thanks to consistent names, docstrings and shorter lines, and it can now be imported without running the demo.
