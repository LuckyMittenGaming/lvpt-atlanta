from pathlib import Path
import subprocess


def run(cmd):
    subprocess.run(cmd, check=True)

p = Path('index.html')
s = p.read_text(encoding='utf-8')

replacements = {
    'Request an LA Event Quote': 'Request an Atlanta Quote',
    'Customize your Atlanta corporate event, team building activation, or client entertainment experience, then send your quote request directly to Las Vegas Poker Training.': 'Customize your Atlanta corporate event, team building activity, corporate outing, casino night, or client entertainment experience, then send your quote request directly to Las Vegas Poker Training.',
    'Professional poker instructors available for Atlanta corporate events, private training experiences, team building activations, and client entertainment.': 'Professional poker instructors available for Atlanta corporate events, private training experiences, team building activities, corporate outings, and client entertainment programs.',
    'Our poker training experiences are a 2-hour minimum, with 3 hours minimum recommended if you want to finish with a tournament. This flow can be adjusted based on group size, skill level, venue, and event goals.': 'Our poker training experiences are a 2-hour minimum, with 3 hours recommended if you want to finish with a tournament. This flow can be adjusted based on guest count, skill level, venue access, timing, and event goals.'
}

for old, new in replacements.items():
    s = s.replace(old, new)

p.write_text(s, encoding='utf-8')

Path('tools/fix_atlanta_leftovers.py').unlink(missing_ok=True)
Path('.github/workflows/fix-atlanta-leftovers.yml').unlink(missing_ok=True)

run(['git', 'config', 'user.name', 'github-actions[bot]'])
run(['git', 'config', 'user.email', '41898282+github-actions[bot]@users.noreply.github.com'])
run(['git', 'add', 'index.html', 'tools/fix_atlanta_leftovers.py', '.github/workflows/fix-atlanta-leftovers.yml'])
run(['git', 'commit', '-m', 'Clean up Atlanta page copy leftovers'])
run(['git', 'push'])
