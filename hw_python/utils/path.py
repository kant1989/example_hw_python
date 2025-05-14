def relative_from_root(path: str):
    import hw_python
    from pathlib import Path

    return Path(hw_python.__file__).parent.parent.joinpath(path).absolute().__str__()
