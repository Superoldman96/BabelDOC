from importlib.metadata import PackageNotFoundError
from importlib.metadata import version

try:
    __version__ = version("pdfminer.six")
except PackageNotFoundError:
    # package is not installed, return default
    __version__ = "0.0"

if __name__ == "__main__":
    print(__version__)
