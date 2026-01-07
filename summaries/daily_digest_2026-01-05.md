# 🤗 Daily Hugging Face Paper Digest - 2026-01-05

Báo cáo được tạo tự động vào lúc 2026-01-06 10:22:28 bằng mô hình `gemini-2.5-flash`.

## 📰 Summary of Papers

--- 

## 1. Youtu-Agent: Scaling Agent Productivity with Automated Generation and Hybrid Policy Optimization

**Tác giả:** Yuchen Shi, Yuzheng Cai, Siqi Cai, Zihan Xu, Lichao Chen, Yulei Qin, Zhijian Zhou, Xiang Fei, Chaofan Qiu, Xiaoyu Tan, Gang Li, Zongyi Li, Haojia Lin, Guocan Cai, Yong Mao, Yunsheng Wu, Ke Li, Xing Sun

**Xuất bản lúc:** 2025-12-31

### Main Problem:
Các framework tác nhân dựa trên Mô hình Ngôn ngữ Lớn (LLM) hiện có phải đối mặt với hai thách thức đáng kể: chi phí cấu hình cao và khả năng tĩnh. Việc xây dựng một tác nhân chất lượng cao thường đòi hỏi nỗ lực thủ công sâu rộng trong việc tích hợp công cụ và kỹ thuật prompt, trong khi các tác nhân đã triển khai gặp khó khăn trong việc thích ứng với các môi trường động nếu không có chi phí tinh chỉnh đắt đỏ.

### Main Idea:
Bài nghiên cứu đề xuất Youtu-Agent, một framework mô-đun được thiết kế để tự động tạo và liên tục phát triển các tác nhân LLM. Youtu-Agent giải quyết các vấn đề này thông qua:
1.  **Hệ thống tạo tự động:** Sử dụng hệ thống cấu hình có cấu trúc để tách biệt môi trường thực thi, bộ công cụ và quản lý ngữ cảnh, cho phép tái sử dụng linh hoạt và tổng hợp tự động. Youtu-Agent giới thiệu hai mô hình tạo: chế độ `Workflow` cho các tác vụ tiêu chuẩn và chế độ `Meta-Agent` cho các yêu cầu phức tạp, không tiêu chuẩn, có khả năng tự động tạo mã công cụ, prompt và cấu hình.
2.  **Hệ thống tối ưu hóa chính sách lai:**
    *   **Module `Agent Practice`:** Cho phép các tác nhân tích lũy kinh nghiệm và cải thiện hiệu suất thông qua tối ưu hóa trong ngữ cảnh mà không cần cập nhật tham số, dựa trên cơ chế Training-free Group Relative Policy Optimization (GRPO).
    *   **Module `Agent RL`:** Tích hợp với các framework đào tạo phân tán để cho phép học tăng cường có thể mở rộng và ổn định cho bất kỳ tác nhân Youtu-Agent nào theo cách end-to-end, quy mô lớn.

### Main Results:
*   Youtu-Agent đạt hiệu suất hiện đại trên WebWalkerQA (71.47%) và GAIA (72.8%) bằng cách sử dụng các mô hình mã nguồn mở.
*   Quy trình tạo tự động đạt tỷ lệ thành công tổng hợp công cụ trên 81%.
*   Module Practice cải thiện hiệu suất trên AIME 2024 và AIME 2025 lần lượt là +2.7% và +5.4%.
*   Đào tạo Agent RL đạt tăng tốc 40% với cải thiện hiệu suất ổn định trên các LLM 7B, nâng cao khả năng lập trình/suy luận lên tới 35% trên các benchmark Toán học và khả năng tìm kiếm lên tới 21% trên các benchmark QA tổng quát/đa bước.

### Conclusion & Future Works:
Youtu-Agent là một framework toàn diện giúp thu hẹp khoảng cách giữa "xây dựng tự động" và "tối ưu hóa liên tục" cho các tác nhân LLM. Nó biến Youtu-Agent từ một framework thực thi tĩnh thành một hệ thống có khả năng tiến hóa liên tục tự cải thiện thông qua kiến trúc mô-đun, cơ chế tạo tự động và hệ thống tối ưu hóa chính sách lai. Văn bản trích dẫn không đề cập cụ thể về hướng nghiên cứu tiếp theo.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2512.24615](https://huggingface.co/papers/2512.24615) |
| ArXiv Abstract | [https://arxiv.org/abs/2512.24615](https://arxiv.org/abs/2512.24615) |
| PDF Download | [https://arxiv.org/pdf/2512.24615.pdf](https://arxiv.org/pdf/2512.24615.pdf) |
| Github Repository | [https://github.com/TencentCloudADP/youtu-agent](https://github.com/TencentCloudADP/youtu-agent) |

--- 

## 2. NeoVerse: Enhancing 4D World Model with in-the-wild Monocular Videos

**Tác giả:** Yuxue Yang, Lue Fan, Ziqi Shi, Junran Peng, Feng Wang, Zhaoxiang Zhang

**Xuất bản lúc:** 2026-01-01

### Main Problem:
Vấn đề cốt lõi mà bài báo đề cập là giới hạn về khả năng mở rộng của các phương pháp mô hình hóa thế giới 4D hiện tại. Hạn chế này xuất phát từ việc phụ thuộc vào dữ liệu 4D đa góc nhìn đắt đỏ và chuyên biệt hoặc quy trình tiền xử lý đào tạo rườm rà. Những giới hạn này cản trở việc tận dụng các video đơn sắc "in-the-wild" phổ biến và giá rẻ, từ đó giới hạn khả năng tổng quát hóa, tính linh hoạt của mô hình, và gây ra gánh nặng tính toán, tiêu thụ bộ nhớ lớn cũng như việc điều chỉnh lược đồ đào tạo kém linh hoạt.

### Main Idea:
Bài báo đề xuất NeoVerse, một mô hình thế giới 4D đa năng được thiết kế để giải quyết các vấn đề về khả năng mở rộng. Ý tưởng chính của NeoVerse là xây dựng một pipeline hoàn chỉnh có thể mở rộng cho các video đơn sắc "in-the-wild" đa dạng. Cụ thể, NeoVerse bao gồm:
1.  Tái tạo 4D Gaussian Splatting (4DGS) theo cơ chế feed-forward và không yêu cầu thông tin về tư thế (pose-free).
2.  Mô hình hóa chuyển động hai chiều để tái tạo hiệu quả và cho phép nội suy trường Gaussian tại các khung hình không phải là khung chính.
3.  Tái tạo cảnh 4D hiệu quả từ các khung hình chính thưa thớt (sparse key frames) theo phương pháp trực tuyến (online) để tăng tốc độ đào tạo.
4.  Mô phỏng các mẫu xuống cấp đơn sắc trực tuyến, bao gồm cắt bỏ Gaussian dựa trên khả năng hiển thị (visibility-based Gaussian Culling), nhằm tạo ra các cặp dữ liệu đào tạo gồm kết xuất chất lượng thấp và khung hình thực tế.
Các kỹ thuật này được kết hợp để tạo ra một quy trình đào tạo có khả năng mở rộng cao cho các video đơn sắc đa dạng.

### Main Results:
- NeoVerse là một phương pháp mô hình hóa thế giới 4D có khả năng mở rộng và được cải thiện đáng kể nhờ tận dụng các video đơn sắc "in-the-wild" đa dạng.
- Mô hình sở hữu tính linh hoạt cao, hỗ trợ nhiều ứng dụng như tái tạo 4D, tạo video đa góc nhìn, chỉnh sửa video, ổn định video và siêu phân giải.
- NeoVerse đạt được hiệu suất tiên tiến (state-of-the-art) trong cả các tác vụ tái tạo và tạo sinh.

### Conclusion & Future Works:
NeoVerse đã thành công trong việc giải quyết các thách thức về khả năng mở rộng của các mô hình thế giới 4D bằng cách tận dụng hiệu quả các video đơn sắc "in-the-wild" phổ biến. Mô hình mang lại tính linh hoạt và hiệu suất vượt trội cho các ứng dụng 4D khác nhau. Trong tương lai, mã nguồn của NeoVerse sẽ được công khai, nhằm mục đích phi tập trung hóa các mô hình thế giới 4D chung và khuyến khích việc sử dụng rộng rãi các video đơn sắc giá thành thấp và đa dạng.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.00393](https://huggingface.co/papers/2601.00393) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.00393](https://arxiv.org/abs/2601.00393) |
| PDF Download | [https://arxiv.org/pdf/2601.00393.pdf](https://arxiv.org/pdf/2601.00393.pdf) |
| Github Repository | [https://github.com/IamCreateAI/NeoVerse](https://github.com/IamCreateAI/NeoVerse) |

