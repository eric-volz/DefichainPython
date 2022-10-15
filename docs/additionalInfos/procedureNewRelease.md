# How to publish a new PyPi package

## 1. Run Tests

Go into the tests folder and run following commands
```bash
pytest node/

pytest ocean/
```

## 2. Change Version

1. setup.py
2. docs/source/conf.py

## 3. Build package and publish

### Requirements
```bash
pip install twine
```

### Build
```bash
python3 setup.py sdist bdist_wheel
```

### Publish
```bash
twine upload dist/*
```

## 4. Publish new release on GitHub

### Heading
DefichainPython v...

### Markdown
```
## Improvements
...

## [The Code base to this release](last commit)
```

## Additional
1. Version tag
2. created binary's

# Publish on TestPyPi

1. Upload
```
twine upload --repository testpypi dist/*
```
2. Install
```
python3 -m pip install --index-url https://test.pypi.org/simple/ defichain
```
