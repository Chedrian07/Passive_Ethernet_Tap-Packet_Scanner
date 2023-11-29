import pyshark
import socket
import os


#output_file_path = "/home/kch3d/Desktop/tshark/Captures/capture.pcap"

# 캡쳐 파일 저장 디렉토리 생성
current_dir = os.getcwd()
captures_dir = os.path.join(current_dir, "Captures")
os.makedirs(captures_dir, exist_ok=True)

output_file_path = os.path.join(captures_dir, "capture.pcap")

def packet_scanner():
    
    #인터페이스 설정 (자동화 구현중)    
    print("Setting interface...")
    iface = 'enp0s5'
    print("Interface: " + iface + " is set")
    
    
    # 패킷 캡처 필터
    display_filter = 'http || ftp || telnet || smtp || imap || icmp'
    
    packet_scan = pyshark.LiveCapture(interface=iface, display_filter=display_filter)
    cnt = 0
    
    while True:
        try:
            for packet in packet_scan.sniff_continuously(packet_count=5):
                # 캡처한 패킷을 파일로 저장
                with open(output_file_path, 'a') as f:
                    f.write(str(packet))
                cnt += 1
                print("Packet Capture Success: " + str(cnt) + " times")
            
            if cnt == 10:
                print("Capture Saved as " + output_file_path)
                if output_file_path is None:
                    print("Error: No capture file")
                else:
                    print("Capture complete.")
                    break
            
        # 네트워크 연결 감지
        except pyshark.capture.capture.TSharkCrashException:
            print("Error: Internet connection is lost.")
            print("Reconnecting...")
            break

    print("Capture complete.")



def zip_file():
    print("Zipping file...")
    os.system("zip -r Packet_Scanner_Result.zip " + output_file_path)
    print("Zip complete.")
    
def upload_file():
    print("Uploading Result file...")

    # 호스트 정보 읽어 오기
    with open('socket_config.txt', 'r') as config_file:
        lines = config_file.readlines()
        host_ip = lines[0].strip().split('=')[1]
        host_port = int(lines[1].strip().split('=')[1])

    # 소켓 생성
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host_ip, host_port))

    file_to_send = 'Packet_Scanner_Result.zip'

    with open(file_to_send, 'rb') as f:
        while True:
            data = f.read(4096) #4096 바이트 단위로 청크 읽기
            if not data:
                break
            s.sendall(data)

    print("File sent successfully.")
    s.close()


if __name__ == '__main__':
    while True:
        packet_scanner()
        zip_file()
        upload_file()
    