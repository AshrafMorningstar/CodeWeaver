
import os
import json
import time
from bot_config import LANGUAGES, PROGRAM_TYPES
from pathlib import Path

# Try to import openai, handle correctness if not installed (for dry-run purposes)
try:
    from openai import OpenAI
except ImportError:
    OpenAI = None

# Helper to get API key safely
def get_api_key():
    return os.environ.get("OPENAI_API_KEY")

def generate_code_file(client, language, program_type):
    # Prompt engineering to ensure requirements are met
    prompt = f"""
    Act as an expert polyglot programmer.
    Generate a complete, working source code file in {language} that implements a {program_type}.
    
    CRITICAL REQUIREMENTS:
    1. The code MUST be at least 100 lines long. Do not use excessive comments or blank lines to cheat, but do include meaningful documentation.
    2. It must be syntactically correct and runnable/compilable.
    3. Include a file header comment with: Language, Author (AI), and Date.
    4. At the top, include a comment showing the command to run/compile this file: "{LANGUAGES.get(language, {}).get('run', 'Run instruction')}".
    5. The code should be self-contained. If imports are needed, use standard libraries where possible.
    
    Output ONLY the raw code. Do not wrap it in markdown block (```), just the code.
    """
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o", # Or gpt-4-turbo
            messages=[{"role": "system", "content": "You are a code generation engine."},
                      {"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=2500
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error generating {language}: {e}")
        return f"// Error generating code for {language}\n// {str(e)}"

def create_300_files(output_dir="generated_code_files"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    api_key = get_api_key()
    if not api_key:
        print("WARNING: 'OPENAI_API_KEY' environment variable not found.")
        print("Running in DRY-RUN mode (generating dummy files).")
        client = None
    else:
        if OpenAI:
            client = OpenAI(api_key=api_key)
        else:
            print("ERROR: openai package not installed. Run 'pip install openai'.")
            return
            
    manifest_path = os.path.join(output_dir, "manifest.json")
    if os.path.exists(manifest_path):
        with open(manifest_path, 'r') as f:
            results = json.load(f)
        file_count = len(results)
        print(f"Resuming from file #{file_count + 1}...")
    else:
        results = []
        file_count = 0
    target_count = 300
    
    # Flatten the combinations to loop through
    # We loop languages, then types, to ensure variety.
    # To get 300 files from ~50 languages, we need ~6 programs per language.
    
    all_langs = list(LANGUAGES.keys())
    
    while file_count < target_count:
        for language in all_langs:
            if file_count >= target_count:
                break
                
            # Pick a program type
            program_type = PROGRAM_TYPES[file_count % len(PROGRAM_TYPES)]
            
            lang_config = LANGUAGES[language]
            ext = lang_config["ext"]
            category = lang_config.get("category", "Other")
            
            # Create directory structure: Category/Language/
            lang_dir = os.path.join(output_dir, category, language)
            if not os.path.exists(lang_dir):
                os.makedirs(lang_dir)
            
            # Sanitize program type for filename
            safe_type = program_type.lower().replace(' ', '_').replace('/', '_').replace('\\', '_')
            filename = f"{file_count + 1:03d}_{safe_type}{ext}"
            
            print(f"Generating [{file_count+1}/{target_count}]: {category}/{language}/{filename}...")
            
            if client:
                code = generate_code_file(client, language, program_type)
            else:
                # Dry run template
                code = f"// Language: {language}\n// Type: {program_type}\n// Category: {category}\n" + ("print('Line {i}');\n" * 105)
            
            # Clean up markdown code blocks
            if code.startswith("```"):
                code = code.split("\n", 1)[1]
            if code.endswith("```"):
                code = code.rsplit("\n", 1)[0]
                
            filepath = os.path.join(lang_dir, filename)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(code)
            
            file_data = {
                "id": file_count + 1,
                "language": language,
                "category": category,
                "program_type": program_type,
                "filename": os.path.join(category, language, filename).replace("\\", "/"),
                "run_cmd": lang_config["run"].format(file=filename, name=os.path.splitext(filename)[0]),
                "lines": len(code.split('\n'))
            }
            results.append(file_data)
            
            file_count += 1

            
            # Sleep briefly to avoid aggressive rate limits if using real API
            if client:
                time.sleep(1) 
                
    # Save manifest
    with open(os.path.join(output_dir, "manifest.json"), 'w') as f:
        json.dump(results, f, indent=2)
        
    print(f"\nSuccess! Generated {file_count} files in '{output_dir}'.")
    print("See manifest.json for details.")

if __name__ == "__main__":
    create_300_files()
