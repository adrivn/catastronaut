# Catastronaut 🧑🚀
 Simple Python wrapper to retrieve data from the spanish Land Registry ("Catastro") API endpoint.

## ✨ Features
- JSON default response can be traversed/modelled using JMESPath syntax. You can choose which data you want to access, how deep, and how to name/label it. More details in the **utils/models.py** file.
- Choose how you want to output the data: raw or in DataFrame (using Polars library)
  - By returning a Polars DataFrame, the user can access its API directly, allowing for further wrangling, transformation or saving the data to disk (JSON, CSV, Parquet, databases, etc.)
- Supports single parameter requests and bulk requests (by passing lists of parameters)
- Verbose error logging and traceback
- Auto-retry and rate limiting
- Caching (TBD)

## ⚡️ Requirements
- [JMESPath][jmespath-href] (allows for easy and custom flattening of nested JSON responses)
- [Polars][polars-href] Pandas replacement written in Rust; multithreaded, vectorized and fast like no other.

## ⚙️ Usage
[Read the docs][docshref]
---

Heavily inspired by [Pycatastro][pycat-href].
Like it? Let me know.
Have ideas? [Submit a pull request][pullreq] or [open an issue][openissue].
Issues to report? [Open an issue][openissue].

[pycat-href]: https://github.com/gisce/pycatastro
[jmespath-href]: https://github.com/jmespath/jmespath.py
[polars-href]: https://github.com/pola-rs/polars/
[docshref]: https://catastronaut.readthedocs.io
[pullreq]: https://github.com/adrivn/catastronaut/compare
[openissue]: https://github.com/adrivn/catastronaut/issues/new/choose
