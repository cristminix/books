Get-ChildItem -Path . -Filter "*.html" -File | ForEach-Object {
    Write-Host "help me convert $_.Name to markdown and maintain its image"
}