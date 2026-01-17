#!/usr/bin/env python3
"""
Script to fix data paths in the notebook after folder reorganization
"""

import json
import os

def fix_data_paths(notebook_path):
    """Fix data paths in Jupyter notebook"""
    
    # Read the notebook
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)
    
    # Track changes
    changes_made = 0
    
    # Process each cell
    for cell in notebook['cells']:
        if cell['cell_type'] == 'code':
            # Process source lines
            for i, line in enumerate(cell['source']):
                # Fix input/output file paths
                if "'../data/raw/" in line:
                    cell['source'][i] = line.replace("'../data/raw/", "'../../data/raw/")
                    changes_made += 1
                    print(f"✅ Fixed data path: ../data/raw/ -> ../../data/raw/")
    
    # Save the updated notebook
    if changes_made > 0:
        with open(notebook_path, 'w', encoding='utf-8') as f:
            json.dump(notebook, f, indent=1, ensure_ascii=False)
        print(f"\n🎉 Successfully updated {changes_made} data path references in {notebook_path}")
    else:
        print(f"ℹ️  No data path updates needed in {notebook_path}")
    
    return changes_made

if __name__ == "__main__":
    notebook_path = "Code_Labelling/notebooks/code_labeling_dataset_enhanced.ipynb"
    
    if os.path.exists(notebook_path):
        changes = fix_data_paths(notebook_path)
        print(f"\n📊 Total changes made: {changes}")
    else:
        print(f"❌ Notebook not found: {notebook_path}")