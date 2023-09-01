import os
from tqdm import tqdm


def build():
    with tqdm(total=100, desc="Build  ") as pbar:
        os.system("python setup.py sdist bdist_wheel > /dev/null 2>&1")
        pbar.update(100)
    print()


def install():
    with tqdm(total=100, desc="Install") as pbar:
        os.system("pip3 install ./dist/ft_package-0.0.1.tar.gz >\
                  /dev/null 2>&1")
        pbar.update(100)
    print()


def show():
    with tqdm(total=100, desc="Display") as pbar:
        pbar.update(100)
    print()
    os.system("pip3 show -v ft_package")
    print()


def test():
    with tqdm(total=100, desc="Tester ") as pbar:
        pbar.update(100)
    print()
    os.system("python3.10 tester.py")


if __name__ == "__main__":
    build()
    install()
    show()
    test()
