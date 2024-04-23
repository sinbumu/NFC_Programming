# NFC_Programming

1. ACR122u 구입 + mac 용 커낵터 설치함

option) brew install libusb 설치
- 환경변수도 쉘에 맞춰서 추가해야함 - 난 .zshrc에 추가
export DYLD_LIBRARY_PATH=/usr/local/lib:$DYLD_LIBRARY_PATH
(m1, m2칩이면 아래)
export DYLD_LIBRARY_PATH=/opt/homebrew/lib:$DYLD_LIBRARY_PATH



2. 가상환경 생성
python3 -m venv myenv 

3. 가상환경 활성화
source myenv/bin/activate 

4. 패키지 설치
pip install pyscard
pip install nfcpy

