# Release

## PyMeasure package

1. Pull the latest `master` branch
2. `git checkout -b v<version>_release`
3. Update CHANGES.rst with the changelog
    * On the repo page, go to Tags->Releases->Draft a new release
    * Add a dummy tag name and select "create tag on publish" -- we will not execute this, just use it to autogenerate a changelog
    * The button "Generate release notes" will generate Markdown text with all PRs since the last tag -- copy that into CHANGES.rst
    * Adapt the format and structure to the previous release message:
    * Divide the entries into categories and try to begin entries with "New", "Add", "Fix" or "Remove" as appropriate. (This could also be automated by the above generator with some labeling effort on our part)
    * We also remove the PR URLs as they clutter the log and condense the new contributors list.
    * Helpful regex entries:
      * For the PR URLs: `by (@[\w-]+) in https://github.com/pymeasure/pymeasure/pull/(\d+)` to `($1, #$2)`.
      * For new contributors: ` made their first contribution in https://github.com/pymeasure/pymeasure/pull/\d+` to `, `
4. Update the version number in CITATION.cff
    * On the line starting with `version: `, replace the current version number with the new version number 
5. Push the changes up as a PR
6. Verify that the builds complete
7. Merge the PR
8. Create a new [release on GitHub](https://github.com/pymeasure/pymeasure/releases)
    * Add a tag name in the format "vX.Y.Z" and select "create tag on publish"
    * You'll have to paste in the changelog entry and probably edit it a bit as that form expects Markdown, not ReST (probably just removing `:code:` tags will be sufficient).
    * Publish the release
8. Approve the _build and upload_ run under Actions.
   This will create the wheel and upload it to PyPI.

## PyPI release - manually

Official guide [here](https://packaging.python.org/en/latest/tutorials/packaging-projects/).

If the upload action does not work, you can create a PyPI release manually:

1. Fetch `master`, build and check the source packages
    - `python -m pip install --upgrade build twine`
    - `python -m build`
    - Check the distributions (`twine check dist/*`, version will not yet be correct)
2. Ensure to have a git tag in the format "vX.Y.Z"
3. Build final packages and confirm the correct version number is being used
     - `python -m build`
     - Check the distributions (`twine check dist/*`)
4. Upload the wheel and source distributions to the test server
    - `python -m twine upload --repository testpypi dist/*`
5. Verify the test repository: https://test.pypi.org/project/PyMeasure
6. Confirm that the installation works (best in a separate environment)
    - `python -m pip install --index-url https://test.pypi.org/simple/ --no-deps pymeasure`
7. Upload to the real repository (`twine upload dist/PyMeasure-<version>*`)
8. Verify that the package is updated: https://pypi.org/project/PyMeasure

## conda-forge feedstock

1. Release to PyPI first (the feedstock pulls from there)
2. Pull the latest `master` branch
3. `git checkout -b v<version>_release`
4. Get the SHA256 hash of the PyPI source package at https://pypi.org/project/PyMeasure/#files
5. Update recipe/meta.yml with the checksum and version number. Important: Work in your personal fork of the feedstock repo (the conda-forge tooling requires that) and create a PR from there.
6. Push the changes up as a PR
7. Verify that the builds complete
8. Merge the PR
