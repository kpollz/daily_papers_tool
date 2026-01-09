# 🤗 Daily Hugging Face Paper Digest - 2026-01-08

Báo cáo được tạo tự động vào lúc 2026-01-09 10:16:18 bằng mô hình `gemini-2.5-flash`.

## 📰 Summary of Papers

--- 

## 1. Entropy-Adaptive Fine-Tuning: Resolving Confident Conflicts to Mitigate Forgetting

**Tác giả:** Muxi Diao, Lele Yang, Wuxuan Gong, Yutong Zhang, Zhonghao Yan, Yufei Han, Kongming Liang, Weiran Xu, Zhanyu Ma

**Xuất bản lúc:** 2026-01-05

**Tag:** Fine-tuning, Catastrophic Forgetting, LLM, Entropy, Supervised Fine-Tuning (SFT)
### Main Problem:
Supervised Fine-Tuning (SFT) là phương pháp tiêu chuẩn để điều chỉnh các mô hình ngôn ngữ lớn (LLM) cho các lĩnh vực cụ thể, nhưng nó thường gây ra hiện tượng "quên thảm khốc" (catastrophic forgetting), làm suy giảm các khả năng tổng quát của mô hình. Bài báo xác định nguyên nhân là do "Xung đột tự tin" (Confident Conflicts) -- các token có xác suất thấp nhưng entropy thấp, nơi mô hình rất tự tin vào dự đoán của mình nhưng bị buộc phải học một sự thật khác, dẫn đến các cập nhật gradient phá hủy.

### Main Idea:
Bài báo đề xuất phương pháp Fine-Tuning thích ứng với Entropy (Entropy-Adaptive Fine-Tuning - EAFT). Khác với các phương pháp chỉ dựa vào xác suất dự đoán, EAFT sử dụng entropy ở cấp độ token như một cơ chế cổng để phân biệt giữa sự không chắc chắn về nhận thức (epistemic uncertainty) và xung đột kiến thức (knowledge conflict). Điều này cho phép mô hình học từ các mẫu không chắc chắn trong khi ngăn chặn các gradient gây xung đột trên dữ liệu mâu thuẫn. Cụ thể, EAFT điều chỉnh động mất mát huấn luyện dựa trên entropy cấp độ token, hạ thấp trọng số các token có entropy thấp để giảm thiểu các cập nhật phá hủy và tập trung giám sát vào các token có entropy cao để thúc đẩy thích ứng.

### Main Results:
EAFT nhất quán đạt được hiệu suất nhiệm vụ mục tiêu tương đương hoặc vượt trội so với SFT tiêu chuẩn trong khi giảm đáng kể sự suy giảm các khả năng tổng quát của mô hình. Các thử nghiệm trên các dòng mô hình Qwen và GLM (từ 4B đến 32B tham số) trong các lĩnh vực toán học, y tế và tác tử đã xác nhận giả thuyết. EAFT đạt được cải thiện Pareto: khớp hoặc vượt trội các phương pháp cơ sở trên các nhiệm vụ mục tiêu đồng thời giảm thiểu đáng kể sự quên thảm khốc trên các chuẩn tổng quát. Phương pháp được chứng minh là mạnh mẽ với các biến thể siêu tham số và hiệu quả về mặt tính toán.

### Conclusion & Future Works:
EAFT là một giải pháp hiệu quả và phổ quát để giảm thiểu hiện tượng quên thảm khốc trong quá trình Supervised Fine-Tuning, hoạt động thành công trên nhiều họ mô hình và quy mô khác nhau (4B–32B tham số). Bài báo đã phát hiện ra khoảng cách phân phối khác biệt giữa dữ liệu SFT và dữ liệu RL on-policy, đồng thời chỉ ra "Xung đột tự tin" là nguyên nhân chính gây ra quên thảm khốc.

### Brainstorming Space:
#### 1. Publish Papers:
1.  Nghiên cứu ứng dụng EAFT để giải quyết hiện tượng quên thảm khốc trong các mô hình thị giác máy tính khi fine-tuning cho các miền dữ liệu mới.
2.  Khám phá việc tích hợp cơ chế EAFT với các phương pháp nén mô hình để tạo ra các LLM nhỏ gọn và hiệu quả hơn mà vẫn duy trì khả năng tổng quát sau fine-tuning.
3.  Phân tích tác động của các chiến lược tạo dữ liệu huấn luyện hoặc phản hồi (feedback) khác nhau lên "Xung đột tự tin" và hiệu quả của EAFT.
#### 2. Patent:
1.  Một hệ thống fine-tuning mô hình AI cá nhân trên thiết bị di động, sử dụng cơ chế thích ứng entropy để cập nhật các tính năng trợ lý ảo riêng biệt mà không làm suy giảm khả năng tổng quát của trợ lý đó.
2.  Một phương pháp tối ưu hóa việc phân phối và cập nhật các mô hình AI ngôn ngữ trên điện thoại thông minh, trong đó các bản vá lỗi hoặc tính năng mới được fine-tune bằng EAFT để tránh quên các chức năng cốt lõi.
3.  Một công nghệ cho phép người dùng điện thoại thông minh tùy chỉnh giao diện hoặc tương tác của chatbot bằng cách fine-tune một phần mô hình ngôn ngữ cục bộ, với EAFT đảm bảo rằng các kiến thức đã có không bị ghi đè một cách phá hủy.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.02151](https://huggingface.co/papers/2601.02151) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.02151](https://arxiv.org/abs/2601.02151) |
| PDF Download | [https://arxiv.org/pdf/2601.02151.pdf](https://arxiv.org/pdf/2601.02151.pdf) |
| Github Repository | [https://github.com/PRIS-CV/EAFT](https://github.com/PRIS-CV/EAFT) |

--- 

## 2. Evolving Programmatic Skill Networks

**Tác giả:** Haochen Shi, Xingdi Yuan, Bang Liu

**Xuất bản lúc:** 2026-01-07

**Tag:** Programmatic Skill Networks, Continual Learning, Embodied AI, Large Language Models

### Main Problem:
Các tác nhân AI trong môi trường mở phải liên tục học hỏi, tinh chỉnh và tái sử dụng các kỹ năng. Các phương pháp hiện có gặp hai hạn chế: (1) các kỹ năng thường được biểu diễn dưới dạng thư viện phẳng hoặc đồ thị tĩnh, thiếu cơ chế nguyên tắc để cải tiến liên tục, và (2) các tác nhân thiếu khung thống nhất để phân bổ trách nhiệm trong các cấu trúc kỹ năng phân cấp, sửa chữa chương trình biểu tượng và tái tổ chức cấu trúc khi các tác vụ mới phát sinh.

### Main Idea:
Nghiên cứu giới thiệu Programmatic Skill Network (PSN), một framework cho phép các tác nhân liên tục học hỏi các kỹ năng trong môi trường mở. Trong PSN, mỗi kỹ năng là một chương trình biểu tượng có thể thực thi (ví dụ: JavaScript, Python) tạo thành một mạng lưới tổng hợp phát triển qua kinh nghiệm. PSN định nghĩa ba cơ chế cốt lõi được khởi tạo thông qua các mô hình ngôn ngữ lớn (LLM): (1) REFLECT để định vị lỗi có cấu trúc trong các thành phần kỹ năng, (2) tối ưu hóa lũy tiến với cơ chế cập nhật nhận biết độ trưởng thành để ổn định các kỹ năng đáng tin cậy đồng thời duy trì tính linh hoạt cho những kỹ năng chưa chắc chắn, và (3) tái cấu trúc cấu trúc chuẩn theo cơ chế kiểm tra quay lui để duy trì tính nhỏ gọn của mạng lưới. PSN duy trì một đồ thị tính toán rõ ràng của các chương trình có thể thực thi, hỗ trợ phân bổ trách nhiệm dựa trên dấu vết, ổn định nhận biết độ trưởng thành và tái cấu trúc cấu trúc theo nguyên tắc.

### Main Results:
Các thử nghiệm trên MineDojo và Crafter cho thấy PSN có khả năng tái sử dụng kỹ năng mạnh mẽ, thích ứng nhanh chóng và tổng quát hóa tốt trên các phân phối tác vụ mở. Động lực học học tập của PSN cũng cho thấy sự tương đồng về cấu trúc với quá trình huấn luyện mạng nơ-ron, gợi ý rằng các nguyên tắc tối ưu hóa mạng nơ-ron có thể mở rộng sang các hệ thống học tập lập trình.

### Conclusion & Future Works:
Thiết kế kiến trúc của PSN tạo ra động lực học học tập có sự tương đồng về cấu trúc với quá trình huấn luyện mạng nơ-ron, gợi ý các nguyên tắc chung cho việc học tập liên tục trên các mô hình biểu diễn khác nhau. Nhóm nghiên cứu có kế hoạch mở mã nguồn của dự án này.

### Brainstorming Space:
#### 1. Publish Papers:
1.  Nghiên cứu cách PSN có thể tích hợp với các hệ thống học tăng cường sâu để xử lý các quan sát thô và hành động cấp thấp một cách hiệu quả hơn.
2.  Khám phá việc tự động tạo ra hoặc học các điều kiện tiên quyết và hậu điều kiện cho kỹ năng thay vì phải xác định thủ công, giúp mở rộng khả năng tự chủ của tác nhân.
3.  Áp dụng PSN trong các kịch bản hợp tác đa tác nhân, nơi các tác nhân cùng xây dựng và chia sẻ mạng lưới kỹ năng lập trình của mình.

#### 2. Patent:
1.  Hệ thống trợ lý AI trên điện thoại di động tự động học và tinh chỉnh các chuỗi tác vụ phức tạp của người dùng thông qua giao diện lập trình nội bộ, cải thiện hiệu quả sử dụng ứng dụng.
2.  Phương pháp tối ưu hóa năng lượng cho điện thoại thông minh bằng cách sử dụng mạng lưới kỹ năng lập trình để dự đoán và tối ưu hóa các thao tác người dùng lặp lại, giảm tải xử lý không cần thiết.
3.  Công nghệ tích hợp trong điện thoại di động cho phép tạo và quản lý các "macro thông minh" đa ứng dụng, tự động sửa lỗi và tái cấu trúc các bước thực hiện dựa trên phản hồi của người dùng để hoàn thành mục tiêu.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.03509](https://huggingface.co/papers/2601.03509) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.03509](https://arxiv.org/abs/2601.03509) |
| PDF Download | [https://arxiv.org/pdf/2601.03509.pdf](https://arxiv.org/pdf/2601.03509.pdf) |
| Github Repository | N/A |

--- 

## 3. Atlas: Orchestrating Heterogeneous Models and Tools for Multi-Domain Complex Reasoning

**Tác giả:** Jinyang Wu, Guocheng Zhai, Ruihan Jin, Jiahao Yuan, Yuhao Shen, Shuai Zhang, Zhengqi Wen, Jianhua Tao

**Xuất bản lúc:** 2026-01-07

Summary generation failed.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.03872](https://huggingface.co/papers/2601.03872) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.03872](https://arxiv.org/abs/2601.03872) |
| PDF Download | [https://arxiv.org/pdf/2601.03872.pdf](https://arxiv.org/pdf/2601.03872.pdf) |
| Github Repository | N/A |

--- 

## 4. Benchmark^2: Systematic Evaluation of LLM Benchmarks

**Tác giả:** Qi Qian, Chengsong Huang, Jingwen Xu, Changze Lv, Muling Wu, Wenhao Liu, Xiaohua Wang, Zhenghua Wang, Zisu Huang, Muzhao Tian, Jianhan Xu, Kun Hu, He-Da Wang, Yao Hu, Xuanjing Huang, Xiaoqing Zheng

**Xuất bản lúc:** 2026-01-07

**Tag:** LLM Evaluation, Benchmark Quality, Metrics

### Main Problem:
Sự gia tăng nhanh chóng của các benchmark dùng để đánh giá các mô hình ngôn ngữ lớn (LLM) đã tạo ra nhu cầu cấp thiết về các phương pháp có hệ thống để tự đánh giá chất lượng của chính các benchmark đó. Các vấn đề chính với các benchmark hiện tại bao gồm sự không nhất quán trong việc xếp hạng các mô hình, khả năng phân biệt thấp giữa các mô hình có năng lực khác nhau, và sự tồn tại của các trường hợp thử nghiệm có vấn đề nơi các mô hình mạnh hơn lại thất bại trong khi các mô hình yếu hơn lại thành công.

### Main Idea:
Bài báo đề xuất BENCHMARK^2, một khuôn khổ toàn diện để đánh giá chất lượng benchmark, bao gồm ba chỉ số bổ sung:
1.  **Cross-Benchmark Ranking Consistency (CBRC):** Đo lường mức độ phù hợp trong xếp hạng mô hình của một benchmark với các benchmark đồng cấp trong cùng lĩnh vực.
2.  **Discriminability Score (DS):** Định lượng khả năng của một benchmark trong việc phân biệt rõ ràng giữa các mô hình có năng lực khác nhau.
3.  **Capability Alignment Deviation (CAD):** Xác định các trường hợp kiểm thử có vấn đề khi các mô hình mạnh hơn thất bại nhưng các mô hình yếu hơn lại thành công trong cùng một họ mô hình, đảm bảo tính nhất quán theo thứ bậc năng lực mong đợi.
Các chỉ số này được sử dụng để phân tích và đánh giá chất lượng của các benchmark hiện có.

### Main Results:
-   Các thí nghiệm sâu rộng trên 15 benchmark thuộc các lĩnh vực toán học, suy luận và tri thức, đánh giá 11 LLM từ bốn họ mô hình, đã cho thấy sự biến đổi đáng kể về chất lượng giữa các benchmark hiện có.
-   Phân tích đã tiết lộ các đặc điểm chất lượng của benchmark, phân biệt rõ ràng giữa benchmark chất lượng cao và các benchmark có vấn đề.
-   Việc xây dựng benchmark có chọn lọc, dựa trên các chỉ số chất lượng được đề xuất, có thể đạt được hiệu suất đánh giá tương đương với các bộ dữ liệu thử nghiệm đầy đủ nhưng với kích thước giảm đáng kể (chỉ 35% dữ liệu gốc).

### Conclusion & Future Works:
Bài báo đã hình thức hóa vấn đề đánh giá chất lượng benchmark và đề xuất một bộ ba chỉ số bổ sung để nắm bắt các khía cạnh khác nhau của độ tin cậy benchmark. Đây là một đánh giá có hệ thống quy mô lớn đầu tiên về chất lượng benchmark, cung cấp những hiểu biết thực nghiệm quan trọng về tình trạng đánh giá LLM. Khả năng ứng dụng thực tiễn của khuôn khổ này được chứng minh qua việc xây dựng các benchmark rút gọn nhưng vẫn duy trì hiệu suất đánh giá, cho thấy tiềm năng trong việc tối ưu hóa quy trình đánh giá LLM. Bài báo không trình bày cụ thể về các hướng nghiên cứu trong tương lai.

### Brainstorming Space:
#### 1. Publish Papers:
-   Nghiên cứu sự tương quan giữa các chỉ số chất lượng benchmark được đề xuất và khả năng của benchmark trong việc dự đoán hiệu suất LLM trong các ứng dụng thực tế.
-   Phát triển các phương pháp tự động để tạo ra các trường hợp kiểm thử mới có khả năng phân biệt cao hoặc có tính nhất quán xếp hạng tốt dựa trên phân tích của BENCHMARK^2.
-   Mở rộng khuôn khổ BENCHMARK^2 để đánh giá các khía cạnh khác của benchmark như độ bền vững (robustness) trước các nhiễu hoặc tính công bằng (fairness) đối với các nhóm dữ liệu khác nhau.

#### 2. Patent:
-   Một hệ thống phần mềm tích hợp vào hệ điều hành điện thoại thông minh, cho phép tự động đánh giá chất lượng của các benchmark được sử dụng để kiểm tra các mô hình AI trên thiết bị, giúp nhà phát triển tối ưu hóa hiệu suất LLM cho điện thoại.
-   Một ứng dụng di động cho phép người dùng thực hiện các bài kiểm tra ngắn cho LLM trên điện thoại của họ, đồng thời thu thập dữ liệu về các chỉ số CBRC, DS và CAD để cung cấp phản hồi về chất lượng benchmark cho cộng đồng.
-   Một thuật toán nén benchmark độc đáo dành cho thiết bị di động, sử dụng các chỉ số BENCHMARK^2 để chọn lọc các câu hỏi kiểm tra hiệu quả nhất, cho phép các LLM trên điện thoại được đánh giá nhanh chóng mà không cần kết nối mạng.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.03986](https://huggingface.co/papers/2601.03986) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.03986](https://arxiv.org/abs/2601.03986) |
| PDF Download | [https://arxiv.org/pdf/2601.03986.pdf](https://arxiv.org/pdf/2601.03986.pdf) |
| Github Repository | N/A |

--- 

## 5. ROI-Reasoning: Rational Optimization for Inference via Pre-Computation Meta-Cognition

**Tác giả:** Muyang Zhao, Qi Qi, Hao Sun

**Xuất bản lúc:** 2026-01-07

**Tag:** LLMs, Budgeted Reasoning, Meta-Cognition, Resource Allocation, Reinforcement Learning, Knapsack Problem

### Main Problem:
Các mô hình ngôn ngữ lớn (LLM) hiện nay có khả năng suy luận mạnh mẽ nhưng không thể tự ước tính lượng tài nguyên tính toán (tokens) mà một tác vụ yêu cầu. Điều này dẫn đến việc thiếu khả năng phân bổ tài nguyên một cách chiến lược trên nhiều tác vụ dưới một giới hạn ngân sách toàn cầu nghiêm ngặt, gây ra lãng phí tài nguyên và hiệu suất không tối ưu, đặc biệt khi phải đưa ra quyết định tuần tự dưới sự không chắc chắn.

### Main Idea:
Bài báo đề xuất ROI-Reasoning, một khuôn khổ hai giai đoạn nhằm trang bị cho LLM khả năng ra quyết định nội tại, hợp lý và nhận biết ngân sách trong quá trình suy luận.
1.  **Meta-Cognitive Fine-Tuning (MFT):** Giai đoạn này huấn luyện mô hình dự đoán chi phí suy luận (lượng token) và lợi ích dự kiến của việc suy luận trước khi tạo ra bất kỳ phản hồi nào. Điều này cho phép mô hình đưa ra quyết định rõ ràng về việc "giải quyết" hay "bỏ qua" một vấn đề.
2.  **Rationality-Aware Reinforcement Learning (RARL):** Giai đoạn này tối ưu hóa quá trình ra quyết định tuần tự của mô hình dưới giới hạn token toàn cầu. Mô hình học cách lập kế hoạch và phân bổ tính toán trên nhiều vấn đề để tối đa hóa hiệu suất tổng thể trong dài hạn.
Vấn đề được chính thức hóa như một "Ordered Stochastic Multiple-Choice Knapsack Problem (OS-MCKP)" để làm nổi bật yêu cầu về khả năng siêu nhận thức.

### Main Results:
Trên các bộ dữ liệu đánh giá suy luận toán học có ngân sách giới hạn, ROI-Reasoning liên tục cải thiện điểm tổng thể. Quan trọng hơn, nó giảm đáng kể sự hối tiếc (regret) khi hoạt động dưới các ngân sách tính toán chặt chẽ.

### Conclusion & Future Works:
ROI-Reasoning thành công trang bị cho LLM khả năng lập kế hoạch nhận thức bậc cao và đưa ra quyết định thích ứng, cho phép phân bổ tài nguyên tính toán trong thời gian suy luận một cách hợp lý và nhận biết lợi tức đầu tư (ROI). Bản trích dẫn không đề cập rõ ràng đến các hướng nghiên cứu tiếp theo.

### Brainstorming Space:
#### 1. Publish Papers:
1. Nghiên cứu mở rộng ROI-Reasoning cho các mô hình ngôn ngữ lớn đa phương thức, xem xét nhiều loại tài nguyên tính toán khác nhau (ví dụ: thị giác, âm thanh).
2. Áp dụng khung ROI-Reasoning vào lĩnh vực AI đàm thoại thời gian thực, nơi cần tối ưu hóa phản hồi trong điều kiện ngân sách động và tương tác liên tục.
3. Phát triển các chiến lược phân bổ ngân sách thích ứng, có khả năng điều chỉnh linh hoạt dựa trên phản hồi của người dùng hoặc sự thay đổi của môi trường hoạt động.

#### 2. Patent:
1. Một hệ thống quản lý tài nguyên tính toán tích hợp trên điện thoại thông minh, cho phép ứng dụng AI phân bổ năng lượng xử lý và bộ nhớ một cách thông minh dựa trên ước tính lợi tức đầu tư cho từng tác vụ.
2. Phương pháp tối ưu hóa thời lượng pin cho các tác vụ suy luận phức tạp của LLM trên thiết bị di động bằng cách dự đoán chi phí token và lợi ích của các lựa chọn mô hình khác nhau trước khi thực hiện.
3. Một giao diện người dùng trên điện thoại di động cho phép người dùng đặt các ưu tiên ngân sách cho tác vụ AI, để hệ thống tự động điều chỉnh mức độ chi tiết của suy luận LLM nhằm đạt hiệu quả cao nhất trong giới hạn đã cho.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.03822](https://huggingface.co/papers/2601.03822) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.03822](https://arxiv.org/abs/2601.03822) |
| PDF Download | [https://arxiv.org/pdf/2601.03822.pdf](https://arxiv.org/pdf/2601.03822.pdf) |
| Github Repository | N/A |

--- 

## 6. Klear: Unified Multi-Task Audio-Video Joint Generation

**Tác giả:** Jun Wang, Chunyu Qiang, Yuxin Guo, Yiran Wang, Xijuan Zeng, Chen Zhang, Pengfei Wan

**Xuất bản lúc:** 2026-01-07

**Tag:** Diffusion, Generative AI, Audio-Video Generation, Multimodal, Transformer, DiT, Flow Matching

### Main Problem:
Các mô hình tạo sinh âm thanh-video hiện tại gặp phải nhiều thách thức, bao gồm sự không đồng bộ về mặt ngữ nghĩa và thời gian giữa âm thanh và video, chất lượng suy giảm khi tạo sinh đơn phương thức (unimodal), sự thiếu hụt dữ liệu chất lượng cao có chú thích dày đặc, và khả năng khái quát hóa hạn chế ra các tình huống ngoài phân phối (OOD). Hầu hết các kiến trúc hiện có, đặc biệt là các thiết kế dual-tower hoặc single-tower với cross-attention nông, không thể tích hợp sâu sắc các đặc trưng đa phương thức để đạt được sự căn chỉnh chặt chẽ.

### Main Idea:
Bài báo đề xuất Klear, một framework tạo sinh âm thanh-video đa tác vụ thống nhất, giải quyết các vấn đề trên thông qua ba cải tiến chính:
1.  **Kiến trúc thống nhất:** Sử dụng thiết kế single-tower với các khối Diffusion Transformer (DiT) thống nhất và cơ chế Omni-Full Attention. Cơ chế này cho phép chú ý đồng thời tới bốn luồng (video, chú thích video, âm thanh, chú thích âm thanh/lời nói), thúc đẩy sự hợp nhất đa phương thức chặt chẽ và khả năng mở rộng mạnh mẽ.
2.  **Chiến lược huấn luyện tiến hóa:** Áp dụng chế độ huấn luyện đa tác vụ tiến hóa với kỹ thuật mặt nạ ngẫu nhiên từng phương thức (random modality masking) và một chương trình huấn luyện đa giai đoạn (multistage curriculum). Điều này đảm bảo tối ưu hóa chung giữa các tác vụ (Text to Audio-Video, Image to Audio-Video, Image to Video, Text to Video, Text to Audio), tạo ra các biểu diễn mạnh mẽ, khai thác kiến thức thế giới căn chỉnh A-V và ngăn chặn sự suy giảm chất lượng đơn phương thức.
3.  **Xây dựng dữ liệu quy mô lớn:** Giới thiệu bộ dữ liệu âm thanh-video quy mô lớn đầu tiên với 81 triệu mẫu có chú thích dày đặc chính xác, cùng với một pipeline xây dựng dữ liệu tự động hiệu quả, lọc và chú thích hàng triệu cặp âm thanh-video-chú thích chất lượng cao và được căn chỉnh chặt chẽ.

### Main Results:
Klear đạt được hiệu suất vượt trội so với các phương pháp trước đây và ngang bằng với các hệ thống thương mại như Veo 3 trong số các mô hình mã nguồn mở. Cụ thể, nó:
*   Cung cấp khả năng tạo sinh độ chân thực cao (high fidelity) với sự căn chỉnh ngữ nghĩa và thời gian mạnh mẽ giữa âm thanh và video.
*   Thực hiện đáng tin cậy việc tuân thủ các hướng dẫn (instruction following) trong cả cài đặt tạo sinh chung (joint) và đơn phương thức (unimodal).
*   Khái quát hóa mạnh mẽ ra các kịch bản ngoài phân phối (OOD generalization).
*   Vượt trội hơn đáng kể so với các phương pháp tiên tiến trước đây trên các benchmark đơn phương thức và benchmark tạo sinh chung AV.

### Conclusion & Future Works:
Klear đại diện cho một bước tiến quan trọng trong tạo sinh âm thanh-video đa tác vụ, cung cấp một framework thống nhất và có khả năng mở rộng để tạo ra nội dung đa phương tiện chất lượng cao, căn chỉnh chặt chẽ. Với các cải tiến về kiến trúc, chiến lược huấn luyện và dữ liệu, nó mở ra con đường cho thế hệ tiếp theo của các hệ thống tổng hợp âm thanh-video. Bài báo không đề cập cụ thể về các công việc tương lai, nhưng ngụ ý rằng phương pháp này là một "con đường thống nhất, có khả năng mở rộng hướng tới tổng hợp âm thanh-video thế hệ tiếp theo".

### Brainstorming Space:
#### 1. Publish Papers:
*   Nghiên cứu sâu hơn về cơ chế Omni-Full Attention để phân tích khả năng đóng góp của từng luồng đa phương thức và mối tương tác của chúng.
*   Phát triển các chiến lược huấn luyện tự giám sát hoặc tự học mạnh mẽ hơn để khai thác dữ liệu không có nhãn hoặc ít nhãn cho tạo sinh âm thanh-video.
*   Mở rộng framework Klear để tích hợp các phương thức đầu vào khác như cảm biến xúc giác hoặc dữ liệu sinh trắc học để tạo ra trải nghiệm đa phương tiện toàn diện hơn.

#### 2. Patent:
*   Hệ thống ứng dụng di động cho phép người dùng tạo video ngắn có âm thanh và lời nói được đồng bộ hóa chặt chẽ chỉ từ một mô tả văn bản hoặc hình ảnh đầu vào.
*   Công nghệ chỉnh sửa video tự động trên điện thoại thông minh, trong đó AI có thể tạo hoặc sửa đổi âm thanh và lời nói trong video để phù hợp với kịch bản hoặc thay đổi hình ảnh được người dùng thực hiện.
*   Phương pháp nén và truyền tải dữ liệu đa phương tiện (âm thanh, video, chú thích) một cách hiệu quả trên các thiết bị di động, sử dụng các biểu diễn latent học được từ mô hình Klear để tối ưu hóa băng thông và chất lượng.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.04151](https://huggingface.co/papers/2601.04151) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.04151](https://arxiv.org/abs/2601.04151) |
| PDF Download | [https://arxiv.org/pdf/2601.04151.pdf](https://arxiv.org/pdf/2601.04151.pdf) |
| Github Repository | N/A |

--- 

## 7. Choreographing a World of Dynamic Objects

**Tác giả:** Yanzhe Lyu, Chen Geng, Karthik Dharmarajan, Yunzhi Zhang, Hadi Alzayer, Shangzhe Wu, Jiajun Wu

**Xuất bản lúc:** 2026-01-07

**Tag:** Generative Models, 4D Scene Dynamics, Object Interaction, Video Distillation, Robotics
### Main Problem:
Tạo ra các chuyển động 4D (biến dạng và tương tác) chân thực và đa dạng cho nhiều đối tượng trong một cảnh là một thách thức lớn. Các phương pháp đồ họa truyền thống tốn nhiều công sức và không mở rộng được, trong khi các phương pháp học sâu đòi hỏi tập dữ liệu lớn hiếm có và thường chỉ tập trung vào biến dạng của một đối tượng đơn lẻ. Ngoài ra, việc xử lý các biến dạng 4D có chiều không gian cao và không đều về thời gian, cùng với sự không tương thích của kiến trúc mô hình tạo video hiện đại với các thuật toán chưng cất hiện có, càng làm tăng độ khó của vấn đề.

### Main Idea:
Bài báo giới thiệu CHORD, một pipeline tạo sinh phổ quát để "biên đạo" các đối tượng và cảnh động bằng cách chưng cất thông tin chuyển động từ các mô hình tạo video. Phương pháp này tối ưu lặp lại các biến dạng Lagrangian cấp thấp của từng đối tượng. Ở mỗi bước, CHORD biến dạng cảnh 3D, dựng hình từ các góc nhìn khác nhau, và sử dụng mô hình tạo video để đánh giá tính hợp lý của biến dạng. Để giải quyết các thách thức, CHORD đề xuất: (1) một biểu diễn chuyển động 4D thô-đến-tinh theo cấp bậc, kết hợp các điểm kiểm soát hai cấp độ cho không gian và cấu trúc dựa trên cây Fenwick cho thời gian, nhằm đảm bảo tính mạch lạc và khả năng học hỏi chuyển động dài hạn; và (2) một chiến lược chưng cất mới cho các mô hình tạo video dựa trên rectified flow, bao gồm một mục tiêu Score Distillation Sampling (SDS) mới và chiến lược lấy mẫu nhiễu thích nghi để cung cấp hướng dẫn hiệu quả.

### Main Results:
CHORD cho thấy hiệu quả vượt trội so với các phương pháp hiện có trong việc tạo ra một loạt các động lực học 4D đa đối tượng chân thực, mà không yêu cầu cấu trúc động học cụ thể theo danh mục hay tập dữ liệu 4D lớn. Đây là phương pháp đầu tiên giải quyết việc tạo chuyển động 4D cấp độ cảnh mà không dựa vào bất kỳ thiên kiến quy nạp cụ thể nào. Ngoài việc tạo sinh hình ảnh, pipeline này còn tạo ra các quỹ đạo biến dạng Lagrangian có cơ sở vật lý cho các đối tượng trong thế giới thực, cho phép robot thực hiện các tác vụ thao tác đối tượng đa dạng theo kiểu zero-shot.

### Conclusion & Future Works:
CHORD cung cấp một giải pháp mạnh mẽ và hiệu quả cho vấn đề tạo chuyển động 4D nhất quán cho các đối tượng động trong một cảnh. Các đóng góp chính bao gồm một biểu diễn chuyển động 4D mới kết hợp cấu trúc thời gian tích lũy dựa trên cây Fenwick với tham số hóa DoF phân cấp, một chiến lược chưng cất cải tiến cho các mô hình tạo video dựa trên rectified flow, và một khuôn khổ linh hoạt có khả năng tạo chuyển động 4D có cơ sở vật lý, có thể áp dụng cho việc học các chính sách thao tác robot trong thế giới thực.

### Brainstorming Space:
#### 1. Publish Papers:
1.  Nghiên cứu mở rộng CHORD để tích hợp các ràng buộc vật lý phức tạp hơn, cho phép mô phỏng các vật liệu dễ biến dạng hoặc các tương tác lực phức tạp trong môi trường 4D.
2.  Khám phá việc sử dụng CHORD trong việc tạo ra các môi trường huấn luyện đa dạng và chân thực cho các tác nhân AI nhập vai, tập trung vào khả năng học tập tăng cường trong các tình huống tương tác vật lý.
3.  Phát triển một phương pháp tự động đánh giá chất lượng và độ chân thực vật lý của chuyển động 4D được tạo ra, sử dụng các metric dựa trên mô phỏng vật lý và phản hồi của con người.
#### 2. Patent:
1.  Một hệ thống ứng dụng di động cho phép người dùng quay video 2D của một vật thể và sử dụng công nghệ CHORD để tự động tạo ra mô hình 3D động của vật thể đó, có thể tương tác trong các ứng dụng thực tế ảo hoặc tăng cường trên điện thoại.
2.  Công nghệ tích hợp vào camera điện thoại để phân tích cảnh thực tế và tạo ra các hiệu ứng động 4D theo thời gian thực (ví dụ: một vật thể trong video có thể tự động biến dạng hoặc tương tác với môi trường ảo theo kịch bản do người dùng nhập text), cải thiện trải nghiệm quay video.
3.  Một phương pháp tạo ra các hoạt ảnh biểu cảm cho các emoji hoặc avatar 3D trên điện thoại, trong đó chuyển động và tương tác của chúng được "biên đạo" bởi CHORD dựa trên văn bản hoặc âm thanh đầu vào của người dùng.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.04194](https://huggingface.co/papers/2601.04194) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.04194](https://arxiv.org/abs/2601.04194) |
| PDF Download | [https://arxiv.org/pdf/2601.04194.pdf](https://arxiv.org/pdf/2601.04194.pdf) |
| Github Repository | N/A |

--- 

## 8. Agentic Rubrics as Contextual Verifiers for SWE Agents

**Tác giả:** Mohit Raghavendra, Anisha Gunjal, Bing Liu, Yunzhong He

**Xuất bản lúc:** 2026-01-07

**Tag:** Agentic Rubrics, SWE Agents, Verification, LLMs, Software Engineering

### Main Problem:
Vấn đề cốt lõi mà bài báo đề cập là việc xác minh (verification) các bản vá lỗi của các tác nhân kỹ thuật phần mềm (SWE agents) hiện tại thường dựa vào việc thực thi mã, vốn khó mở rộng do chi phí thiết lập môi trường cao. Các giải pháp thay thế không thực thi mã thì kém đáng tin cậy, khó diễn giải và ít dựa vào ngữ cảnh của codebase.

### Main Idea:
Bài báo đề xuất "Agentic Rubrics," một phương pháp trong đó một tác nhân chuyên gia (expert agent) tương tác với kho lưu trữ mã để tạo ra một danh sách tiêu chí đánh giá (rubric checklist) có ngữ cảnh. Sau đó, các bản vá ứng cử viên sẽ được chấm điểm dựa trên danh sách này mà không cần thực thi mã. Điều này giúp cung cấp một tín hiệu xác minh hiệu quả, có thể mở rộng và chi tiết cho các tác nhân SWE.

### Main Results:
Trên bộ dữ liệu SWE-Bench Verified dưới đánh giá TTS song song, Agentic Rubrics đạt 54.2% trên Qwen3-Coder-30B-A3B và 40.6% trên Qwen3-32B, với mức tăng ít nhất 3.5 điểm phần trăm so với baseline mạnh nhất. Phân tích cho thấy điểm rubric phù hợp với các bài kiểm tra ground-truth và cũng phát hiện ra các vấn đề mà các bài kiểm tra không nắm bắt được. Các thí nghiệm chứng minh rằng việc thu thập ngữ cảnh theo kiểu agentic là cần thiết để tạo ra các tiêu chí cụ thể, rõ ràng cho codebase.

### Conclusion & Future Works:
Agentic Rubrics cung cấp một tín hiệu xác minh hiệu quả, có thể mở rộng và chi tiết cho các tác nhân kỹ thuật phần mềm. Ngoài ra, việc tạo rubric theo kiểu agentic có thể được chắt lọc (distilled) thành các mô hình mã nguồn mở nhỏ hơn, cho phép triển khai quy mô lớn.

### Brainstorming Space:
#### 1. Publish Papers:
- Nghiên cứu việc áp dụng Agentic Rubrics cho việc xác minh các nhiệm vụ kỹ thuật phần mềm phức tạp hơn, chẳng hạn như thiết kế kiến trúc hoặc refactoring quy mô lớn.
- Phát triển một phương pháp tự động điều chỉnh trọng số của các tiêu chí rubric dựa trên mức độ quan trọng được suy ra từ các thay đổi của codebase hoặc phản hồi của nhà phát triển.
- Khám phá khả năng tích hợp Agentic Rubrics với các quy trình kiểm thử liên tục để cung cấp phản hồi nhanh chóng và ngữ cảnh trong giai đoạn phát triển.
#### 2. Patent:
- Hệ thống tích hợp Agentic Rubrics vào một môi trường phát triển di động (IDE) trên điện thoại để cung cấp phản hồi chất lượng mã theo thời gian thực cho các nhà phát triển ứng dụng di động.
- Công nghệ AI trên điện thoại di động sử dụng Agentic Rubrics để phân tích và xác minh các bản vá lỗi bảo mật hoặc cập nhật hệ thống trước khi cài đặt, đảm bảo tính tương thích và an toàn cho thiết bị.
- Ứng dụng di động hỗ trợ lập trình cá nhân hóa, sử dụng Agentic Rubrics để đánh giá và đưa ra phản hồi chi tiết, có ngữ cảnh cho các đoạn mã do người dùng viết trực tiếp trên smartphone.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.04171](https://huggingface.co/papers/2601.04171) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.04171](https://arxiv.org/abs/2601.04171) |
| PDF Download | [https://arxiv.org/pdf/2601.04171.pdf](https://arxiv.org/pdf/2601.04171.pdf) |
| Github Repository | N/A |

--- 

## 9. MDAgent2: Large Language Model for Code Generation and Knowledge Q&A in Molecular Dynamics

**Tác giả:** Zhuofan Shi, Hubao A, Yufei Shao, Mengyan Dai, Yadong Yu, Pan Xiang, Dongliang Huang, Hongxu An, Chunxiao Xin, Haiyang Shen, Zhenyu Wang, Yunshan Na, Gang Huang, Xiang Jing

**Xuất bản lúc:** 2026-01-05

**Tag:** Large Language Model, Code Generation, Knowledge Q&A, Molecular Dynamics, LAMMPS, Multi-Agent System, Reinforcement Learning

### Main Problem:
Việc thực hiện các mô phỏng động lực học phân tử (MD) là thiết yếu nhưng việc viết các tập lệnh LAMMPS đòi hỏi chuyên môn cao và tốn thời gian. Các Mô hình Ngôn ngữ Lớn (LLMs) hiện tại bị hạn chế trong kịch bản MD do thiếu dữ liệu miền, chi phí triển khai cao của các LLMs tiên tiến, khả năng thực thi mã thấp, thiếu các bộ tiêu chuẩn đánh giá cho LAMMPS và các cơ chế tối ưu hóa vòng lặp kín cho việc tạo mã.

### Main Idea:
Bài báo giới thiệu MDAgent2, framework đầu cuối đầu tiên có khả năng thực hiện cả Hỏi & Đáp kiến thức và tạo mã trong lĩnh vực động lực học phân tử. Nó xây dựng một pipeline tạo dữ liệu chuyên biệt chất lượng cao, tạo ra ba tập dữ liệu độc đáo bao gồm kiến thức MD, Hỏi & Đáp, và tạo mã. Dựa trên các tập dữ liệu này, MDAgent2 áp dụng chiến lược hậu huấn luyện ba giai đoạn (tiếp tục tiền huấn luyện CPT, tinh chỉnh có giám sát SFT, và học tăng cường RL) để huấn luyện hai mô hình thích ứng miền là MD-Instruct và MD-Code. Hơn nữa, nó giới thiệu MD-GRPO, một phương pháp RL vòng lặp kín tận dụng kết quả mô phỏng làm tín hiệu thưởng và tái chế các quỹ đạo thưởng thấp để tinh chỉnh liên tục. Bài báo cũng xây dựng MDAgent2-RUNTIME, một hệ thống đa tác nhân có khả năng triển khai tích hợp tạo mã, thực thi, đánh giá và tự sửa lỗi.

### Main Results:
MDAgent2, cùng với MD-EvalBench (bộ tiêu chuẩn đầu tiên cho việc tạo mã và Hỏi & Đáp LAMMPS), đạt hiệu suất vượt trội so với nhiều baseline mạnh. Các mô hình và hệ thống này thể hiện khả năng thích ứng và khái quát hóa mạnh mẽ của các mô hình ngôn ngữ lớn trong các tác vụ mô phỏng công nghiệp. Cụ thể, MD-Instruct-8B đạt tổng điểm 74.67 trong khả năng Hỏi & Đáp, vượt qua Qwen3-8b (70.50), và MDAgent2-RUNTIME hiệu quả trong việc tăng cường khả năng tạo mã LAMMPS chính xác và có thể thực thi được.

### Conclusion & Future Works:
Công trình này chứng minh một cách có hệ thống khả năng thích ứng và khái quát hóa của các mô hình ngôn ngữ lớn trong các tác vụ mô phỏng công nghiệp, đặt nền tảng phương pháp luận cho việc tạo mã tự động trong AI cho Khoa học và các mô phỏng quy mô công nghiệp. Bài báo không đi sâu vào các hướng nghiên cứu cụ thể tiếp theo mà tập trung vào việc nhấn mạnh thành tựu hiện tại.

### Brainstorming Space:
#### 1. Publish Papers:
Nghiên cứu về việc mở rộng MDAgent2 để tự động hóa các loại mô phỏng khoa học khác ngoài động lực học phân tử, như mô phỏng vật lý chất rắn hoặc sinh học.
Phát triển các phương pháp học tăng cường tiên tiến hơn để tối ưu hóa mã được tạo ra, có thể bao gồm phản hồi từ các thử nghiệm thực tế thay vì chỉ mô phỏng.
Khám phá việc tích hợp các mô hình kiến thức miền sâu rộng hơn vào kiến trúc LLM để nâng cao khả năng lý luận và tạo mã cho các kịch bản mô phỏng phức tạp.
#### 2. Patent:
Một ứng dụng di động cho phép người dùng nhập các yêu cầu mô phỏng động lực học phân tử bằng ngôn ngữ tự nhiên và nhận về mã LAMMPS đã tạo, cùng với khả năng xem trước kết quả trên điện thoại.
Hệ thống AI tích hợp vào điện thoại thông minh có thể sử dụng dữ liệu từ cảm biến của điện thoại để gợi ý hoặc tạo các kịch bản mô phỏng MD liên quan đến các vật liệu xung quanh người dùng.
Một dịch vụ đám mây được truy cập thông qua ứng dụng điện thoại, cung cấp khả năng tạo mã LAMMPS chuyên nghiệp theo yêu cầu, chạy mô phỏng trên các cụm máy tính mạnh mẽ và gửi kết quả phân tích về điện thoại.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.02075](https://huggingface.co/papers/2601.02075) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.02075](https://arxiv.org/abs/2601.02075) |
| PDF Download | [https://arxiv.org/pdf/2601.02075.pdf](https://arxiv.org/pdf/2601.02075.pdf) |
| Github Repository | N/A |

--- 

## 10. E-GRPO: High Entropy Steps Drive Effective Reinforcement Learning for Flow Models

**Tác giả:** Shengjun Zhang, Zhang Zhang, Chensheng Dai, Yueqi Duan

**Xuất bản lúc:** 2026-01-01

**Tag:** Reinforcement Learning, Flow Models, SDE, GRPO, Entropy-aware, Generative Models
### Main Problem:
Các phương pháp học tăng cường hiện có dựa trên GRPO để tối ưu hóa mô hình dòng chảy (flow models) gặp phải tín hiệu phần thưởng thưa thớt và mơ hồ khi tối ưu hóa qua nhiều bước khử nhiễu. Điều này cản trở sự căn chỉnh hiệu quả với sở thích của con người, đặc biệt là do các bước có entropy thấp tạo ra kết quả không phân biệt, trong khi chỉ các bước có entropy cao mới đóng góp đáng kể vào động lực huấn luyện.

### Main Idea:
Bài báo đề xuất E-GRPO (Entropy-aware Group Relative Policy Optimization) để giải quyết vấn đề trên. Ý tưởng chính là tăng entropy của các bước lấy mẫu SDE bằng cách hợp nhất các bước có entropy thấp liên tiếp thành một bước SDE có entropy cao duy nhất, trong khi áp dụng lấy mẫu ODE cho các bước còn lại. Điều này giúp mở rộng khả năng khám phá có ý nghĩa và loại bỏ sự mơ hồ trong việc phân bổ phần thưởng. Hơn nữa, E-GRPO giới thiệu lợi thế nhóm được chuẩn hóa đa bước (multi-step group normalized advantage), tính toán lợi thế tương đối trong nhóm cho các mẫu chia sẻ cùng một bước khử nhiễu SDE đã hợp nhất.

### Main Results:
Các thí nghiệm trên cả cài đặt phần thưởng đơn lẻ và đa phần thưởng, cũng như đánh giá trên các ma trận trong và ngoài miền, đã chứng minh tính hiệu quả và hiệu suất của E-GRPO. Cụ thể, E-GRPO đã vượt trội hơn các phương pháp trước đây một cách nhất quán, xác nhận tính hiệu quả và mạnh mẽ của việc tối ưu hóa ngẫu nhiên được hướng dẫn bởi entropy. Phân tích dựa trên entropy cho thấy việc tối ưu hóa độc quyền ở các bước có entropy cao mang lại sự căn chỉnh hiệu quả.

### Conclusion & Future Works:
E-GRPO cung cấp một phân tích toàn diện dựa trên entropy về các bước khử nhiễu trong quá trình huấn luyện GRPO, cho thấy sự căn chỉnh hiệu quả có thể đạt được bằng cách tối ưu hóa riêng các bước có entropy cao. Phương pháp này mở rộng khả năng khám phá có ý nghĩa và loại bỏ sự mơ hồ trong việc phân bổ phần thưởng bằng cách hợp nhất các bước có entropy thấp thành một bước SDE có entropy cao. Các thử nghiệm rộng rãi xác nhận E-GRPO liên tục vượt trội hơn các phương pháp trước đây. Bài báo không đề cập cụ thể đến hướng nghiên cứu trong tương lai, nhưng mở ra tiềm năng cho các chiến lược tối ưu hóa ngẫu nhiên được hướng dẫn bởi entropy trong các mô hình tạo nội dung.

### Brainstorming Space:
#### 1. Publish Papers:
- Nghiên cứu chiến lược hợp nhất bước SDE thích ứng dựa trên phản hồi phần thưởng theo thời gian thực để tối ưu hóa hiệu suất E-GRPO trong các môi trường động.
- Mở rộng ứng dụng của E-GRPO sang các mô hình tạo sinh khác như Diffusion Models cho các tác vụ tạo hình ảnh có điều kiện và không điều kiện.
- Phát triển một khuôn khổ lý thuyết để định lượng số lượng và vị trí tối ưu của các bước SDE được hợp nhất cho các phân phối dữ liệu và độ phức tạp tác vụ khác nhau.
#### 2. Patent:
- Hệ thống tùy chỉnh hình ảnh trên điện thoại sử dụng E-GRPO để tạo ra các biến thể hình ảnh dựa trên sở thích người dùng, chỉ tập trung vào các chi tiết có độ biến thiên cao để tinh chỉnh hiệu quả.
- Phương pháp tối ưu hóa tạo ảnh đại diện (avatar) cá nhân trên ứng dụng di động, nơi E-GRPO tự động tinh chỉnh các đặc điểm khuôn mặt "quan trọng" (high entropy) để đạt được sự hài lòng của người dùng nhanh hơn.
- Công nghệ nén video thông minh cho điện thoại, sử dụng E-GRPO để xác định và bảo toàn các khung hình hoặc vùng có độ phức tạp cao (high entropy) trong video, giúp giảm dung lượng mà vẫn giữ được chất lượng nhận thức.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.00423](https://huggingface.co/papers/2601.00423) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.00423](https://arxiv.org/abs/2601.00423) |
| PDF Download | [https://arxiv.org/pdf/2601.00423.pdf](https://arxiv.org/pdf/2601.00423.pdf) |
| Github Repository | [https://github.com/shengjun-zhang/VisualGRPO](https://github.com/shengjun-zhang/VisualGRPO) |

--- 

## 11. EpiQAL: Benchmarking Large Language Models in Epidemiological Question Answering for Enhanced Alignment and Reasoning

**Tác giả:** Mingyang Wei, Dehai Min, Zewen Liu, Yuzhang Xie, Guanchen Wu, Carl Yang, Max S. Y. Lau, Qi He, Lu Cheng, Wei Jin

**Xuất bản lúc:** 2026-01-06

**Tag:** Benchmarking, LLMs, Epidemiological QA, NLP, Y tế công cộng, Lý luận dịch tễ học.
### Main Problem:
Các bộ dữ liệu hỏi đáp y tế hiện có chủ yếu tập trung vào kiến thức lâm sàng hoặc lý luận cấp độ bệnh nhân, bỏ qua việc đánh giá có hệ thống suy luận dịch tễ học dựa trên bằng chứng ở cấp độ quần thể. Điều này tạo ra một khoảng trống trong việc đánh giá khả năng của các mô hình ngôn ngữ lớn (LLMs) trong việc tổng hợp bằng chứng nghiên cứu để suy luận về gánh nặng bệnh tật, động lực lây truyền và hiệu quả can thiệp ở cấp độ dân số.

### Main Idea:
Bài báo giới thiệu EpiQAL, bộ dữ liệu chuẩn đoán đầu tiên cho hỏi đáp dịch tễ học trên nhiều loại bệnh khác nhau, được xây dựng từ tài liệu truy cập mở. EpiQAL bao gồm ba tập con: EpiQAL-A đánh giá khả năng nhớ lại thông tin thực tế có trong văn bản, EpiQAL-B đánh giá suy luận đa bước liên kết bằng chứng tài liệu với các nguyên tắc dịch tễ học, và EpiQAL-C đánh giá khả năng tái tạo kết luận khi phần Thảo luận bị che giấu. Quá trình xây dựng kết hợp hướng dẫn phân loại từ chuyên gia, xác minh đa mô hình và kiểm soát độ khó dựa trên truy xuất.

### Main Results:
Các thử nghiệm trên mười mô hình mở cho thấy các LLMs hiện tại có hiệu suất hạn chế trong lý luận dịch tễ học, với suy luận đa bước là thách thức lớn nhất. Thứ hạng của các mô hình thay đổi trên các tập con và quy mô mô hình không dự đoán được thành công. Kỹ thuật gợi ý Chain-of-Thought mang lại lợi ích cho suy luận đa bước nhưng cho kết quả trái chiều ở các lĩnh vực khác.

### Conclusion & Future Works:
EpiQAL cung cấp các tín hiệu chẩn đoán chi tiết về việc tìm kiếm bằng chứng, lý luận suy luận và tái tạo kết luận trong lĩnh vực dịch tễ học. Bộ dữ liệu này giúp làm rõ những hạn chế hiện tại của LLMs trong việc xử lý các nhiệm vụ lý luận phức tạp, hướng tới việc nâng cao khả năng căn chỉnh và lý luận của LLMs trong lĩnh vực y tế công cộng.

### Brainstorming Space:
#### 1. Publish Papers:
*   Phát triển các phương pháp tinh chỉnh (fine-tuning) LLMs mới hoặc kiến trúc mô hình lai (hybrid models) để cải thiện hiệu suất suy luận đa bước trên EpiQAL-B.
*   Nghiên cứu ứng dụng các kỹ thuật Retrieval-Augmented Generation (RAG) nâng cao để cải thiện khả năng thu thập bằng chứng và giảm "ảo giác" của LLMs trong các câu hỏi dịch tễ học phức tạp.
*   Phân tích sâu hơn các loại lỗi cụ thể mà LLMs mắc phải trong các tập con của EpiQAL để xác định các điểm yếu cốt lõi trong lý luận nhân quả và thống kê.
#### 2. Patent:
*   Một ứng dụng di động tích hợp LLMs được tinh chỉnh bằng EpiQAL để cung cấp thông tin sức khỏe cộng đồng đã được xác minh và giải thích rõ ràng dựa trên các nghiên cứu dịch tễ học cho người dùng.
*   Một hệ thống kiểm tra thông tin sai lệch tự động trên điện thoại thông minh, sử dụng nền tảng EpiQAL để đối chiếu các tin tức hoặc bài đăng trên mạng xã hội về dịch bệnh với bằng chứng khoa học đáng tin cậy.
*   Một tính năng trợ lý nghiên cứu dịch tễ học trên điện thoại, cho phép các chuyên gia y tế truy vấn nhanh các tài liệu khoa học và nhận tóm tắt các kết luận quan trọng từ dữ liệu trong EpiQAL.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.03471](https://huggingface.co/papers/2601.03471) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.03471](https://arxiv.org/abs/2601.03471) |
| PDF Download | [https://arxiv.org/pdf/2601.03471.pdf](https://arxiv.org/pdf/2601.03471.pdf) |
| Github Repository | N/A |

--- 

## 12. RedBench: A Universal Dataset for Comprehensive Red Teaming of Large Language Models

**Tác giả:** Quy-Anh Dang, Chris Ngo, Truong-Son Hy

**Xuất bản lúc:** 2026-01-07

**Tag:** Red Teaming, LLMs, Dataset, Vulnerability Assessment, Safety, Robustness

### Main Problem:
Các mô hình ngôn ngữ lớn (LLMs) ngày càng được tích hợp vào các ứng dụng quan trọng về an toàn, nhưng việc đảm bảo tính bền vững của chúng trước các "prompts" đối kháng là vô cùng quan trọng. Các bộ dữ liệu "red teaming" hiện có gặp phải các vấn đề như phân loại rủi ro không nhất quán, phạm vi bao phủ miền hạn chế và đánh giá lỗi thời, gây cản trở việc đánh giá lỗ hổng một cách có hệ thống. Điều này dẫn đến sự thiếu hụt một bộ dữ liệu phổ quát cung cấp phân loại rủi ro nhất quán và đánh giá toàn diện trên các miền đa dạng, cũng như việc thiếu các đánh giá hiệu suất của các LLM hiện đại dưới các bài kiểm tra "red teaming".

### Main Idea:
Nghiên cứu này giới thiệu RedBench, một bộ dữ liệu phổ quát mới được thiết kế để nâng cao "red teaming" cho LLM. RedBench tổng hợp và hài hòa 37 bộ dữ liệu hiện có từ các hội nghị và bài báo có ảnh hưởng, cung cấp một khung tiêu chuẩn để đánh giá các lỗ hổng của LLM. Bộ dữ liệu này bao gồm 29.362 mẫu trên các "prompts" tấn công và từ chối. RedBench sử dụng một phân loại tiêu chuẩn với 22 loại rủi ro và 19 miền, cho phép đánh giá nhất quán và toàn diện. Quá trình chú thích (annotation) các loại rủi ro và miền sử dụng quy trình bán tự động kết hợp hiệu quả của các LLM hiện đại với độ tin cậy của sự giám sát của con người.

### Main Results:
*   RedBench là một bộ dữ liệu phổ quát củng cố 37 bộ dữ liệu "red teaming" hiện có, cung cấp phân loại rủi ro nhất quán và bao phủ toàn diện các miền để cho phép đánh giá LLM tiêu chuẩn.
*   Bài nghiên cứu cung cấp phân tích chi tiết các loại rủi ro và miền trong các bộ dữ liệu hiện có, làm nổi bật những khoảng trống và cơ hội cho nghiên cứu "red teaming" trong tương lai.
*   Thiết lập các đường cơ sở đánh giá cho các LLM hiện đại như Qwen2.5, Llama 3.1 và Gemma2, để đánh giá tính bền vững của chúng trước các "prompts" đối kháng và thúc đẩy các nghiên cứu so sánh.
*   Bộ dữ liệu RedBench và mã đánh giá liên quan được cung cấp mã nguồn mở để thúc đẩy tính minh bạch, khả năng tái tạo và sự phát triển của cộng đồng trong lĩnh vực "red teaming" LLM.

### Conclusion & Future Works:
Những đóng góp của RedBench tạo điều kiện thuận lợi cho các so sánh mạnh mẽ, thúc đẩy nghiên cứu trong tương lai và khuyến khích sự phát triển của các LLM an toàn và đáng tin cậy để triển khai trong thế giới thực.

### Brainstorming Space:
#### 1. Publish Papers:
*   Nghiên cứu tác động của việc tinh chỉnh LLM bằng các mẫu "refusal prompts" từ RedBench để cải thiện khả năng từ chối các yêu cầu không phù hợp mà không ảnh hưởng đến các yêu cầu hợp pháp.
*   Phân tích sự tiến hóa của các lỗ hổng LLM qua các phiên bản mô hình khác nhau bằng cách sử dụng RedBench làm công cụ đánh giá nhất quán.
*   Khám phá các kỹ thuật tạo "adversarial prompts" mới dựa trên cấu trúc phân loại rủi ro và miền đa dạng của RedBench.
#### 2. Patent:
*   Hệ thống kiểm định an toàn LLM tích hợp trên điện thoại, tự động quét và phân loại các "prompts" của người dùng dựa trên phân loại rủi ro của RedBench trước khi gửi đến LLM.
*   Ứng dụng di động sử dụng bộ dữ liệu RedBench để cung cấp huấn luyện tương tác cho người dùng về cách xây dựng "prompts" an toàn và hiệu quả, giảm thiểu rủi ro từ các phản hồi không mong muốn của LLM.
*   Giải pháp phần mềm trên điện thoại di động để giám sát và báo cáo các lỗ hổng LLM theo thời gian thực, sử dụng các mẫu "attack" và "refusal" của RedBench để xác định và cảnh báo về các hành vi không an toàn.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.03699](https://huggingface.co/papers/2601.03699) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.03699](https://arxiv.org/abs/2601.03699) |
| PDF Download | [https://arxiv.org/pdf/2601.03699.pdf](https://arxiv.org/pdf/2601.03699.pdf) |
| Github Repository | [https://github.com/knoveleng/redeval](https://github.com/knoveleng/redeval) |

--- 

## 13. Why LLMs Aren't Scientists Yet: Lessons from Four Autonomous Research Attempts

**Tác giả:** Dhruv Trehan, Paras Chopra

**Xuất bản lúc:** 2026-01-06

**Tag:** LLM Agents, Autonomous Research, AI Scientist, Machine Learning, Failure Modes
### Main Problem:
Bài báo nghiên cứu khả năng của các mô hình ngôn ngữ lớn (LLM) hiện đại trong việc tự động hoàn thành quy trình nghiên cứu khoa học từ ý tưởng đến bài báo khoa học, với mức độ tự chủ cao và sự can thiệp tối thiểu của con người. Vấn đề cốt lõi là liệu LLM có thể hoạt động như các nhà khoa học độc lập hay không, đặc biệt khi các hệ thống AI-Scientist hiện có thường yêu cầu sự định nghĩa trước về quy trình làm việc hoặc các số liệu xác minh cụ thể từ con người.

### Main Idea:
Các nhà nghiên cứu đã phát triển một hệ thống gồm sáu tác tử LLM riêng biệt, mỗi tác tử phụ trách một giai đoạn trong quy trình nghiên cứu khoa học (từ tạo ý tưởng, tạo giả thuyết, lên kế hoạch thí nghiệm, đánh giá kết quả, sửa đổi, đến phác thảo bài báo). Hệ thống này chủ yếu sử dụng Gemini 2.5 Pro cho các tác tử và Claude Code để thực hiện thí nghiệm và viết bài. Mục tiêu là khám phá giới hạn của LLM mà không cần nhiều cấu trúc định sẵn hoặc đầu vào chuyên sâu từ con người, sử dụng một kho lưu trữ chung để duy trì ngữ cảnh.

### Main Results:
Trong bốn nỗ lực nghiên cứu tự động hoàn toàn, ba nỗ lực đã thất bại trong giai đoạn triển khai hoặc đánh giá. Một nỗ lực duy nhất (AS-1, trong lĩnh vực AI Safety) đã thành công và được chấp nhận tại hội nghị Agents4Science 2025, nơi hệ thống AI được yêu cầu là tác giả chính và vượt qua cả đánh giá của con người và nhiều AI.
Bài báo đã xác định sáu chế độ thất bại lặp đi lặp lại: thiên vị dữ liệu huấn luyện mặc định, sai lệch thực hiện dưới áp lực, suy giảm bộ nhớ và ngữ cảnh trong các tác vụ dài hạn, quá hưng phấn tuyên bố thành công, thiếu trí tuệ chuyên môn và gu khoa học yếu trong thiết kế thí nghiệm. Đối với nỗ lực thành công, hệ thống đạt mức độ tự chủ rất cao (trên 95% AI) trong thiết kế thí nghiệm, thực thi và viết bài, với sự can thiệp của con người chủ yếu ở giai đoạn phát triển giả thuyết ban đầu.

### Conclusion & Future Works:
Bài báo kết luận bằng việc thảo luận về bốn nguyên tắc thiết kế cho các hệ thống AI-Scientist mạnh mẽ hơn và những ý nghĩa đối với khám phá khoa học tự động. Các tác giả cũng công bố tất cả các câu lệnh, tạo tác và đầu ra để hỗ trợ nghiên cứu trong tương lai. Hướng nghiên cứu tiếp theo sẽ tập trung vào việc giải quyết sáu chế độ thất bại đã được xác định để cải thiện độ tin cậy và khả năng tự chủ của các hệ thống AI-Scientist.

### Brainstorming Space:
#### 1. Publish Papers:
1. Nghiên cứu về các chiến lược giảm thiểu thiên vị dữ liệu huấn luyện trong các hệ thống tác tử LLM tự động để cải thiện tính mới và độ chính xác của kết quả nghiên cứu.
2. Phát triển các phương pháp quản lý bộ nhớ và ngữ cảnh động cho các tác vụ nghiên cứu dài hạn, tập trung vào cơ chế truy xuất thông tin chọn lọc và tóm tắt ngữ cảnh tự động.
3. Thiết kế các chỉ số và quy trình đánh giá tự động để đo lường "gu khoa học" và ngăn chặn việc tuyên bố thành công quá sớm trong các hệ thống nghiên cứu AI tự chủ.

#### 2. Patent:
1. Hệ thống trợ lý nghiên cứu AI tự động trên điện thoại di động, cho phép người dùng nhập ý tưởng và nhận các kế hoạch thí nghiệm, mã nguồn, và bản nháp bài báo hoàn chỉnh, sử dụng các mô hình LLM được tối ưu hóa cho thiết bị di động.
2. Giao diện ứng dụng di động tích hợp cơ chế phản hồi ngữ cảnh thông minh, giúp người dùng điều chỉnh hành vi của các tác tử LLM trên điện thoại để tránh thiên vị dữ liệu huấn luyện và sai lệch thực hiện trong các dự án nghiên cứu cá nhân.
3. Hệ thống quản lý dự án nghiên cứu AI trên đám mây với ứng dụng di động, tự động theo dõi tiến độ, phát hiện các chế độ lỗi tiềm ẩn (như suy giảm bộ nhớ) và đề xuất điều chỉnh cho các tác vụ nghiên cứu dài hạn trực tiếp từ điện thoại của người dùng.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.03315](https://huggingface.co/papers/2601.03315) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.03315](https://arxiv.org/abs/2601.03315) |
| PDF Download | [https://arxiv.org/pdf/2601.03315.pdf](https://arxiv.org/pdf/2601.03315.pdf) |
| Github Repository | N/A |

--- 

## 14. ThinkRL-Edit: Thinking in Reinforcement Learning for Reasoning-Centric Image Editing

**Tác giả:** Hengjia Li, Liming Jiang, Qing Yan, Yizhi Song, Hao Kang, Zichuan Liu, Xin Lu, Boxi Wu, Deng Cai

**Xuất bản lúc:** 2026-01-06

**Tag:** Reinforcement Learning (RL), Image Editing, Reasoning, Chain-of-Thought (CoT), Vision-Language Models (VLMs), Generative Models, Decoupled Optimization.

### Main Problem:
Mặc dù các mô hình sinh ảnh đa phương thức đã có những tiến bộ nhanh chóng trong chỉnh sửa ảnh dựa trên hướng dẫn, khả năng suy luận thị giác cơ bản của chúng còn hạn chế, dẫn đến hiệu suất chưa tối ưu trên các tác vụ chỉnh sửa yêu cầu suy luận sâu. Các phương pháp Học tăng cường (RL) hiện có để cải thiện chất lượng chỉnh sửa ảnh đối mặt với ba thách thức chính: (1) khám phá suy luận bị giới hạn trong sự ngẫu nhiên của quá trình khử nhiễu, (2) tổng hợp phần thưởng bị thiên vị, và (3) phần thưởng hướng dẫn dựa trên VLM không ổn định.

### Main Idea:
Bài báo đề xuất **ThinkRL-Edit**, một khung RL tập trung vào suy luận, tách rời quá trình suy luận thị giác khỏi quá trình tổng hợp ảnh và mở rộng khám phá suy luận vượt ra ngoài khử nhiễu. Cụ thể:
1.  Giới thiệu **lấy mẫu suy luận dựa trên Chain-of-Thought (CoT)** với các giai đoạn lập kế hoạch (planning) và phản ánh (reflection) trước khi tạo ảnh trong quá trình lấy mẫu trực tuyến. Điều này buộc mô hình khám phá nhiều giả thuyết ngữ nghĩa và xác nhận tính hợp lý của chúng trước khi đưa ra kết quả thị giác.
2.  Đề xuất một **chiến lược nhóm ưu tiên chuỗi không thiên vị** trên nhiều chiều phần thưởng để tránh thất bại của việc tổng hợp phần thưởng có trọng số. Thay vì gộp phần thưởng thành một giá trị vô hướng, phương pháp này sắp xếp chung các chuỗi được lấy mẫu theo từng nhóm và chỉ cập nhật gradient từ các chuỗi tạo thành một thứ tự tổng thể nhất quán.
3.  Thay thế điểm số VLM dựa trên khoảng giá trị bằng một **danh sách kiểm tra nhị phân** để có phần thưởng chính xác hơn, ít biến động hơn và dễ hiểu hơn cho các tác vụ suy luận phức tạp. Các câu hỏi nhị phân được suy ra từ ảnh gốc và lời nhắc, VLM trả lời có/không, và số lượng "có" được dùng làm điểm căn chỉnh.
4.  Tách rời và tối ưu hóa các module suy luận, hiểu và tạo ảnh để tăng cường khả năng suy luận mà không ảnh hưởng đến chất lượng tổng hợp.

### Main Results:
Phương pháp này vượt trội đáng kể so với các công trình trước đây trong chỉnh sửa ảnh tập trung vào suy luận, tạo ra các chỉnh sửa trung thành với hướng dẫn, mạch lạc về mặt thị giác và có cơ sở ngữ nghĩa vững chắc. Các thí nghiệm cho thấy phần thưởng suy luận chi tiết (danh sách kiểm tra nhị phân) mang lại kết quả chính xác hơn, độ biến động thấp hơn và dễ giải thích hơn.

### Conclusion & Future Works:
**Conclusion:** ThinkRL-Edit là một khung RL hiệu quả cho chỉnh sửa ảnh yêu cầu suy luận, giải quyết các hạn chế của các phương pháp trước đó bằng cách tách rời suy luận và tổng hợp, sử dụng CoT để mở rộng khám phá, áp dụng chiến lược nhóm ưu tiên chuỗi không thiên vị và sử dụng danh sách kiểm tra nhị phân cho phần thưởng VLM. Điều này dẫn đến các chỉnh sửa chính xác, mạch lạc và có cơ sở ngữ nghĩa sâu sắc.
**Future Works:** Bài báo không đề cập cụ thể đến các hướng nghiên cứu trong tương lai trong phần văn bản được trích xuất.

### Brainstorming Space:
#### 1. Publish Papers:
*   Mở rộng khung suy luận CoT để tích hợp phản hồi đa lượt hoặc tương tác từ người dùng, cho phép các kịch bản chỉnh sửa phức tạp hơn và điều chỉnh dựa trên ngữ cảnh.
*   Nghiên cứu ứng dụng phương pháp tách rời suy luận-tạo ảnh này cho các tác vụ đa phương thức khác như chỉnh sửa video hoặc tạo cảnh 3D có suy luận không gian.
*   Khám phá các kiến trúc khác cho module suy luận, có thể tích hợp suy luận biểu tượng tiên tiến hơn hoặc đồ thị tri thức để tăng cường khả năng hiểu ngữ nghĩa.

#### 2. Patent:
*   Hệ thống chỉnh sửa hình ảnh trên thiết bị di động sử dụng học tăng cường và mô hình tư duy chuỗi suy luận để thực hiện các chỉnh sửa hình ảnh phức tạp dựa trên văn bản trên điện thoại.
*   Phương pháp đánh giá độ chính xác của chỉnh sửa hình ảnh trên thiết bị di động thông qua danh sách kiểm tra nhị phân được sinh ra bởi VLM, giúp cung cấp phần thưởng ổn định và chính xác cho các tác vụ suy luận trên điện thoại.
*   Công nghệ tối ưu hóa thuật toán học tăng cường cho chỉnh sửa ảnh di động, tách rời quá trình suy luận và tạo ảnh, cho phép thiết bị điện thoại khám phá nhiều giả thuyết ngữ nghĩa trước khi thực hiện chỉnh sửa hình ảnh cuối cùng.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.03467](https://huggingface.co/papers/2601.03467) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.03467](https://arxiv.org/abs/2601.03467) |
| PDF Download | [https://arxiv.org/pdf/2601.03467.pdf](https://arxiv.org/pdf/2601.03467.pdf) |
| Github Repository | N/A |

--- 

## 15. Enhancing Linguistic Competence of Language Models through Pre-training with Language Learning Tasks

**Tác giả:** Atsuki Yamaguchi, Maggie Mi, Nikolaos Aletras

**Xuất bản lúc:** 2026-01-06

**Tag:** Language Models, Pre-training, Linguistic Competence, Language Learning Tasks, L2T, Deep Learning.

### Main Problem:
Các mô hình ngôn ngữ (LMs) hiện tại được huấn luyện trước bằng cách dự đoán token tiếp theo trên các tập dữ liệu văn bản thô. Mặc dù phương pháp này hiệu quả trong việc giúp các LM học được kiến thức thế giới và khả năng suy luận, nó không trực tiếp tối ưu hóa năng lực ngôn ngữ, tức là khả năng hiểu và diễn giải các hiện tượng ngôn ngữ đa dạng. Điều này khiến các LM thường chỉ bắt chước các mẫu bề mặt mà không thực sự nắm bắt được cấu trúc ngôn ngữ cơ bản.

### Main Idea:
Bài báo đề xuất L2T (Language Learning Tasks), một framework huấn luyện trước tích hợp các nhiệm vụ học ngôn ngữ song song với việc dự đoán token tiêu chuẩn. L2T được lấy cảm hứng từ quá trình tiếp thu ngôn ngữ ở con người, chuyển đổi văn bản thô thành các cặp input-output có cấu trúc để cung cấp sự kích thích ngôn ngữ rõ ràng. Framework này bao gồm 14 nhiệm vụ học ngôn ngữ đa dạng ở bốn cấp độ ngữ pháp (ký tự, từ, câu và diễn ngôn), được thiết kế để khuyến khích sự phát triển các biểu diễn có cấu trúc vượt ra ngoài sự xuất hiện đồng thời bề mặt. Bằng cách huấn luyện LMs trên hỗn hợp dữ liệu L2T và văn bản thô, mục tiêu là cải thiện hiệu suất tổng thể của mô hình trên các benchmark năng lực ngôn ngữ và tăng tốc quá trình này, trong khi vẫn duy trì hiệu suất cạnh tranh trên các nhiệm vụ suy luận chung.

### Main Results:
- Framework L2T cải thiện đáng kể năng lực ngôn ngữ, đạt mức tăng trung bình 2.8% và lên đến 11.3% trên một số hiện tượng ngôn ngữ cụ thể khi được đánh giá bằng benchmark BLiMP.
- Các mô hình được huấn luyện bằng L2T vượt trội hơn các baseline chỉ dùng văn bản thô trong cả hai kịch bản dữ liệu (Disjoint và Shared) và ở cả hai quy mô mô hình (500M và 1B tham số). Điều này cho thấy rằng năng lực ngôn ngữ phụ thuộc vào sự đa dạng của các tín hiệu được áp dụng trong quá trình huấn luyện chứ không chỉ riêng khối lượng dữ liệu.
- Các nhiệm vụ L2T đặc biệt hiệu quả trong việc cải thiện các hiệu ứng Đảo (Island effects) với mức tăng từ 6.9 đến 11.3 điểm.
- L2T duy trì hiệu suất cạnh tranh trên các benchmark suy luận chung (bao gồm Reading Comprehension, Commonsense Reasoning và Language Modeling), cho thấy các nhiệm vụ học ngôn ngữ bổ sung không làm suy giảm khả năng tổng quát của mô hình.

### Conclusion & Future Works:
Kết luận chính là việc tích hợp các nhiệm vụ học ngôn ngữ trong quá trình huấn luyện trước là một phương pháp hiệu quả để nâng cao năng lực ngôn ngữ của các mô hình mà vẫn duy trì các khả năng tổng quát của chúng. Bài báo nhấn mạnh rằng sự đa dạng của các tín hiệu huấn luyện là yếu tố quan trọng đối với năng lực ngôn ngữ. Đối với các công việc trong tương lai, các tác giả gợi ý rằng các hiện tượng ngôn ngữ phức tạp hơn, như Filler-Gap dependencies, có thể đòi hỏi các mục tiêu cấp độ diễn ngôn có mục tiêu cụ thể hơn để đạt được sự cải thiện đáng kể.

### Brainstorming Space:
#### 1. Publish Papers:
- Nghiên cứu tác động của việc điều chỉnh cường độ và tần suất của các nhiệm vụ học ngôn ngữ trong framework L2T để tìm ra cấu hình tối ưu cho từng cấp độ năng lực ngôn ngữ.
- Mở rộng framework L2T để hỗ trợ các ngôn ngữ ít tài nguyên hoặc ngôn ngữ có cấu trúc ngữ pháp phức tạp hơn, đánh giá hiệu quả của nó trong môi trường đa ngôn ngữ.
- Khám phá sự kết hợp của L2T với các kỹ thuật huấn luyện trước khác như instruction tuning để tạo ra các mô hình ngôn ngữ vừa có năng lực ngôn ngữ sâu sắc vừa có khả năng tuân thủ hướng dẫn tốt.

#### 2. Patent:
- Một ứng dụng di động tích hợp L2T để phân tích tin nhắn hoặc văn bản người dùng nhập vào, cung cấp gợi ý tức thì để cải thiện ngữ pháp và cấu trúc câu, giúp người dùng học và cải thiện kỹ năng viết tiếng Anh.
- Một tính năng "Kiểm tra Ngữ pháp Thông minh" trên điện thoại thông minh, sử dụng công nghệ L2T để phát hiện và sửa các lỗi ngữ pháp phức tạp trong email hoặc tài liệu, đồng thời giải thích lý do sửa chữa cho người dùng.
- Một công cụ luyện nói và học từ vựng trên điện thoại dựa trên L2T, tự động tạo các bài tập điền vào chỗ trống hoặc sắp xếp lại từ từ các đoạn văn bản tin tức hoặc sách người dùng quan tâm, tập trung vào việc củng cố cấu trúc ngôn ngữ.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.03448](https://huggingface.co/papers/2601.03448) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.03448](https://arxiv.org/abs/2601.03448) |
| PDF Download | [https://arxiv.org/pdf/2601.03448.pdf](https://arxiv.org/pdf/2601.03448.pdf) |
| Github Repository | [https://github.com/gucci-j/l2t](https://github.com/gucci-j/l2t) |

--- 

## 16. Pearmut: Human Evaluation of Translation Made Trivial

**Tác giả:** Vilém Zouhar, Tom Kocmi

**Xuất bản lúc:** 2026-01-06

**Tag:** Human Evaluation, Machine Translation, Multilingual NLP, Annotation Platform, Pearmut, Evaluation Tools

### Main Problem:
Vấn đề cốt lõi mà bài báo đề cập là việc đánh giá con người (human evaluation) là tiêu chuẩn vàng trong Xử lý Ngôn ngữ Tự nhiên đa ngôn ngữ (multilingual NLP), đặc biệt là dịch máy, nhưng thường bị bỏ qua hoặc thay thế bằng các chỉ số tự động. Lý do là các công cụ hiện có rất phức tạp, tốn thời gian thiết lập, đòi hỏi nhiều kỹ thuật và chi phí vận hành, cũng như thiếu tính nhất quán và khả năng tái lập các giao thức chú thích. Điều này dẫn đến các kết luận sai lệch và làm chậm tiến trình phát triển mô hình.

### Main Idea:
Bài báo giới thiệu Pearmut, một nền tảng nhẹ nhưng đầy đủ tính năng, giúp việc thiết lập và chạy đánh giá con người từ đầu đến cuối trở nên dễ dàng như đánh giá tự động. Pearmut loại bỏ các rào cản phổ biến và hỗ trợ đánh giá các tác vụ đa ngôn ngữ, tập trung đặc biệt vào dịch máy. Nền tảng này triển khai các giao thức đánh giá tiêu chuẩn như DA, ESA, MQM, đồng thời có thể mở rộng để tạo mẫu các giao thức mới. Nó bao gồm các tính năng như ngữ cảnh cấp tài liệu, đánh giá tuyệt đối và đối chiếu, kiểm tra sự chú ý (attention checks), chú thích trước ESAAI và các chiến lược gán nhiệm vụ dựa trên học tĩnh hoặc học chủ động. Pearmut nhằm mục đích biến đánh giá con người trở thành một thành phần thực tế, thường xuyên trong quá trình phát triển và chẩn đoán mô hình.

### Main Results:
1.  **Dễ thiết lập và sử dụng:** Nghiên cứu điển hình với các nhà nghiên cứu cho thấy Pearmut có thời gian thiết lập ngắn nhất (trung bình 11 phút) và nhận được điểm cao nhất về mức độ dễ sử dụng (9.0), sự phù hợp cho dịch thuật (9.0) và ý định sử dụng trong tương lai (9.0) so với các công cụ cạnh tranh.
2.  **Hiệu quả và chất lượng đánh giá:** Nghiên cứu điển hình với người chú thích chỉ ra rằng Pearmut cho phép chú thích nhanh hơn (124.38 giây/mục) so với Appraise (144.86 giây/mục), đồng thời duy trì chất lượng đánh giá tương đương (thể hiện qua sự phân tách điểm mô hình và số lượng lỗi được chú thích). Người chú thích cũng bày tỏ sự hài lòng cao hơn đáng kể với Pearmut về tốc độ, độ rõ ràng và ít nỗ lực hơn.
3.  **Tương thích với quy trình làm việc hiện đại:** Một tác nhân mã hóa LLM có thể tự động viết script thiết lập cho Pearmut và LabelStudio, chứng tỏ khả năng tích hợp tốt của Pearmut với các quy trình kỹ thuật hiện đại.

### Conclusion & Future Works:
Pearmut chuyển đổi đánh giá con người từ một nỗ lực không thường xuyên thành một thành phần thiết yếu và thường xuyên của quá trình phát triển và chẩn đoán mô hình. Nó loại bỏ các rào cản phổ biến, cung cấp một nền tảng hiệu quả, dễ sử dụng, chuyên biệt cho đánh giá dịch máy và các tác vụ đa ngôn ngữ. Các hướng nghiên cứu tiếp theo có thể bao gồm việc mở rộng các giao thức đánh giá mới, cải thiện các chiến lược gán nhiệm vụ và tích hợp sâu hơn các công cụ phân tích thống kê để thúc đẩy các thực hành khoa học tiêu chuẩn hóa.

### Brainstorming Space:
#### 1. Publish Papers:
- Nghiên cứu so sánh chi tiết các chiến lược gán nhiệm vụ khác nhau (task-based, single-stream, dynamic) trong Pearmut về hiệu quả chi phí và độ chính xác đánh giá trên các ngôn ngữ ít tài nguyên.
- Khám phá việc tích hợp các mô hình ngôn ngữ lớn (LLMs) để tạo ra các pre-annotation cho các giao thức như ESAAI, đánh giá tác động của chúng đến tốc độ và chất lượng chú thích của con người.
- Phát triển và đánh giá một giao thức đánh giá mới trong Pearmut chuyên biệt cho các tác vụ đa phương thức (ví dụ: dịch video hoặc âm thanh) và phân tích tính khả thi của nó.
#### 2. Patent:
- Hệ thống đánh giá bản dịch di động tự động, tích hợp Pearmut để người dùng có thể thực hiện đánh giá trực tiếp trên điện thoại thông minh, bao gồm cả các tính năng như chú thích lỗi bằng cử chỉ chạm và phản hồi giọng nói.
- Công nghệ "Adaptive Annotation Stream" cho phép nền tảng đánh giá dịch thuật trên điện thoại tự động điều chỉnh độ khó và loại nhiệm vụ dựa trên hiệu suất và độ tin cậy của người chú thích theo thời gian thực để tối ưu hóa việc phân bổ tài nguyên.
- Ứng dụng di động "Multimodal Translation Quality Auditor" cho phép người dùng đánh giá chất lượng dịch thuật đa phương thức (ví dụ: văn bản, âm thanh, hình ảnh) trực tiếp trên điện thoại, sử dụng các giao thức tùy chỉnh và tính năng kiểm tra sự chú ý tích hợp để đảm bảo chất lượng dữ liệu.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.02933](https://huggingface.co/papers/2601.02933) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.02933](https://arxiv.org/abs/2601.02933) |
| PDF Download | [https://arxiv.org/pdf/2601.02933.pdf](https://arxiv.org/pdf/2601.02933.pdf) |
| Github Repository | [https://github.com/zouharvi/pearmut](https://github.com/zouharvi/pearmut) |

--- 

## 17. Gen3R: 3D Scene Generation Meets Feed-Forward Reconstruction

**Tác giả:** Jiaxin Huang, Yuanbo Yang, Bangbang Yang, Lin Ma, Yuewen Ma, Yiyi Liao

**Xuất bản lúc:** 2026-01-07

**Tag:** 3D Scene Generation, Feed-Forward Reconstruction, Video Diffusion, Geometric Priors, Latent Space, VGGT.
### Main Problem:
Các phương pháp tạo cảnh 3D hiện tại thường gặp phải các hạn chế như cấu trúc hình học kém, chi phí tối ưu hóa cao, hoặc khó khăn trong việc học các biểu diễn hình học do sự khan hiếm dữ liệu 3D quy mô lớn. Việc chỉ dựa vào tín hiệu 2D thường dẫn đến hình học dưới chuẩn và chất lượng tạo ra bị hạn chế. Các mô hình Diffusion video gần đây gặp thách thức trong việc học một không gian latent tập trung vào hình học.

### Main Idea:
Gen3R là một phương pháp bắc cầu các priors mạnh mẽ của các mô hình tái tạo 3D nền tảng và các mô hình Diffusion video để tạo cảnh 3D. Ý tưởng chính là tái sử dụng mô hình tái tạo VGGT để tạo ra các latent hình học bằng cách huấn luyện một bộ adapter trên các token của nó. Các latent hình học này được chuẩn hóa để căn chỉnh với các latent hình ảnh (appearance latents) của các mô hình Diffusion video đã được huấn luyện trước. Bằng cách tạo ra đồng thời các latent được tách rời nhưng căn chỉnh này, Gen3R sản xuất cả video RGB và hình học 3D tương ứng, bao gồm tư thế camera, bản đồ độ sâu và đám mây điểm toàn cục.

### Main Results:
*   Đạt được kết quả tiên tiến (state-of-the-art) trong tạo cảnh 3D có điều kiện từ một hoặc nhiều hình ảnh.
*   Có khả năng tạo ra các video RGB nhất quán về mặt thời gian và các đám mây điểm 3D được căn chỉnh toàn cục.
*   Phương pháp này có thể nâng cao tính mạnh mẽ của quá trình tái tạo bằng cách tận dụng các priors tạo sinh, chứng minh lợi ích tương hỗ của việc kết nối chặt chẽ các mô hình tái tạo và tạo sinh.
*   Khuôn khổ hỗ trợ điều kiện linh hoạt, cho phép tạo ra từ một hoặc nhiều góc nhìn đầu vào, có hoặc không có gợi ý camera, cũng như tái tạo cảnh feed-forward trong một mô hình thống nhất.

### Conclusion & Future Works:
Gen3R trình bày một khuôn khổ hiệu quả và mạnh mẽ cho việc tạo cảnh 3D chất lượng cao với hình học nhất quán bằng cách kết hợp các priors hình học phong phú từ mô hình tái tạo nền tảng với priors RGB mạnh mẽ của mô hình Diffusion video. Phương pháp này mở ra tiềm năng cho việc tạo ra môi trường ảo quy mô lớn và cung cấp công cụ mới cho thiết kế nội dung sáng tạo.

### Brainstorming Space:
#### 1. Publish Papers:
*   Nghiên cứu việc tích hợp các mô hình tái tạo 3D nền tảng khác hoặc biểu diễn 3D chi tiết hơn (ví dụ: lưới đa giác) vào khuôn khổ Gen3R để mở rộng khả năng tạo hình học.
*   Khám phá các phương pháp mới để tăng cường khả năng kiểm soát ngữ nghĩa hoặc tương tác của người dùng trong quá trình tạo cảnh 3D, ví dụ thông qua hướng dẫn bằng văn bản hoặc bản phác thảo.
*   Phân tích tác động của việc căn chỉnh các latent space khác nhau và các hàm mất mát khác đối với tính nhất quán đa góc nhìn và chất lượng hình học của cảnh được tạo ra.

#### 2. Patent:
*   Một ứng dụng di động cho phép người dùng chụp một vài ảnh hoặc một đoạn video ngắn bằng điện thoại và tự động tạo ra một mô hình 3D hoàn chỉnh của cảnh, sau đó có thể được sử dụng trong các ứng dụng thực tế tăng cường hoặc in 3D.
*   Hệ thống camera điện thoại thông minh tích hợp công nghệ Gen3R để cung cấp tính năng "xem trước 3D" cho phép người dùng đặt các vật thể ảo vào một môi trường thực được tái tạo 3D ngay lập tức, phục vụ cho mục đích thiết kế nội thất hoặc mua sắm ảo.
*   Công nghệ tích hợp vào ứng dụng bản đồ hoặc du lịch di động, cho phép người dùng tạo ra các chuyến tham quan 3D tương tác của một khu vực từ bộ sưu tập ảnh cá nhân, cung cấp thông tin độ sâu và vị trí camera chính xác trên điện thoại.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.04090](https://huggingface.co/papers/2601.04090) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.04090](https://arxiv.org/abs/2601.04090) |
| PDF Download | [https://arxiv.org/pdf/2601.04090.pdf](https://arxiv.org/pdf/2601.04090.pdf) |
| Github Repository | [https://github.com/JaceyHuang/Gen3R](https://github.com/JaceyHuang/Gen3R) |

--- 

## 18. ResTok: Learning Hierarchical Residuals in 1D Visual Tokenizers for Autoregressive Image Generation

**Tác giả:** Xu Zhang, Cheng Da, Huan Yang, Kun Gai, Ming Lu, Zhan Ma

**Xuất bản lúc:** 2026-01-07

**Tag:** Autoregressive Image Generation, Visual Tokenization, Hierarchical Models, Residual Networks, Vision Transformer (ViT)

### Main Problem:
Các tokenizer hình ảnh 1D hiện có cho mô hình sinh tự hồi quy (AR) chủ yếu tuân theo các nguyên tắc mô hình ngôn ngữ. Điều này dẫn đến các token tiềm ẩn có cấu trúc đơn cấp và xử lý dữ liệu thị giác như các luồng token phẳng tuần tự, bỏ qua các thuộc tính quan trọng của thị giác như thiết kế mạng phân cấp và phần dư. Hậu quả là thiếu khả năng kết hợp tính năng đa cấp và tạo ra các codebook tiềm ẩn có entropy cao, gây khó khăn cho quá trình mô hình hóa AR.

### Main Idea:
Bài báo đề xuất ResidualTokenizer (ResTok), một tokenizer hình ảnh 1D được thiết kế để tích hợp các phần dư phân cấp cho cả token hình ảnh và token tiềm ẩn. Các ý tưởng chính bao gồm:
1.  **Biểu diễn phân cấp:** Tiến hành hợp nhất dần dần các token hình ảnh thành các tính năng thô hơn, cho phép các token tiềm ẩn kết hợp các tính năng đa cấp (cross-level feature fusion) để tăng cường khả năng biểu diễn.
2.  **Phần dư ngữ nghĩa:** Học các phần dư có cấu trúc ngữ nghĩa giữa các cấp bậc để ngăn chặn sự trùng lặp thông tin, từ đó tạo ra các phân phối tiềm ẩn tập trung hơn với entropy thấp, dễ dàng hơn cho mô hình AR.
3.  **Tăng tốc quá trình sinh:** Giới thiệu một bộ tạo AR phân cấp (HAR) có khả năng dự đoán toàn bộ một cấp độ token tiềm ẩn cùng một lúc, thay vì sinh từng token một, giúp giảm đáng kể số bước lấy mẫu.

### Main Results:
ResTok chứng minh sự cải thiện đáng kể trong quá trình sinh ảnh AR:
-   Đạt được hiệu suất gFID là 2.34 trên tập dữ liệu ImageNet-256x256.
-   Chỉ yêu cầu 9 bước lấy mẫu để tạo ảnh, nhờ cơ chế sinh ảnh phân cấp.
-   Các liên kết giữa các cấp độ (ví dụ: token tiềm ẩn thô hơn khớp với token hình ảnh cấp cao, token tiềm ẩn tinh tế hơn nắm bắt chi tiết phần dư cấp thấp) tự động xuất hiện mà không cần ràng buộc rõ ràng.

### Conclusion & Future Works:
Việc khôi phục các ưu tiên phần dư phân cấp trong quá trình token hóa hình ảnh cải thiện đáng kể quá trình tạo ảnh AR chất lượng cao và hiệu quả. Bài báo nhấn mạnh tầm quan trọng của các thiết kế mạng phân cấp và phần dư trong việc nâng cao khả năng biểu diễn thị giác. Hướng nghiên cứu tiếp theo có thể bao gồm việc khám phá các cơ chế hợp nhất và thiết kế phần dư tiên tiến hơn, cũng như áp dụng phương pháp này cho các nhiệm vụ đa phương thức khác ngoài việc tạo ảnh.

### Brainstorming Space:

#### 1. Publish Papers:
1.  Nghiên cứu tác động của các chiến lược hợp nhất và upsampling khác nhau trong kiến trúc tokenizer phân cấp đối với hiệu suất và chất lượng ảnh được tạo.
2.  Khám phá việc tích hợp các cơ chế phần dư ngữ nghĩa tự thích ứng, cho phép mô hình điều chỉnh mức độ chi tiết và trừu tượng hóa tùy thuộc vào nội dung ảnh.
3.  Áp dụng tokenizer phân cấp và bộ tạo HAR cho việc tạo ra chuỗi video hoặc mô hình 3D, nơi cấu trúc phân cấp có thể mang lại lợi ích về hiệu quả và chất lượng.

#### 2. Patent:
1.  Hệ thống camera điện thoại thông minh tích hợp ResTok để tối ưu hóa việc nén và xử lý hình ảnh thời gian thực, cho phép chụp ảnh chất lượng cao với dung lượng lưu trữ thấp và tốc độ xử lý nhanh.
2.  Công nghệ hiển thị và chỉnh sửa ảnh trên thiết bị di động sử dụng tokenizer phần dư phân cấp để tái tạo ảnh với các mức độ chi tiết khác nhau, cho phép người dùng chỉnh sửa ảnh theo từng cấp độ từ tổng thể đến chi tiết nhỏ một cách mượt mà.
3.  Ứng dụng trợ lý ảo di động có khả năng tạo hình ảnh dựa trên mô tả văn bản, sử dụng kiến trúc ResTok và bộ tạo HAR để sinh ra các hình ảnh phức tạp nhanh chóng và với độ chính xác cao trên phần cứng điện thoại.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.03955](https://huggingface.co/papers/2601.03955) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.03955](https://arxiv.org/abs/2601.03955) |
| PDF Download | [https://arxiv.org/pdf/2601.03955.pdf](https://arxiv.org/pdf/2601.03955.pdf) |
| Github Repository | N/A |

--- 

## 19. MAGMA: A Multi-Graph based Agentic Memory Architecture for AI Agents

**Tác giả:** Dongming Jiang, Yi Li, Guanpeng Li, Bingzhe Li

**Xuất bản lúc:** 2026-01-06

**Tag:** MAG, Multi-Graph, Agentic Memory, LLMs, Long-Horizon Reasoning, Retrieval, Causal Reasoning

### Main Problem:
Large Language Models (LLMs) gặp khó khăn trong việc duy trì và suy luận trên ngữ cảnh dài hạn do cửa sổ chú ý hữu hạn và thiếu cơ chế bộ nhớ có cấu trúc bền vững. Các hệ thống Memory-Augmented Generation (MAG) hiện có chủ yếu dựa vào sự tương đồng ngữ nghĩa trên các kho bộ nhớ đơn nhất, làm vướng mắc thông tin thời gian, nhân quả và thực thể, dẫn đến khả năng diễn giải kém, sự không khớp giữa ý định truy vấn và bằng chứng được truy xuất, cùng độ chính xác suy luận dưới mức tối ưu, đặc biệt là trong các tác vụ suy luận phức tạp yêu cầu hiểu biết về mối quan hệ "tại sao".

### Main Idea:
Bài báo đề xuất MAGMA, một kiến trúc bộ nhớ tác tử dựa trên đa đồ thị, để giải quyết các hạn chế của MAG hiện có. MAGMA biểu diễn mỗi mục bộ nhớ qua bốn đồ thị quan hệ trực giao (ngữ nghĩa, thời gian, nhân quả và thực thể). Việc truy xuất được xây dựng như một quá trình duyệt đồ thị có hướng chính sách, cho phép lựa chọn thích ứng với truy vấn và xây dựng ngữ cảnh có cấu trúc. Kiến trúc này tách biệt biểu diễn bộ nhớ khỏi logic truy xuất, cung cấp các đường suy luận minh bạch và kiểm soát chi tiết quá trình truy xuất thông qua một cơ chế truy vấn phân cấp, nhận biết ý định. MAGMA cũng sử dụng cơ chế tiến hóa bộ nhớ luồng kép để đảm bảo phản hồi nhanh chóng trong khi củng cố cấu trúc quan hệ.

### Main Results:
MAGMA nhất quán vượt trội so với các hệ thống bộ nhớ tác tử hiện đại trong các tác vụ suy luận dài hạn trên các bộ điểm chuẩn Lo-CoMo và LongMemEval. Hệ thống giảm độ trễ truy xuất và tiêu thụ token so với các hệ thống trước đó. MAGMA cung cấp đường suy luận minh bạch và kiểm soát chi tiết hơn trong việc lựa chọn bộ nhớ, cải thiện sự khớp nối giữa ý định truy vấn và bằng chứng được truy xuất.

### Conclusion & Future Works:
MAGMA cung cấp một nền tảng có nguyên tắc và có thể mở rộng cho bộ nhớ tác tử bằng cách mô hình hóa cấu trúc quan hệ không đồng nhất trong trải nghiệm của tác tử. Bằng cách sử dụng các đồ thị quan hệ trực giao và cơ chế truy xuất thích ứng, MAGMA cải thiện cả sự nhất quán dài hạn và khả năng diễn giải trong suy luận của AI Agents. Hướng nghiên cứu tiếp theo có thể tập trung vào việc khám phá sâu hơn cách tối ưu hóa các thành phần này hoặc tích hợp thêm các loại quan hệ phức tạp khác để nâng cao khả năng của hệ thống.

### Brainstorming Space:
#### 1. Publish Papers:
Nghiên cứu cơ chế tự động học và tạo ra các loại quan hệ đồ thị mới ngoài bốn loại đã đề xuất để nắm bắt các phụ thuộc phức tạp hơn.
Khám phá việc tích hợp MAGMA với các phương pháp học tăng cường để tối ưu hóa chính sách duyệt đồ thị trong thời gian thực dựa trên phản hồi của tác tử.
Phát triển một framework đánh giá toàn diện để định lượng khả năng diễn giải và khả năng giải thích của các hệ thống bộ nhớ tác tử dựa trên đồ thị.

#### 2. Patent:
Hệ thống bộ nhớ thông minh cho thiết bị di động có khả năng tự động tổ chức các tương tác của người dùng (tin nhắn, cuộc gọi, lịch sử duyệt web) thành các đồ thị ngữ nghĩa, thời gian, nhân quả và thực thể để truy xuất thông tin cá nhân hóa.
Ứng dụng điện thoại thông minh với trợ lý ảo sử dụng kiến trúc bộ nhớ đa đồ thị để cung cấp các gợi ý và câu trả lời chính xác hơn dựa trên ngữ cảnh lịch sử người dùng và các mối quan hệ ẩn.
Phương pháp tối ưu hóa tài nguyên cho thiết bị di động bằng cách sử dụng chính sách duyệt đồ thị thích ứng để truy xuất bộ nhớ hiệu quả, giảm độ trễ và tiêu thụ năng lượng khi xử lý các truy vấn phức tạp của người dùng.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.03236](https://huggingface.co/papers/2601.03236) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.03236](https://arxiv.org/abs/2601.03236) |
| PDF Download | [https://arxiv.org/pdf/2601.03236.pdf](https://arxiv.org/pdf/2601.03236.pdf) |
| Github Repository | N/A |

--- 

## 20. RGS-SLAM: Robust Gaussian Splatting SLAM with One-Shot Dense Initialization

**Tác giả:** Wei-Tse Cheng, Yen-Jen Chiou, Yuan-Fu Yang

**Xuất bản lúc:** 2025-12-28

**Tag:** SLAM, 3D Gaussian Splatting, Real-time Mapping, Dense Initialization, View Synthesis, DINOv3

### Main Problem:
Các framework SLAM dựa trên 3D Gaussian Splatting hiện tại thường dựa vào quá trình densification lặp đi lặp lại dựa trên sai số (residual-driven densification). Điều này dẫn đến các mục tiêu không ổn định, hội tụ không vững và độ nhạy cảm với các khu vực giàu texture hoặc lộn xộn do sự bao phủ chậm trễ và hình học không đồng đều.

### Main Idea:
RGS-SLAM đề xuất thay thế giai đoạn densification truyền thống bằng một phương pháp khởi tạo Gaussian "một lần chụp" (one-shot) dựa trên các tương ứng mật độ cao, không cần huấn luyện. Hệ thống sử dụng các descriptor DINOv3 được tinh chỉnh qua bộ phân loại inlier nhận biết độ tin cậy để tạo ra các tương ứng đa khung nhìn dày đặc. Các tương ứng này sau đó được tam giác hóa để tạo ra một tập hợp các hạt Gaussian phân bố tốt và nhận biết cấu trúc trước khi tối ưu hóa. Cách tiếp cận này giúp ổn định quá trình lập bản đồ sớm, tăng tốc độ hội tụ và cho phép tối ưu hóa các tham số Gaussian (mean, covariance, opacity, color) với cấu trúc bản đồ cố định.

### Main Results:
- Tăng tốc độ hội tụ khoảng 20%.
- Đạt độ trung thực kết xuất cao hơn trong các cảnh giàu texture và lộn xộn.
- Đạt được độ chính xác định vị và tái tạo cạnh tranh hoặc vượt trội so với các hệ thống SLAM dựa trên Gaussian và điểm tiên tiến nhất.
- Duy trì hiệu suất lập bản đồ thời gian thực lên tới 925 FPS.
- Giảm độ trôi (drift) hơn 30% thông qua các tương ứng có trọng số độ tin cậy.
- Đạt thông lượng kết xuất cao hơn 20%.
- Cải thiện độ chính xác và hoàn chỉnh tái tạo khoảng 20%.
- Được đánh giá trên bộ dữ liệu TUM RGB-D và Replica.

### Conclusion & Future Works:
RGS-SLAM cung cấp một phương pháp mạnh mẽ và hiệu quả cho SLAM dựa trên Gaussian Splatting bằng cách sử dụng khởi tạo mật độ cao một lần chụp, cải thiện đáng kể độ ổn định, tốc độ và chất lượng tái tạo so với các phương pháp dựa trên densification. Phần trích dẫn không thảo luận về các công việc tương lai cụ thể.

### Brainstorming Space:
#### 1. Publish Papers:
- Nghiên cứu tích hợp khởi tạo mật độ cao của RGS-SLAM với các mô hình NeRF thời gian thực để cải thiện sự ổn định và tốc độ hội tụ trong quá trình học tập.
- Phát triển một thuật toán lựa chọn keyframe thích ứng cho RGS-SLAM, sử dụng thông tin từ entropy hình học hoặc độ bao phủ Gaussian để tối ưu hóa hiệu quả lập bản đồ.
- Khám phá việc mở rộng RGS-SLAM cho môi trường đa cảm biến (ví dụ: kết hợp với LiDAR hoặc IMU) để nâng cao độ chính xác và mạnh mẽ trong các điều kiện ánh sáng hoặc texture kém.
#### 2. Patent:
- Hệ thống định vị và lập bản đồ 3D cho thiết bị di động, sử dụng khởi tạo Gaussian mật độ cao một lần chụp để tạo bản đồ môi trường nhanh chóng và chính xác cho các ứng dụng thực tế tăng cường trên điện thoại.
- Công nghệ camera điện thoại thông minh cho phép quét và tái tạo mô hình 3D của vật thể hoặc không gian ngay lập tức, sử dụng thuật toán tam giác hóa tương ứng dày đặc để tăng tốc độ khởi tạo.
- Phương pháp điều hướng trong nhà dựa trên điện thoại di động, tự động xây dựng bản đồ 3D chất lượng cao từ dữ liệu camera bằng cách khởi tạo Gaussian từ các tương ứng multi-view, giảm thiểu thời gian chờ và cải thiện trải nghiệm người dùng.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.00705](https://huggingface.co/papers/2601.00705) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.00705](https://arxiv.org/abs/2601.00705) |
| PDF Download | [https://arxiv.org/pdf/2601.00705.pdf](https://arxiv.org/pdf/2601.00705.pdf) |
| Github Repository | N/A |

