# ALSM QuizBank — Ngân hàng Câu hỏi Trắc nghiệm GDPT 2018

Kho dữ liệu câu hỏi trắc nghiệm tương tác chuẩn GDPT 2018 và Moodle XML/JSON, phục vụ cho ứng dụng **`tracnghiem.exe`** và hệ sinh thái giảng dạy **ALSM**.

## 📊 Tổng quan dữ liệu
- **Tổng số bài học (Tiết PPCT)**: 514 bài
- **Tổng số câu hỏi**: 13,061 câu hỏi
- **Tổng số hình ảnh SGK đi kèm**: 528 ảnh
- **Môn học**:
  - **Tin học**: Khối 8
  - **Toán học**: Khối 6, Khối 7, Khối 8, Khối 9

## 🧩 Các loại câu hỏi hỗ trợ (Moodle Standard)
1. `multichoice`: Trắc nghiệm nhiều lựa chọn (1 đáp án đúng hoặc nhiều đáp án).
2. `truefalse`: Câu hỏi Đúng / Sai.
3. `matching`: Ghép nối 2 cột khái niệm.
4. `gapselect`: Chọn từ trong dropdown điền vào chỗ trống `[[1]]`, `[[2]]`.
5. `ddwtos`: Kéo thả từ/cụm từ vào đoạn văn bản.
6. `shortanswer`: Điền câu trả lời ngắn / biểu thức toán.
7. `calculatedsimple`: Câu hỏi tính toán theo công thức ngẫu nhiên.
8. **Công thức Toán học LaTeX**: Render mượt mà qua KaTeX / MathJax.
9. **Hình ảnh SGK**: Tự động liên kết thư mục `images/`.

## 📁 Cấu trúc thư mục
```text
QuizBank/
  ├── catalog.json                 # Chỉ mục nhanh PPCT, tiêu đề và số lượng câu hỏi
  ├── schema_quiz.json             # Chuẩn cấu trúc JSON cho giáo viên nạp đề mới
  ├── README.md                    # Tài liệu hướng dẫn
  ├── Tin_hoc/
  │     └── Khối_8/
  │           ├── [001][Tin học]_[Khối 8]...json
  │           └── images/
  └── Toán_hoc/
        ├── Khối_6/
        ├── Khối_7/
        ├── Khối_8/
        └── Khối_9/
```

## 🚀 Tích hợp phần mềm tracnghiem.exe
- **Chế độ đơn (1 HS)**: Kiểm tra bài cũ cá nhân.
- **Chế độ đối kháng (2 HS)**: Chia đôi màn hình, bấm phím/chuột độc lập.
- **Chế độ đấu trường (3-4 HS)**: Multi-Mouse qua USB Hub, biểu đồ thống kê xếp hạng.

---
*Bản quyền & Biên soạn: Nguyễn Văn Trí (nguyenvantri30)*
