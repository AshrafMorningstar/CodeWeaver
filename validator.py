"""
/*
 * © 2022-2026 Ashraf Morningstar
 * GitHub: https://github.com/AshrafMorningstar
 *
 * This project is a personal recreation of existing projects, developed by Ashraf Morningstar 
 * for learning and skill development. Original project concepts remains the intellectual 
 * property of their respective creators.
 */
"""

import os
import json

def validate_files(output_dir="generated_code_files"):
    manifest_path = os.path.join(output_dir, "manifest.json")
    if not os.path.exists(manifest_path):
        print(f"Manifest not found at {manifest_path}. Run omnicoder.py first.")
        return

    with open(manifest_path, 'r') as f:
        files = json.load(f)

    stats = {
        "total_files": len(files),
        "pass_count": 0,
        "fail_count": 0,
        "languages": {},
        "failures": []
    }

    print(f"Validating {stats['total_files']} files...")

    for entry in files:
        # manifest filename now includes the RELATIVE path (e.g. Web/JavaScript/001_calculator.js)
        # We assume output_dir is the root of where files are generated.
        filepath = os.path.join(output_dir, entry["filename"])
        
        # Double check actual file metrics
        if not os.path.exists(filepath):
            stats["fail_count"] += 1
            stats["failures"].append({"file": entry["filename"], "reason": "File missing"})
            continue
            
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
            line_count = len(lines)
            
        lang = entry["language"]
        stats["languages"][lang] = stats["languages"].get(lang, 0) + 1
        
        if line_count < 99:
            stats["fail_count"] += 1
            stats["failures"].append({"file": entry["filename"], "lines": line_count, "reason": "Under 99 lines"})
            print(f"FAIL: {entry['filename']} ({line_count} lines)")
        else:
            stats["pass_count"] += 1
            
    print("\n--- Validation Report ---")
    print(f"Total: {stats['total_files']}")
    print(f"Passed: {stats['pass_count']}")
    print(f"Failed: {stats['fail_count']}")
    
    if stats["failures"]:
        print("\nFailures:")
        for fail in stats["failures"]:
            print(f" - {fail}")
    else:
        print("\nAll files passed the line count check!")

if __name__ == "__main__":
    validate_files()
