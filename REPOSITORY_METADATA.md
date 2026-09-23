# Repository Technical Documentation

## Overview

| Field | Details |
|---|---|
| Repository | `vanshepamsystm/SELENIUM-FULL-COURSE-` |
| Branch scanned | `main` |
| Primary language | Python |
| Project type | Selenium WebDriver automation training repository with pytest-based tests, fixtures, page objects, data-driven examples, and standalone scripts |
| Documentation generated | 2026-03-31 |
| Source head | `b80781f334ba246d6a9b4b1d45f5faba36630841` (`intial commit`) |

## Standard Data

| Category | Extracted data |
|---|---|
| Python source files | Broad collection distributed across Selenium practice, PyTest, Page Object Model, framework, data-driven, and end-to-end directories |
| Test framework | pytest; test modules use `test_` naming and fixtures in `conftest.py` |
| Browser automation | Selenium WebDriver with Chrome, Firefox, and Edge examples |
| Test reporting | `pytest-html` imports and checked-in HTML reports/assets in several directories |
| Test data | JSON (`New Folder/file.json`, `Practice Project/file.json`) and Excel workbooks accessed with `openpyxl` |
| Configuration | `Practice Project/pytest.ini` defines the `smoke` marker |
| Generated artifacts | Multiple `__pycache__` trees, screenshots/report assets, HTML reports, and PNGs are committed |
| External systems exercised | SauceDemo, Rahul Shetty Academy Angular practice/login pages, and EPAM |

## Code Metadata

### Entry points and execution surfaces

- **pytest suites:** `Framework/test_file.py`, `Practice Project/test_file.py`, `Official CODE/test_framework.py`, `Py Test/test_demo1.py`, `Py Test/test_demo2.py`, `Understand Conftestt/*`, `Understanding Scope In Pytest/*`, `parametrized fixtures/test_crossbrowser.py`, and data-driven fixture modules.
- **Standalone scripts:** Selenium examples under `PYTHON SELENIUM/`, `Practice of selenium/`, `Additional/`, `Data Driven Testing/`, and `EPAM/` execute from module top level.
- **End-to-end flows:** `End to End Project/production.py` and `Official CODE/end to end project file.py` demonstrate direct browser workflows.
- **Pytest configuration:** `Practice Project/pytest.ini`; fixture setup is supplied by directory-local `conftest.py` files.
- **Page-object entry points:** `Practice Project/Sign.py`, `inventory.py`, `cart_page.py`, and `Official CODE/OfficialPageObjects/*.py`.

### Framework patterns

- Browser fixtures select Chrome, Firefox, or Edge through pytest command-line options.
- Page objects encapsulate locators and actions; `Practice Project/BasePage.py` centralizes waits, clicks, text reads, and input.
- Data-driven tests use `pytest.mark.parametrize`, JSON loading, fixture parameters, and Excel via `openpyxl`.
- Synchronization uses implicit waits and `WebDriverWait` with expected conditions.
- Failure reporting includes a pytest hook intended to capture screenshots and attach them to `pytest-html` reports.

## Dependencies

No `requirements.txt`, `pyproject.toml`, `setup.py`, `Pipfile`, `package.json`, or `pom.xml` was found on `main`. Dependencies inferred from imports and configuration are:

| Dependency | Evidence / role |
|---|---|
| `selenium` | WebDriver, locators, waits, browser automation |
| `pytest` | Test discovery, fixtures, parametrization, markers |
| `pytest-html` | HTML reporting and report extras |
| `openpyxl` | Excel workbook read/write examples |
| Python standard library | `json`, `os`, `time` |
| Browser drivers | Chrome, Firefox, and Edge drivers are expected to be available/configured at runtime |

## Repository Structure

- `PYTHON SELENIUM/`, `Practice of selenium/`: foundational Selenium exercises.
- `Py Test/`, `Theory PyTest/`, `Understanding Scope In Pytest/`, `Understand Conftestt/`: pytest concepts and fixture examples.
- `Framework/`, `Practice Project/`, `Official CODE/`, `PageObjectModel/`: increasingly structured automation frameworks.
- `Data Driven Testing/`, `DATA DRIVEN FIXTURES PyTEST/`, `parametrized fixtures/`: data and cross-browser examples.
- `End to End Project/`, `EPAM/`, `Additional/`: end-to-end and miscellaneous scripts.

## Compliance

| Control | Status / observation |
|---|---|
| Dependency manifest | **Gap** — no standard dependency lock or manifest found; dependencies are inferred from imports. |
| Secrets management | **At risk** — source contains hard-coded credentials and local Windows paths; rotate/remove credentials and use environment variables or a secret store. |
| Test data handling | **At risk** — JSON files contain user-like credentials/profile data; review whether this is synthetic and avoid committing real personal data. |
| Generated artifacts | **Needs improvement** — `__pycache__`, screenshots, and reports are committed; add suitable ignore rules. |
| Data Privacy Standards | **Action required** — define data classification, consent/legal basis, minimization, retention/deletion, masking of credentials and personal data, access control, and incident handling for test data and generated artifacts. |

## Disaster Recovery Strategy

- **Source recovery:** Keep `main` protected and maintain the documentation branch/PR workflow; retain repository history and periodically export critical source/configuration.
- **Dependency recovery:** Add and back up a pinned dependency manifest (at minimum Selenium, pytest, pytest-html, and openpyxl) and document supported Python/browser versions.
- **Test environment recovery:** Document browser/driver provisioning, URLs, non-production test accounts, and required environment variables. Do not restore hard-coded secrets from source control.
- **Artifact recovery:** Store reports and screenshots in controlled CI artifacts with defined retention; exclude caches and local paths from source backups.
- **Validation:** After recovery, run a smoke subset using the `smoke` marker and verify browser fixture startup, page-object imports, and report generation.
- **Ownership and cadence:** Assign an owner for backup/restore procedures, test restoration at least quarterly, and record recovery time and recovery point objectives.

## Findings and Recommended Next Steps

1. Add `requirements.txt` or `pyproject.toml` with pinned, supported versions.
2. Remove credentials and machine-specific paths from code and JSON; parameterize through environment variables or CI secrets.
3. Fix inconsistent fixture option access (`getoption("browser_name")` versus `getoption("--browser_name")`) and ensure unsupported browser values fail clearly.
4. Add `.gitignore` entries for `__pycache__/`, screenshots, local reports, and IDE metadata.
5. Normalize imports and naming, remove duplicate imports, and repair stale page-object examples before using them as production templates.
6. Add CI to run a deterministic smoke suite and publish reports without committing generated output.
