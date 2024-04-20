# the input file path
$inFile = "logs"

# the output file path
$outFile = "out_ps.txt"

# search file for pattern
$searchRes = Select-String -Path $inFile -Pattern "CMPN\{[^\}]+\}|picoCTF\{[^\}]+\}|fastctf\{[^\}]+\}|[A-Z]+_[A-Z]+" -AllMatches -CaseSensitive  | ForEach-Object { $_.Matches.Value } 

# output on the out file
$searchRes |  Set-Content -Path $outFile