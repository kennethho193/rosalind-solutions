def read_input(file_path: str) -> str:
    """Reads the entire contents of a Rosalind input file as a string (stripped of trailing newlines)."""
    with open(file_path, 'r') as f:
        return f.read().strip()