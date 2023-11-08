from awesome_git_mosaic.usecases.write_mosaic import WriteMosaic


def write(
    text: str,
    strength: int = 5,
    multiply: int = 1,
    with_spaces: bool = True,
    background: bool = False,
    inverted: bool = False,
):
    WriteMosaic().write(
        text, strength, multiply, with_spaces, background, inverted
    )  # pragma: no cover
