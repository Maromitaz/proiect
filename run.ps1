# Check common installation paths
$chromePaths = @(
    "C:\Program Files\Google\Chrome\Application\chrome.exe",
    "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    "$env:LOCALAPPDATA\Google\Chrome\Application\chrome.exe"
)

$foundPath = $chromePaths | Where-Object { Test-Path $_ }

if ($foundPath) {
    Write-Output "Chrome found at: $foundPath"
} else {
    # Check registry for user installation
    $chromeRegPath = "HKCU:\Software\Google\Chrome\BLBeacon"
    if (Test-Path $chromeRegPath) {
        $chromeInstallPath = (Get-ItemProperty -Path $chromeRegPath).exe
        Write-Output "Chrome found in registry at: $chromeInstallPath"
    } else {
        Write-Output "Chrome not found."
    }
}
