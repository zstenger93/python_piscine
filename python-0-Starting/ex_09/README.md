# The Package

## Build

```
python setup.py sdist bdist_wheel
```

## Install

```
pip3 install ./dist/ft_package-0.0.1.tar.gz
```

## Display

```
pip3 show -v ft_package
```

## Test

```
python3.10 tester.py
```

## Uninstall

```
pip3 uninstall ft_package
```

# Information

ft_package

This Python module defines a function called `setup()`.

The `setup()` function creates a distribution of the `ft_package` package.

The `setup()` function takes the following arguments:

* `name`: The name of the package.
* `version`: The version of the package.
* `description`: A brief description of the package.
* `author`: The author of the package.
* `author_email`: The author's email address.
* `url`: The URL for the package's homepage.
* `packages`: A list of the directories that contain Python modules.
* `classifiers`: A list of keywords that are used to categorize the package.
* `entry_points`: A list of console scripts for the package.

The `setup()` function returns a dictionary that contains the metadata for the package.

Here is an explanation of each of the arguments:

* `name`: The name of the package. This is the name that will be used to install the package.
* `version`: The version of the package. This is a string that uniquely identifies the version of the package.
* `description`: A brief description of the package. This description will be displayed when the user installs the package.
* `author`: The author of the package. This is the name of the person or organization that created the package.
* `author_email`: The author's email address. This is the email address that the user can contact if they have any questions about the package.
* `url`: The URL for the package's homepage. This is the URL where the user can find more information about the package.
* `packages`: A list of the directories that contain Python modules. This list tells the setuptools module where to find the Python modules that are included in the package.
* `classifiers`: A list of keywords that are used to categorize the package. These keywords are used by package managers to find packages that are relevant to the user's needs.
* `entry_points`: A list of console scripts for the package. These scripts can be run from the command line.