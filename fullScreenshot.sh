 #!/usr/bin/env bash
scriptDir="/home/popcorn9499/Scripts/uploader/"
time=$(date +%Y_M-%m_D-%d_T-%H_%M-%S-%N)
fileFormat="files/%Time%__%Date%_%File%"
cd "$scriptDir"
fileName="$scriptDir/$time.png"
flameshot full -r > "$fileName"

python upload.py "$fileFormat" "$fileName"


rm $fileName