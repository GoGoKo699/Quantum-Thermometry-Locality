# Hosted Markdown verification

This optional read-only workflow checks the mathematics displayed by GitHub at an exact public commit. It complements the [scientific checks](../README.md). It does not execute the temperature-estimation experiment or establish a theorem.

The collector inventories every tracked Markdown page at the requested commit, compiles each source expression into reference MathML, and visits the actual commit-pinned GitHub page in an unsigned-in Chromium context. It compares the complete hosted MathML structure, expression counts, relations, labels and display geometry at widths of 1440 and 760 pixels. The [text contract](math-contract.json) adds explicit expected text for the headline results. Source compilation alone cannot satisfy the hosted comparison.

## Run locally

The tested dependencies are Node.js 18 or later, Python 3.10 or later, Git, Playwright 1.56.1, MathJax 3.2.1 and Playwright's Chromium browser. Install the Node dependencies in a temporary directory outside the repository:

```bash
npm install --prefix /tmp/thermometry-hosted-deps playwright@1.56.1 mathjax-full@3.2.1
/tmp/thermometry-hosted-deps/node_modules/.bin/playwright install chromium
NODE_PATH=/tmp/thermometry-hosted-deps/node_modules node verification/hosted/capture_hosted_math.cjs \
  --root "$PWD" \
  --repository GoGoKo699/Quantum-Thermometry-Locality \
  --revision "$(git rev-parse HEAD)" \
  --contract verification/hosted/math-contract.json \
  --output /tmp/thermometry-hosted-evidence
```

The revision must exist on public GitHub, and the output directory must be absent or empty. Use a new directory for a new attempt so earlier evidence is preserved. The inventory reads exact Git objects and ignores working-tree changes.

The repository workflow performs the same check on the pull request's head commit or on the revision selected for a manual run. It has read-only repository permissions and uploads its evidence even when the comparison fails. A run records the exact source tree, software versions, captured pages, screenshots, comparison results and artifact hashes.

## Interpret a result

`hosted-report.json` reports whether the automatic comparison passed. A failure can identify missing renderer capability, a failed connection, an access restriction, a source/host mismatch or a display that exceeds the available width. Preserve the cause and inspect the affected page before changing source or choosing a permitted execution environment.

A passing structural report still requires visual inspection of the screenshots for legibility, tables and navigation. It does not certify mathematical equivalence beyond the comparison performed, scientific correctness, all browsers, or future changes to GitHub's renderer. Changes to source expressions require a fresh capture and corresponding text-contract updates where applicable.
