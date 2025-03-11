def ft_tqdm(lst: range):
    """
    ft_tqdm(lst: range) -> generator

    Mimics the behavior of the built-in tqdm function.
    Iterates over lst, updating a progress bar on the same line using carriage
    returns, and yields each element of lst. The progress bar displays a
    percentage, a visual bar (using '=' and '>' characters), and the
    current/total count.

    Example output (for lst = range(333)):
    100%|[================================>]| 333/333
    """
    total = len(lst)
    bar_width = 60
    for i, item in enumerate(lst):
        progress = (i + 1) / total
        percentage = int(progress * 100)
        filled = int(progress * bar_width)
        if filled == 0:
            bar = ">" + " " * (bar_width - 1)
        elif filled < bar_width:
            bar = "=" * (filled - 1) + ">" + " " * (bar_width - filled)
        else:
            bar = "=" * (bar_width - 1) + ">"
        print(f"\r{percentage}%|[{bar}]| {i+1}/{total}", end="", flush=True)
        yield item
    print()
