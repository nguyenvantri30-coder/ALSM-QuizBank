# -*- coding: utf-8 -*-
"""
Script hỗ trợ đồng bộ Ngân hàng câu hỏi QuizBank lên GitHub cá nhân (nguyenvantri30)
Chạy script này khi bạn muốn khởi tạo hoặc cập nhật QuizBank lên GitHub.
"""

import os
import sys
import subprocess

QUIZBANK_DIR = os.path.dirname(os.path.abspath(__file__))

def run_cmd(cmd):
    sys.stdout.buffer.write(f">> {cmd}\n".encode('utf-8'))
    res = subprocess.run(cmd, shell=True, cwd=QUIZBANK_DIR, capture_output=True, text=True)
    if res.stdout:
        sys.stdout.buffer.write(res.stdout.encode('utf-8'))
    if res.stderr:
        sys.stdout.buffer.write(res.stderr.encode('utf-8'))
    return res.returncode

def main():
    sys.stdout.buffer.write(b"=== DONG BO QUIZBANK LEN GITHUB ===\n")
    
    # Kiem tra thu muc git
    git_dir = os.path.join(QUIZBANK_DIR, '.git')
    if not os.path.exists(git_dir):
        sys.stdout.buffer.write(b"1. Khoi tao Git repository...\n")
        run_cmd("git init")
        run_cmd("git branch -M main")
    else:
        sys.stdout.buffer.write(b"Git repository da ton tai.\n")
        
    sys.stdout.buffer.write(b"2. Them tat ca file vao commit...\n")
    run_cmd("git add .")
    
    msg = "Cap nhat QuizBank: 514 bai hoc, 13,061 cau hoi, 528 anh SGK"
    sys.stdout.buffer.write(b"3. Tao commit...\n")
    run_cmd(f'git commit -m "{msg}"')
    
    sys.stdout.buffer.write(b"\n4. Kiem tra Remote Origin...\n")
    res = subprocess.run("git remote get-url origin", shell=True, cwd=QUIZBANK_DIR, capture_output=True, text=True)
    if res.returncode != 0 or not res.stdout.strip():
        repo_url = "https://github.com/nguyenvantri30/ALSM-QuizBank.git"
        sys.stdout.buffer.write(f"Dat remote mac dinh: {repo_url}\n".encode('utf-8'))
        run_cmd(f"git remote add origin {repo_url}")
    else:
        sys.stdout.buffer.write(f"Remote hien tai: {res.stdout.strip()}\n".encode('utf-8'))
        
    sys.stdout.buffer.write(b"\n5. Day len GitHub (git push)...\n")
    ret = run_cmd("git push -u origin main")
    if ret == 0:
        sys.stdout.buffer.write(b"\n==> DONG BO THANH CONG 100% LEN GITHUB!\n")
    else:
        sys.stdout.buffer.write(b"\n[Luu y]: Neu day len that bai, hay dam bao ban da tao repository 'ALSM-QuizBank' tren https://github.com/new truoc khi push.\n")

if __name__ == '__main__':
    main()
