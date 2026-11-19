# Thí nghiệm tổ hợp mật khẩu (Password Combination Experiment)

Một dự án nhỏ bằng Python để học về cách số lượng chuỗi ký tự có thể tạo ra tăng nhanh như thế nào khi tăng độ dài.

> **Chỉ dùng cho mục đích học tập.** Chỉ chạy chương trình này với mật khẩu và hệ thống của bạn hoặc nơi bạn được phép thử nghiệm rõ ràng. Đây không phải công cụ kiểm thử bảo mật và tuyệt đối không dùng để truy cập tài khoản, thiết bị, tệp hay dịch vụ của người khác.

## Chương trình làm gì

Chương trình yêu cầu bạn nhập một mật khẩu, sau đó tạo các chuỗi ký tự từ:

- chữ cái viết thường (`a-z`)
- chữ số (`0-9`)
- một số ký tự đặc biệt chọn sẵn

Trong lúc tạo chuỗi, chương trình kiểm tra xem mật khẩu bạn nhập có nằm trong danh sách đang tạo hay không. Cuối cùng, nó in ra mật khẩu, tổng số chuỗi đã tạo và thời gian chạy.

Dự án này giúp bạn thực hành vòng lặp, list, list comprehension lồng nhau, xử lý chuỗi và hiểu tại sao đoán mật khẩu dài lại tốn nhiều tài nguyên tính toán.

## Yêu cầu

- Python 3
- Không cần cài thêm thư viện ngoài (chỉ dùng module có sẵn `time` của Python)

## Cách chạy

1. Lưu file code với tên `password-crackerd.py` cùng thư mục với file `README.md` này.
2. Mở terminal tại thư mục đó.
3. Chạy lệnh:

```bash
python3 password-crackerd.py
```
