## CTF 5

### Problem
There’s a flag in the file “logs” (Hint: grep) \
_The flag structure can be one of three:_
1. CMPN{some_text}
2. picoCTF{some_text}
3. fastctf{some_text}
4. SOME_TEXT

### Solution
picoCTF{grep_is_good_to_find_things_dba08a45}



### Assumptions till now
- `SOME_TEXT` flag need to have at least char before and after `_`

### Tools
- bash (`grep`)
- powershell script language (`Select-String`)
- regex


### Pattern
__`CMPN\{[^\}]+\}|picoCTF\{[^\}]+\}|fastctf\{[^\}]+\}|[A-Z]+_[A-Z]+`__
- using ORing `|` between two flags
1. for CMPN{some_text} `CMPN\{[^\}]+\}`
2. for picoCTF{some_text} `picoCTF\{[^\}]+\}`
3. for fastctf{some_text} `fastctf\{[^\}]+\}`
4. for SOME_TEXT `[A-Z]+_[A-Z]` \

### Commands
1. grep: `grep -Eo '$pattern' "$in_file" > "$out_file"`
    - `-E` &emsp;--extended-regexp  &emsp;  PATTERNS are extended regular expressions
    - `-o` &emsp;--only-matching    &emsp;  show only nonempty parts of lines that match

2. Select-String:
    - `Select-String -Path $inFile -Pattern "$pattern" -AllMatches -CaseSensitive  | ForEach-Object { $_.Matches.Value } `
    

### How to run?
### For Linux Users
```
    chmod +x search_flags.sh
```
```
    ./search_flags.sh
```
### For Windows Users
try in powershell: 
```
.\search_flags.ps1
```
if not working first time open it in admin mode and set the execution policy to allow the current session to run scripts:
```
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
```
after finish playing with script set the execution policy back to its original value by closing the current PowerShell session and opening a new one

### Folder Structure
```
.
└── CTF-5 (SEARCH)/
    ├── search_flags.ps1  # powershell script
    ├── search_flags.sh   # bash script 
    ├── logs              # input file
    ├── out_bash.txt      # bash script output
    └── out_ps.txt        # powershell script output
```

