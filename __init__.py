from .gongzuo import *
from .cstxt import *
NODE_CLASS_MAPPINGS = {
    "gongzuo": gongzuo,
    "Example": gongzuotostring,
    "cstxt": txt_input,
    "txt_len": txt_len,
    "fenkuai": fenkuai,
    "fen_ai": fen_ai,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "gongzuo": "gongzuo",
    "Example": "gongzuotostring Node",
    "cstxt": "txt_input",
    "txt_len": "txt_len",
    "fenkuai": "fenkuai",
    "fen_ai":" fen_ai",
}

