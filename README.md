# loggerplus

Multiprocess-safe rotating file logger (`RobustLogger`) plus `format_exception_with_variables` error helpers.

## Install

```bash
pip install -e .
# or from GitHub:
pip install git+https://github.com/bodencrouch/LoggerPlus.git
```

## Versioning

PyPI already has `loggerplus==0.1.3` (older `bodencrouch/LoggerPlus`). This tree is **0.2.0**: self-contained (no `utility.*` imports) and default log filenames use `loggerplus` instead of `pykotor`. See the catalog diff note in [pykotor-extracted-libs](https://github.com/bodencrouch/pykotor-extracted-libs/blob/main/docs/loggerplus-pypi-diff.md).

## Origin

Extracted from the [PyKotor](https://github.com/bodencrouch/PyKotor) monorepo `utility` / related packages.
KotOR-specific couplings were removed or made optional for standalone use.

### DAG
Foundation package. Many other extracted libs depend on this.

## License

LGPL-3.0-or-later


> **Note:** Published as [`bodencrouch/LoggerPlus`](https://github.com/bodencrouch/LoggerPlus) (GitHub repo names are case-insensitive).
