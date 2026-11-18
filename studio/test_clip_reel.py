"""Self-check: caption chunks never split a number whisper tokenized as "10" + ",000"."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
from clip_reel import chunk_words

w = [(0, 1, " utensils"), (1, 2, " throughout"), (2, 3, " the"), (3, 4, " country."), (4, 5, " 10"), (5, 6, ",000"), (6, 7, " pounds")]
assert [t for _, _, t in chunk_words(w)] == ["utensils throughout the country. 10,000", "pounds"]
assert chunk_words([(0, 1, " ....."), (1, 2, " ...")]) == []
print("clip_reel self-check: ok")
