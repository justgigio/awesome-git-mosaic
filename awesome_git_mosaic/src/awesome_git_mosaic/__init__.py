from usecases.write_mosaic import WriteMosaic

def write(text: str, strength: int = 5, multiply: int = 1, background: bool = False):
  WriteMosaic().write(text, strength, multiply, background)
