import os


def uninstall():
    os.system("rm -rf build")
    os.system("rm -rf dist")
    os.system("rm -rf ft_package.egg-info")
    os.system("rm -rf ft_package/__pycache__")
    os.system("pip3 uninstall ft_package")


if __name__ == "__main__":
    uninstall()
