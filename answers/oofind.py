words = ('Spooky', 'Understood', 'Harpoon')
for w in words:
    pos = w.find('oo')
    pct = pos / len(w) * 100
    print(f'I found \'oo\' in "{w}" at {pct:.1f}%')