# SimpleRev

- Tôi sử dụng IDA để có thể dịch mã

![main](./images/main.png)

- Ngoài hàm Decry ra thì có vẻ mọi thứ khá bình thường

![decry1](./images/decry1.png)

- Vào bên trong hàm Decry thì thấy có hai biến là src và v9 có khởi tạo giá trị hex, lật lại thì được src được gán là NDCLS và v9 là hadow

![key3](./images/key3.png)

- Có key3 là kills

![key1](./images/key1.png)

- Cos key1 là ADSFK
- Từ đó có thể suy ra được text = killshadow và key = ADSFKNDCLS
- Sau đó ta thấy đoạn giá trị của key sẽ được đổi về chữ thường nên key = adsfkndcls

![decry2](./images/decry2.png)

- Đây là đoạn mã chúng ta cần phân tích

<a href="./decode.py" target="_blank">
  <img src="./images/res.png" alt="Python decode script" style="cursor: pointer;">
</a>

- Tôi có viết lại đoạn giải bằng python như trên và nhận được flag

<details>
<summary style="cursor: pointer">FLAG</summary>

```
flag{KLDQCUDFZO}
```
</details>
