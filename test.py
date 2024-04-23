from smartcard.System import readers
from smartcard.util import toHexString

# 사용 가능한 리더기 확인
r = readers()
print("Available readers:", r)

# 첫 번째 리더기 사용
reader = r[0]
print("Using:", reader)

# 세션 시작
connection = reader.createConnection()
connection.connect()

# APDU 명령 예제 (AID 포함 SELECT COMMAND)
command = [0x00, 0xA4, 0x04, 0x00, 0x07, 0xA0, 0x00, 0x00, 0x00, 0x03, 0x86, 0x98, 0x07]
print("Sending APDU command:", toHexString(command))

# 명령 전송
response, sw1, sw2 = connection.transmit(command)
print("Response:", toHexString(response))
print("Status words: %02X %02X" % (sw1, sw2))
