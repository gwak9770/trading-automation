# Repository Guidelines

## Project Structure & Module Organization

This repository currently contains no application code, tests, dependency manifests, or build configuration. Keep the root focused on project documentation and configuration. As implementation begins, group application code in component-local `src/` directories under `youtube-analyzer/` and `trading-bot/`, automated tests in `tests/`, and reusable development utilities in `scripts/` when needed. Add asset directories only when needed, and document their purpose in `README.md`.

## Build, Test, and Development Commands

No build, test, or local execution commands are currently configured. When selecting the project toolchain, add reproducible setup, run, lint, and test commands to `README.md` and the appropriate dependency manifest. Specify the required runtime version. Do not document example commands as working commands until their configuration exists and they have been verified.

## Coding Style & Naming Conventions

Follow the formatter and idioms of the chosen implementation language. Use consistent indentation within each file, descriptive module names, and names that express intent. Introduce formatter and linter configuration alongside the first source files. Keep modules focused, and avoid mixing configuration, external service access, and business logic in one module.

## Testing Guidelines

No testing framework or coverage threshold is established. Add automated tests with each meaningful behavior change, using descriptive names such as `test_<behavior>` where supported. Keep tests deterministic and independent of live accounts or network services. Document the test command when the framework is introduced.

## Commit & Pull Request Guidelines

No Git history is available to establish existing commit conventions. Use concise, imperative commit subjects, such as `Add configuration validation`. Keep changes focused. Pull requests should describe the purpose, summarize behavior changes, link relevant issues, and report validation performed. Explain any checks that could not run.

## Security & Configuration

Never commit credentials, account identifiers, or private configuration. Provide placeholder configuration examples and ignore local secret files. If trading integrations are added, use mocks or sandbox environments for tests and require explicit configuration before enabling live execution.

## Project Records and Continuity

- Read `PROJECT_STATUS.md` and `NEXT_STEPS.md` before starting work.
- Distinguish implemented, tested, planned, and unverified behavior. Never claim servers or live trading are complete without evidence.
- At task end, update relevant documents, test results, errors, and `NEXT_STEPS.md`; record important changes in `CHANGELOG.md`.
- Use repository-relative paths and document runtime versions and reproducible commands for work on other computers.
- Preserve existing files and Git history. Do not delete history, force-push, or overwrite existing remote content without explicit user approval.
- Obtain final user confirmation before creating the GitHub remote repository and performing the first push.

## Trading and Secret Handling

- Never commit Binance keys, tokens, passwords, account identifiers, SSH private keys, private configuration, raw large videos, or unnecessary logs and temporary files, even to a private repository.
- Inspect staged changes for secrets before committing; `.gitignore` is not a substitute for inspection.
- Keep live execution disabled by default when implemented. Require explicit configuration and validate backtesting, paper trading, risk limits, and recovery before live use.
- Treat Naver Cloud server setup as in progress / verification required until actual provisioning and operation are evidenced.

## Korean Text Encoding and Verification

- Save Korean text and Markdown explicitly as UTF-8; preserve existing instructions.
- Treat PowerShell console output encoding separately from file storage encoding.
- After writing, reread actual bytes with strict UTF-8 decoding and verify expected Korean text, replacement characters and unexpected question-mark sequences.
- Use ASCII-escaped JSON or Unicode code points when console rendering is unreliable.
- Literal question marks cannot be repaired by changing encoding; reconstruct only from confirmed context and record the rewrite.
- Exclude temporary verification files and unnecessary backups from Git; recheck staged content before committing.
