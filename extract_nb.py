import json

with open('churn_analysis.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

with open('notebook_summary.txt', 'w', encoding='utf-8') as out:
    for i, cell in enumerate(nb.get('cells', [])):
        if cell['cell_type'] == 'markdown':
            out.write(f'\n--- CELL {i} (MARKDOWN) ---\n')
            out.write(''.join(cell.get('source', [])))
            out.write('\n')
        elif cell['cell_type'] == 'code':
            out.write(f'\n--- CELL {i} (CODE) ---\n')
            out.write(''.join(cell.get('source', [])))
            out.write('\n')
