#!/usr/bin/env python3
"""
Script to fix image save paths in the notebook after folder reorganization
"""

import json
import os

def fix_notebook_paths(notebook_path):
    """Fix image save paths in Jupyter notebook"""
    
    # Read the notebook
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)
    
    # Track changes
    changes_made = 0
    
    # Image files that need path updates
    image_files = [
        'clustering_metrics.png',
        'cluster_wordclouds.png', 
        'cluster_visualization_2d.png',
        'cluster_distribution.png',
        'final_emotion_distribution.png'
    ]
    
    # Process each cell
    for cell in notebook['cells']:
        if cell['cell_type'] == 'code':
            # Process source lines
            for i, line in enumerate(cell['source']):
                for img_file in image_files:
                    old_path = f"'{img_file}'"
                    new_path = f"'../images/{img_file}'"
                    
                    if old_path in line:
                        cell['source'][i] = line.replace(old_path, new_path)
                        changes_made += 1
                        print(f"✅ Fixed: {old_path} -> {new_path}")
    
    # Save the updated notebook
    if changes_made > 0:
        with open(notebook_path, 'w', encoding='utf-8') as f:
            json.dump(notebook, f, indent=1, ensure_ascii=False)
        print(f"\n🎉 Successfully updated {changes_made} path references in {notebook_path}")
    else:
        print(f"ℹ️  No path updates needed in {notebook_path}")
    
    return changes_made

if __name__ == "__main__":
    notebook_path = "Code_Labelling/notebooks/code_labeling_dataset_enhanced.ipynb"
    
    if os.path.exists(notebook_path):
        changes = fix_notebook_paths(notebook_path)
        print(f"\n📊 Total changes made: {changes}")
    else:
        print(f"❌ Notebook not found: {notebook_path}")