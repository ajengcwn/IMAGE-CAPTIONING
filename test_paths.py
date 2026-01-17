#!/usr/bin/env python3
"""
Test script to verify all paths are working correctly after reorganization
"""

import os
import json
from pathlib import Path

def test_notebook_paths():
    """Test that all paths in notebook are correct"""
    print("🧪 Testing notebook paths...")
    
    notebook_path = "Code_Labelling/notebooks/code_labeling_dataset_enhanced.ipynb"
    
    if not os.path.exists(notebook_path):
        print(f"❌ Notebook not found: {notebook_path}")
        return False
    
    # Read notebook
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook = json.load(f)
    
    # Check for old paths (should not exist)
    old_paths_found = []
    new_paths_found = []
    
    for cell in notebook['cells']:
        if cell['cell_type'] == 'code':
            for line in cell['source']:
                # Check for old direct paths
                if any(img in line for img in ['clustering_metrics.png', 'cluster_distribution.png']) and '../images/' not in line and 'savefig' in line:
                    old_paths_found.append(line.strip())
                
                # Check for new correct paths
                if '../images/' in line and 'savefig' in line:
                    new_paths_found.append(line.strip())
    
    print(f"✅ Found {len(new_paths_found)} correct image paths")
    print(f"❌ Found {len(old_paths_found)} old image paths")
    
    if old_paths_found:
        print("Old paths still found:")
        for path in old_paths_found:
            print(f"  - {path}")
    
    return len(old_paths_found) == 0

def test_data_paths():
    """Test that data paths are accessible from notebook location"""
    print("\n🧪 Testing data paths...")
    
    notebook_dir = Path("Code_Labelling/notebooks")
    
    # Test input data path (should be ../../data/raw/ from notebook location)
    input_path = notebook_dir / "../../data/raw/dataset_clean.csv"
    input_exists = input_path.exists()
    print(f"{'✅' if input_exists else '❌'} Input data: {input_path} {'exists' if input_exists else 'NOT FOUND'}")
    
    # Test output data path (directory should exist)
    output_dir = notebook_dir / "../../data/raw"
    output_dir_exists = output_dir.exists()
    print(f"{'✅' if output_dir_exists else '❌'} Output directory: {output_dir} {'exists' if output_dir_exists else 'NOT FOUND'}")
    
    return input_exists and output_dir_exists

def test_image_paths():
    """Test that image directory exists and is accessible from notebook"""
    print("\n🧪 Testing image paths...")
    
    notebook_dir = Path("Code_Labelling/notebooks")
    images_dir = notebook_dir / "../images"
    
    images_exists = images_dir.exists()
    print(f"{'✅' if images_exists else '❌'} Images directory: {images_dir} {'exists' if images_exists else 'NOT FOUND'}")
    
    if images_exists:
        image_files = list(images_dir.glob("*.png"))
        print(f"✅ Found {len(image_files)} PNG files in images directory")
        for img in image_files[:3]:  # Show first 3
            print(f"  - {img.name}")
        if len(image_files) > 3:
            print(f"  ... and {len(image_files) - 3} more")
    
    return images_exists

def test_folder_structure():
    """Test the overall folder structure"""
    print("\n🧪 Testing folder structure...")
    
    expected_structure = {
        "Code_Labelling/README.md": "Main README",
        "Code_Labelling/docs/": "Documentation folder",
        "Code_Labelling/images/": "Images folder", 
        "Code_Labelling/notebooks/": "Notebooks folder",
        "Code_Labelling/notebooks/code_labeling_dataset_enhanced.ipynb": "Main notebook"
    }
    
    all_good = True
    for path, description in expected_structure.items():
        exists = os.path.exists(path)
        print(f"{'✅' if exists else '❌'} {description}: {path}")
        if not exists:
            all_good = False
    
    return all_good

if __name__ == "__main__":
    print("🔍 TESTING PATH INTEGRITY AFTER FOLDER REORGANIZATION")
    print("=" * 60)
    
    tests = [
        ("Notebook Paths", test_notebook_paths),
        ("Data Paths", test_data_paths), 
        ("Image Paths", test_image_paths),
        ("Folder Structure", test_folder_structure)
    ]
    
    results = []
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"❌ {test_name} failed with error: {e}")
            results.append((test_name, False))
    
    print("\n" + "=" * 60)
    print("📊 TEST RESULTS SUMMARY:")
    
    all_passed = True
    for test_name, passed in results:
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"  {status} - {test_name}")
        if not passed:
            all_passed = False
    
    print(f"\n🎯 Overall Status: {'✅ ALL TESTS PASSED' if all_passed else '❌ SOME TESTS FAILED'}")
    
    if all_passed:
        print("\n🎉 Folder reorganization completed successfully!")
        print("   All paths are working correctly and code should run without issues.")
    else:
        print("\n⚠️  Some issues found. Please review the failed tests above.")