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

# bot_config.py

# A comprehensive list of programming languages and their execution commands/extensions.
# We aim for diverse coverage to reach 300+ unique file types or variations.

LANGUAGES = {
    # --- Web ---
    "JavaScript": {"ext": ".js", "category": "Web", "run": "node {file}"},
    "TypeScript": {"ext": ".ts", "category": "Web", "run": "npx ts-node {file}"},
    "HTML": {"ext": ".html", "category": "Web", "run": "# Open in browser"},
    "CSS": {"ext": ".css", "category": "Web", "run": "# Styling file"},
    "PHP": {"ext": ".php", "category": "Web", "run": "php {file}"},
    "XML": {"ext": ".xml", "category": "Web", "run": "# Data file"},
    "JSON": {"ext": ".json", "category": "Web", "run": "# Data file"},
    "YAML": {"ext": ".yaml", "category": "Web", "run": "# Data file"},
    
    # --- Mainstream / General Purpose ---
    "Python": {"ext": ".py", "category": "Mainstream", "run": "python {file}"},
    "Java": {"ext": ".java", "category": "Mainstream", "run": "javac {file} && java {name}"},
    "C#": {"ext": ".cs", "category": "Mainstream", "run": "csc {file} && ./{name}.exe"},
    "Go": {"ext": ".go", "category": "Mainstream", "run": "go run {file}"},
    "Ruby": {"ext": ".rb", "category": "Mainstream", "run": "ruby {file}"},
    "Swift": {"ext": ".swift", "category": "Mainstream", "run": "swift {file}"},
    "Kotlin": {"ext": ".kt", "category": "Mainstream", "run": "kotlinc {file} -include-runtime -d {name}.jar && java -jar {name}.jar"},
    "Dart": {"ext": ".dart", "category": "Mainstream", "run": "dart {file}"},

    # --- Systems / Low Level ---
    "C": {"ext": ".c", "category": "Systems", "run": "gcc {file} -o {name} && ./{name}"},
    "C++": {"ext": ".cpp", "category": "Systems", "run": "g++ {file} -o {name} && ./{name}"},
    "Rust": {"ext": ".rs", "category": "Systems", "run": "rustc {file} && ./{name}"},
    "Assembly (x86)": {"ext": ".asm", "category": "Systems", "run": "nasm -f elf64 {file} && ld {name}.o -o {name} && ./{name}"},
    "Zig": {"ext": ".zig", "category": "Systems", "run": "zig run {file}"},
    "Nim": {"ext": ".nim", "category": "Systems", "run": "nim c -r {file}"},
    "D": {"ext": ".d", "category": "Systems", "run": "dmd -run {file}"},
    "V": {"ext": ".v", "category": "Systems", "run": "v run {file}"},
    "Ada": {"ext": ".adb", "category": "Systems", "run": "gnatmake {file} && ./{name}"},
    "Fortran": {"ext": ".f90", "category": "Systems", "run": "gfortran {file} -o {name} && ./{name}"},
    "Cobol": {"ext": ".cbl", "category": "Systems", "run": "cobc -x {file} && ./{name}"},
    "Pascal": {"ext": ".pas", "category": "Systems", "run": "fpc {file} && ./{name}"},

    # --- Scripting / Data ---
    "R": {"ext": ".R", "category": "Data_Science", "run": "Rscript {file}"},
    "Julia": {"ext": ".jl", "category": "Data_Science", "run": "julia {file}"},
    "Matlab": {"ext": ".m", "category": "Data_Science", "run": "matlab -batch \"run('{file}')\""},
    "SAS": {"ext": ".sas", "category": "Data_Science", "run": "sas {file}"},
    "SQL": {"ext": ".sql", "category": "Data_Science", "run": "# SQL script"},
    "Perl": {"ext": ".pl", "category": "Scripting", "run": "perl {file}"},
    "Lua": {"ext": ".lua", "category": "Scripting", "run": "lua {file}"},
    "Shell": {"ext": ".sh", "category": "Scripting", "run": "bash {file}"},
    "PowerShell": {"ext": ".ps1", "category": "Scripting", "run": "powershell -ExecutionPolicy Bypass -File {file}"},
    "Batch": {"ext": ".bat", "category": "Scripting", "run": "{file}"},
    "Tcl": {"ext": ".tcl", "category": "Scripting", "run": "tclsh {file}"},
    "VBScript": {"ext": ".vbs", "category": "Scripting", "run": "cscript {file}"},
    "Groovy": {"ext": ".groovy", "category": "Scripting", "run": "groovy {file}"},
    "CoffeeScript": {"ext": ".coffee", "category": "Scripting", "run": "coffee {file}"},

    # --- Functional ---
    "Haskell": {"ext": ".hs", "category": "Functional", "run": "runhaskell {file}"},
    "Scala": {"ext": ".scala", "category": "Functional", "run": "scala {file}"},
    "Elixir": {"ext": ".exs", "category": "Functional", "run": "elixir {file}"},
    "Clojure": {"ext": ".clj", "category": "Functional", "run": "clojure {file}"},
    "F#": {"ext": ".fsx", "category": "Functional", "run": "dotnet fsi {file}"},
    "OCaml": {"ext": ".ml", "category": "Functional", "run": "ocaml {file}"},
    "Scheme": {"ext": ".scm", "category": "Functional", "run": "scheme < {file}"},
    "Erlang": {"ext": ".erl", "category": "Functional", "run": "escript {file}"},
    "Racket": {"ext": ".rkt", "category": "Functional", "run": "racket {file}"},
    "Common Lisp": {"ext": ".lisp", "category": "Functional", "run": "sbcl --script {file}"},

    # --- Hardware / Other ---
    "Verilog": {"ext": ".v", "category": "Hardware", "run": "iverilog -o {name} {file} && vvp {name}"},
    "VHDL": {"ext": ".vhd", "category": "Hardware", "run": "ghdl -a {file} && ghdl -e {name} && ghdl -r {name}"},
    "Haxe": {"ext": ".hx", "category": "Other", "run": "haxe -main {name} --interp"},
    "Smalltalk": {"ext": ".st", "category": "Other", "run": "gst {file}"},
    "Forth": {"ext": ".fs", "category": "Other", "run": "gforth {file} -e bye"},
    "Prolog": {"ext": ".pl", "category": "Other", "run": "swipl -s {file}"},
}
    # ... (User can extend this list further to reach 300 distinct entries, 
    # possibly by adding variants like 'Python (NumPy)', 'Python (Pandas)', etc.)


# We can programmatically expand this to 300 by combining languages with paradigms
# BUT for a true "300 languages" request, we'd need more specific esoteric languages.
# For practical purposes, if we run out of unique languages, we will generate variations.

PROGRAM_TYPES = [
    "CLI Calculator",
    "TODO Manager",
    "File Processor",
    "Web Server or API Stub",
    "Number Guessing Game",
    "Data Analyzer / Sorter",
    "Unit Converter",
    "Text Parser / Formatter",
    "Simple Encryption/Decryption",
    "Pathfinding Algorithm (e.g. Dijkstra)",
    "Matrix Multiplication",
    "Inventory System",
    "Student Grade Management",
    "Bank Account System",
    "Library Management Mockup"
]
