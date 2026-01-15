# 🤗 Daily Hugging Face Paper Digest - 2026-01-13

Báo cáo được tạo tự động vào lúc 2026-01-14 10:03:44 bằng mô hình `gemini-2.5-flash`.

## 📰 Summary of Papers

--- 

## 1. Watching, Reasoning, and Searching: A Video Deep Research Benchmark on Open Web for Agentic Video Reasoning *(175 votes)*

**Tác giả:** Chengwen Liu, Xiaomin Yu, Zhuoyue Chang, Zhe Huang, Shuo Zhang, Heng Lian, Kunyi Wang, Rui Xu, Sen Hu, Jianheng Hou, Hao Peng, Chengwei Qin, Xiaobin Hu, Hong Peng, Ronghao Chen, Huacan Wang

**Xuất bản lúc:** 2026-01-11

**Tag:** Video Deep Research, Open-domain QA, Multimodal Large Language Models (MLLMs), Agentic AI, Video Reasoning, Web Search, Benchmark

### I. Main Problem:
Vấn đề cốt lõi mà bài báo đề cập là sự thiếu hụt các benchmark đáng tin cậy để đánh giá khả năng suy luận video trong các tình huống thực tế, nơi các manh mối thị giác trong video thường chỉ mang tính cục bộ và các câu trả lời cần xác minh lại phân tán trên web mở. Các benchmark hiện có thường giới hạn trong bối cảnh dữ liệu đóng hoặc chủ yếu dựa trên văn bản, không thể đánh giá được khả năng kết hợp khai thác manh mối video đa khung, tìm kiếm thông tin tương tác trên web và suy luận đa bước để xác thực thông tin.

### II. Main Idea:
Bài báo đề xuất VideoDR, một benchmark nghiên cứu chuyên sâu về video đầu tiên, được thiết kế để đánh giá khả năng suy luận video có tác nhân trong môi trường web mở. VideoDR yêu cầu các mô hình thực hiện các bước sau:
1.  **Trích xuất neo thị giác đa khung:** Nhận diện và tổng hợp các manh mối hình ảnh từ nhiều khung hình trong video.
2.  **Truy xuất thông tin tương tác trên web:** Sử dụng công cụ tìm kiếm trên trình duyệt để định vị bằng chứng tiềm năng trên web mở.
3.  **Suy luận đa bước:** Thực hiện suy luận đa bước trên không gian bằng chứng kết hợp từ video và các trang web để đưa ra câu trả lời duy nhất và có thể kiểm chứng được.
Benchmark được xây dựng thông qua quy trình chú thích thủ công và kiểm soát chất lượng nghiêm ngặt, đảm bảo mỗi câu hỏi đều phụ thuộc đồng thời vào cả video và kết quả tìm kiếm trên web.

### III. Main Results:
-   VideoDR là benchmark đầu tiên có hệ thống để nghiên cứu các tác nhân video trong môi trường web mở, cung cấp các mẫu chất lượng cao trải rộng trên sáu miền ngữ nghĩa khác nhau.
-   Đánh giá các mô hình ngôn ngữ lớn đa phương thức (MLLMs) cả mã nguồn đóng và mã nguồn mở dưới hai mô hình Workflow và Agentic cho thấy phương pháp Agentic không phải lúc nào cũng vượt trội hơn Workflow. Hiệu quả của Agentic phụ thuộc vào khả năng của mô hình trong việc duy trì các neo video ban đầu qua các chuỗi truy xuất dài.
-   Phân tích sâu hơn chỉ ra rằng "Goal Drift" (lạc mất mục tiêu) và "Long-horizon Consistency" (tính nhất quán dài hạn) là những nút thắt cổ chai cốt lõi hạn chế sự phát triển của các tác nhân nghiên cứu video chuyên sâu thế hệ tiếp theo.

### IV. Conclusion & Future Works:
Bài báo kết luận rằng VideoDR cung cấp một benchmark có hệ thống để nghiên cứu các tác nhân video trong môi trường web mở và đã làm sáng tỏ những thách thức chính đối với các tác nhân nghiên cứu video chuyên sâu thế hệ tiếp theo. Hướng nghiên cứu tiếp theo cần tập trung vào việc giải quyết các vấn đề "Goal Drift" và "Long-horizon Consistency" để cải thiện hiệu suất của các mô hình trong việc duy trì sự gắn kết với các neo video ban đầu qua các chuỗi suy luận và tìm kiếm dài.

### V. Brainstorming Space:
#### 1. Publish Papers:
1.  Nghiên cứu các kiến trúc mô hình mới giúp duy trì "video anchors" hiệu quả hơn trong quá trình tìm kiếm thông tin đa bước trên web mở.
2.  Phát triển các phương pháp đánh giá định lượng cho "Goal Drift" và "Long-horizon Consistency" trong các tác vụ suy luận đa phương thức.
3.  Khám phá việc tích hợp các kỹ thuật suy luận nhân quả để cải thiện khả năng tổng hợp bằng chứng từ video và web trong các tác vụ QA.

#### 2. Patent:
1.  Hệ thống trợ lý AI di động cho phép người dùng quay video và đặt câu hỏi mở, sau đó AI sẽ tìm kiếm thông tin trên web để trả lời dựa trên các manh mối trong video, hiển thị kết quả trực tiếp trên điện thoại.
2.  Ứng dụng di động có khả năng ghi lại cảnh quan hoặc vật thể từ video, sau đó tự động tìm kiếm thông tin liên quan trên mạng và cung cấp các gợi ý hành động hoặc sản phẩm dựa trên nội dung video.
3.  Công nghệ tích hợp vào camera điện thoại để nhận diện các đối tượng hoặc sự kiện trong video theo thời gian thực, đồng thời tự động truy xuất các thông tin bổ sung từ web để cung cấp ngữ cảnh hoặc xác thực thông tin cho người dùng khi họ đang xem hoặc quay video.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.06943](https://huggingface.co/papers/2601.06943) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.06943](https://arxiv.org/abs/2601.06943) |
| PDF Download | [https://arxiv.org/pdf/2601.06943.pdf](https://arxiv.org/pdf/2601.06943.pdf) |
| Github Repository | [https://github.com/QuantaAlpha/VideoDR-Benchmark](https://github.com/QuantaAlpha/VideoDR-Benchmark) |

--- 

## 2. BabyVision: Visual Reasoning Beyond Language *(156 votes)*

**Tác giả:** Liang Chen, Weichu Xie, Yiyan Liang, Hongfeng He, Hans Zhao, Zhibo Yang, Zhiqi Huang, Haoning Wu, Haoyu Lu, Y. charles, Yiping Bao, Yuantao Fan, Guopeng Li, Haiyang Shen, Xuanzhong Chen, Wendong Xu, Shuzheng Si, Zefan Cai, Wenhao Chai, Ziqi Huang, Fangfu Liu, Tianyu Liu, Baobao Chang, Xiaobo Hu, Kaiyuan Chen, Yixin Ren, Yang Liu, Yuan Gong, Kuan Li

**Xuất bản lúc:** 2026-01-10

**Tag:** MLLMs, Visual Reasoning, Benchmark, Early Vision, Generative Models, Visual Perception

### I. Main Problem:
Các mô hình ngôn ngữ lớn đa phương thức (MLLM) hiện đại vẫn phụ thuộc nhiều vào các tiên nghiệm ngôn ngữ để bù đắp cho khả năng hiểu thị giác còn yếu. Chúng liên tục thất bại trong các tác vụ thị giác cơ bản mà con người, kể cả trẻ 3 tuổi, có thể giải quyết dễ dàng, cho thấy MLLM thiếu các nguyên lý thị giác nền tảng. Các đánh giá hiện có thường nhắm mục tiêu vào các nhiệm vụ cấp cao, dựa trên kiến thức và ít tập trung vào các khả năng suy luận thị giác độc lập với ngôn ngữ.

### II. Main Idea:
Nghiên cứu giới thiệu BABYVISION, một bộ tiêu chuẩn được thiết kế để đánh giá các khả năng thị giác cốt lõi của MLLM độc lập với kiến thức ngôn ngữ. BABYVISION bao gồm 388 câu hỏi, chia thành 22 loại phụ trong 4 danh mục chính: Phân biệt chi tiết, Theo dõi thị giác, Nhận thức không gian và Nhận dạng mẫu thị giác. Bộ tiêu chuẩn này tập trung vào các kỹ năng thị giác sớm mà con người phát triển trước khi có ngôn ngữ. Ngoài ra, nghiên cứu còn đề xuất BABYVISION-GEN, một phiên bản tạo sinh để đánh giá suy luận thị giác thông qua việc tạo ảnh thay vì chỉ đầu ra ngôn ngữ, kèm theo một bộ công cụ đánh giá tự động đạt độ đồng thuận 96% với đánh giá của con người.

### III. Main Results:
- Các MLLM hàng đầu có hiệu suất thấp hơn đáng kể so với con người trên BABYVISION. Cụ thể, Gemini3-Pro-Preview đạt 49.7%, kém xa trẻ 6 tuổi và mức trung bình 94.1% của người lớn.
- Khoảng cách hiệu suất tuyệt đối giữa mô hình tốt nhất và người lớn là 44.4%.
- Các thất bại lớn nhất của MLLM xuất hiện trong các tác vụ Theo dõi thị giác và Nhận thức không gian, cho thấy chúng mất khả năng theo dõi đối tượng và thiếu trí tưởng tượng không gian.
- Các mô hình tạo sinh cho thấy những cải thiện đầy hứa hẹn trên BABYVISION-GEN đối với các tác vụ khó cho MLLM, đặc biệt là theo dõi thị giác và phân biệt chi tiết, mặc dù độ tin cậy tổng thể vẫn còn hạn chế.

### IV. Conclusion & Future Works:
BABYVISION đã bóc trần một lỗ hổng đáng kể trong khả năng suy luận thị giác cơ bản của MLLM, không được phát hiện bởi các bộ tiêu chuẩn hiện có. Tiến bộ trong việc giải quyết các thách thức của BABYVISION đại diện cho một bước tiến quan trọng hướng tới khả năng nhận thức và suy luận thị giác ở cấp độ con người. Hướng nghiên cứu tiếp theo sẽ khám phá cách đào tạo dựa trên học tăng cường (RLVR) và các mô hình tạo sinh có thể cải thiện hơn nữa hiệu suất suy luận thị giác.

### V. Brainstorming Space:
#### 1. Publish Papers:
- Nghiên cứu so sánh chi tiết hiệu suất của MLLM trên BABYVISION với các kiến trúc mô hình thị giác truyền thống để xác định lợi thế và hạn chế của từng phương pháp.
- Phát triển các phương pháp đào tạo MLLM mới tích hợp các module học tập "trước ngôn ngữ" để cải thiện trực tiếp khả năng thị giác cơ bản của chúng.
- Phân tích sâu hơn các loại lỗi cụ thể mà MLLM mắc phải trên BABYVISION để tạo ra các chiến lược khắc phục mục tiêu cho từng danh mục tác vụ.
#### 2. Patent:
- Một ứng dụng di động sử dụng AI có khả năng hướng dẫn người dùng nhận diện và theo dõi các vật thể trong môi trường thực tế, ví dụ như tìm đường đi qua một mê cung vật lý.
- Công nghệ camera điện thoại thông minh có thể nhận diện các mẫu hình thị giác phức tạp và đề xuất cách sắp xếp vật thể hoặc trang trí để tạo ra bố cục hài hòa.
- Một hệ thống hỗ trợ trên điện thoại di động giúp trẻ em phát triển kỹ năng phân biệt thị giác chi tiết thông qua các trò chơi tương tác, phát hiện sự khác biệt nhỏ giữa các hình ảnh.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.06521](https://huggingface.co/papers/2601.06521) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.06521](https://arxiv.org/abs/2601.06521) |
| PDF Download | [https://arxiv.org/pdf/2601.06521.pdf](https://arxiv.org/pdf/2601.06521.pdf) |
| Github Repository | [https://github.com/UniPat-AI/BabyVision](https://github.com/UniPat-AI/BabyVision) |

--- 

## 3. PaCoRe: Learning to Scale Test-Time Compute with Parallel Coordinated Reasoning *(65 votes)*

**Tác giả:** Jingcheng Hu, Yinmin Zhang, Shijie Shang, Xiaobo Yang, Yue Peng, Zhewei Huang, Hebin Zhou, Xin Wu, Jie Cheng, Fanqi Wan, Xiangwen Kong, Chengyuan Yao, Kaiwen Yan, Ailin Huang, Hongyu Zhou, Qi Han, Zheng Ge, Daxin Jiang, Xiangyu Zhang, Heung-Yeung Shum

**Xuất bản lúc:** 2026-01-09

**Tag:** PaCoRe, Language Models, Test-Time Compute, Parallel Reasoning, Reinforcement Learning, Context Window.

### I. Main Problem:
Vấn đề cốt lõi mà bài báo đề cập là giới hạn của các mô hình ngôn ngữ hiện đại trong việc mở rộng khả năng tính toán trong thời gian kiểm thử (Test-Time Compute - TTC) vượt xa suy luận tuần tự trong một cửa sổ ngữ cảnh cố định, khiến chúng không thể giải quyết hiệu quả các tác vụ suy luận phức tạp và dài hạn.

### II. Main Idea:
Bài báo giới thiệu PaCoRe (Parallel Coordinated Reasoning), một khung đào tạo và suy luận được thiết kế để vượt qua giới hạn về TTC. PaCoRe chuyển đổi từ mô hình tuần tự truyền thống sang thúc đẩy TTC thông qua khám phá song song quy mô lớn, được điều phối qua kiến trúc truyền thông điệp qua nhiều vòng. Mỗi vòng thực hiện nhiều quỹ đạo suy luận song song, nén các phát hiện của chúng thành các thông điệp có giới hạn ngữ cảnh, và tổng hợp các thông điệp này để hướng dẫn vòng tiếp theo và cuối cùng đưa ra câu trả lời cuối cùng. Quá trình này được đào tạo end-to-end bằng học tăng cường dựa trên kết quả quy mô lớn, giúp mô hình nắm vững khả năng tổng hợp cần thiết.

### III. Main Results:
PaCoRe cho phép mở rộng TTC hiệu quả lên đến hàng triệu token mà không vượt quá giới hạn ngữ cảnh. Phương pháp này mang lại những cải tiến đáng kể trên nhiều lĩnh vực khác nhau, đặc biệt là trong toán học: một mô hình PaCoRe-8B đạt 94.5% trên HMMT 2025, vượt qua GPT-5 (93.2%) bằng cách mở rộng TTC hiệu quả lên khoảng hai triệu token. Các tác giả đã mã nguồn mở các checkpoint mô hình, dữ liệu đào tạo và toàn bộ pipeline suy luận.

### IV. Conclusion & Future Works:
PaCoRe giải quyết hiệu quả hạn chế của các mô hình ngôn ngữ về khả năng mở rộng TTC do giới hạn cửa sổ ngữ cảnh, đạt được hiệu suất vượt trội thông qua suy luận song song và khả năng tổng hợp được đào tạo bằng học tăng cường. Việc công bố mã nguồn và dữ liệu sẽ thúc đẩy các nghiên cứu và phát triển tiếp theo trong cộng đồng.

### V. Brainstorming Space:
#### 1. Publish Papers:
1. Nghiên cứu các phương pháp nén thông điệp (message compaction) tiên tiến hơn, có thể sử dụng các mô hình tóm tắt để giữ lại nhiều ngữ cảnh quan trọng hơn thay vì chỉ kết luận cuối cùng.
2. Áp dụng PaCoRe vào các lĩnh vực khác đòi hỏi suy luận dài hạn như phân tích tài liệu pháp lý, phát hiện khoa học hoặc thiết kế kỹ thuật, đánh giá hiệu quả trên các tập dữ liệu chuyên biệt.
3. Khám phá các chiến lược tối ưu để điều chỉnh số lượng quỹ đạo song song và số vòng phối hợp cho các loại vấn đề khác nhau, có thể tự động điều chỉnh dựa trên độ phức tạp của tác vụ.
#### 2. Patent:
1. Hệ thống trợ lý ảo trên điện thoại sử dụng kiến trúc PaCoRe để xử lý các yêu cầu đa bước, phức tạp từ người dùng bằng cách phân tách và tổng hợp thông tin song song mà không làm tràn bộ nhớ ngữ cảnh của thiết bị.
2. Ứng dụng giải toán hoặc lập trình trên điện thoại thông minh tích hợp PaCoRe, cho phép người dùng nhập các bài toán phức tạp và nhận được lời giải chi tiết thông qua việc khám phá nhiều phương án giải song song và nén kết quả thành các thông điệp nhỏ gọn hiển thị trên màn hình di động.
3. Công nghệ tối ưu hóa tài nguyên thiết bị di động bằng cách sử dụng PaCoRe để thực hiện các tác vụ suy luận nặng ký trong nền, phân chia công việc thành các vòng xử lý nhỏ gọn, đảm bảo hiệu suất cao và tiết kiệm pin trên điện thoại.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.05593](https://huggingface.co/papers/2601.05593) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.05593](https://arxiv.org/abs/2601.05593) |
| PDF Download | [https://arxiv.org/pdf/2601.05593.pdf](https://arxiv.org/pdf/2601.05593.pdf) |
| Github Repository | [https://github.com/stepfun-ai/PaCoRe](https://github.com/stepfun-ai/PaCoRe) |

--- 

## 4. MHLA: Restoring Expressivity of Linear Attention via Token-Level Multi-Head *(31 votes)*

**Tác giả:** Kewei Zhang, Ye Huang, Yufan Deng, Jincheng Yu, Junsong Chen, Huan Ling, Enze Xie, Daquan Zhou

**Xuất bản lúc:** 2026-01-12

**Tag:** Linear Attention, Multi-Head Attention, Expressivity Restoration, Global Context Collapse, Scalability, Transformer

### I. Main Problem:
Kiến trúc Transformer với cơ chế self-attention có độ phức tạp về thời gian và bộ nhớ là bậc hai (quadratic), hạn chế khả năng mở rộng cho các ứng dụng quy mô lớn và tác vụ chuỗi dài như tạo ảnh độ phân giải cao và tạo video. Linear attention cung cấp một giải pháp thay thế hiệu quả hơn với độ phức tạp tuyến tính, nhưng lại thường làm giảm hiệu suất đáng kể do mất đi khả năng thích ứng với từng truy vấn riêng lẻ. Vấn đề cốt lõi này được xác định là "global context collapse", nơi mô hình mất đi sự đa dạng trong biểu diễn thông tin. Các giải pháp hiện có thường tái tạo chi phí tính toán thông qua các module bổ sung, làm mất đi mục đích ban đầu về hiệu quả.

### II. Main Idea:
Bài báo đề xuất Multi-Head Linear Attention (MHLA) nhằm khôi phục khả năng biểu cảm của linear attention mà vẫn duy trì độ phức tạp tuyến tính và không cần các module bổ sung. MHLA giải quyết vấn đề "global context collapse" bằng cách chia các token thành các "heads" (khối) không trùng lặp theo chiều token. Với mỗi khối, MHLA tính toán các tóm tắt key-value cục bộ. Sau đó, mỗi khối truy vấn sẽ tính toán một hỗn hợp các tóm tắt key-value cục bộ được điều kiện bởi truy vấn, cho phép khôi phục sự đa dạng biểu diễn và tính chọn lọc phụ thuộc vào truy vấn. Quá trình này được tối ưu hóa với độ phức tạp O(N) và chỉ dựa vào các phép toán nhân ma trận tổng quát (GEMM) tiêu chuẩn.

### III. Main Results:
MHLA đã chứng minh hiệu quả vượt trội so với các baseline linear attention hiện có với chi phí tính toán không đáng kể. Nó khôi phục phần lớn sức mạnh biểu cảm của softmax attention trong khi duy trì độ phức tạp tuyến tính. Các kết quả chính bao gồm:
*   Cải thiện 3.6% trên tác vụ phân loại ImageNet.
*   Tăng 6.3% trên tác vụ Xử lý Ngôn ngữ Tự nhiên (NLP).
*   Cải thiện 12.6% trên tác vụ tạo ảnh.
*   Tăng cường 41% trên tác vụ tạo video so với linear attention thông thường, tất cả đều trong cùng độ phức tạp thời gian.
MHLA cũng được chứng minh là làm tăng đáng kể "rank" của ma trận trọng số attention và giảm "entropy", cho thấy khả năng chú ý phong phú và tập trung hơn.

### IV. Conclusion & Future Works:
MHLA là một giải pháp hiệu quả cho vấn đề "global context collapse" trong linear attention, khôi phục khả năng biểu cảm và sự đa dạng token-level mà vẫn duy trì độ phức tạp tuyến tính. Phương pháp này tránh được việc thêm các module phụ trợ, khiến nó trở thành một lựa chọn mạnh mẽ để mở rộng các mô hình Transformer cho các tác vụ chuỗi dài và dữ liệu lớn.

### V. Brainstorming Space:
#### 1. Publish Papers:
*   Nghiên cứu sự kết hợp của MHLA với các kỹ thuật nén mô hình (pruning, quantization) để triển khai hiệu quả trên các thiết bị tài nguyên hạn chế.
*   Khám phá ứng dụng của MHLA trong các lĩnh vực mới như phân tích dữ liệu chuỗi thời gian hoặc mô hình hóa đồ thị.
*   Phân tích định lượng sâu hơn về mối quan hệ giữa số lượng "heads" trong MHLA và hiệu suất mô hình trên các loại dữ liệu khác nhau.

#### 2. Patent:
*   Hệ thống camera an ninh trên điện thoại thông minh sử dụng MHLA để phân tích và nhận diện hành vi bất thường trong chuỗi video dài theo thời gian thực mà vẫn tiết kiệm pin.
*   Công nghệ hiển thị thông tin động trên màn hình điện thoại, tự động tổng hợp và hiển thị các nội dung quan trọng từ nhiều nguồn dữ liệu chuỗi dài bằng MHLA.
*   Ứng dụng chỉnh sửa âm thanh chuyên nghiệp trên điện thoại di động, sử dụng MHLA để xử lý và tạo hiệu ứng cho các bản ghi âm dài với độ chính xác cao và tốc độ nhanh.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.07832](https://huggingface.co/papers/2601.07832) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.07832](https://arxiv.org/abs/2601.07832) |
| PDF Download | [https://arxiv.org/pdf/2601.07832.pdf](https://arxiv.org/pdf/2601.07832.pdf) |
| Github Repository | [https://github.com/DAGroup-PKU/MHLA](https://github.com/DAGroup-PKU/MHLA) |

--- 

## 5. X-Coder: Advancing Competitive Programming with Fully Synthetic Tasks, Solutions, and Tests *(30 votes)*

**Tác giả:** Jie Wu, Haoling Li, Xin Zhang, Jiani Guo, Jane Luo, Steven Liu, Yangyu Huang, Ruihang Chu, Scarlett Li, Yujiu Yang

**Xuất bản lúc:** 2026-01-11

**Tag:** Competitive Programming, Code LLMs, Synthetic Data Generation, Supervised Fine-tuning (SFT), Reinforcement Learning (RL), Code Reasoning
### I. Main Problem:
Các mô hình ngôn ngữ mã (Code LLMs) hiện tại gặp thách thức lớn với lập trình cạnh tranh do nhu cầu suy luận chuyên sâu và độ phức tạp logic cao. Sự phụ thuộc nặng nề vào dữ liệu thực tế đã hạn chế khả năng mở rộng của chúng. Các bộ dữ liệu lập trình cạnh tranh hiện có rất khan hiếm, thường được tái sử dụng và không đủ quy mô, độ khó cũng như sự đa dạng để hỗ trợ việc cải thiện liên tục các Code LLM. Việc thu thập dữ liệu thực tế mới cũng rất khó khăn, và các biến thể dữ liệu được tổng hợp từ các tài nguyên hiện có bị giới hạn bởi các nhiệm vụ gốc.

### II. Main Idea:
Bài nghiên cứu khám phá một cách tiếp cận hoàn toàn tổng hợp: huấn luyện Code LLM bằng các tác vụ, giải pháp và bộ kiểm thử được tạo hoàn toàn, mà không cần dựa vào dữ liệu thực tế. Để đạt được điều này, bài báo đề xuất một quy trình tổng hợp dữ liệu mới có tên SynthSmith, sử dụng phương pháp tổng hợp dựa trên tính năng. SynthSmith được thiết kế để tạo ra các tác vụ đa dạng và thách thức trong lập trình cạnh tranh, cùng với các giải pháp và kiểm thử đã được xác minh, hỗ trợ cả huấn luyện tinh chỉnh có giám sát (SFT) và học tăng cường (RL).

Quy trình SynthSmith bao gồm bốn bước chính:
1.  **Tạo tác vụ:** Trích xuất và phát triển các tính năng liên quan đến lập trình cạnh tranh từ các đoạn mã nhỏ, sau đó kết hợp chúng vào cấu trúc cây để tạo ra các kịch bản vấn đề mới mẻ và đầy thách thức theo nhiều phong cách khác nhau (như Codeforces, LeetCode, AtCoder).
2.  **Tạo đầu vào kiểm thử:** Sử dụng cả phương pháp dựa trên gợi ý (prompting) và dựa trên công cụ (tool-based, ví dụ như CYaRon) để tạo ra các bộ đầu vào kiểm thử đa dạng và toàn diện, bao gồm cả các trường hợp tiêu chuẩn và trường hợp biên.
3.  **Tạo giải pháp ứng viên:** Tạo ra nhiều giải pháp ứng viên cho mỗi tác vụ bằng cách sử dụng các mô hình ngôn ngữ lớn (LLM) suy luận tiên tiến, đảm bảo mỗi giải pháp bao gồm quy trình suy luận đầy đủ và triển khai mã Python không có lỗi cú pháp.
4.  **Xác minh kép giải pháp và kiểm thử:**
    *   **Bước 1:** Xác minh các trường hợp kiểm thử thông qua bỏ phiếu đồng thuận từ nhiều giải pháp ứng viên để xác định kết quả đầu ra đúng tạm thời, đồng thời gán trọng số cho các trường hợp kiểm thử dựa trên độ khó.
    *   **Bước 2:** Xác minh các giải pháp bằng cách đánh giá có trọng số trên bộ kiểm thử chính và xác thực trên một tập kiểm tra độc lập (hold-out validation set) để chọn ra giải pháp "vàng" (golden solution) đáng tin cậy và có khả năng khái quát hóa.

Dựa trên dữ liệu tổng hợp chất lượng cao này, bài báo giới thiệu dòng mô hình X-Coder, được huấn luyện theo mô hình SFT-sau-đó-RL (SFT-then-RL), nhằm đạt được những cải tiến đáng kể về hiệu suất trong lập trình cạnh tranh.

### III. Main Results:
*   **Hiệu suất vượt trội:** Dòng mô hình X-Coder, đặc biệt là X-Coder-7B, đạt tỷ lệ vượt qua ấn tượng 62.9 avg@8 trên LiveCodeBench v5 và 55.8 avg@8 trên v6.
*   **Vượt qua các mô hình lớn hơn:** X-Coder-7B, với chỉ 7B tham số, vượt trội hơn các mô hình lớn hơn như DeepCoder-14B-Preview và AReal-boba-14B, cũng như các mô hình cùng kích thước khác trên cả hai phiên bản LiveCodeBench.
*   **Quy luật mở rộng:** Các quy luật mở rộng được duy trì trên bộ dữ liệu tổng hợp, và nghiên cứu đã khám phá những chiều mở rộng hiệu quả hơn.
*   **Hiểu biết sâu sắc về RL:** Cung cấp những hiểu biết về học tăng cường tập trung vào mã, bao gồm nguyên tắc "tốt hơn sẽ tốt hơn" và khả năng phục hồi của RL trước sự giám sát nhiễu.
*   **Phân tích yếu tố hiệu suất:** Nghiên cứu phân tích các yếu tố chính định hình hiệu suất, bao gồm độ dài của Chain-of-Thought (CoT), ảnh hưởng của việc xác minh giải pháp, phong cách tác vụ và chiến lược chọn dữ liệu.
*   **Điểm nghẽn và mối quan hệ:** Khám phá các điểm nghẽn giới hạn khả năng suy luận mã và mối quan hệ dây chuyền giữa độ khó tác vụ, độ dài suy luận và tỷ lệ vượt qua.
*   **Hành vi nhận thức:** Các nghiên cứu điển hình đã phát hiện các hành vi nhận thức mới nổi sau SFT và RL, chẳng hạn như "phần thưởng gian lận" (reward hacking) và các mô hình không mong muốn.

### IV. Conclusion & Future Works:
**Kết luận:** Việc mở rộng quy mô dữ liệu tổng hợp chất lượng cao và áp dụng huấn luyện theo giai đoạn (SFT-then-RL) có thể thúc đẩy đáng kể khả năng suy luận mã, đồng thời giảm bớt sự phụ thuộc vào dữ liệu mã thực tế. Cách tiếp cận tổng hợp hoàn toàn và quy trình SynthSmith chứng minh tiềm năng mạnh mẽ trong việc tạo ra dữ liệu lập trình cạnh tranh đa dạng và thách thức.

**Hướng nghiên cứu tiếp theo (ngụ ý):** Cần nghiên cứu sâu hơn về các chiến lược RL để giảm thiểu các hành vi tiêu cực như "phần thưởng gian lận" đã được quan sát. Ngoài ra, việc tiếp tục khám phá các chiều mở rộng hiệu quả của dữ liệu tổng hợp và cải thiện sự hiểu biết về mối quan hệ giữa độ khó tác vụ, độ dài suy luận và tỷ lệ vượt qua bài kiểm thử là những lĩnh vực tiềm năng cho nghiên cứu trong tương lai.

### V. Brainstorming Space:
#### 1. Publish Papers:
*   Nghiên cứu các phương pháp tiên tiến để tự động hóa việc phát hiện và giảm thiểu các hành vi không mong muốn như reward hacking trong các mô hình ngôn ngữ mã được huấn luyện bằng dữ liệu tổng hợp.
*   Khám phá hiệu quả của việc tổng hợp dữ liệu lập trình cạnh tranh đa ngôn ngữ để nâng cao khả năng suy luận của Code LLM trên các ngôn ngữ lập trình khác nhau.
*   Phân tích định lượng và định tính về mối quan hệ giữa độ khó của nhiệm vụ tổng hợp, độ dài chuỗi suy luận và tỷ lệ vượt qua bài kiểm tra để tối ưu hóa việc tạo dữ liệu.

#### 2. Patent:
*   Hệ thống và phương pháp tạo tự động các bài toán lập trình cạnh tranh đa dạng, giải pháp và bộ kiểm thử hoàn toàn tổng hợp cho việc huấn luyện và đánh giá mô hình AI trên điện thoại di động.
*   Phương pháp xác minh kép các giải pháp và bộ kiểm thử cho các bài toán lập trình bằng cách sử dụng bỏ phiếu đồng thuận và đánh giá có trọng số để đảm bảo độ tin cậy khi triển khai trên thiết bị di động.
*   Giao thức huấn luyện xếp tầng (SFT-then-RL) được tối ưu hóa cho các mô hình ngôn ngữ mã trên nền tảng di động, cho phép nâng cao khả năng suy luận mã với dữ liệu tổng hợp và tài nguyên tính toán hạn chế.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.06953](https://huggingface.co/papers/2601.06953) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.06953](https://arxiv.org/abs/2601.06953) |
| PDF Download | [https://arxiv.org/pdf/2601.06953.pdf](https://arxiv.org/pdf/2601.06953.pdf) |
| Github Repository | [https://github.com/JieWu02/X-Coder](https://github.com/JieWu02/X-Coder) |

--- 

## 6. GlimpRouter: Efficient Collaborative Inference by Glimpsing One Token of Thoughts *(26 votes)*

**Tác giả:** Wenhao Zeng, Xuteng Zhang, Yuling Shi, Chao Hu, Yuting Chen, Beijun Shen, Xiaodong Gu

**Xuất bản lúc:** 2026-01-08

**Tag:** Large Language Models, Collaborative Inference, Reasoning, Latency Reduction, Entropy-based Routing

### I. Main Problem:
Các mô hình suy luận lớn (LRMs) đạt hiệu suất vượt trội thông qua việc tạo ra chuỗi suy luận nhiều bước, nhưng khả năng này lại đi kèm với độ trễ suy luận và chi phí tính toán đáng kể. Mặc dù suy luận cộng tác hứa hẹn một giải pháp bằng cách phân bổ công việc giữa các mô hình nhẹ và mô hình lớn, thách thức cơ bản vẫn là xác định khi nào một bước suy luận cần khả năng của mô hình lớn hay hiệu quả của mô hình nhỏ. Các chiến lược định tuyến hiện có thường dựa vào xác suất token cục bộ hoặc xác minh sau quá trình, điều này gây ra chi phí suy luận đáng kể.

### II. Main Idea:
Bài báo đề xuất GlimpRouter, một khung suy luận cộng tác từng bước không cần huấn luyện, dựa trên quan điểm mới rằng độ khó của một bước suy luận có thể được suy ra từ token đầu tiên của nó. Lấy cảm hứng từ hiện tượng "Aha Moment" trong LRMs, các tác giả chứng minh rằng entropy của token khởi tạo (Hinit) là một chỉ số dự đoán mạnh mẽ về độ khó của bước. GlimpRouter sử dụng một mô hình trọng lượng nhẹ để chỉ tạo ra token đầu tiên của mỗi bước suy luận. Nếu entropy của token khởi tạo này vượt quá một ngưỡng nhất định, bước suy luận sẽ được chuyển cho một mô hình lớn hơn; ngược lại, mô hình nhẹ sẽ tiếp tục tạo ra toàn bộ bước. Cơ chế này giúp phân bổ tính toán hiệu quả dựa trên "một cái nhìn thoáng qua về suy nghĩ" thay vì đánh giá toàn bộ bước.

### III. Main Results:
- GlimpRouter giảm đáng kể độ trễ suy luận trong khi vẫn duy trì độ chính xác hoặc thậm chí cải thiện nó.
- Trên benchmark AIME25, GlimpRouter đạt cải thiện đáng kể 10.7% về độ chính xác và giảm 25.9% độ trễ suy luận so với mô hình lớn độc lập.
- Phân tích cho thấy entropy của token khởi tạo (Hinit) có phân bố hai đỉnh và đuôi nặng, cho thấy nó là một tín hiệu phân biệt độ khó mạnh mẽ, không giống như các chỉ số khác có phân bố đơn đỉnh hẹp.
- Quan sát thấy mối tương quan âm một cách đơn điệu và chặt chẽ giữa Hinit và mức độ tương đồng giữa đầu ra của mô hình nhỏ và mô hình lớn (được đo bằng BLEU-4 và SBERT), khẳng định rằng các bước có Hinit thấp có thể được mô hình nhẹ xử lý hiệu quả mà không ảnh hưởng đến kết quả.

### IV. Conclusion & Future Works:
Bài báo kết luận rằng GlimpRouter cung cấp một cơ chế đơn giản nhưng hiệu quả để phân bổ tài nguyên tính toán dựa trên một tín hiệu tối thiểu từ sự khởi đầu của một bước suy luận. Điều này giúp giảm đáng kể độ trễ suy luận trong khi duy trì hoặc nâng cao hiệu quả của các mô hình suy luận lớn (LRMs), mang lại một giải pháp thiết thực cho việc triển khai chúng. Hướng nghiên cứu tiếp theo có thể bao gồm việc khám phá cách tích hợp chiến lược định tuyến cấp độ bước này với các phương pháp giải mã suy đoán cấp độ token để tạo ra tốc độ tăng tốc bổ sung và tổng hợp.

### V. Brainstorming Space:
#### 1. Publish Papers:
- Nghiên cứu sâu hơn về mối quan hệ giữa các tín hiệu "Aha Moment" và cấu trúc nội tại của các mô hình ngôn ngữ lớn để phát triển các chỉ số độ khó tinh vi hơn.
- Phát triển một phương pháp thích ứng để tự động điều chỉnh ngưỡng entropy trong GlimpRouter dựa trên các đặc điểm của tác vụ hoặc phản hồi thời gian thực.
- Mở rộng GlimpRouter sang các nhiệm vụ suy luận đa phương thức bằng cách tích hợp thông tin độ khó từ các dạng dữ liệu khác nhau vào quyết định định tuyến.

#### 2. Patent:
- Hệ thống quản lý năng lượng thông minh cho điện thoại di động, sử dụng GlimpRouter để phân luồng các yêu cầu từ trợ lý ảo hoặc ứng dụng AI sang mô hình trên thiết bị (tiêu thụ ít năng lượng) hoặc mô hình đám mây (tiêu thụ nhiều năng lượng) dựa trên độ phức tạp của yêu cầu.
- Công nghệ tối ưu hóa hiệu suất ứng dụng AI trên thiết bị di động, tự động chuyển đổi giữa các phiên bản mô hình ngôn ngữ khác nhau (nhẹ và nặng) dựa trên entropy của token đầu tiên được dự đoán, nhằm cung cấp phản hồi nhanh chóng và duy trì tuổi thọ pin.
- Phương pháp điều khiển chip xử lý AI trên điện thoại, tự động điều chỉnh tần số hoặc kích hoạt các nhân xử lý chuyên dụng dựa trên ngưỡng Hinit được tính toán, đảm bảo tài nguyên được phân bổ hiệu quả chỉ khi cần thiết cho các tác vụ suy luận phức tạp.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.05110](https://huggingface.co/papers/2601.05110) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.05110](https://arxiv.org/abs/2601.05110) |
| PDF Download | [https://arxiv.org/pdf/2601.05110.pdf](https://arxiv.org/pdf/2601.05110.pdf) |
| Github Repository | [https://github.com/Zengwh02/GlimpRouter](https://github.com/Zengwh02/GlimpRouter) |

--- 

## 7. Lost in the Noise: How Reasoning Models Fail with Contextual Distractors *(24 votes)*

**Tác giả:** Seongyun Lee, Yongrae Jo, Minju Seo, Moontae Lee, Minjoon Seo

**Xuất bản lúc:** 2026-01-12

**Tag:** Reasoning, RAG, AI Agents, Robustness, Noise, Benchmarking, LLM Evaluation, Reinforcement Learning

### I. Main Problem:
Các mô hình suy luận và hệ thống AI tác tử hiện nay, dù ngày càng phụ thuộc vào thông tin bên ngoài, nhưng lại thiếu khả năng xử lý hiệu quả các ngữ cảnh đầu vào có nhiễu trong thế giới thực. Các benchmark hiện tại chỉ đánh giá trong môi trường "sạch", dẫn đến cái nhìn sai lệch về năng lực của mô hình. Các mô hình tiên tiến nhất trải qua sự sụt giảm hiệu suất nghiêm trọng (lên đến 80%) khi đối mặt với nhiễu ngữ cảnh. Hơn nữa, các quy trình tác tử thường khuếch đại lỗi do quá tin tưởng vào đầu ra công cụ nhiễu, và những yếu tố gây nhiễu có thể dẫn đến sự sai lệch ngoài ý muốn. Các phương pháp phổ biến như nhắc lệnh, kỹ thuật ngữ cảnh, SFT và học tăng cường chỉ dựa trên phần thưởng kết quả đều không đảm bảo độ bền vững.

### II. Main Idea:
Bài báo giới thiệu **NoisyBench**, một bộ benchmark toàn diện được thiết kế để đánh giá có hệ thống độ bền vững của mô hình trên 11 bộ dữ liệu trong các tác vụ RAG, suy luận, căn chỉnh và sử dụng công cụ đối với nhiều loại nhiễu khác nhau, bao gồm tài liệu ngẫu nhiên, lịch sử trò chuyện không liên quan và những yếu tố gây nhiễu tiêu cực khó. Để tăng cường khả năng phục hồi của mô hình, bài báo đề xuất **Rationale-Aware Reward (RARE)**, một hàm phần thưởng đơn giản nhưng hiệu quả, củng cố quá trình suy luận bằng cách khuyến khích việc xác định thông tin hữu ích trong ngữ cảnh nhiễu. Ngoài ra, **NoisyInstruct** là một tập dữ liệu huấn luyện để dạy mô hình loại bỏ các yếu tố gây nhiễu.

### III. Main Results:
*   Các mô hình hiện đại cho thấy sự sụt giảm hiệu suất thảm khốc lên đến 80% khi gặp phải các yếu tố gây nhiễu ngữ cảnh.
*   Các quy trình tác tử có thể khuếch đại lỗi do quá tin tưởng vào đầu ra công cụ nhiễu, và nhiễu có thể kích hoạt sự sai lệch ngoài ý muốn ngay cả khi không có ý định đối kháng.
*   Các kỹ thuật như nhắc lệnh, kỹ thuật ngữ cảnh, SFT và học tăng cường chỉ dựa trên phần thưởng kết quả không đủ để đảm bảo độ bền vững.
*   RARE tăng cường đáng kể khả năng phục hồi bằng cách khuyến khích nhận diện thông tin hữu ích trong nhiễu, cải thiện tỷ lệ lọc yếu tố gây nhiễu trong chuỗi suy luận và mang lại độ chính xác cuối cùng cao hơn so với phần thưởng dựa trên kết quả đơn thuần.
*   Nghiên cứu phát hiện xu hướng nghịch đảo: Tăng cường tính toán trong thời gian kiểm tra (sử dụng nhiều token suy luận hơn) lại dẫn đến hiệu suất kém hơn trong các thiết lập có nhiễu.
*   Phân tích sự chú ý cho thấy các mô hình tập trung không cân đối vào các token gây nhiễu, đặc biệt là trong các dự đoán không chính xác.

### IV. Conclusion & Future Works:
Công trình này phơi bày khoảng cách đáng kể giữa các benchmark "sạch" và môi trường nhiễu thực tế mà các hệ thống AI tác tử vận hành. Bằng cách giới thiệu NoisyBench, NoisyInstruct và RARE, nghiên cứu cung cấp nền tảng để đánh giá và cải thiện độ bền vững với nhiễu, đồng thời đưa ra những hiểu biết quan trọng cho việc phát triển thế hệ tác tử có khả năng suy luận mạnh mẽ và đáng tin cậy hơn.

### V. Brainstorming Space:
#### 1. Publish Papers:
*   Nghiên cứu về việc tích hợp RARE với các kiến trúc mô hình mới được thiết kế để xử lý ngữ cảnh dài, đánh giá hiệu quả của việc kết hợp này trong việc duy trì độ chính xác và khả năng lọc nhiễu.
*   Khám phá các phương pháp tự động tạo ra các loại nhiễu "hard negative" hiệu quả hơn để liên tục thách thức và cải thiện khả năng lọc nhiễu của mô hình trong NoisyBench.
*   Phân tích sâu hơn về cơ chế "inverse scaling trend" và đề xuất các giải pháp kiến trúc hoặc huấn luyện để ngăn chặn sự suy giảm hiệu suất khi mô hình sử dụng nhiều token suy luận hơn trong môi trường nhiễu.

#### 2. Patent:
*   Hệ thống trợ lý ảo trên điện thoại thông minh sử dụng Rationale-Aware Reward để lọc bỏ thông tin không liên quan từ lịch sử trò chuyện hoặc các tài liệu được truy xuất, đảm bảo phản hồi chính xác và đáng tin cậy cho các yêu cầu của người dùng.
*   Ứng dụng bảo mật và kiểm duyệt nội dung trên thiết bị di động tích hợp cơ chế phát hiện và bỏ qua các "hard negative distractors" trong các cuộc hội thoại hoặc bài viết, giúp người dùng tránh bị hiểu lầm hoặc tiếp nhận thông tin sai lệch.
*   Công nghệ tích hợp vào các ứng dụng ghi chú hoặc công cụ năng suất trên điện thoại, sử dụng NoisyBench để liên tục đánh giá và cải thiện khả năng của AI trong việc tổng hợp thông tin quan trọng từ các nguồn nhiễu, đồng thời giảm thiểu sự phụ thuộc vào các thông tin không chính xác.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.07226](https://huggingface.co/papers/2601.07226) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.07226](https://arxiv.org/abs/2601.07226) |
| PDF Download | [https://arxiv.org/pdf/2601.07226.pdf](https://arxiv.org/pdf/2601.07226.pdf) |
| Github Repository | N/A |

--- 

## 8. OS-Symphony: A Holistic Framework for Robust and Generalist Computer-Using Agent *(22 votes)*

**Tác giả:** Bowen Yang, Kaiming Jin, Zhenyu Wu, Zhaoyang Liu, Qiushi Sun, Zehao Li, JingJing Xie, Zhoumianze Liu, Fangzhi Xu, Kanzhi Cheng, Qingyun Li, Yian Wang, Yu Qiao, Zun Wang, Zichen Ding

**Xuất bản lúc:** 2026-01-12

**Tag:** Computer-Using Agents, Multimodal RAG, Reflection, Orchestration
### I. Main Problem:
Các tác nhân sử dụng máy tính (Computer-Using Agents - CUAs) hiện tại, mặc dù được cải thiện đáng kể nhờ Vision-Language Models (VLMs), vẫn gặp khó khăn về tính bền vững (robustness) trong các quy trình làm việc dài hạn và khả năng tổng quát hóa (generalization) trong các lĩnh vực mới. Những hạn chế này xuất phát từ việc thiếu kiểm soát chi tiết đối với việc quản lý ngữ cảnh hình ảnh lịch sử và sự thiếu hụt khả năng truy xuất hướng dẫn có nhận biết hình ảnh.

### II. Main Idea:
Bài báo giới thiệu OS-SYMPHONY, một khuôn khổ toàn diện bao gồm một Orchestrator điều phối hai đổi mới chính để tự động hóa mạnh mẽ:
1.  **Reflection-Memory Agent (RMA):** Sử dụng bộ nhớ dài hạn dựa trên các "cột mốc" (milestone) để lưu giữ ảnh chụp màn hình quan trọng và các quỹ đạo trừu tượng. Điều này cho phép tự sửa lỗi ở cấp độ quỹ đạo, giảm thiểu việc mất ngữ cảnh hình ảnh trong các tác vụ dài hạn và tạo ra các phản hồi ý nghĩa để tinh chỉnh kế hoạch.
2.  **Versatile Tool Agents (với Multimodal Searcher):** Áp dụng mô hình "See-Act" để điều hướng một môi trường sandbox dựa trên trình duyệt nhằm tổng hợp các hướng dẫn trực tiếp, được căn chỉnh trực quan. Điều này giải quyết các vấn đề về độ trung thực trong các kịch bản chưa từng thấy, giúp tác nhân có được kiến thức đa phương thức bên ngoài.

### III. Main Results:
OS-SYMPHONY mang lại hiệu suất vượt trội trên ba tiêu chuẩn trực tuyến, thiết lập các kết quả hiện đại mới (state-of-the-art):
*   OSWorld: Đạt 65.84% (tăng 2.4% so với SOTA trước đó).
*   WindowsAgentArena: Đạt 63.5% (tăng 6.9% so với SOTA trước đó).
*   MacOSArena: Đạt 46.0% (tăng 38.0% so với SOTA trước đó).
Khuôn khổ này cũng cho phép các VLM mã nguồn mở thực hiện thành công các tác vụ dài hạn hoặc chưa từng thấy mà trước đây vượt quá khả năng của chúng.

### IV. Conclusion & Future Works:
OS-SYMPHONY là một khuôn khổ toàn diện, mang lại sự cải thiện đáng kể về hiệu suất cho các tác nhân sử dụng máy tính, đặc biệt trong các tác vụ dài hạn và chưa từng thấy. Khung này giải quyết các thách thức chính về quản lý bộ nhớ (ngữ cảnh hình ảnh) và tổng quát hóa (truy xuất kiến thức đa phương thức). Hướng nghiên cứu tiếp theo bao gồm việc tối ưu hóa hơn nữa cơ chế phản hồi và bộ nhớ đa phương thức, cũng như mở rộng ứng dụng sang các môi trường điều hành và loại tác vụ phức tạp hơn.

### V. Brainstorming Space:
#### 1. Publish Papers:
1.  Nghiên cứu các phương pháp tiên tiến để tự động xác định và trích xuất các "milestone" hình ảnh quan trọng từ các quỹ đạo tương tác người dùng dài để cải thiện hiệu quả bộ nhớ của Reflection-Memory Agent.
2.  Phát triển một hệ thống Multimodal Searcher có khả năng không chỉ truy xuất mà còn tạo ra các hướng dẫn trực quan tương tác, điều chỉnh theo ngữ cảnh người dùng cụ thể trong thời gian thực.
3.  Khám phá việc tích hợp các mô hình học tăng cường để tối ưu hóa chiến lược điều phối của Orchestrator, cho phép nó tự động học cách ưu tiên và kết hợp các Tool Agents khác nhau dựa trên loại nhiệm vụ và tình huống lỗi.

#### 2. Patent:
1.  Một hệ thống trợ lý ảo trên điện thoại thông minh có khả năng tự động thực hiện các tác vụ phức tạp bằng cách tìm kiếm và làm theo các hướng dẫn trực quan được tổng hợp tự động từ web, ví dụ như tạo shortcut ứng dụng hoặc thay đổi cài đặt sâu.
2.  Một ứng dụng trên điện thoại di động giúp người dùng ghi lại một chuỗi hành động trên điện thoại, sau đó AI tự động phân tích và tạo ra một "hướng dẫn hình ảnh" có thể được sử dụng để tự động lặp lại hoặc hướng dẫn người khác thực hiện tác vụ đó một cách chính xác.
3.  Công nghệ tích hợp vào hệ điều hành điện thoại, cho phép một tác nhân AI nhận diện khi người dùng gặp khó khăn hoặc lặp lại một hành động không hiệu quả, sau đó tự động tìm kiếm các hướng dẫn trực quan và đề xuất hoặc thực hiện các bước khắc phục phù hợp.
4.  Một phương pháp tự động hóa trên điện thoại di động mà qua đó, AI có thể tự động duyệt các trang web hỗ trợ, xem các video hướng dẫn và trích xuất các bước hành động cụ thể để giải quyết các vấn đề phần mềm hoặc cấu hình trên chính thiết bị đó.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.07779](https://huggingface.co/papers/2601.07779) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.07779](https://arxiv.org/abs/2601.07779) |
| PDF Download | [https://arxiv.org/pdf/2601.07779.pdf](https://arxiv.org/pdf/2601.07779.pdf) |
| Github Repository | [https://github.com/OS-Copilot/OS-Symphony](https://github.com/OS-Copilot/OS-Symphony) |

--- 

## 9. Beyond Hard Masks: Progressive Token Evolution for Diffusion Language Models *(20 votes)*

**Tác giả:** Linhao Zhong, Linyu Wu, Bozhen Fang, Tianjian Feng, Chenchen Jing, Wen Wang, Jiaheng Zhang, Hao Chen, Chunhua Shen

**Xuất bản lúc:** 2026-01-12

**Tag:** Diffusion, Language Models, Parallel Decoding, Iterative Refinement, Soft Token Evolution, Continuous Trajectory Supervision

### I. Main Problem:
Các Diffusion Language Models (DLMs) hiện tại, đặc biệt là Masked Diffusion Language Models (MDLMs), gặp phải vấn đề khi sử dụng cơ chế hard binary masking và gán token rời rạc. Điều này khiến mô hình không thể sửa đổi các quyết định sớm và bỏ qua việc tận dụng các biểu diễn xác suất trung gian trong quá trình tinh chỉnh lặp lại. Ngoài ra, MDLMs lãng phí tài nguyên tính toán khi dự đoán phân phối token cho tất cả các vị trí nhưng chỉ cập nhật một phần nhỏ.

### II. Main Idea:
Bài báo đề xuất EvoToken-DLM, một phương pháp mô hình ngôn ngữ dựa trên Diffusion mới thay thế các hard binary masks bằng phân phối soft token có khả năng phát triển (evolving soft token distributions). EvoToken-DLM cho phép quá trình chuyển đổi dần dần từ trạng thái masked sang đầu ra rời rạc thông qua tinh chỉnh lặp đi lặp lại. Các token được biểu diễn dưới dạng phân phối xác suất trên toàn bộ từ vựng và trải qua bốn trạng thái tiến hóa: [MASK] -> Soft([MASK] U V) -> Soft(V) -> [Decode]. Để hỗ trợ quá trình tiến hóa liên tục này, mô hình giới thiệu cơ chế giám sát quỹ đạo liên tục (continuous trajectory supervision), nhằm điều chỉnh mục tiêu huấn luyện với các cập nhật xác suất lặp lại.

### III. Main Results:
EvoToken-DLM liên tục đạt được hiệu suất vượt trội trên nhiều điểm chuẩn, vượt qua các mô hình DLM dựa trên Diffusion và MDLMs mạnh mẽ. Phương pháp này tích hợp liền mạch với các cơ chế KV-caching và mở rộng một cách tự nhiên sang cài đặt blockwise diffusion, chứng tỏ tính ứng dụng rộng rãi và khả năng nâng cao hiệu quả tổng thể của DLM.

### IV. Conclusion & Future Works:
EvoToken-DLM cung cấp một cách tiếp cận hiệu quả và tổng quát để cải thiện Diffusion Language Models bằng cách thay thế hard masks bằng các soft token distributions tiến hóa, cho phép giải mã có thể sửa đổi và tinh chỉnh liên tục. Hướng nghiên cứu tiếp theo có thể tập trung vào việc khám phá các chiến lược tinh chỉnh quỹ đạo (trajectory refinement strategies) tiên tiến hơn và ứng dụng EvoToken-DLM vào các nhiệm vụ sinh ngôn ngữ phức tạp hơn.

### V. Brainstorming Space:
#### 1. Publish Papers:
1. Nghiên cứu cách EvoToken-DLM có thể được áp dụng để tăng cường khả năng chỉnh sửa và tương tác của các chatbot trong thời gian thực.
2. Khám phá các phương pháp mới để tối ưu hóa continuous trajectory supervision nhằm giảm chi phí tính toán trong quá trình huấn luyện mà vẫn duy trì hiệu suất cao.
3. Phân tích ảnh hưởng của các kích thước block khác nhau và chiến lược lựa chọn token trong blockwise decoding của EvoToken-DLM đến chất lượng và tốc độ sinh văn bản.

#### 2. Patent:
1. Một hệ thống nhập liệu văn bản thông minh trên điện thoại di động sử dụng EvoToken-DLM để gợi ý và tự động sửa các từ bị lỗi hoặc chưa hoàn chỉnh một cách linh hoạt, cho phép người dùng dễ dàng chỉnh sửa các gợi ý.
2. Ứng dụng chỉnh sửa văn bản trên điện thoại tích hợp EvoToken-DLM, cho phép người dùng thay đổi các phần của câu hoặc đoạn văn một cách liền mạch, với khả năng hoàn tác và đề xuất các lựa chọn thay thế dựa trên phân phối xác suất của token.
3. Phương pháp tạo nội dung động cho ứng dụng tin tức hoặc mạng xã hội trên điện thoại, sử dụng EvoToken-DLM để sinh ra các tiêu đề hoặc tóm tắt bài viết có thể được tinh chỉnh liên tục bởi thuật toán để phù hợp với sở thích của người dùng và ngữ cảnh hiển thị.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.07351](https://huggingface.co/papers/2601.07351) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.07351](https://arxiv.org/abs/2601.07351) |
| PDF Download | [https://arxiv.org/pdf/2601.07351.pdf](https://arxiv.org/pdf/2601.07351.pdf) |
| Github Repository | [https://github.com/aim-uofa/EvoTokenDLM](https://github.com/aim-uofa/EvoTokenDLM) |

--- 

## 10. Controllable Memory Usage: Balancing Anchoring and Innovation in Long-Term Human-Agent Interaction *(19 votes)*

**Tác giả:** Muzhao Tian, Zisu Huang, Xiaohua Wang, Jingwen Xu, Zhengkang Guo, Qi Qian, Yuanzhe Shen, Kaitao Song, Jiakang Yuan, Changze Lv, Xiaoqing Zheng

**Xuất bản lúc:** 2026-01-08

**Tag:** Long-Term Human-Agent Interaction, LLM Memory, Memory Anchoring, Controllable Memory, SteeM, Personalization, Innovation

### I. Main Problem:
Các tác nhân dựa trên LLM trong tương tác dài hạn gặp phải vấn đề "Memory Anchoring" (neo giữ bởi ký ức), nơi tác nhân bị mắc kẹt bởi các tương tác trong quá khứ khi sử dụng toàn bộ thông tin liên quan, hoặc ngược lại là thiếu tận dụng ký ức khi loại trừ hoàn toàn. Các hệ thống hiện có thường áp dụng cách tiếp cận "tất cả hoặc không gì cả" đối với việc sử dụng bộ nhớ, thiếu một cơ chế cho phép người dùng kiểm soát linh hoạt mức độ phụ thuộc vào ký ức theo thời gian thực để cân bằng giữa tính nhất quán và khả năng đổi mới. Ngay cả khi được nhắc nhở để "sáng tạo", LLM vẫn thường thể hiện "rò rỉ ký ức" từ lịch sử.

### II. Main Idea:
Bài báo đề xuất SteerableMemory Agent (SteeM), một framework cho phép người dùng điều chỉnh động mức độ phụ thuộc của mô hình vào ký ức. SteeM xem xét mức độ phụ thuộc vào ký ức như một chiều hành vi có thể kiểm soát rõ ràng bởi người dùng, cho phép chuyển đổi từ chế độ "fresh-start" (thúc đẩy sự đổi mới) đến chế độ "high-fidelity" (tuân thủ chặt chẽ lịch sử tương tác). Framework này được phát triển bằng cách tạo dữ liệu căn chỉnh sở thích (preference-aligned data generation), sau đó áp dụng Fine-Tuning có giám sát (SFT) và GRPO (Generalized Reinforcement Learning from Preferences).

### III. Main Results:
SteeM vượt trội hơn đáng kể so với các phương pháp nhắc nhở thông thường và các chiến lược che giấu ký ức cứng nhắc. Nó cung cấp khả năng kiểm soát sắc thái và hiệu quả hơn cho sự cộng tác cá nhân hóa giữa người và tác nhân, cho phép người dùng đạt được sự cân bằng chính xác hơn giữa nhận thức về ký ức và sự độc lập trong suy luận trên nhiều nhiệm vụ dài hạn khác nhau. Nghiên cứu cũng giới thiệu một chỉ số hành vi về sự phụ thuộc vào ký ức để định lượng ảnh hưởng của các tương tác trong quá khứ đối với các đầu ra hiện tại và tiết lộ hiện tượng "Memory Anchoring" ở các LLM hiện đại.

### IV. Conclusion & Future Works:
Bài báo kết luận rằng việc biến mức độ phụ thuộc vào ký ức của tác nhân thành một chiều hành vi có thể kiểm soát bởi người dùng là một sự thay đổi mô hình quan trọng. SteeM thành công trong việc cho phép người dùng điều hướng sự đánh đổi giữa tính nhất quán và sự đổi mới dựa trên nhu cầu tức thời, thay đổi của họ. Hướng nghiên cứu tiếp theo có thể mở rộng khả năng điều khiển này sang các khía cạnh khác của tương tác LLM và khám phá các phương pháp hiệu quả hơn để tạo dữ liệu căn chỉnh sở thích.

### V. Brainstorming Space:
#### 1. Publish Papers:
1. Nghiên cứu cách tích hợp khả năng điều khiển bộ nhớ động này vào các kiến trúc RAG để tinh chỉnh việc truy xuất và sử dụng thông tin từ cơ sở tri thức bên ngoài.
2. Phát triển các phương pháp đánh giá định lượng cho sự cân bằng giữa tính nhất quán và đổi mới trong các tác nhân LLM, vượt ra ngoài sự phụ thuộc vào ký ức.
3. Khám phá cách áp dụng các nguyên tắc kiểm soát bộ nhớ của SteeM để giảm thiểu thiên vị hoặc thúc đẩy sự sáng tạo trong các tác vụ tạo nội dung cụ thể.
#### 2. Patent:
1. Hệ thống điều khiển mức độ phụ thuộc vào bộ nhớ của trợ lý ảo trên điện thoại, cho phép người dùng tùy chỉnh liệu trợ lý có nên dựa nhiều vào lịch sử trò chuyện để đưa ra câu trả lời nhất quán hay ưu tiên các phản hồi mới mẻ, độc lập.
2. Phương pháp tích hợp thanh trượt hoặc nút điều chỉnh trên giao diện ứng dụng chatbot di động, cho phép người dùng thiết lập mức độ "sáng tạo" hoặc "ghi nhớ" của chatbot cho từng tương tác cụ thể.
3. Công nghệ "chế độ quên tạm thời" cho các ứng dụng tin nhắn và trợ lý ảo trên điện thoại, nơi người dùng có thể kích hoạt để tác nhân tạm thời bỏ qua một phần lịch sử tương tác để đưa ra góc nhìn mới mẻ hơn cho các yêu cầu hiện tại.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.05107](https://huggingface.co/papers/2601.05107) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.05107](https://arxiv.org/abs/2601.05107) |
| PDF Download | [https://arxiv.org/pdf/2601.05107.pdf](https://arxiv.org/pdf/2601.05107.pdf) |
| Github Repository | N/A |

--- 

## 11. DrivingGen: A Comprehensive Benchmark for Generative Video World Models in Autonomous Driving *(17 votes)*

**Tác giả:** Yang Zhou, Hao Shao, Letian Wang, Zhuofan Zong, Hongsheng Li, Steven L. Waslander

**Xuất bản lúc:** 2026-01-04

**Tag:** Generative Video Models, World Models, Autonomous Driving, Benchmark, Evaluation Metrics, Dataset

### I. Main Problem:
Lĩnh vực các mô hình thế giới tạo video trong lái xe tự hành hiện đang thiếu một chuẩn mực đánh giá toàn diện và nghiêm ngặt để đo lường tiến độ và định hướng ưu tiên nghiên cứu. Các đánh giá hiện có còn hạn chế: các chỉ số video chung bỏ qua các yếu tố hình ảnh quan trọng về an toàn; tính hợp lý của quỹ đạo hiếm khi được định lượng; sự nhất quán về mặt thời gian và cấp độ tác nhân bị bỏ qua; và khả năng kiểm soát với điều kiện ego bị phớt lờ. Hơn nữa, các bộ dữ liệu hiện tại không bao phủ đủ sự đa dạng về điều kiện cần thiết cho việc triển khai thực tế, bao gồm thời tiết, thời gian trong ngày, khu vực địa lý và các thao tác phức tạp.

### II. Main Idea:
Để giải quyết những hạn chế trên, bài báo giới thiệu DrivingGen, chuẩn mực toàn diện đầu tiên cho các mô hình thế giới tạo video trong lái xe tự hành. DrivingGen kết hợp một bộ dữ liệu đánh giá đa dạng được tuyển chọn từ cả các bộ dữ liệu lái xe và nguồn video quy mô internet, bao gồm nhiều điều kiện thời tiết, thời gian trong ngày, khu vực địa lý và các thao tác phức tạp. Chuẩn mực này còn đi kèm với một bộ các chỉ số mới đánh giá đồng thời tính chân thực trực quan, tính hợp lý của quỹ đạo, sự mạch lạc về thời gian và khả năng kiểm soát.

### III. Main Results:
Việc thử nghiệm 14 mô hình tiên tiến trên DrivingGen cho thấy những đánh đổi rõ ràng: các mô hình chung tạo ra hình ảnh đẹp mắt hơn nhưng vi phạm các quy tắc vật lý, trong khi các mô hình chuyên biệt cho lái xe nắm bắt chuyển động một cách thực tế nhưng lại kém về chất lượng hình ảnh. DrivingGen cung cấp những hiểu biết quan trọng về điểm mạnh và điểm yếu của từng phương pháp tiếp cận.

### IV. Conclusion & Future Works:
DrivingGen cung cấp một khung đánh giá thống nhất để thúc đẩy phát triển các mô hình thế giới lái xe đáng tin cậy, có thể kiểm soát và triển khai được, từ đó hỗ trợ mô phỏng mở rộng, lập kế hoạch và ra quyết định dựa trên dữ liệu. Tất cả các thành phần của DrivingGen – bộ dữ liệu và mã đánh giá – đều được phát hành công khai để hỗ trợ nghiên cứu có thể tái tạo và thúc đẩy mô phỏng lái xe thực tế.

### V. Brainstorming Space:
#### 1. Publish Papers:
*   Nghiên cứu về phương pháp tạo video thế giới mới có khả năng cân bằng giữa chất lượng hình ảnh trực quan và độ chính xác vật lý của quỹ đạo chuyển động.
*   Phát triển các chỉ số đánh giá chuyên sâu hơn về tính nhất quán của tác nhân và an toàn, đặc biệt trong các tình huống hiểm nghèo không được đại diện trong dữ liệu đào tạo.
*   Khám phá việc sử dụng học tăng cường để tối ưu hóa các mô hình thế giới tạo video, tập trung vào việc tuân thủ các quy tắc vật lý và khả năng kiểm soát.
#### 2. Patent:
*   Một hệ thống đánh giá video thế giới lái xe tự động tích hợp các chỉ số đa chiều về chất lượng hình ảnh, tính vật lý của quỹ đạo và tính nhất quán thời gian, chạy trên nền tảng đám mây để cung cấp dịch vụ đánh giá cho các nhà phát triển.
*   Một phương pháp tạo dữ liệu tổng hợp cho lái xe tự hành, tập trung vào việc tạo ra các kịch bản hiếm gặp (thời tiết khắc nghiệt, tương tác phức tạp) với độ chân thực cao, được kiểm chứng bởi DrivingGen.
*   Một thiết bị kiểm tra an toàn cho xe tự hành sử dụng các mô hình thế giới tạo video để mô phỏng các tình huống nguy hiểm và đánh giá phản ứng của hệ thống lái xe tự hành, tích hợp khả năng kiểm soát điều kiện đầu vào của xe.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.01528](https://huggingface.co/papers/2601.01528) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.01528](https://arxiv.org/abs/2601.01528) |
| PDF Download | [https://arxiv.org/pdf/2601.01528.pdf](https://arxiv.org/pdf/2601.01528.pdf) |
| Github Repository | [https://github.com/youngzhou1999/DrivingGen](https://github.com/youngzhou1999/DrivingGen) |

--- 

## 12. MegaFlow: Large-Scale Distributed Orchestration System for the Agentic Era *(15 votes)*

**Tác giả:** Lei Zhang, Mouxiang Chen, Ruisheng Cao, Jiawei Chen, Fan Zhou, Yiheng Xu, Jiaxi Yang, Liang Chen, Changwei Luo, Kai Zhang, Fan Yan, KaShun Shum, Jiajun Zhang, Zeyu Cui, Hu Feng, Junyang Lin, Binyuan Hui, Min Yang

**Xuất bản lúc:** 2026-01-12

**Tag:** Agentic AI, Distributed System, Orchestration, Large-Scale Training, Cloud Computing

### I. Main Problem:
Sự phát triển nhanh chóng của các hệ thống AI tương tác và tự chủ (thời đại tác nhân) đòi hỏi hạ tầng phức tạp để điều phối các tương tác giữa tác nhân và môi trường trên quy mô lớn cho các tác vụ phức tạp như kỹ thuật phần mềm và sử dụng máy tính. Hạ tầng mã nguồn mở hiện có không thể hỗ trợ hiệu quả việc huấn luyện và đánh giá trên các tác vụ tác nhân phức tạp này, dẫn đến ba nút thắt chính: hạn chế về bảo mật và cô lập (Security and Isolation Constraints), giới hạn khả năng mở rộng lưu trữ (Storage Scalability Limitations), và nút thắt về thông lượng tính toán (Computational Throughput Bottlenecks).

### II. Main Idea:
Bài báo giới thiệu MegaFlow, một hệ thống điều phối phân tán quy mô lớn được thiết kế để giải quyết những thách thức về hạ tầng trong việc huấn luyện tác nhân AI. MegaFlow cho phép lập lịch trình hiệu quả, phân bổ tài nguyên và quản lý tác vụ chi tiết cho các tác vụ tác nhân-môi trường. Nó trừu tượng hóa hạ tầng huấn luyện tác nhân thành ba dịch vụ độc lập: Model Service (xử lý tính toán mô hình và cập nhật tham số), Agent Service (điều phối chiến lược thực thi tác nhân, thu thập kinh nghiệm), và Environment Service (cung cấp môi trường thực thi tương tác và ảo hóa, quản lý lập lịch tác vụ phân tán). Các dịch vụ này tương tác thông qua giao diện thống nhất, cho phép mở rộng độc lập và phân bổ tài nguyên linh hoạt. MegaFlow áp dụng chiến lược tài nguyên đàn hồi ("many-small-instances"), mô hình thực thi lai (tạm thời và bền bỉ), điều phối hướng sự kiện, và ủy quyền thành phần chuyên biệt.

### III. Main Results:
MegaFlow đã thành công trong việc điều phối hàng chục nghìn tác vụ tác nhân đồng thời, duy trì độ ổn định hệ thống cao và sử dụng tài nguyên hiệu quả. Hệ thống đạt được mức giảm chi phí 32% và khả năng mở rộng nhất quán lên hàng chục nghìn tác vụ đồng thời, với việc xác thực trong sản xuất qua hơn 2 triệu lượt thực thi huấn luyện tác nhân. MegaFlow khắc phục các hạn chế về bảo mật/cô lập bằng cách di chuyển khối lượng công việc container hóa sang dịch vụ điện toán đám mây đàn hồi, giải quyết các giới hạn về khả năng mở rộng lưu trữ bằng cách cung cấp ảnh container theo yêu cầu, và phá vỡ các nút thắt thông lượng tính toán bằng cách điều phối hàng nghìn phiên bản nhẹ.

### IV. Conclusion & Future Works:
MegaFlow giải quyết một khoảng trống hạ tầng quan trọng trong bối cảnh AI tác nhân mới nổi bằng cách cho phép huấn luyện tác nhân quy mô lớn. Thông điệp cuối cùng là MegaFlow cung cấp một giải pháp mạnh mẽ và hiệu quả cho những thách thức liên quan đến quy mô và độ phức tạp của việc huấn luyện AI tác nhân. Văn bản trích dẫn không đề cập rõ ràng đến các hướng nghiên cứu tiếp theo.

### V. Brainstorming Space:
#### 1. Publish Papers:
Nghiên cứu phát triển các thuật toán lập lịch trình động và thích ứng trong MegaFlow để tối ưu hóa hiệu suất cho các tác vụ tác nhân có tính chất ngắt quãng và yêu cầu tài nguyên không đồng nhất. Khám phá việc tích hợp MegaFlow với các khung học tăng cường phân tán (distributed RL frameworks) tiên tiến để hỗ trợ huấn luyện các mô hình tác nhân đa tác nhân trên quy mô lớn hơn nữa. Phân tích ảnh hưởng của kiến trúc ba dịch vụ của MegaFlow đến khả năng chịu lỗi và tính bền vững của hệ thống khi đối mặt với các lỗi dịch vụ riêng lẻ hoặc sự cố mạng.

#### 2. Patent:
Hệ thống điều phối tài nguyên AI thông minh cho thiết bị di động, tự động phân chia và chuyển giao các tác vụ học tăng cường phức tạp giữa thiết bị và đám mây dựa trên mức độ sử dụng pin và hiệu năng. Phương pháp cung cấp môi trường thực thi ảo hóa an toàn và theo yêu cầu cho các ứng dụng AI tương tác trên điện thoại thông minh, giảm thiểu rủi ro bảo mật và tối ưu hóa bộ nhớ cục bộ. Công nghệ tối ưu hóa lưu trữ dữ liệu AI trên điện thoại di động bằng cách sử dụng cơ chế cung cấp ảnh container theo yêu cầu từ đám mây, cho phép các ứng dụng AI nặng hoạt động hiệu quả mà không tốn dung lượng bộ nhớ cố định.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.07526](https://huggingface.co/papers/2601.07526) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.07526](https://arxiv.org/abs/2601.07526) |
| PDF Download | [https://arxiv.org/pdf/2601.07526.pdf](https://arxiv.org/pdf/2601.07526.pdf) |
| Github Repository | N/A |

--- 

## 13. Boosting Latent Diffusion Models via Disentangled Representation Alignment *(14 votes)*

**Tác giả:** John Page, Xuesong Niu, Kai Wu, Kun Gai

**Xuất bản lúc:** 2026-01-09

**Tag:** Diffusion, Latent Diffusion Models, VAE, Representation Alignment, Semantic Disentanglement

### I. Main Problem:
Các Latent Diffusion Model (LDM) tạo ra hình ảnh chất lượng cao bằng cách hoạt động trong không gian tiềm ẩn nén, thường thu được qua các VAE. Tuy nhiên, các nghiên cứu gần đây thường sử dụng cùng một mục tiêu căn chỉnh (alignment target) cho cả VAE và LDM với Vision Foundation Models (VFM), bỏ qua các yêu cầu biểu diễn khác biệt cơ bản của chúng. LDM cần các khái niệm ngữ nghĩa cấp cao để tạo mô hình sinh, trong khi VAE nên ưu việt trong khả năng phân tách ngữ nghĩa (semantic disentanglement) để mã hóa thông tin chi tiết cấp thuộc tính một cách có cấu trúc. Sự bỏ qua này dẫn đến hiệu suất tạo ảnh và hiệu quả huấn luyện chưa tối ưu.

### II. Main Idea:
Bài báo đề xuất Semantic-disentangled VAE (Send-V AE), được tối ưu hóa rõ ràng cho việc học biểu diễn phân tách bằng cách căn chỉnh không gian tiềm ẩn của nó với hệ thống phân cấp ngữ nghĩa của các VFM đã được huấn luyện trước. Phương pháp này sử dụng một mạng lưới ánh xạ phi tuyến tinh vi để chuyển đổi biểu diễn tiềm ẩn của VAE, căn chỉnh chúng với biểu diễn từ các VFM. Mạng ánh xạ này được thiết kế để thu hẹp khoảng cách biểu diễn giữa việc phân tách cấp thuộc tính và ngữ nghĩa cấp cao do VFM cung cấp, từ đó nâng cao khả năng phân tách ngữ nghĩa của VAE.

### III. Main Results:
*   Xác định khả năng phân tách ngữ nghĩa là một thuộc tính cốt lõi của các VAE thân thiện với quá trình tạo ảnh, được xác minh bằng mối tương quan chặt chẽ giữa độ chính xác dự đoán thuộc tính cấp thấp và hiệu suất tạo ảnh đầu ra.
*   Send-V AE tăng tốc đáng kể quá trình huấn luyện các mô hình khuếch tán dựa trên dòng chảy (flow-based transformers) như SiTs.
*   Thiết lập kỷ lục mới về điểm FID (Fréchet Inception Distance) hiện đại: 1.21 (có hướng dẫn phân loại miễn phí) và 1.75 (không có hướng dẫn phân loại miễn phí) trên ImageNet độ phân giải 256x256.

### IV. Conclusion & Future Works:
Bài báo khẳng định khả năng phân tách ngữ nghĩa là một thuộc tính cốt lõi của các VAE thân thiện với quá trình tạo ảnh, và phương pháp Send-V AE đã chứng minh được hiệu quả vượt trội. Send-V AE, thông qua việc căn chỉnh với VFM bằng mạng ánh xạ phi tuyến, không chỉ nâng cao khả năng phân tách ngữ nghĩa của VAE mà còn tăng tốc đáng kể quá trình huấn luyện mô hình khuếch tán và đạt được hiệu suất tạo ảnh hiện đại. Hướng nghiên cứu tiếp theo có thể khám phá sâu hơn cách tối ưu hóa mạng ánh xạ hoặc áp dụng nguyên lý này cho các loại bộ mã hóa ảnh khác.

### V. Brainstorming Space:
#### 1. Publish Papers:
*   Nghiên cứu ảnh hưởng của các kiến trúc mạng ánh xạ phi tuyến khác nhau lên khả năng phân tách ngữ nghĩa và hiệu suất của VAE.
*   Phân tích định lượng chi tiết hơn mối quan hệ giữa các loại thuộc tính (màu sắc, hình dạng, texture) và khả năng phân tách của VAE, cũng như ảnh hưởng của chúng đến chất lượng ảnh tạo ra.
*   Áp dụng nguyên lý căn chỉnh biểu diễn phân tách của Send-V AE cho các loại bộ mã hóa hình ảnh khác ngoài VAE, ví dụ như tokenizer rời rạc hoặc các mô hình mã hóa tự động khác.

#### 2. Patent:
*   Hệ thống chỉnh sửa ảnh thông minh trên điện thoại di động cho phép người dùng điều chỉnh các thuộc tính cụ thể của đối tượng trong ảnh (ví dụ: thay đổi màu áo, kiểu tóc) một cách độc lập và chính xác nhờ VAE phân tách ngữ nghĩa.
*   Công nghệ tạo hình đại diện (avatar) cá nhân hóa cho ứng dụng gọi video trên điện thoại, tự động tạo ra các biểu cảm hoặc phụ kiện dựa trên các thuộc tính riêng biệt được học từ khuôn mặt người dùng.
*   Phương pháp tăng cường chất lượng video ngắn trên điện thoại bằng cách sử dụng VAE được tối ưu hóa để phân tách các yếu tố như ánh sáng, môi trường và đối tượng, cho phép chỉnh sửa hậu kỳ linh hoạt hơn và giảm nhiễu hiệu quả.
*   Ứng dụng camera điện thoại có khả năng tối ưu hóa ảnh tự động bằng cách nhận diện và điều chỉnh các thuộc tính của đối tượng trong ảnh, ví dụ như làm sáng da, điều chỉnh màu sắc trang phục mà không ảnh hưởng đến các yếu tố khác.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.05823](https://huggingface.co/papers/2601.05823) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.05823](https://arxiv.org/abs/2601.05823) |
| PDF Download | [https://arxiv.org/pdf/2601.05823.pdf](https://arxiv.org/pdf/2601.05823.pdf) |
| Github Repository | N/A |

--- 

## 14. What Users Leave Unsaid: Under-Specified Queries Limit Vision-Language Models *(14 votes)*

**Tác giả:** Dasol Choi, Guijin Son, Hanwool Lee, Minhyuk Kim, Hyunwoo Ko, Teabin Lim, Ahn Eungyeol, Jungwhan Kim, Seunghyeok Hong, Youngsook Song

**Xuất bản lúc:** 2026-01-07

**Tag:** Vision-Language Models, Benchmarking, Under-Specified Queries, HAERAE-Vision

### I. Main Problem:
Các mô hình thị giác-ngôn ngữ (VLM) hiện tại chủ yếu được đánh giá trên các bộ dữ liệu với các câu hỏi rõ ràng, có cấu trúc tốt, trong khi các truy vấn của người dùng thực tế thường không chính thức, thiếu chi tiết và dựa nhiều vào hình ảnh để cung cấp ngữ cảnh. Điều này tạo ra một khoảng cách đáng kể giữa hiệu suất mô hình trên các benchmark và khả năng ứng dụng trong thế giới thực, nơi người dùng thường để lại nhiều thông tin không được nói rõ.

### II. Main Idea:
Nghiên cứu giới thiệu HAERAE-Vision, một bộ dữ liệu benchmark mới gồm 653 câu hỏi hình ảnh thực tế được thu thập từ các cộng đồng trực tuyến của Hàn Quốc. Để định lượng tác động của việc thiếu chi tiết trong truy vấn, mỗi câu hỏi gốc (không rõ ràng) được ghép nối với một phiên bản viết lại rõ ràng, tạo ra tổng cộng 1.306 biến thể truy vấn. HAERAE-Vision được xây dựng thông qua một quy trình lọc sáu giai đoạn nghiêm ngặt từ hơn 86.000 ứng cử viên để đảm bảo chất lượng và tính đại diện cho các tương tác đa phương thức thực tế.

### III. Main Results:
- Các mô hình VLM tiên tiến nhất (như GPT-5 và Gemini 2.5 Pro) đạt dưới 50% độ chính xác trên các truy vấn gốc (không rõ ràng) trong HAERAE-Vision.
- Việc làm rõ truy vấn (explicitation) giúp cải thiện đáng kể hiệu suất từ 8 đến 22 điểm phần trăm, với các mô hình nhỏ hơn có mức cải thiện lớn nhất.
- Ngay cả khi có hỗ trợ tìm kiếm web, các truy vấn thiếu chi tiết vẫn cho hiệu suất kém hơn so với các truy vấn rõ ràng không cần tìm kiếm, cho thấy các hệ thống truy xuất hiện tại chưa thể bù đắp cho những gì người dùng không nói rõ.
- Một phần đáng kể của khó khăn trong các VLM không phải do giới hạn khả năng của mô hình mà do tính chất thiếu chi tiết tự nhiên của các truy vấn người dùng.

### IV. Conclusion & Future Works:
Nghiên cứu kết luận rằng việc thiếu chi tiết tự nhiên trong các truy vấn của người dùng là một thách thức cơ bản đối với các mô hình thị giác-ngôn ngữ, và các benchmark hiện tại chưa phản ánh đúng thực tế này. HAERAE-Vision đóng vai trò là một công cụ quan trọng để đánh giá các VLM trong bối cảnh thực tế hơn, cho thấy sự cần thiết phải phát triển các mô hình có thể suy luận tốt hơn ý định của người dùng từ các truy vấn không rõ ràng và thông tin hình ảnh. Hướng nghiên cứu tiếp theo có thể tập trung vào việc phát triển các phương pháp để các VLM chủ động yêu cầu làm rõ hoặc suy luận ngữ cảnh còn thiếu để cải thiện hiệu suất trong các tình huống thực tế.

### V. Brainstorming Space:
#### 1. Publish Papers:
Phát triển một phương pháp VLM mới có khả năng tự động tạo ra các câu hỏi làm rõ để thu hẹp khoảng cách thông tin từ các truy vấn không rõ ràng. Xây dựng một benchmark đa ngôn ngữ tương tự HAERAE-Vision để nghiên cứu tác động của việc thiếu chi tiết truy vấn trên nhiều nền văn hóa và ngôn ngữ khác nhau. Nghiên cứu cơ chế "suy luận ý định" trong VLM để cho phép chúng hiểu ngữ cảnh và mục đích của người dùng ngay cả khi truy vấn thiếu chi tiết, không cần đến bước làm rõ.

#### 2. Patent:
Một hệ thống ứng dụng di động cho phép người dùng chụp ảnh và đặt câu hỏi không rõ ràng, sau đó AI trên điện thoại tự động làm rõ truy vấn và cung cấp câu trả lời chính xác. Công nghệ tích hợp vào camera điện thoại thông minh để phân tích hình ảnh và gợi ý các câu hỏi làm rõ khi người dùng nhập truy vấn ngắn gọn, giúp họ nhận được thông tin chính xác hơn. Một giao diện người dùng dựa trên AI trên điện thoại thông minh, nơi các truy vấn hình ảnh thiếu chi tiết được tự động chuyển đổi thành truy vấn rõ ràng bằng cách phân tích bối cảnh hình ảnh và lịch sử tương tác của người dùng.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.06165](https://huggingface.co/papers/2601.06165) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.06165](https://arxiv.org/abs/2601.06165) |
| PDF Download | [https://arxiv.org/pdf/2601.06165.pdf](https://arxiv.org/pdf/2601.06165.pdf) |
| Github Repository | [https://github.com/HAE-RAE/HAERAE-VISION](https://github.com/HAE-RAE/HAERAE-VISION) |

--- 

## 15. ET-Agent: Incentivizing Effective Tool-Integrated Reasoning Agent via Behavior Calibration *(13 votes)*

**Tác giả:** Yifei Chen, Guanting Dong, Zhicheng Dou

**Xuất bản lúc:** 2026-01-11

**Tag:** LLMs, Tool-Integrated Reasoning (TIR), Agent, Behavior Calibration, Reinforcement Learning

### I. Main Problem:
Vấn đề cốt lõi là các khung đào tạo tác nhân dựa trên Mô hình Ngôn ngữ Lớn (LLMs) hiện tại thường chỉ tập trung vào độ chính xác của câu trả lời mà bỏ qua việc hiệu chỉnh các mẫu hành vi cụ thể trong các tác vụ suy luận tích hợp công cụ (TIR). Điều này dẫn đến các hành động không hiệu quả của tác nhân như gọi công cụ thừa thãi hoặc không đủ, cũng như logic suy luận bị lỗi, gây khó khăn cho việc khám phá các quỹ đạo hiệu quả.

### II. Main Idea:
Bài báo đề xuất ET-Agent, một khung đào tạo để hiệu chỉnh hành vi sử dụng công cụ của tác nhân thông qua hai thành phần phối hợp: Self-evolving Data Flywheel và Behavior Calibration Training. Self-evolving Data Flywheel tạo ra dữ liệu nâng cao để tinh chỉnh LLM, cải thiện khả năng khám phá của nó. Dựa trên dữ liệu này, Behavior Calibration Training gồm hai pha sẽ dần dần hiệu chỉnh các mẫu hành vi sai lệch thành hành vi tối ưu. Cụ thể, nó sử dụng Action Space Exploration Fine-tuning để mở rộng không gian hành động, sau đó là Iterative Behavior Calibration Reinforcement Learning kết hợp Group-wise Pareto Sampling và Curriculum RL Training để điều chỉnh hành động.

### III. Main Results:
Các thử nghiệm chuyên sâu xác nhận ET-Agent vượt trội trên nhiều khía cạnh bao gồm độ chính xác, hiệu quả, sự cô đọng của suy luận và độ chính xác thực thi công cụ. ET-Agent đạt được hiệu suất tốt nhất trên tất cả các khía cạnh đã kiểm tra, cho thấy sự thành công của việc hiệu chỉnh hành vi TIR. Nó cải thiện đáng kể hiệu quả hành vi, sự cô đọng của suy luận và tỷ lệ thành công thực thi trong khi vẫn duy trì độ chính xác cao.

### IV. Conclusion & Future Works:
ET-Agent cung cấp những hiểu biết thực tế cho nghiên cứu trong lĩnh vực suy luận tích hợp công cụ (TIR) bằng cách giải quyết triệt để vấn đề hiệu chỉnh hành vi sử dụng công cụ của tác nhân LLM, dẫn đến hiệu suất vượt trội trên nhiều tiêu chí.

### V. Brainstorming Space:
#### 1. Publish Papers:
1. Nghiên cứu cách áp dụng cơ chế tự tiến hóa của ET-Agent để tạo ra các tập dữ liệu tự sửa lỗi cho các tác vụ suy luận phức tạp.
2. Khám phá các phương pháp mới để tích hợp hiệu chỉnh hành vi đa tác nhân trong các môi trường TIR hợp tác.
3. Đánh giá khả năng của ET-Agent trong việc giảm thiểu thiên vị và cải thiện tính công bằng trong các quyết định sử dụng công cụ.
#### 2. Patent:
1. Hệ thống trợ lý AI trên điện thoại thông minh sử dụng ET-Agent để tự động tối ưu hóa việc gọi các ứng dụng và chức năng hệ thống, giảm thời gian xử lý và tiêu thụ pin.
2. Phương pháp hiệu chỉnh hành vi cho tác nhân chatbot trên thiết bị di động, giúp chatbot đưa ra các gợi ý sử dụng công cụ (ví dụ: tìm kiếm thông tin, lên lịch) chính xác và hiệu quả hơn, tránh các bước không cần thiết.
3. Công nghệ phần mềm cho thiết bị di động cho phép các ứng dụng tích hợp công cụ học hỏi và điều chỉnh hành vi sử dụng tài nguyên (CPU, mạng) của chúng dựa trên phản hồi của người dùng và hiệu suất thực tế, được tối ưu hóa bởi khung ET-Agent.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.06860](https://huggingface.co/papers/2601.06860) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.06860](https://arxiv.org/abs/2601.06860) |
| PDF Download | [https://arxiv.org/pdf/2601.06860.pdf](https://arxiv.org/pdf/2601.06860.pdf) |
| Github Repository | N/A |

