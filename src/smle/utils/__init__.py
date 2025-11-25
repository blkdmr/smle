import random
import numpy as np

try:
    import torch
except ImportError as e:
    raise RuntimeError(
        "Torch is required by smle."
        "Install it yourself (GPU/CPU) or use 'pip install smle[torch]'."
    ) from e

def set_seed(seed: int) -> None:
    """
    Sets the random seed for Python, NumPy, and PyTorch to ensure reproducibility.
    """
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)

    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False


import secrets
import random

def generate_haiku_id() -> str:
    # A curated list of "beautiful" words
    adjectives = [
        "autumn", "hidden", "bitter", "misty", "silent",
        "empty", "dry", "dark", "summer", "icy", "delicate",
        "quiet", "white", "cool", "spring", "winter", "patient",
        "twilight", "dawn", "crimson", "wispy", "weathered",
        "blue", "billowing", "broken", "cold", "damp", "falling",
        "frosty", "green", "long", "late", "lingering"
    ]

    nouns = [
        "waterfall", "river", "breeze", "moon", "rain",
        "wind", "sea", "morning", "snow", "lake", "sunset",
        "pine", "shadow", "leaf", "dawn", "glitter", "forest",
        "hill", "cloud", "meadow", "sun", "glade", "bird",
        "brook", "butterfly", "bush", "dew", "dust", "field",
        "fire", "flower", "firefly", "feather", "grass"
    ]

    # Select words
    adj = random.choice(adjectives)
    noun = random.choice(nouns)

    # Add a secure hex suffix (2 bytes = 4 hex chars) to ensure uniqueness
    # Use secrets (not random) for the numeric part for security
    suffix = secrets.token_hex(2)

    return f"{adj}_{noun}_{suffix}"