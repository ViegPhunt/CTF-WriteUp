# [ACTF新生赛2020]Oruga

- Tôi sử dụng IDA để có thể dịch mã

![main](./images/main.png)
- Đọc trong hàm main thì không có gì đặc biệt ngoài hàm sub_78A

![sub_78A_1](./images/sub_78A_1.png)
![sub_78A_2](./images/sub_78A_2.png)
- Đọc qua hàm sub_78A thì thấy có byte_201020 có sẵn và cần khai thác, cùng với các giá trị so sánh có sẵn 87, 69, 77, 74

![byte_201020](./images/byte_201020.png)
- Đọc và xuất dữ liệu của byte_201020

![gen](./images/gen.png)
- Tôi tiến hành tạo lại một ma trận dựa trên dữ liệu của byte_201020

- Sau đó tôi tiến hành giải tay dựa vào:
  - 87 là W (lên trên)
  - 69 là E (sang phải)
  - 77 là M (xuống dưới)
  - 74 là J (sang trái)

![result](./images/result.png)
- Sau khi tự giải ma trận và nhận được flag

<details>
<summary style="cursor: pointer">FLAG</summary>

```
flag{MEWEMEWJMEWJM}
```
</details>
