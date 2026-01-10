# 🤗 Daily Hugging Face Paper Digest - 2026-01-09

Báo cáo được tạo tự động vào lúc 2026-01-10 13:28:12 bằng mô hình `gemini-2.5-flash`.

## 📰 Summary of Papers

--- 

## 1. GDPO: Group reward-Decoupled Normalization Policy Optimization for Multi-reward RL Optimization

**Tác giả:** Shih-Yang Liu, Xin Dong, Ximing Lu, Shizhe Diao, Peter Belcak, Mingjie Liu, Min-Hung Chen, Hongxu Yin, Yu-Chiang Frank Wang, Kwang-Ting Cheng, Yejin Choi, Jan Kautz, Pavlo Molchanov

**Xuất bản lúc:** 2026-01-08

**Tag:** RL, Multi-reward Optimization, Policy Optimization, LLMs, Normalization, GDPO
### Main Problem:
Các mô hình ngôn ngữ lớn (LLMs) cần căn chỉnh theo nhiều sở thích đa dạng của con người, vượt ra ngoài độ chính xác. Các phương pháp tối ưu hóa RL đa phần thưởng hiện có, đặc biệt là Group Relative Policy Optimization (GRPO), khi áp dụng trực tiếp cho việc chuẩn hóa các tổ hợp phần thưởng khác nhau, có thể khiến chúng "sụp đổ" thành các giá trị ưu thế (advantage values) giống hệt nhau. Điều này làm giảm độ phân giải của tín hiệu huấn luyện, dẫn đến hội tụ dưới mức tối ưu và đôi khi là lỗi huấn luyện sớm, do mất đi sự phân biệt quan trọng giữa các chiều phần thưởng.

### Main Idea:
Bài báo giới thiệu Group reward-Decoupled Normalization Policy Optimization (GDPO), một phương pháp tối ưu hóa chính sách mới để giải quyết vấn đề sụp đổ tín hiệu phần thưởng của GRPO. GDPO thực hiện bằng cách tách rời việc chuẩn hóa từng phần thưởng riêng lẻ theo nhóm (group-wise normalization for each reward separately) trước khi tổng hợp. Điều này giúp bảo toàn trung thực hơn sự khác biệt tương đối giữa các phần thưởng, cho phép tối ưu hóa đa phần thưởng chính xác hơn và cải thiện đáng kể sự ổn định huấn luyện. Sau khi chuẩn hóa từng phần thưởng theo nhóm, GDPO áp dụng chuẩn hóa ưu thế theo lô (batch-wise advantage normalization) để duy trì phạm vi số ổn định, độc lập với số lượng phần thưởng, và cải thiện sự ổn định của việc cập nhật.

### Main Results:
- GDPO nhất quán vượt trội so với GRPO trên ba tác vụ: gọi công cụ (tool calling), suy luận toán học (math reasoning) và suy luận mã hóa (coding reasoning).
- GDPO cho thấy khả năng hội tụ đến điểm phần thưởng cao hơn về độ chính xác và định dạng trong tác vụ gọi công cụ.
- Trong các tác vụ toán học khó, GDPO đạt độ chính xác cao hơn tới 6.3% (với DeepSeek-R1-1.5B) và 2.3% (với Qwen3-4B-Instruct) so với GRPO, đồng thời giữ cho phản hồi ngắn gọn hơn.
- GDPO bảo tồn một số lượng lớn hơn đáng kể các nhóm ưu thế riêng biệt so với GRPO (kể cả GRPO không có chuẩn hóa độ lệch chuẩn), dẫn đến các ước tính ưu thế cung cấp tín hiệu huấn luyện biểu cảm hơn.
- Những kết quả này chứng minh tính hiệu quả và khả năng tổng quát hóa của GDPO cho tối ưu hóa học tăng cường đa phần thưởng, cho thấy sự hội tụ huấn luyện được cải thiện và hiệu suất tốt hơn.

### Conclusion & Future Works:
GDPO là một giải pháp thay thế tốt hơn cho GRPO trong tối ưu hóa RL đa phần thưởng, khắc phục hiệu quả vấn đề sụp đổ tín hiệu phần thưởng của GRPO bằng cách tách rời chuẩn hóa phần thưởng. Nó đạt được hiệu suất vượt trội và sự ổn định cao hơn, cho phép mô hình căn chỉnh tốt hơn với nhiều sở thích đa dạng. Bài báo cũng cung cấp một cái nhìn tổng quan có hệ thống về cách sửa đổi các hàm phần thưởng và điều chỉnh trọng số phần thưởng để phù hợp hơn với các ưu tiên khác nhau.

### Brainstorming Space:
#### 1. Publish Papers:
- Nghiên cứu ứng dụng GDPO trong các lĩnh vực tối ưu hóa đa mục tiêu khác như robot học và hệ thống khuyến nghị để cải thiện hiệu suất cân bằng mục tiêu.
- Khám phá cơ chế gán trọng số thích ứng cho các phần thưởng riêng lẻ trong GDPO, cho phép mô hình tự động điều chỉnh ưu tiên theo ngữ cảnh và giai đoạn huấn luyện.
- Phân tích nguyên nhân sụp đổ tín hiệu phần thưởng ở các thuật toán tối ưu hóa chính sách khác ngoài GRPO và đề xuất các giải pháp chuẩn hóa tách rời tương tự.
#### 2. Patent:
- Một hệ thống trợ lý ảo trên điện thoại thông minh sử dụng GDPO để tối ưu hóa đồng thời độ chính xác câu trả lời, sự tuân thủ định dạng và giới hạn độ dài phản hồi.
- Phương pháp điều chỉnh gợi ý văn bản trên bàn phím di động, sử dụng GDPO để cân bằng giữa tốc độ nhập liệu, tỷ lệ dự đoán từ chính xác và sự phù hợp với phong cách ngôn ngữ của người dùng.
- Một công nghệ lọc nội dung trên thiết bị di động, áp dụng GDPO để tối ưu hóa đồng thời tính an toàn, độ phù hợp với sở thích cá nhân và chất lượng thông tin của nội dung hiển thị.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.05242](https://huggingface.co/papers/2601.05242) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.05242](https://arxiv.org/abs/2601.05242) |
| PDF Download | [https://arxiv.org/pdf/2601.05242.pdf](https://arxiv.org/pdf/2601.05242.pdf) |
| Github Repository | [https://github.com/NVlabs/GDPO](https://github.com/NVlabs/GDPO) |

--- 

## 2. RL-AWB: Deep Reinforcement Learning for Auto White Balance Correction in Low-Light Night-time Scenes

**Tác giả:** Yuan-Kang Lee, Kuan-Lin Chen, Chia-Che Chang, Yu-Lun Liu

**Xuất bản lúc:** 2026-01-08

**Tag:** Deep Reinforcement Learning, Auto White Balance, Color Constancy, Low-Light, Nighttime, Statistical Methods, Image Signal Processing (ISP)
### Main Problem:
Vấn đề cốt lõi mà bài báo đề cập là khó khăn trong việc thực hiện cân bằng trắng tự động (AWB) chính xác trong các cảnh thiếu sáng ban đêm. Các thách thức bao gồm nhiễu đáng kể do ánh sáng yếu và cài đặt ISO cao, điều kiện chiếu sáng phức tạp, sự phá vỡ các giả định thống kê của thuật toán AWB truyền thống, khả năng tổng quát hóa kém khi triển khai trên các cảm biến camera khác nhau, và độ nhạy cao của các thuật toán với việc lựa chọn tham số. Các phương pháp học sâu hiện tại cũng đòi hỏi lượng lớn dữ liệu huấn luyện được gắn nhãn và gặp vấn đề về tổng quát hóa đa cảm biến.

### Main Idea:
Bài báo giới thiệu RL-AWB, một khuôn khổ mới kết hợp các phương pháp thống kê với học tăng cường sâu (Deep Reinforcement Learning) để giải quyết vấn đề cân bằng trắng trong cảnh đêm. Phương pháp này bắt đầu bằng một thuật toán hằng số màu thống kê mới được thiết kế riêng cho cảnh đêm (SGP-LRD - Salient Gray Pixels with Local Reflectance Differences), tích hợp phát hiện các điểm ảnh xám nổi bật và ước tính chiếu sáng. Dựa trên nền tảng này, RL-AWB phát triển một phương pháp học tăng cường đầu tiên cho hằng số màu, mô phỏng các chuyên gia điều chỉnh AWB chuyên nghiệp bằng cách động điều chỉnh tối ưu các tham số của thuật toán thống kê cho từng hình ảnh. Cách tiếp cận lai này giữ được khả năng giải thích và tính độc lập với cảm biến của các phương pháp thống kê, đồng thời có được khả năng thích ứng của các phương pháp dựa trên học sâu, tất cả với yêu cầu dữ liệu huấn luyện tối thiểu.

### Main Results:
Các thí nghiệm đã chứng minh rằng RL-AWB đạt được khả năng tổng quát hóa vượt trội trên cả hình ảnh thiếu sáng và đủ sáng. Phương pháp này có thể tối ưu hóa các tham số cho các hình ảnh cảnh đêm khác nhau với tốc độ nhanh hơn, không yêu cầu kiến thức ground-truth về chiếu sáng trước, và mang lại lợi thế tổng quát hóa đa cảm biến tốt hơn. Thuật toán SGP-LRD đạt hiệu suất ước tính chiếu sáng hàng đầu trên các bộ dữ liệu benchmark cảnh đêm công khai. Khung RL-AWB với huấn luyện Soft Actor-Critic và học tăng dần hai giai đoạn (two-stage curriculum learning) cho phép tối ưu hóa tham số cho từng hình ảnh với hiệu quả dữ liệu vượt trội, chỉ cần 5 hình ảnh huấn luyện mỗi bộ dữ liệu để đạt được khả năng tổng quát hóa đa cảm biến vượt trội so với các phương pháp hiện đại. Bài báo cũng đóng góp bộ dữ liệu đêm đa camera đầu tiên, LEVI, gồm 700 ảnh từ hai cảm biến để đánh giá hằng số màu đa cảm biến.

### Conclusion & Future Works:
RL-AWB được trình bày như một giải pháp mạnh mẽ và hiệu quả cho cân bằng trắng tự động trong cảnh đêm thiếu sáng. Bằng cách kết hợp một thuật toán thống kê có thể giải thích được với khả năng ra quyết định thích ứng của học tăng cường, phương pháp này vượt qua những hạn chế của các cách tiếp cận truyền thống và học sâu. RL-AWB thể hiện hiệu suất vượt trội, đặc biệt là về khả năng tổng quát hóa đa cảm biến và hiệu quả dữ liệu, mở ra hướng đi mới cho cân bằng trắng trong nhiếp ảnh tính toán. Bài viết không đề cập cụ thể đến các hướng nghiên cứu tương lai.

### Brainstorming Space:
#### 1. Publish Papers:
*   Nghiên cứu so sánh các kiến trúc tác tử học tăng cường khác nhau và các hàm phần thưởng (reward functions) để điều chỉnh tham số AWB, đặc biệt tập trung vào khả năng chống nhiễu và độ chính xác trong điều kiện ánh sáng cực yếu.
*   Phát triển một thuật toán SGP-LRD nâng cao tích hợp phân đoạn ngữ nghĩa (semantic segmentation) để phát hiện pixel xám nổi bật một cách thông minh hơn, điều chỉnh động ngưỡng lọc dựa trên nội dung cảnh thay vì các tham số cố định.
*   Khám phá việc tích hợp RL-AWB vào một đường ống xử lý tín hiệu hình ảnh (ISP) hoàn chỉnh, sử dụng học tăng cường để điều phối và tối ưu hóa đồng thời các mô-đun ISP khác như khử nhiễu và ánh xạ tông màu.
#### 2. Patent:
*   Hệ thống điều chỉnh AWB trên điện thoại thông minh sử dụng mô hình học tăng cường tích hợp để tự động tối ưu hóa các tham số cân bằng trắng dựa trên phân tích đặc điểm nhiễu và quang phổ chiếu sáng của từng khung hình camera trong thời gian thực, đặc biệt cho ảnh chụp đêm.
*   Phương pháp tự động thích ứng thuật toán cân bằng trắng cho các cảm biến camera điện thoại mới, trong đó một tác tử học tăng cường được huấn luyện với dữ liệu ít ỏi để nhanh chóng học các chỉnh sửa tham số cần thiết để đạt được màu sắc chính xác trên nhiều mẫu điện thoại khác nhau.
*   Tính năng "AWB thông minh theo ngữ cảnh" trong ứng dụng camera điện thoại, nơi tác tử học tăng cường không chỉ điều chỉnh cân bằng trắng mà còn điều chỉnh các tham số liên quan khác dựa trên nhận diện cảnh đêm cụ thể (ví dụ: cảnh đường phố, bầu trời đêm, trong nhà với đèn neon) để mang lại kết quả hình ảnh tối ưu và tự nhiên nhất.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.05249](https://huggingface.co/papers/2601.05249) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.05249](https://arxiv.org/abs/2601.05249) |
| PDF Download | [https://arxiv.org/pdf/2601.05249.pdf](https://arxiv.org/pdf/2601.05249.pdf) |
| Github Repository | [https://github.com/BrianChen1120/RL-AWB](https://github.com/BrianChen1120/RL-AWB) |

--- 

## 3. Learnable Multipliers: Freeing the Scale of Language Model Matrix Layers

**Tác giả:** Maksim Velikanov, Ilyas Chahed, Jingwei Zuo, Dhia Eddine Rhaiem, Younes Belkada, Hakim Hacid

**Xuất bản lúc:** 2026-01-08

**Tag:** Language Models, Optimization, Weight Decay, Learnable Multipliers, µP, Neural Network Scaling
### Main Problem:
Vấn đề cốt lõi mà bài báo đề cập là các chuẩn của ma trận trọng số (weight norms) trong các lớp ma trận của mô hình ngôn ngữ lớn (LLM) bị giới hạn bởi các siêu tham số tối ưu hóa, đặc biệt là sự cân bằng giữa nhiễu gradient ngẫu nhiên và suy giảm trọng số (weight decay - WD). Điều này khiến mô hình không học được tỷ lệ tối ưu cho dữ liệu đào tạo, dẫn đến hiệu suất không tối ưu.
### Main Idea:
Bài báo đề xuất phương pháp "Learnable Multipliers" (LRM) để giải phóng tỷ lệ của các lớp ma trận trong LLM. Thay vì để chuẩn trọng số bị khóa trong trạng thái cân bằng nhiễu-WD, các bộ nhân có thể học (scalar hoặc per-row/per-column multipliers) được gắn vào các ma trận trọng số. Những bộ nhân này được học tự do, cho phép mô hình tự thích nghi với tỷ lệ tối ưu dựa trên dữ liệu. Phương pháp này được coi là một sự tổng quát hóa có thể học được và biểu cảm hơn của các bộ nhân µP, với mục tiêu cải thiện hiệu suất và giảm chi phí tinh chỉnh siêu tham số.
### Main Results:
*   Việc bổ sung các bộ nhân có thể học giúp ma trận trọng số thích nghi với tỷ lệ tối ưu, cải thiện hiệu suất mô hình so với trạng thái cân bằng nhiễu-WD.
*   Phương pháp này hoạt động tốt hơn một baseline µP được tinh chỉnh kỹ lưỡng và làm giảm đáng kể chi phí tính toán khi tinh chỉnh bộ nhân (không cần tinh chỉnh các bộ nhân forward và weight decay).
*   Các bộ nhân có thể học dẫn đến biểu diễn phong phú hơn và phân phối tỷ lệ đa dạng hơn trên các khối residual và cho các đặc trưng nội bộ.
*   Hiệu suất được cải thiện liên tục trong suốt quá trình tiền huấn luyện đầu cuối, duy trì khoảng cách hiệu suất tăng dần so với baseline.
*   Các bộ nhân có thể học duy trì mức hiệu suất tương tự bất kể được khởi tạo bằng các giá trị µP được tinh chỉnh cho forward và WD, tuy nhiên, việc tinh chỉnh tỷ lệ học của bộ nhân vẫn quan trọng.
*   Phương pháp này có thể áp dụng cho nhiều kiến trúc (attention, SSM, MLP) và các trình tối ưu hóa khác nhau (Adam, Muon), cho thấy những cải thiện và hành vi tương tự.
### Conclusion & Future Works:
Các bộ nhân có thể học là một phương pháp hiệu quả để giải quyết vấn đề tỷ lệ của các lớp ma trận trong LLM, cho phép mô hình học các biểu diễn phong phú hơn và cải thiện hiệu suất mà không cần tinh chỉnh siêu tham số phức tạp cho các bộ nhân forward và weight decay. Hướng nghiên cứu tiếp theo có thể bao gồm việc khám phá các khía cạnh thực tế như đối xứng forward-pass và cách mở rộng tỷ lệ theo chiều rộng của các bộ nhân đã học, cũng như việc tích hợp sâu hơn vào các kiến trúc và trình tối ưu hóa mới.
### Brainstorming Space:
#### 1. Publish Papers:
*   Nghiên cứu sâu hơn về tương tác giữa Learnable Multipliers và các kỹ thuật điều chuẩn khác như dropout hoặc regularizers tùy chỉnh để tối ưu hóa hiệu suất LLM.
*   Khám phá ứng dụng và hiệu quả của Learnable Multipliers trong các kiến trúc LLM mới nổi như Mixture-of-Experts hoặc các mô hình đa phương thức.
*   Phân tích lý thuyết về sự hội tụ và ổn định của các thuật toán tối ưu khi kết hợp với Learnable Multipliers trong các mạng thần kinh cực sâu.
#### 2. Patent:
*   Một hệ thống tối ưu hóa AI trên thiết bị di động sử dụng bộ nhân có thể học để tinh chỉnh các mô hình ngôn ngữ nhỏ hơn, cải thiện hiệu suất và hiệu quả năng lượng cho các tác vụ AI cục bộ trên điện thoại.
*   Một phương pháp huấn luyện mô hình AI tùy chỉnh trên đám mây cho các ứng dụng di động, trong đó các bộ nhân có thể học được áp dụng để đảm bảo hiệu suất ổn định và khả năng mở rộng trên nhiều loại thiết bị điện thoại khác nhau.
*   Một phần mềm SDK cho nhà phát triển ứng dụng di động cho phép tự động điều chỉnh tỷ lệ của các lớp mạng thần kinh trong các mô hình nhúng, giúp các ứng dụng AI chạy mượt mà hơn trên phần cứng điện thoại đa dạng.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.04890](https://huggingface.co/papers/2601.04890) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.04890](https://arxiv.org/abs/2601.04890) |
| PDF Download | [https://arxiv.org/pdf/2601.04890.pdf](https://arxiv.org/pdf/2601.04890.pdf) |
| Github Repository | [https://github.com/tiiuae/falcon-h1](https://github.com/tiiuae/falcon-h1) |

--- 

## 4. Token-Level LLM Collaboration via FusionRoute

**Tác giả:** Nuoya Xiong, Yuhang Zhou, Hanqing Zeng, Zhaorun Chen, Furong Huang, Shuchao Bi, Lizhu Zhang, Zhuokai Zhao

**Xuất bản lúc:** 2026-01-08

**Tag:** LLM Collaboration, Token-Level Routing, Mixture of Experts, Router, Logit Addition
### Main Problem:
Các mô hình ngôn ngữ lớn (LLM) tổng quát rất đắt đỏ để huấn luyện và triển khai, trong khi các mô hình chuyên biệt nhỏ hơn thì hiệu quả hơn nhưng lại kém khả năng tổng quát hóa. Các phương pháp hợp tác LLM hiện có như MoE yêu cầu huấn luyện tốn kém, hệ thống đa tác nhân (MAS) không hiệu quả và thiếu cơ chế phân bổ tác vụ động, còn model merging dễ bị nhiễu thông số. Các phương pháp hợp tác cấp độ token trước đây không đủ mạnh mẽ khi các mô hình chuyên gia hoạt động kém hoặc chiến lược lựa chọn không chính xác.

### Main Idea:
Bài báo đề xuất FusionRoute, một framework hợp tác đa LLM cấp độ token mạnh mẽ và hiệu quả. FusionRoute sử dụng một router nhẹ để đồng thời (i) chọn chuyên gia phù hợp nhất ở mỗi bước giải mã và (ii) đóng góp một logit bổ sung để tinh chỉnh hoặc sửa phân phối next-token của chuyên gia đã chọn thông qua phép cộng logit. Cơ chế kép này cho phép FusionRoute vượt qua giới hạn của việc chỉ chọn chuyên gia, mang lại sự mạnh mẽ thông qua việc giảm thiểu lỗi của chuyên gia và hiệu quả bằng cách tránh overhead của các phương pháp hợp tác LLM trước đây. Quá trình huấn luyện của FusionRoute gồm hai giai đoạn: Supervised Fine-Tuning (SFT) để thiết lập khả năng dự đoán token và lựa chọn chuyên gia, sau đó là giai đoạn tối ưu hóa sở thích (preference optimization) để tinh chỉnh chính sách cuối cùng.

### Main Results:
Về mặt lý thuyết, bài báo chứng minh rằng việc hợp tác cấp độ token chỉ dựa vào chuyên gia bị giới hạn một cách cơ bản, không thể đạt được chính sách giải mã tối ưu trừ khi có các giả định bao phủ toàn cầu mạnh mẽ. Ngược lại, bộ tạo bổ sung của FusionRoute vượt qua giới hạn này và cho phép phục hồi chính sách tối ưu.
Về mặt thực nghiệm, trên cả các dòng mô hình Llama-3 và Gemma-2, cùng với các benchmark đa dạng như suy luận toán học, tạo mã và thực hiện chỉ dẫn, FusionRoute vượt trội hơn so với các phương pháp hợp tác cấp độ chuỗi và token, model merging, và cả direct fine-tuning, đồng thời vẫn cạnh tranh với các chuyên gia miền trên các tác vụ riêng của chúng.

### Conclusion & Future Works:
FusionRoute cung cấp một giải pháp robust, hiệu quả và có khả năng áp dụng rộng rãi cho vấn đề hợp tác LLM bằng cách kết hợp lựa chọn chuyên gia và bổ sung kiến thức ở cấp độ token. Hệ thống này tự động điều phối các LLM chuyên biệt, cải thiện hiệu suất nhất quán trên nhiều tác vụ và bộ dữ liệu. Bài báo không đề cập cụ thể đến các hướng nghiên cứu trong tương lai.

### Brainstorming Space:
#### 1. Publish Papers:
*   Nghiên cứu kiến trúc router tiên tiến hơn hoặc các chiến lược huấn luyện tự giám sát để tối ưu hóa việc phân bổ chuyên gia và đóng góp logit bổ sung trong FusionRoute.
*   Mở rộng FusionRoute để xử lý các mô hình đa phương thức (multimodal LLMs) hoặc các tác vụ tạo sinh có cấu trúc (structured generation tasks) bằng cách tích hợp các chuyên gia và tín hiệu bổ sung từ các modal khác nhau.
*   Khám phá cơ chế điều chỉnh động các chuyên gia hoặc thêm mới các chuyên gia vào hệ thống FusionRoute đang hoạt động mà không cần huấn luyện lại toàn bộ.
#### 2. Patent:
*   Một hệ thống trợ lý AI trên điện thoại di động sử dụng FusionRoute để chuyển đổi mượt mà giữa các LLM chuyên biệt (ví dụ: một cho viết email, một cho giải toán) ở cấp độ token, mang lại phản hồi nhanh và chính xác hơn cho người dùng.
*   Công nghệ bàn phím thông minh trên điện thoại có khả năng dự đoán từ tiếp theo bằng cách kết hợp một mô hình ngôn ngữ chung nhỏ với các LLM chuyên biệt (ví dụ: cho y tế, kỹ thuật) thông qua logit bổ sung của FusionRoute để đưa ra gợi ý chính xác theo ngữ cảnh.
*   Một tính năng tạo nội dung tự động trên điện thoại (ví dụ: soạn tin nhắn, tạo bài đăng mạng xã hội) tận dụng FusionRoute để kết hợp các mô hình chuyên biệt cho từng loại nội dung, tối ưu hóa hiệu suất và giảm tài nguyên xử lý trên thiết bị.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.05106](https://huggingface.co/papers/2601.05106) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.05106](https://arxiv.org/abs/2601.05106) |
| PDF Download | [https://arxiv.org/pdf/2601.05106.pdf](https://arxiv.org/pdf/2601.05106.pdf) |
| Github Repository | N/A |

--- 

## 5. RelayLLM: Efficient Reasoning via Collaborative Decoding

**Tác giả:** Chengsong Huang, Tong Zheng, Langlin Huang, Jinyuan Li, Haolin Liu, Jiaxin Huang

**Xuất bản lúc:** 2026-01-08

**Tag:** Efficient Reasoning, Collaborative Decoding, LLM, SLM, Token-level collaboration, Reinforcement Learning

### Main Problem:
Việc triển khai Large Language Models (LLMs) cho các tác vụ suy luận phức tạp gặp phải hạn chế về chi phí tính toán cao và độ trễ lớn, trong khi Small Language Models (SLMs) tiết kiệm tài nguyên lại thiếu năng lực suy luận cần thiết. Các phương pháp hợp tác hiện có, như phân tầng hoặc định tuyến, hoạt động ở mức độ hạt thô bằng cách chuyển toàn bộ truy vấn sang LLM, dẫn đến lãng phí tính toán đáng kể khi SLM có khả năng xử lý phần lớn các bước suy luận.

### Main Idea:
Bài nghiên cứu đề xuất RelayLLM, một khung công tác mới để suy luận hiệu quả thông qua giải mã hợp tác ở cấp độ token. RelayLLM cho phép SLM đóng vai trò là một bộ điều khiển chủ động, tự động gọi LLM chỉ cho các token quan trọng thông qua một lệnh đặc biệt (`<call>n</call>`), qua đó "chuyển tiếp" quá trình tạo. Khung đào tạo gồm hai giai đoạn được giới thiệu: giai đoạn khởi động (warm-up) và Tối ưu hóa chính sách tương đối nhóm (Group Relative Policy Optimization - GRPO). Giai đoạn khởi động dạy mô hình cấu trúc cú pháp của lệnh gọi, và GRPO, sử dụng một phần thưởng nhận biết ngữ cảnh, hướng dẫn mô hình cân bằng giữa tính độc lập và việc tìm kiếm sự hỗ trợ chiến lược, đồng thời phạt cả chi phí lãng phí và lỗi có thể tránh được.

### Main Results:
RelayLLM đã cải thiện độ chính xác trung bình từ 42.5% lên 49.52% trên sáu bộ dữ liệu benchmark, thu hẹp đáng kể khoảng cách hiệu suất giữa hai mô hình. Điều này đạt được chỉ bằng cách gọi LLM cho 1.07% tổng số token được tạo ra, mang lại mức giảm chi phí 98.2% so với các bộ định tuyến ngẫu nhiên có hiệu suất tương đương. So với Random Router, RelayLLM cho thấy cải thiện độ chính xác 6.9%. Các đánh giá cũng tiết lộ rằng mô hình SLM đã tiếp thu các mẫu suy luận hiệu quả trong quá trình hợp tác, cho phép nó vượt qua các baseline trên các benchmark dễ hơn ngay cả khi không có sự hỗ trợ của chuyên gia.

### Conclusion & Future Works:
RelayLLM là một framework hiệu quả giúp cải thiện đáng kể năng lực suy luận của các mô hình ngôn ngữ nhỏ bằng cách hợp tác chiến lược với các mô hình lớn ở cấp độ token, qua đó giảm thiểu chi phí và độ trễ đáng kể. Bài nghiên cứu chứng minh khả năng của mô hình nhỏ trong việc tự điều khiển và chỉ yêu cầu hỗ trợ khi cần thiết. Đoạn trích này không đề cập đến các hướng nghiên cứu tiếp theo.

### Brainstorming Space:
#### 1. Publish Papers:
1.  Nghiên cứu các phương pháp tiên tiến để tự động xác định số lượng token `n` cần gọi từ LLM dựa trên độ phức tạp của ngữ cảnh và độ tự tin của SLM.
2.  Khám phá việc áp dụng RelayLLM cho các tác vụ tạo nội dung đa phương tiện, nơi SLM xử lý các phần thông thường và LLM được gọi cho các chi tiết sáng tạo hoặc kỹ thuật phức tạp.
3.  Phát triển một cơ chế RelayLLM đa cấp, nơi các SLM có kích thước khác nhau có thể hợp tác tuần tự trước khi gọi một LLM để tối ưu hóa chi phí hơn nữa.

#### 2. Patent:
1.  Hệ thống quản lý tài nguyên AI trên điện thoại di động sử dụng cơ chế RelayLLM để tự động điều phối giữa mô hình ngôn ngữ nhỏ chạy cục bộ và mô hình ngôn ngữ lớn trên đám mây, tối ưu hóa pin và dữ liệu.
2.  Phương pháp tăng cường trợ lý giọng nói trên điện thoại thông minh, cho phép thiết bị xử lý các lệnh đơn giản cục bộ và tự động gọi LLM trên đám mây cho các yêu cầu phức tạp hơn, phản hồi được tích hợp liền mạch.
3.  Công nghệ soạn thảo văn bản thông minh trên điện thoại di động sử dụng RelayLLM, với SLM cung cấp các gợi ý cơ bản và LLM được gọi cho các đoạn văn chuyên sâu hoặc chỉnh sửa ngữ pháp phức tạp, nâng cao trải nghiệm người dùng.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.05167](https://huggingface.co/papers/2601.05167) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.05167](https://arxiv.org/abs/2601.05167) |
| PDF Download | [https://arxiv.org/pdf/2601.05167.pdf](https://arxiv.org/pdf/2601.05167.pdf) |
| Github Repository | [https://github.com/Chengsong-Huang/RelayLLM](https://github.com/Chengsong-Huang/RelayLLM) |

--- 

## 6. AT^2PO: Agentic Turn-based Policy Optimization via Tree Search

**Tác giả:** Zefang Zong, Dingwei Chen, Yang Li, Qi Yi, Bo Zhou, Chengming Li, Bo Qian, Peng Chen, Jie Jiang

**Xuất bản lúc:** 2026-01-08

**Tag:** Agentic Reinforcement Learning, LLM Agents, Tree Search, Policy Optimization, Multi-turn Tasks

### Main Problem:
Các tác nhân LLM trong RL hướng tác nhân (Agentic RL) đối mặt với ba thách thức chính khi xử lý các tác vụ đa lượt: 1) Đa dạng khám phá bị hạn chế do các phương pháp hiện có không ưu tiên chiến lược việc mở rộng các lượt có độ không chắc chắn cao hoặc tiềm năng lớn. 2) Vấn đề gán tín hiệu thưởng thưa thớt (sparse credit assignment) vì phần thưởng thường chỉ có sẵn ở cuối quỹ đạo, gây khó khăn trong việc gán tín dụng cho các bước hành động trung gian cụ thể. 3) Sự không phù hợp cơ bản giữa cấu trúc theo lượt của các tác vụ tác nhân và các mục tiêu tối ưu hóa chính sách phẳng hiện có, dẫn đến các bản cập nhật chính sách không ổn định và kém hiệu quả.

### Main Idea:
Bài báo giới thiệu AT2PO (Agentic Turn-based Policy Optimization via Tree Search), một khung thống nhất cho Agentic RL đa lượt, giải quyết ba thách thức trên bằng cách tích hợp ba thành phần chính:
1.  **Entropy-Guided Tree Expansion:** Một cấu trúc cây cấp độ lượt cho phép mở rộng cây tìm kiếm một cách chiến lược từ các lượt có độ không chắc chắn cao nhất để tối đa hóa hiệu quả khám phá.
2.  **Turn-wise Credit Assignment:** Cơ chế gán tín hiệu thưởng theo từng lượt để truyền các phần thưởng thưa thớt ngược qua cây, tính toán các ước lượng giá trị và lợi thế chi tiết theo từng lượt.
3.  **Agentic Turn-based Policy Optimization (ATPO):** Một mục tiêu học tập cấp độ lượt mới, thực hiện lấy mẫu quan trọng và cắt xén ở cấp độ lượt, điều chỉnh các bản cập nhật chính sách với đơn vị ra quyết định tự nhiên của các tương tác tác nhân, cải thiện sự ổn định và hiệu suất. ATPO được thiết kế để có thể tích hợp vào bất kỳ quy trình RL đa lượt nào.

### Main Results:
AT2PO cải thiện hiệu suất một cách nhất quán so với các baseline tiên tiến, đạt mức tăng trung bình lên tới 1.84 điểm phần trăm trên bảy bộ benchmark. Các nghiên cứu ablation cũng xác nhận hiệu quả của từng thành phần trong khung AT2PO.

### Conclusion & Future Works:
AT2PO là một khung thống nhất giải quyết các thách thức cốt lõi trong Agentic RL đa lượt, giúp tạo ra các rollouts đa dạng và chất lượng cao hơn, tận dụng hiệu quả hơn các phần thưởng thưa thớt, và tối ưu hóa chính sách phù hợp với mô hình tác nhân đa lượt. Bài báo không đề cập cụ thể về hướng nghiên cứu trong tương lai.

### Brainstorming Space:
#### 1. Publish Papers:
1.  Nghiên cứu mở rộng Entropy-Guided Tree Expansion bằng cách tích hợp các heuristic dựa trên kiến thức miền cụ thể để định hướng khám phá hiệu quả hơn trong các môi trường tác vụ phức tạp.
2.  Khám phá các phương pháp gán tín hiệu thưởng theo lượt nâng cao, chẳng hạn như sử dụng mô hình thưởng học được ở cấp độ lượt hoặc phản hồi từ chuyên gia để cải thiện chất lượng tín hiệu huấn luyện.
3.  Áp dụng ATPO vào các tác vụ tác nhân đa phương thức, nơi tác nhân phải tương tác với nhiều loại công cụ và dữ liệu đầu vào khác nhau, để kiểm tra khả năng mở rộng và hiệu suất của khung.

#### 2. Patent:
1.  Hệ thống trợ lý ảo trên điện thoại thông minh sử dụng tối ưu hóa chính sách theo lượt để cải thiện khả năng ra quyết định và sử dụng công cụ hiệu quả trong các cuộc trò chuyện đa lượt với người dùng.
2.  Phương pháp tối ưu hóa hành vi tác nhân điều khiển tác vụ tự động trên điện thoại di động, ví dụ như đặt lịch hẹn hoặc mua sắm trực tuyến, bằng cách ưu tiên khám phá các lựa chọn hành động không chắc chắn nhất để đạt được kết quả tốt hơn.
3.  Công nghệ gán tín hiệu thưởng tinh chỉnh theo từng bước cho các ứng dụng giáo dục hoặc hướng dẫn trên điện thoại, cho phép hệ thống cung cấp phản hồi chính xác và kịp thời hơn dựa trên các tương tác theo lượt của người dùng.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.04767](https://huggingface.co/papers/2601.04767) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.04767](https://arxiv.org/abs/2601.04767) |
| PDF Download | [https://arxiv.org/pdf/2601.04767.pdf](https://arxiv.org/pdf/2601.04767.pdf) |
| Github Repository | [https://github.com/zzfoutofspace/ATPO](https://github.com/zzfoutofspace/ATPO) |

--- 

## 7. RoboVIP: Multi-View Video Generation with Visual Identity Prompting Augments Robot Manipulation

**Tác giả:** Boyang Wang, Haoran Zhang, Shujie Zhang, Jinkun Hao, Mingda Jia, Qi Lv, Yucheng Mao, Zhaoyang Lyu, Jia Zeng, Xudong Xu, Jiangmiao Pang

**Xuất bản lúc:** 2026-01-08

**Tag:** Diffusion, Video Generation, Multi-View, Robot Manipulation, Data Augmentation, Visual Identity Prompting, Segmentation

### Main Problem:
Vấn đề cốt lõi mà bài báo đề cập là sự thiếu hụt dữ liệu thao tác robot đa dạng, số lượng lớn và chất lượng cao cần thiết để huấn luyện các chính sách robot hiệu quả. Các phương pháp thu thập dữ liệu trong thế giới thực gặp khó khăn về khả năng mở rộng do các ràng buộc về phần cứng và thiết lập vật lý. Các phương pháp tăng cường dữ liệu hiện có bằng mô hình khuếch tán dựa trên văn bản thường bỏ qua nhu cầu về quan sát đa góc nhìn (multi-view) và nhất quán theo thời gian (temporally coherent), đồng thời các lời nhắc văn bản không đủ để xác định cài đặt cảnh chi tiết hoặc nắm bắt các chi tiết cấp thấp.

### Main Idea:
Bài báo đề xuất RoboVIP, một khuôn khổ tăng cường dữ liệu thao tác robot sử dụng mô hình khuếch tán video dựa trên inpainting đa góc nhìn với "visual identity prompting". Giải pháp này bao gồm ba phần chính:
1.  **Hệ thống phân đoạn tự động hướng hành động (Action-guided Segmentation):** Sử dụng thông tin hành động (đặc biệt là trạng thái kẹp gắp 1D) để định vị chính xác robot và các đối tượng tương tác trong video, giúp khắc phục các hạn chế của việc áp dụng trực tiếp các mô hình ngoài luồng.
2.  **Visual Identity Prompting:** Giới thiệu việc sử dụng một hoặc nhiều hình ảnh mẫu (exemplar images) làm đầu vào điều kiện cho mô hình khuếch tán video, cho phép tạo ra nội dung nhất quán về mặt ngữ nghĩa và chi tiết cấp thấp hơn trong các vùng được inpaint, khắc phục hạn chế của lời nhắc văn bản.
3.  **Quy trình tuyển chọn Visual Identity Pool có khả năng mở rộng:** Tự động xây dựng một kho lưu trữ lớn (hàng triệu hình ảnh) các "visual identities" từ các tập dữ liệu robot hiện có, đảm bảo tính "plug-and-play" của khuôn khổ.
Mục tiêu là tạo ra các video đa góc nhìn, nhất quán về mặt thời gian để làm phong phú dữ liệu huấn luyện cho các mô hình chính sách robot.

### Main Results:
-   RoboVIP đã chứng minh khả năng tạo ra các chuỗi video đa góc nhìn, nhất quán theo thời gian với các cảnh nền và vật thể trên bàn đa dạng thông qua kỹ thuật "visual identity prompting".
-   Việc sử dụng dữ liệu thao tác được tăng cường bởi RoboVIP để huấn luyện các mô hình chính sách tầm nhìn-ngôn ngữ-hành động (VLA) như pi0 và Octo, cũng như các mô hình chính sách thị giác-vận động (visuomotor policy) như Diffusion Policy, đã mang lại những cải tiến hiệu suất nhất quán về tỷ lệ thành công.
-   Hiệu quả của RoboVIP được đánh giá trên 12K quỹ đạo BridgeV2 trong mô phỏng và 100 quỹ đạo robot thế giới thực, cho thấy những cải tiến nhất quán.
-   Điều này thể hiện tính thực tiễn của RoboVIP cho việc huấn luyện VLA quy mô lớn và học chính sách với dữ liệu thấp.

### Conclusion & Future Works:
RoboVIP cung cấp một giải pháp mạnh mẽ để giải quyết sự khan hiếm dữ liệu trong điều khiển robot bằng cách tạo ra các quan sát thị giác đa góc nhìn, nhất quán theo thời gian và phong phú về bối cảnh thông qua việc sử dụng visual identity prompting và inpainting video. Thành công của nó trong việc cải thiện hiệu suất của các mô hình chính sách VLA và visuomotor cho thấy tiềm năng to lớn của việc tăng cường dữ liệu bằng mô hình tạo sinh. Hướng nghiên cứu tiếp theo có thể tập trung vào việc khám phá các loại điều kiện hoặc tín hiệu khác để hướng dẫn tạo sinh, cũng như mở rộng khả năng của RoboVIP để xử lý các tác vụ phức tạp hơn hoặc các tương tác robot động hơn.

### Brainstorming Space:
#### 1. Publish Papers:
-   Nghiên cứu cách tích hợp các mô hình ngôn ngữ lớn (LLM) để tạo ra các lời nhắc văn bản chi tiết hơn và nhất quán hơn, kết hợp với visual identity prompting để đạt được sự kiểm soát tạo sinh cao hơn.
-   Khám phá việc sử dụng các mô hình tạo sinh 3D thay vì 2D để tăng cường dữ liệu robot, nhằm cung cấp các tín hiệu không gian phong phú hơn và cải thiện khả năng suy luận 3D cho robot.
-   Phát triển một phương pháp tự động để đánh giá chất lượng và sự đa dạng của dữ liệu tăng cường, đảm bảo rằng dữ liệu được tạo ra thực sự có lợi cho việc học chính sách robot và không tạo ra các "artifact" gây nhiễu.

#### 2. Patent:
-   Hệ thống ứng dụng di động cho phép người dùng chụp ảnh đối tượng thực tế bằng điện thoại và tự động tạo ra các môi trường ảo đa dạng xung quanh đối tượng đó để huấn luyện robot ảo.
-   Công nghệ tích hợp vào camera điện thoại để phát hiện và phân đoạn đối tượng trong thời gian thực, sau đó sử dụng các hình ảnh được chụp làm "visual identity prompts" để tạo ra các kịch bản tương tác robot tùy chỉnh trên đám mây.
-   Thiết bị đeo tay hoặc ứng dụng di động có khả năng ghi lại các tương tác người-đối tượng bằng camera điện thoại, sử dụng dữ liệu này như "visual identity prompts" để mô phỏng và tăng cường dữ liệu huấn luyện cho robot thực hiện các tác vụ hỗ trợ con người.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.05241](https://huggingface.co/papers/2601.05241) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.05241](https://arxiv.org/abs/2601.05241) |
| PDF Download | [https://arxiv.org/pdf/2601.05241.pdf](https://arxiv.org/pdf/2601.05241.pdf) |
| Github Repository | [https://github.com/RoboVIP/RoboVIP_VDM](https://github.com/RoboVIP/RoboVIP_VDM) |

--- 

## 8. Few Tokens Matter: Entropy Guided Attacks on Vision-Language Models

**Tác giả:** Mengqi He, Xinyu Tian, Xin Shen, Jinhong Ni, Shu Zou, Zhaoyuan Yang, Jing Zhang

**Xuất bản lúc:** 2025-12-26

**Tag:** VLM, Adversarial Attack, Entropy, Token
### Main Problem: Các mô hình Vision-Language Models (VLM) dễ bị tấn công đối kháng. Các phương pháp tấn công dựa trên entropy trước đây tối đa hóa sự không chắc chắn trên toàn bộ các bước giải mã, giả định mọi token đều đóng góp như nhau vào sự mất ổn định của mô hình. Tuy nhiên, bài báo này tiết lộ chỉ một phần nhỏ (20%) các token có độ entropy cao, đóng vai trò là điểm quyết định trong quá trình tạo sinh tự hồi quy, chi phối mạnh mẽ quỹ đạo đầu ra, khiến VLM dễ bị tấn công có mục tiêu và tạo ra nội dung có hại.
### Main Idea: Bài báo đề xuất tấn công Adversarial có hướng dẫn bằng Entropy (EGA) bằng cách tập trung các nhiễu đối kháng vào một phần nhỏ (20%) các token có độ entropy cao trong quá trình tạo sinh tự hồi quy của VLM. Phương pháp này dựa trên giả thuyết rằng việc thao túng các token có độ entropy cao này là đủ để làm chệch hướng mô tả. EGA sử dụng một từ vựng ngoại tuyến để xác định các vị trí hiệu quả mà không cần tính toán nội bộ entropy của mô hình, đạt được tỷ lệ tấn công thành công và tỷ lệ gây hại cao.
### Main Results:
- Chỉ 20% các token có độ entropy cao là đủ để tấn công VLM thành công, cho thấy một phần nhỏ token chi phối tính dễ bị tổn thương của VLM.
- Tấn công tập trung vào các vị trí entropy cao này đạt được sự suy giảm ngữ nghĩa tương đương với các phương pháp toàn cục trong khi sử dụng ngân sách ít hơn đáng kể.
- Các cuộc tấn công có chọn lọc này khiến 35-49% các đầu ra lành tính trở thành có hại trên nhiều VLM đại diện.
- Tấn công EGA đạt tỷ lệ tấn công thành công cạnh tranh (93-95%) và tỷ lệ gây hại mạnh mẽ (42-47% trên tạo chú thích ảnh, 24-28% trên VQA).
- Các token có độ entropy cao này tái diễn trên các VLM có kiến trúc đa dạng, cho thấy khả năng chuyển giao khả thi (tỷ lệ gây hại 17-26% trên các mục tiêu chưa từng thấy).
### Conclusion & Future Works: Bài báo kết luận rằng các VLM có một lỗ hổng quan trọng khi chỉ một phần nhỏ các token có độ entropy cao có thể bị thao túng để gây suy giảm ngữ nghĩa đáng kể và tạo ra nội dung có hại, với khả năng chuyển giao cao giữa các mô hình. Điều này phơi bày những điểm yếu mới trong cơ chế an toàn của VLM hiện tại, ngụ ý cần có các nghiên cứu tiếp theo về phòng thủ và tăng cường tính an toàn cho các mô hình này.
### Brainstorming Space:
#### 1. Publish Papers:
- Phát triển các chiến lược phòng thủ mới nhằm chống lại các cuộc tấn công dựa trên token có độ entropy cao trong VLM.
- Điều tra xem liệu các điểm quyết định có độ entropy cao tương tự có tồn tại và có thể bị khai thác trong các mô hình AI tạo sinh khác hay không.
- Khám phá việc sử dụng giám sát entropy thời gian thực trong quá trình suy luận VLM để phát hiện và giảm thiểu các cuộc tấn công đối kháng tiềm năng.
#### 2. Patent:
- Hệ thống phát hiện tấn công Adversarial tích hợp trên điện thoại thông minh, cảnh báo người dùng khi nội dung tạo bởi VLM có khả năng bị thao túng hoặc có hại.
- Phương pháp tăng cường tính an toàn cho trợ lý ảo trên điện thoại bằng cách giám sát và trung hòa các token có độ entropy cao trong phản hồi, ngăn chặn việc tạo ra nội dung không mong muốn.
- Ứng dụng điện thoại thông minh cung cấp tính năng "kiểm tra độ tin cậy" cho nội dung đa phương thức, làm nổi bật các phần văn bản hoặc hình ảnh có độ không chắc chắn cao do VLM tạo ra.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2512.21815](https://huggingface.co/papers/2512.21815) |
| ArXiv Abstract | [https://arxiv.org/abs/2512.21815](https://arxiv.org/abs/2512.21815) |
| PDF Download | [https://arxiv.org/pdf/2512.21815.pdf](https://arxiv.org/pdf/2512.21815.pdf) |
| Github Repository | N/A |

--- 

## 9. VideoAuto-R1: Video Auto Reasoning via Thinking Once, Answering Twice

**Tác giả:** Shuming Liu, Mingchen Zhuge, Changsheng Zhao, Jun Chen, Lemeng Wu, Zechun Liu, Chenchen Zhu, Zhipeng Cai, Chong Zhou, Haozhe Liu, Ernie Chang, Saksham Suri, Hongyu Xu, Qi Qian, Wei Wen, Balakrishnan Varadarajan, Zhuang Liu, Hu Xu, Florian Bordes, Raghuraman Krishnamoorthi, Bernard Ghanem, Vikas Chandra, Yunyang Xiong

**Xuất bản lúc:** 2026-01-08

**Tag:** Video Understanding, Auto-Reasoning, Chain-of-Thought (CoT), Multimodal LLM, Efficiency, Adaptive Reasoning

### Main Problem:
Các mô hình hiểu video sử dụng Chain-of-Thought (CoT) thường không cải thiện đáng kể độ chính xác so với trả lời trực tiếp trên nhiều tác vụ, nhưng lại tiêu tốn tài nguyên tính toán cao hơn và dẫn đến hiệu quả thấp. Chiến lược "always-thinking" gây ra độ trễ cao và chi phí suy luận lớn do tạo ra các phản hồi dài. Việc mở rộng các phương pháp "auto-thinking" hiện có từ văn bản và hình ảnh sang video là không dễ dàng do mối tương quan yếu giữa lý luận tường minh và độ chính xác, cùng với sự mơ hồ về hình ảnh và nhiễu thời gian, dẫn đến huấn luyện không ổn định.

### Main Idea:
Đề xuất VideoAuto-R1, một khung hiểu video áp dụng chiến lược "lý luận khi cần thiết" ("reason-when-necessary"). Trong quá trình huấn luyện, mô hình tuân theo mô hình "Suy nghĩ một lần, Trả lời hai lần" ("Thinking Once, Answering Twice"): đầu tiên tạo một câu trả lời ban đầu, sau đó thực hiện lý luận và cuối cùng xuất ra một câu trả lời đã xem xét. Cả hai câu trả lời đều được giám sát bằng phần thưởng có thể kiểm chứng, với trọng số lớn hơn cho câu trả lời cuối cùng để khuyến khích tinh chỉnh. Trong quá trình suy luận, mô hình sử dụng điểm tin cậy của câu trả lời ban đầu để xác định có nên tiếp tục lý luận hay không thông qua cơ chế thoát sớm (early-exit) dựa trên ngưỡng.

### Main Results:
* Đạt được độ chính xác hàng đầu (state-of-the-art) trên các tiêu chuẩn QA video và định vị thời gian (temporal grounding) với hiệu quả được cải thiện đáng kể.
* Giảm độ dài phản hồi trung bình khoảng 3.3 lần (ví dụ, từ 149 xuống còn 44 token) trong khi vẫn duy trì độ chính xác.
* Tỷ lệ kích hoạt chế độ "suy nghĩ" thấp trên các tác vụ tập trung vào nhận thức (25% trên MVBench) nhưng cao hơn trên các tác vụ cần lý luận chuyên sâu (51% trên VideoMMMU).
* Chỉ ra rằng lý luận dựa trên ngôn ngữ tường minh có lợi nhưng không phải lúc nào cũng cần thiết cho việc hiểu video.
* Là nghiên cứu có hệ thống đầu tiên chứng minh rằng các mô hình lý luận video hiện có hoạt động tương đương ở chế độ trả lời trực tiếp và CoT, cảnh báo việc dựa dẫm vô điều kiện vào CoT.

### Conclusion & Future Works:
VideoAuto-R1 cung cấp một giải pháp lý luận thích ứng hiệu quả và tiết kiệm chi phí cho việc hiểu video bằng cách chỉ kích hoạt quá trình lý luận khi cần thiết, cân bằng giữa độ chính xác và hiệu suất. Công trình này cho thấy việc dựa dẫm vô điều kiện vào Chain-of-Thought cho các tác vụ video là không tối ưu do chi phí tính toán cao và lợi ích khiêm tốn trên nhiều tác vụ.

### Brainstorming Space:
#### 1. Publish Papers:
*   Nghiên cứu cơ chế xác định ngưỡng tin cậy động thay vì cố định để tối ưu hóa việc kích hoạt chế độ lý luận trên các loại video và tác vụ khác nhau.
*   Mở rộng khung VideoAuto-R1 để tích hợp các loại lý luận chuyên biệt hơn (ví dụ: lý luận quan hệ đối tượng, lý luận ngữ cảnh dài hạn) và đánh giá tác động của chúng đến hiệu suất và hiệu quả.
*   Áp dụng mô hình "Suy nghĩ một lần, Trả lời hai lần" cho các miền đa phương thức khác như hiểu hình ảnh-âm thanh, nơi cần cân bằng giữa nhận thức và lý luận sâu.

#### 2. Patent:
*   Hệ thống ứng dụng điện thoại thông minh cho phép người dùng quay video và nhận câu trả lời tức thì, với khả năng tự động phân tích chi tiết nếu câu hỏi phức tạp, tối ưu hóa thời gian chờ và mức sử dụng pin.
*   Phương pháp xử lý video trên thiết bị di động tích hợp cơ chế "early-exit" dựa trên độ tin cậy của câu trả lời ban đầu để giảm tải tính toán cho các tác vụ phân tích video AI, kéo dài thời lượng pin điện thoại.
*   Công nghệ trợ lý ảo trên điện thoại có khả năng phân tích video theo thời gian thực để trả lời câu hỏi của người dùng, tự động quyết định khi nào cần suy luận sâu hơn để cung cấp thông tin chính xác mà không làm chậm trải nghiệm người dùng.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.05175](https://huggingface.co/papers/2601.05175) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.05175](https://arxiv.org/abs/2601.05175) |
| PDF Download | [https://arxiv.org/pdf/2601.05175.pdf](https://arxiv.org/pdf/2601.05175.pdf) |
| Github Repository | [https://github.com/IVUL-KAUST/VideoAuto-R1/](https://github.com/IVUL-KAUST/VideoAuto-R1/) |

--- 

## 10. VerseCrafter: Dynamic Realistic Video World Model with 4D Geometric Control

**Tác giả:** Sixiao Zheng, Minghao Yin, Wenbo Hu, Xiaoyu Li, Ying Shan, Yanwei Fu

**Xuất bản lúc:** 2026-01-08

**Tag:** Video World Model, 4D Geometric Control, Dynamic Video Generation, Multi-Object Motion Control, Camera Control, Diffusion Model, Dataset Generation

### Main Problem:
Các mô hình thế giới video hiện có gặp khó khăn trong việc cung cấp khả năng kiểm soát thống nhất và chính xác chuyển động của camera và nhiều đối tượng. Điều này xuất phát từ bản chất 2D của video, trong khi thế giới thực vận hành trong không gian 4D (không gian-thời gian). Các phương pháp hiện tại thường giới hạn ở cảnh tĩnh, không kiểm soát được chuyển động của nhiều đối tượng, hoặc sử dụng các không gian kiểm soát 2D/3D không đầy đủ (ví dụ: quỹ đạo thưa thớt nhiễu loạn, hộp giới hạn cứng nhắc, mô hình tham số giới hạn theo loại). Hơn nữa, việc thiếu dữ liệu huấn luyện quy mô lớn với chú thích 4D rõ ràng cũng là một thách thức lớn.

### Main Idea:
Bài báo đề xuất VerseCrafter, một mô hình thế giới video nhận biết 4D, cho phép kiểm soát rõ ràng và nhất quán cả động lực camera và đối tượng trong một trạng thái thế giới hình học 4D thống nhất. Giải pháp này tập trung vào một biểu diễn `4D Geometric Control` mới, mã hóa trạng thái thế giới thông qua một đám mây điểm nền tĩnh và các quỹ đạo Gaussian 3D cho từng đối tượng. Biểu diễn này linh hoạt, không phụ thuộc vào loại đối tượng và ghi lại cả đường đi và sự chiếm chỗ 3D xác suất của đối tượng theo thời gian. Các điều khiển 4D này được biến đổi thành tín hiệu điều kiện để điều khiển một mô hình khuếch tán video đã được huấn luyện trước (Wan2.1-14B) thông qua một `GeoAdapter` nhẹ. Để khắc phục vấn đề thiếu dữ liệu, VerseCrafter còn phát triển một công cụ tự động để trích xuất các điều khiển 4D cần thiết từ các video thực tế, tạo ra bộ dữ liệu `VerseControl4D` quy mô lớn và đa dạng.

### Main Results:
VerseCrafter tạo ra các video có độ chân thực cao, nhất quán về góc nhìn và tuân thủ chính xác các động lực được chỉ định. Mô hình này theo dõi chuyển động mong muốn tốt hơn so với các phương pháp hiện có như Yume và Uni3C, đồng thời khớp chặt chẽ với video ground-truth. Khả năng kiểm soát được cải thiện đáng kể nhờ không gian điều khiển `4D Geometric Control` thống nhất, cho phép điều khiển camera và chuyển động đa đối tượng một cách rõ ràng và chính xác.

### Conclusion & Future Works:
VerseCrafter thiết lập một phương pháp mới để tạo video thực tế, động lực với khả năng kiểm soát hình học 4D chính xác và thống nhất. Việc giới thiệu biểu diễn `4D Geometric Control` và bộ dữ liệu `VerseControl4D` tự động được chú thích đã giải quyết các thách thức lớn trong việc điều khiển động lực đa đối tượng và thiếu dữ liệu. Hướng nghiên cứu tiếp theo có thể mở rộng khả năng kiểm soát động lực phức tạp hơn hoặc tích hợp với các tương tác thời gian thực.

### Brainstorming Space:
#### 1. Publish Papers:
1. Phát triển phương pháp để tinh chỉnh các quỹ đạo Gaussian 3D dựa trên phản hồi của người dùng hoặc tương tác vật lý để tạo ra các cảnh động lực học phức tạp hơn.
2. Mở rộng mô hình để tự động suy luận và tạo ra các điều khiển 4D Geometric Control cho các vật thể mới không có trong dữ liệu huấn luyện ban đầu.
3. Nghiên cứu cách tích hợp `VerseCrafter` vào các môi trường mô phỏng thực tế ảo để tạo ra trải nghiệm tương tác với các đối tượng động.

#### 2. Patent:
1. Hệ thống tạo video động có thể điều khiển trên điện thoại thông minh, cho phép người dùng định nghĩa quỹ đạo 3D và chuyển động camera cho các đối tượng trong video được quay bằng điện thoại.
2. Ứng dụng di động sử dụng công nghệ `4D Geometric Control` để chỉnh sửa video, cho phép người dùng thay đổi chuyển động của đối tượng và camera một cách trực quan trên màn hình cảm ứng, với sự nhất quán về 3D.
3. Phương pháp tích hợp camera điện thoại và cảm biến chiều sâu (ví dụ: LiDAR trên iPhone) để tự động tạo đám mây điểm nền và quỹ đạo Gaussian 3D cho các đối tượng trong cảnh quay, sau đó sử dụng dữ liệu này để tái tạo hoặc chỉnh sửa video động lực.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.05138](https://huggingface.co/papers/2601.05138) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.05138](https://arxiv.org/abs/2601.05138) |
| PDF Download | [https://arxiv.org/pdf/2601.05138.pdf](https://arxiv.org/pdf/2601.05138.pdf) |
| Github Repository | N/A |

--- 

## 11. The Illusion of Specialization: Unveiling the Domain-Invariant "Standing Committee" in Mixture-of-Experts Models

**Tác giả:** Yan Wang, Yitao Xu, Nanhan Shen, Jinyan Su, Jimin Huang, Zining Zhu

**Xuất bản lúc:** 2026-01-06

**Tag:** Mixture-of-Experts (MoE), Large Language Models (LLMs), Model Interpretation, Sparse Routing, Expert Specialization

### Main Problem:
Giả định phổ biến rằng các mô hình Mixture-of-Experts (MoE) đạt được khả năng chuyên môn hóa miền thông qua định tuyến thưa thớt bị nghi ngờ. Các nghiên cứu trước đây về MoE tập trung vào sự chuyên môn hóa của từng chuyên gia, nhưng chưa rõ liệu các chuyên gia có tự tổ chức thành các nhóm ổn định, được kích hoạt đồng thời xuyên suốt các nhiệm vụ hay không, gây ra sự thiếu hiệu quả trong đào tạo do các hàm mất mát cân bằng tải đi ngược lại xu hướng tự nhiên của mô hình.

### Main Idea:
Bài báo giới thiệu COMMITTEEAUDIT, một khung phân tích hậu nghiệm để kiểm toán tổ chức cấu trúc cấp nhóm của các mô hình MoE đã được huấn luyện trước. Khung này phân tích hành vi định tuyến ở cấp độ nhóm chuyên gia thay vì từng chuyên gia riêng lẻ, sử dụng xếp hạng tối ưu Pareto và chẩn đoán ổn định để định lượng sự tổ chức của nhóm chuyên gia xuyên suốt các miền khác nhau. Mục tiêu là khám phá một "Standing Committee" (Ủy ban Thường trực) bất biến theo miền.

### Main Results:
*   Phát hiện một "Standing Committee" bất biến theo miền: một liên minh nhỏ gọn gồm các chuyên gia được định tuyến liên tục chiếm phần lớn khối lượng định tuyến trên các miền, lớp và ngân sách định tuyến, ngay cả khi kiến trúc đã bao gồm các chuyên gia chia sẻ.
*   Phân tích định tính cho thấy Standing Committee neo giữ cấu trúc suy luận và cú pháp, trong khi các chuyên gia ngoại vi xử lý kiến thức chuyên biệt theo miền.
*   Tiết lộ một thiên hướng cấu trúc mạnh mẽ đối với tính toán tập trung, cho thấy sự chuyên môn hóa trong các mô hình MoE ít phổ biến hơn nhiều so với suy nghĩ thông thường.
*   Chỉ ra rằng các mục tiêu đào tạo hiện tại, như các hàm mất mát cân bằng tải, có thể đang đi ngược lại con đường tối ưu hóa tự nhiên của mô hình, do đó hạn chế hiệu quả đào tạo và hiệu suất.
*   COMMITTEEAUDIT là một framework độc lập với mô hình, định lượng tổ chức chuyên gia cấp nhóm vượt ra ngoài các thống kê kích hoạt cá nhân.
*   Phát hiện một tổ chức cốt lõi-ngoại vi, nơi các thành viên ủy ban neo giữ các cấu trúc logic và cú pháp, trong khi các chuyên gia ngoại vi quản lý kiến thức chuyên biệt theo miền.

### Conclusion & Future Works:
Bài báo thách thức quan điểm phổ biến về sự chuyên môn hóa của MoE bằng cách chứng minh sự tồn tại của một "Standing Committee" bất biến theo miền, cho thấy một thiên hướng cấu trúc mạnh mẽ hướng tới tính toán tập trung. Điều này ngụ ý rằng các mục tiêu đào tạo hiện có có thể không tối ưu và thậm chí còn cản trở quá trình tối ưu hóa tự nhiên của mô hình. Hướng nghiên cứu tiếp theo có thể bao gồm việc phát triển các mục tiêu đào tạo mới và kiến trúc MoE tận dụng hoặc thích ứng với thiên hướng tính toán tập trung tự nhiên này, thay vì cố gắng loại bỏ nó, nhằm cải thiện hiệu quả và hiệu suất.

### Brainstorming Space:
#### 1. Publish Papers:
*   Thiết kế và thử nghiệm các hàm mất mát cân bằng tải mới trong MoE nhằm tận dụng "Standing Committee" thay vì thúc đẩy việc sử dụng đồng đều các chuyên gia.
*   Nghiên cứu quá trình hình thành "Standing Committee" trong các giai đoạn đào tạo khác nhau để hiểu rõ hơn về các yếu tố ảnh hưởng đến sự xuất hiện của nó.
*   Mở rộng COMMITTEEAUDIT để phân tích sự cộng tác giữa các chuyên gia trong MoE trên nhiều loại nhiệm vụ và miền dữ liệu đa dạng hơn.

#### 2. Patent:
*   Một hệ thống định tuyến MoE thích ứng cho thiết bị di động có khả năng nhận diện và ưu tiên kích hoạt "Standing Committee" để xử lý các tác vụ ngôn ngữ phổ biến, giảm thiểu độ trễ cho các ứng dụng AI trên điện thoại.
*   Một phương pháp quản lý tài nguyên thông minh cho chip AI trên smartphone, tự động phân bổ tài nguyên tính toán dựa trên việc xác định "Standing Committee" và các chuyên gia ngoại vi, tối ưu hóa năng lượng và hiệu suất.
*   Một kiến trúc MoE được tinh chỉnh cho điện thoại thông minh, trong đó "Standing Committee" được tối ưu hóa để luôn hoạt động hiệu quả cho các chức năng cốt lõi của trợ lý AI, trong khi các chuyên gia khác được kích hoạt có chọn lọc cho các yêu cầu cụ thể của người dùng.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.03425](https://huggingface.co/papers/2601.03425) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.03425](https://arxiv.org/abs/2601.03425) |
| PDF Download | [https://arxiv.org/pdf/2601.03425.pdf](https://arxiv.org/pdf/2601.03425.pdf) |
| Github Repository | N/A |

--- 

## 12. Agent-as-a-Judge

**Tác giả:** Runyang You, Hongru Cai, Caiqi Zhang, Qiancheng Xu, Meng Liu, Tiezheng Yu, Yongqi Li, Wenjie Li

**Xuất bản lúc:** 2026-01-08

**Tag:** Agent-as-a-Judge, LLM-as-a-Judge, AI Evaluation, Multi-Agent Systems, Survey

### Main Problem:
Bài báo này chỉ ra rằng mặc dù LLM-as-a-Judge đã cách mạng hóa đánh giá AI, nhưng độ tin cậy của nó bị hạn chế khi đánh giá các tác vụ ngày càng phức tạp, chuyên biệt và nhiều bước. Các vấn đề bao gồm sự thiên vị cố hữu, khả năng suy luận nông cạn một lần và không thể xác minh đánh giá dựa trên các quan sát trong thế giới thực, dẫn đến các đánh giá không chính xác và thiếu chi tiết.

### Main Idea:
Bài báo này trình bày một khảo sát toàn diện đầu tiên về sự chuyển đổi từ LLM-as-a-Judge sang Agent-as-a-Judge. Giải pháp đề xuất là Agent-as-a-Judge, nơi các tác nhân (agents) sử dụng khả năng lập kế hoạch, xác minh bằng công cụ, cộng tác đa tác nhân và bộ nhớ liên tục để cho phép đánh giá mạnh mẽ hơn, có thể xác minh và chi tiết hơn. Mục tiêu là cung cấp một khuôn khổ thống nhất để điều hướng lĩnh vực đang thay đổi này, xác định các chiều chính của sự thay đổi mô hình, thiết lập một phân loại phát triển, tổ chức các phương pháp luận cốt lõi, khảo sát các ứng dụng và phân tích các thách thức để đưa ra lộ trình nghiên cứu.

### Main Results:
Là một bài báo khảo sát, các kết quả chính là những đóng góp của nghiên cứu này. Bài báo đã xác định và mô tả sự chuyển đổi từ LLM-as-a-Judge sang Agent-as-a-Judge, tóm tắt xu hướng phát triển của các tác nhân đánh giá thành ba giai đoạn tiến bộ: Procedural, Reactive và Self-Evolving. Nghiên cứu cũng tổ chức các phương pháp luận cốt lõi thành năm phần chính (cộng tác đa tác nhân, lập kế hoạch, tích hợp công cụ, bộ nhớ và cá nhân hóa, các mô hình tối ưu hóa) và khảo sát các ứng dụng của chúng trong các lĩnh vực chung và chuyên nghiệp. Cuối cùng, bài báo phân tích các thách thức biên giới và xác định các hướng nghiên cứu đầy hứa hẹn, cung cấp một lộ trình chiến lược cho thế hệ đánh giá AI mạnh mẽ và có thể xác minh tiếp theo.

### Conclusion & Future Works:
Agent-as-a-Judge đại diện cho một bước tiến quan trọng trong đánh giá AI, vượt qua các hạn chế của LLM-as-a-Judge bằng cách sử dụng các tác nhân có khả năng lập kế hoạch, xác minh bằng công cụ, cộng tác và bộ nhớ. Tương lai của Agent-as-a-Judge nằm ở việc phát triển các hệ thống Self-Evolving có khả năng tự tinh chỉnh các thành phần bên trong và điều chỉnh quy tắc đánh giá linh hoạt, mặc dù vẫn còn thách thức trong việc đảm bảo sự ổn định trong quá trình tự sửa đổi. Bài báo cung cấp một lộ trình rõ ràng để phát triển thế hệ tiếp theo của các hệ thống đánh giá bằng tác nhân mạnh mẽ và có thể xác minh.

### Brainstorming Space:
#### 1. Publish Papers:
1. Nghiên cứu các chiến lược mới để phát triển các Agent-as-a-Judge tự tiến hóa (Self-Evolving) có khả năng tự động học và điều chỉnh các tiêu chí đánh giá theo thời gian mà vẫn đảm bảo độ tin cậy.
2. Khám phá các phương pháp tích hợp công cụ (tool integration) đa dạng và thông minh hơn cho Agent-as-a-Judge để xác minh các tác vụ phức tạp đòi hỏi tương tác với môi trường bên ngoài thực tế hoặc dữ liệu đa phương thức.
3. Thiết kế các khuôn khổ cộng tác đa tác nhân (multi-agent collaboration) có khả năng phân công vai trò động và tối ưu hóa quy trình tranh luận để giảm thiểu thiên vị và nâng cao chất lượng đánh giá cuối cùng.
#### 2. Patent:
1. Hệ thống đánh giá hiệu suất ứng dụng di động thông minh sử dụng Agent-as-a-Judge để mô phỏng hành vi người dùng, kiểm tra các chức năng và xác minh tính ổn định trên nhiều thiết bị điện thoại khác nhau.
2. Công nghệ trợ lý cá nhân trên điện thoại di động tích hợp Agent-as-a-Judge để kiểm tra tính chính xác của thông tin do LLM tạo ra, đặc biệt trong các lĩnh vực nhạy cảm như tư vấn tài chính hoặc y tế thông qua các công cụ tìm kiếm và cơ sở dữ liệu xác thực.
3. Ứng dụng điện thoại thông minh cho việc đánh giá chất lượng ảnh hoặc video được tạo bởi AI, sử dụng Agent-as-a-Judge với các công cụ tích hợp như phân tích pixel và đối chiếu dữ liệu hình ảnh để xác định tính chân thực và lỗi tạo sinh.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.05111](https://huggingface.co/papers/2601.05111) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.05111](https://arxiv.org/abs/2601.05111) |
| PDF Download | [https://arxiv.org/pdf/2601.05111.pdf](https://arxiv.org/pdf/2601.05111.pdf) |
| Github Repository | [https://github.com/ModalityDance/Awesome-Agent-as-a-Judge](https://github.com/ModalityDance/Awesome-Agent-as-a-Judge) |

--- 

## 13. Plenoptic Video Generation

**Tác giả:** Xiao Fu, Shitao Tang, Min Shi, Xian Liu, Jinwei Gu, Ming-Yu Liu, Dahua Lin, Chen-Hsuan Lin

**Xuất bản lúc:** 2026-01-08

**Tag:** Plenoptic Video, Generative Video Re-rendering, Autoregressive, Multi-view Consistency, Spatio-temporal Memory, Camera Control, Diffusion, Video Generation

### Main Problem:
Các phương pháp tái tạo video tạo sinh được điều khiển bằng camera hiện tại gặp khó khăn trong việc duy trì tính nhất quán không gian-thời gian (spatio-temporal consistency) và đồng bộ hóa góc nhìn (view synchronization) trong các kịch bản đa góc nhìn, đặc biệt ở những vùng "ảo ảnh" (hallucinated regions) không nhìn thấy từ góc nhìn nguồn. Điều này là do tính ngẫu nhiên vốn có của các mô hình tạo sinh và bộ nhớ không gian tầm xa hạn chế, dẫn đến sự sai lệch hình học và mất đồng bộ góc nhìn.

### Main Idea:
Bài báo giới thiệu PlenopticDreamer, một framework tạo sinh để tái tạo video điều khiển bằng camera. Giải pháp này đồng bộ hóa các "ảo ảnh" tạo sinh để duy trì bộ nhớ không gian-thời gian dài hạn trên các góc nhìn chồng chéo. Ý tưởng cốt lõi là huấn luyện một mô hình điều kiện video đa đầu vào - đơn đầu ra (multi-in-single-out) theo cách tự hồi quy (autoregressive), được hỗ trợ bởi một chiến lược truy xuất video có hướng dẫn bằng camera (dựa trên 3D FOV) để chọn các video nổi bật từ các thế hệ trước làm đầu vào điều kiện. Ngoài ra, quá trình huấn luyện còn tích hợp progressive context-scaling để cải thiện sự hội tụ, self-conditioning để tăng cường sự mạnh mẽ chống lại suy giảm hình ảnh tầm xa do tích lũy lỗi, và cơ chế long-video conditioning để hỗ trợ tạo video dài hơn.

### Main Results:
PlenopticDreamer đạt hiệu suất state-of-the-art trong việc tái tạo video trên các benchmark Basic và Agibot. Framework này mang lại khả năng đồng bộ hóa góc nhìn vượt trội, hình ảnh chất lượng cao (high-fidelity visuals), kiểm soát camera chính xác và các biến đổi góc nhìn đa dạng (ví dụ: third-person sang third-person, hoặc head-view sang gripper-view trong thao tác robot). Nó cũng hỗ trợ tạo ra các chuỗi video dài.

### Conclusion & Future Works:
PlenopticDreamer là framework tái tạo video tạo sinh điều khiển bằng camera đầu tiên tích hợp bộ nhớ không gian-thời gian dài hạn, giải quyết hiệu quả các thách thức về tính nhất quán đa góc nhìn mà các phương pháp trước đây gặp phải. Thành công của nó trong việc đạt được sự đồng bộ hóa góc nhìn, độ trung thực hình ảnh và kiểm soát camera chính xác mở ra nhiều ứng dụng tiềm năng trong sáng tạo nội dung và AI thực thể. Bài báo không nêu rõ các hướng nghiên cứu tương lai cụ thể ngoài những khả năng đã được framework thể hiện.

### Brainstorming Space:
#### 1. Publish Papers:
1. Nghiên cứu ảnh hưởng của các phương pháp mã hóa thông tin camera (ví dụ: biểu diễn ma trận chiếu trực tiếp) lên hiệu suất và độ chính xác của PlenopticDreamer trong các môi trường phức tạp.
2. Mở rộng PlenopticDreamer để hỗ trợ tương tác người dùng theo thời gian thực, cho phép người dùng điều khiển camera và chỉnh sửa nội dung video trong quá trình tái tạo.
3. Phát triển một mô hình đánh giá tự động mới cho tính nhất quán không gian-thời gian trong video đa góc nhìn, vượt ra ngoài các chỉ số chất lượng hình ảnh truyền thống.

#### 2. Patent:
1. Hệ thống tái tạo video đa góc nhìn trên điện thoại di động, cho phép người dùng quay một đoạn video và sau đó dễ dàng thay đổi quỹ đạo camera hoặc góc nhìn của video đó thông qua giao diện cảm ứng trực quan trên điện thoại.
2. Công nghệ tạo hiệu ứng "quay lại" tự động cho video trên điện thoại, cho phép người dùng chọn một đối tượng hoặc khu vực trong video đã quay và xem nó từ các góc độ mới không có trong bản gốc, hữu ích cho việc xem lại các khoảnh khắc thể thao hoặc sự kiện.
3. Ứng dụng điện thoại thông minh tích hợp PlenopticDreamer để tạo ra các trải nghiệm thực tế tăng cường (AR) tùy chỉnh, nơi video quay bằng camera điện thoại có thể được tái tạo và hòa trộn với các yếu tố ảo từ nhiều góc độ khác nhau.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.05239](https://huggingface.co/papers/2601.05239) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.05239](https://arxiv.org/abs/2601.05239) |
| PDF Download | [https://arxiv.org/pdf/2601.05239.pdf](https://arxiv.org/pdf/2601.05239.pdf) |
| Github Repository | N/A |

--- 

## 14. CoV: Chain-of-View Prompting for Spatial Reasoning

**Tác giả:** Haoyu Zhao, Akide Liu, Zeyu Zhang, Weijie Wang, Feng Chen, Ruihan Zhu, Gholamreza Haffari, Bohan Zhuang

**Xuất bản lúc:** 2026-01-08

**Tag:** Embodied Question Answering, Spatial Reasoning, VLM, Prompting, Test-time Reasoning, Active Exploration

### Main Problem:
Các mô hình thị giác-ngôn ngữ (VLM) hiện tại dành cho trả lời câu hỏi thực thể (EQA) trong môi trường 3D bị giới hạn bởi một tập hợp các góc nhìn cố định và hữu hạn, điều này cản trở khả năng thu thập ngữ cảnh liên quan đến câu hỏi và thực hiện suy luận không gian phức tạp, đặc biệt khi ngữ cảnh phân tán hoặc bị che khuất.

### Main Idea:
Bài báo đề xuất Chain-of-View (CoV) prompting, một framework suy luận không cần huấn luyện, hoạt động tại thời điểm kiểm tra (test-time) để biến VLM thành một công cụ suy luận góc nhìn chủ động thông qua quá trình khám phá từ tổng thể đến chi tiết. CoV bao gồm hai giai đoạn: (i) Coarse-grained View Selection, nơi một agent chọn các góc nhìn neo liên quan đến câu hỏi và loại bỏ các khung hình thừa, và (ii) Fine-grained View Adjustment, nơi agent điều chỉnh góc nhìn một cách tỉ mỉ bằng cách lặp lại các suy luận và thực hiện các hành động camera rời rạc (ví dụ: xoay, di chuyển) để thu thập bằng chứng hình ảnh phân biệt và giải quyết sự mơ hồ về không gian.

### Main Results:
CoV đạt được cải thiện trung bình +11.56% về LLM-Match trên bộ dữ liệu OpenEQA, với mức tăng tối đa +13.62% trên Qwen3-VL-Flash. Framework này cũng thể hiện khả năng mở rộng tại thời điểm kiểm tra (test-time scaling): tăng ngân sách hành động tối thiểu giúp cải thiện trung bình thêm +2.51%, đạt đỉnh +3.73% trên Gemini-2.5-Flash. CoV còn cho thấy hiệu suất mạnh mẽ trên ScanQA (116 CIDEr / 31.9 EM@1) và SQA3D (51.1 EM@1).

### Conclusion & Future Works:
CoV là một chiến lược hiệu quả, độc lập với mô hình để cải thiện khả năng suy luận không gian trong EQA 3D mà không cần huấn luyện bổ sung, thông qua việc lựa chọn góc nhìn phù hợp với câu hỏi và tìm kiếm góc nhìn mở. Kết quả cho thấy tiềm năng của các chiến lược mở rộng tại thời điểm kiểm tra để nâng cao hiểu biết về cảnh vật mà không yêu cầu huấn luyện mô hình hay tinh chỉnh tập dữ liệu, làm cho framework trở nên mạnh mẽ và dễ thích nghi trên các tác vụ và miền 3D đa dạng.

### Brainstorming Space:
#### 1. Publish Papers:
1.  Nghiên cứu áp dụng CoV vào các tác vụ robot thực tế như định vị và xây dựng bản đồ đồng thời (SLAM) để tăng cường độ chính xác của bản đồ trong các môi trường phức tạp.
2.  Khám phá việc tích hợp CoV với các mô hình thế giới được xây dựng tự động để cho phép suy luận không gian dài hạn và lập kế hoạch đường đi tối ưu hơn.
3.  Phát triển một phương pháp CoV thích ứng tự động điều chỉnh chiến lược khám phá dựa trên độ phức tạp của câu hỏi và thông tin đã thu thập được.
#### 2. Patent:
1.  Hệ thống hỗ trợ quan sát thông minh cho camera điện thoại, tự động đề xuất và thực hiện các điều chỉnh góc nhìn (xoay, di chuyển) để thu thập thông tin hình ảnh đầy đủ nhất cho một đối tượng hoặc khu vực được người dùng chỉ định.
2.  Công nghệ trợ lý thực tế ảo (AR) trên điện thoại, sử dụng CoV để hướng dẫn người dùng di chuyển camera của họ nhằm tìm kiếm các vật phẩm cụ thể trong nhà, cung cấp mô tả không gian chi tiết và dẫn đường trực quan.
3.  Tính năng "khám phá cảnh quan" cho ứng dụng bản đồ hoặc du lịch trên điện thoại, cho phép người dùng đặt câu hỏi về một địa điểm và CoV sẽ mô phỏng việc di chuyển qua các góc nhìn để cung cấp câu trả lời không gian chi tiết như thể họ đang ở đó.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.05172](https://huggingface.co/papers/2601.05172) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.05172](https://arxiv.org/abs/2601.05172) |
| PDF Download | [https://arxiv.org/pdf/2601.05172.pdf](https://arxiv.org/pdf/2601.05172.pdf) |
| Github Repository | [https://github.com/ziplab/CoV](https://github.com/ziplab/CoV) |

--- 

## 15. DiffCoT: Diffusion-styled Chain-of-Thought Reasoning in LLMs

**Tác giả:** Shidong Cao, Hongzhan Lin, Yuxuan Gu, Ziyang Luo, Jing Ma

**Xuất bản lúc:** 2026-01-07

**Tag:** Diffusion, Chain-of-Thought (CoT), LLMs, Reasoning, Error Correction, Exposure Bias, Preference Optimization

### Main Problem:
Các mô hình ngôn ngữ lớn (LLMs) khi sử dụng lập luận Chain-of-Thought (CoT) để giải quyết các vấn đề toán học đa bước thường dễ bị ảnh hưởng bởi lỗi tích lũy và sai lệch phơi nhiễm (exposure bias). Các lỗi ban đầu có thể lan truyền không thể đảo ngược qua quá trình giải mã tự hồi quy, dẫn đến kết quả cuối cùng không chính xác do mỗi bước sau phụ thuộc vào các bước trước đó, và mô hình chỉ được huấn luyện trên các tiền tố đúng nhưng phải đối mặt với các tiền tố có lỗi trong quá trình suy luận.

### Main Idea:
Bài báo đề xuất DIFFCOT, một framework CoT theo phong cách diffusion, cải cách lập luận CoT thành một quá trình khử nhiễu lặp đi lặp lại. DIFFCOT tích hợp các nguyên tắc diffusion ở cấp độ bước lập luận thông qua cơ chế cửa sổ trượt (sliding-window mechanism), cho phép tạo và sửa chữa các bước trung gian một cách thống nhất, đồng thời vẫn giữ được tính tự hồi quy ở cấp độ token. Để duy trì tính nhất quán về nhân quả, bài báo còn giới thiệu một lịch trình nhiễu diffusion có tính nhân quả (causal diffusion noise schedule) tôn trọng cấu trúc thời gian của chuỗi lập luận.

### Main Results:
DIFFCOT liên tục vượt trội hơn các phương pháp tối ưu hóa sở thích (CoT preference optimization) hiện có. Các thí nghiệm rộng rãi trên ba bộ dữ liệu chuẩn về lập luận CoT đa bước cho thấy DIFFCOT đạt được sự cải thiện đáng kể về độ mạnh mẽ và khả năng sửa lỗi trong lập luận CoT so với các phương pháp State-of-The-Art (SoTA).

### Conclusion & Future Works:
DIFFCOT trình bày một framework lập luận CoT mới dựa trên diffusion, giải quyết hiệu quả vấn đề sai lệch phơi nhiễm và tích lũy lỗi. Bằng cách tái định dạng quá trình suy luận thành một quy trình khử nhiễu lặp lại, nó mang lại khả năng sửa lỗi hồi cứu và sự mạnh mẽ hơn cho LLM. Tác giả tin rằng DIFFCOT có thể thiết lập một mô hình thống nhất và thích ứng cho lập luận CoT trong LLMs.

### Brainstorming Space:
#### 1. Publish Papers:
*   Nghiên cứu ứng dụng DIFFCOT cho các loại nhiệm vụ lập luận phức tạp khác ngoài toán học, ví dụ như lập luận logic hoặc khoa học, để đánh giá tính tổng quát của phương pháp.
*   Khám phá các phương pháp mới để sinh ra nhiễu và lịch trình nhiễu cho DIFFCOT nhằm tối ưu hóa quá trình khử nhiễu, đặc biệt là với các loại lỗi lập luận đặc thù.
*   Phát triển phiên bản DIFFCOT kết hợp với học tăng cường (Reinforcement Learning) để cải thiện quá trình tối ưu hóa sở thích và hướng dẫn mô hình đến các chuỗi lập luận hiệu quả hơn.

#### 2. Patent:
*   Hệ thống trợ lý ảo trên điện thoại thông minh tích hợp DIFFCOT để cung cấp các giải pháp toán học chi tiết, có khả năng tự động sửa các bước sai lầm trong quá trình giải quyết.
*   Tính năng soạn thảo văn bản thông minh cho điện thoại, nơi DIFFCOT phân tích và đề xuất chỉnh sửa các chuỗi lập luận trong văn bản (ví dụ: email, báo cáo) để cải thiện tính logic và chính xác.
*   Ứng dụng học tập trên điện thoại cho phép người dùng nhập các bước giải bài tập và sử dụng DIFFCOT để đánh giá, chỉ ra và sửa chữa các lỗi trong chuỗi suy nghĩ của người dùng.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.03559](https://huggingface.co/papers/2601.03559) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.03559](https://arxiv.org/abs/2601.03559) |
| PDF Download | [https://arxiv.org/pdf/2601.03559.pdf](https://arxiv.org/pdf/2601.03559.pdf) |
| Github Repository | N/A |

--- 

## 16. DocDancer: Towards Agentic Document-Grounded Information Seeking

**Tác giả:** Qintong Zhang, Xinjie Lv, Jialong Wu, Baixuan Li, Zhengwei Tao, Guochen Yan, Huanyao Zhang, Bin Wang, Jiahao Xu, Haitao Mi, Wentao Zhang

**Xuất bản lúc:** 2026-01-08

**Tag:** DocQA, Agentic AI, Information Seeking, Tool Utilization, Data Synthesis, Open-Source LLM

### Main Problem:
Các tác nhân DocQA hiện tại thiếu khả năng sử dụng công cụ hiệu quả, chủ yếu phụ thuộc vào các mô hình mã nguồn đóng và gặp phải sự khan hiếm dữ liệu đào tạo chất lượng cao cho các hành vi tác nhân tự chủ. Các phương pháp DocQA truyền thống bị giới hạn bởi độ dài đầu vào và khả năng xử lý các tài liệu dài, đa phương thức.

### Main Idea:
Bài báo giới thiệu DocDancer, một tác nhân tài liệu mã nguồn mở được đào tạo end-to-end. Nghiên cứu đề xuất một khung tác nhân điều khiển bằng công cụ mô hình hóa rõ ràng quá trình khám phá và hiểu tài liệu, sử dụng các công cụ "Search" để thu thập thông tin toàn cục và "Read" để hiểu cục bộ. Để giải quyết vấn đề thiếu dữ liệu đào tạo chất lượng cao, nghiên cứu giới thiệu một quy trình tổng hợp dữ liệu "Exploration-then-Synthesis", tạo ra các cặp câu hỏi-trả lời thông qua tương tác lặp đi lặp lại và suy luận đa quan sát trên các tài liệu nguồn.

### Main Results:
DocDancer, được đào tạo trên dữ liệu tổng hợp, đã chứng minh hiệu quả trên hai điểm chuẩn hiểu tài liệu ngữ cảnh dài là MMLongBench-Doc và DocBench. Khi được tích hợp với một mô hình ngôn ngữ lớn (LLM) độc quyền, khung này đạt được hiệu suất state-of-the-art. Các phiên bản DocDancer được xây dựng trên các mô hình mã nguồn mở (Qwen3-4B-Thinking và Qwen3-30B-A3B-Thinking) cũng đạt kết quả cạnh tranh, với mô hình 30B-A3B đạt state-of-the-art trong một số thiết lập chỉ với 5.000 mẫu đào tạo. Các phân tích sâu hơn cung cấp những hiểu biết có giá trị về thiết kế công cụ tác nhân và vai trò của dữ liệu tổng hợp.

### Conclusion & Future Works:
Nghiên cứu đóng góp một khung tác nhân DocQA hiệu quả dựa trên nguyên tắc tìm kiếm thông tin và một quy trình tổng hợp dữ liệu tự động tạo ra dữ liệu đào tạo chất lượng cao cho việc học hành vi tác nhân. Các kết quả thực nghiệm chứng minh hiệu quả vượt trội của DocDancer và cung cấp những hiểu biết thực tế để thiết kế các hệ thống tác nhân hiệu quả. Hướng nghiên cứu tiếp theo có thể tập trung vào việc mở rộng khả năng của DocDancer cho các loại tài liệu đa dạng hơn và các tác vụ tìm kiếm thông tin phức tạp hơn.

### Brainstorming Space:
#### 1. Publish Papers:
- Phát triển một khung tác nhân DocQA sử dụng các mô hình ngôn ngữ nhỏ hơn để giảm chi phí tính toán mà vẫn duy trì hiệu suất cao.
- Nghiên cứu tác động của việc kết hợp các công cụ chuyên biệt hóa cho từng loại tài liệu (ví dụ: công cụ cho bảng biểu, công cụ cho biểu đồ) vào khung DocDancer.
- Khám phá các phương pháp tổng hợp dữ liệu tự động mới để tạo ra các kịch bản tương tác phức tạp hơn, đòi hỏi suy luận đa bước sâu rộng hơn.

#### 2. Patent:
- Hệ thống trợ lý tài liệu thông minh trên điện thoại có khả năng đọc hiểu và trả lời câu hỏi từ bất kỳ tài liệu PDF nào, sử dụng công cụ Search và Read tích hợp.
- Phương pháp tạo dữ liệu đào tạo tự động cho các ứng dụng đọc hiểu tài liệu trên thiết bị di động, cho phép các mô hình DocQA được tùy chỉnh nhanh chóng.
- Ứng dụng điện thoại thông minh cho phép người dùng chụp ảnh hoặc quét tài liệu, sau đó sử dụng tác nhân DocDancer để trích xuất thông tin và tóm tắt theo yêu cầu.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.05163](https://huggingface.co/papers/2601.05163) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.05163](https://arxiv.org/abs/2601.05163) |
| PDF Download | [https://arxiv.org/pdf/2601.05163.pdf](https://arxiv.org/pdf/2601.05163.pdf) |
| Github Repository | N/A |

--- 

## 17. Re-Align: Structured Reasoning-guided Alignment for In-Context Image Generation and Editing

**Tác giả:** Runze He, Yiji Cheng, Tiankai Hang, Zhimin Li, Yu Xu, Zijin Yin, Shiyi Zhang, Wenxun Dai, Penghui Du, Ao Ma, Chunyu Wang, Qinglin Lu, Jizhong Han, Jiao Dai

**Xuất bản lúc:** 2026-01-08

**Tag:** Diffusion, Reinforcement Learning, In-Context Learning, Multimodal, Image Generation, Image Editing, Chain-of-Thought

### Main Problem:
Các mô hình multimodal thống nhất hiện tại gặp khó khăn trong việc thực hiện chính xác ý định của người dùng khi tạo và chỉnh sửa ảnh theo ngữ cảnh (ICGE) từ các prompt đan xen văn bản và hình ảnh phức tạp. Mặc dù các mô hình này có khả năng hiểu hứa hẹn, nhưng sức mạnh đó thường không thể chuyển giao hiệu quả sang quá trình tạo ảnh, dẫn đến sự không khớp giữa khả năng lý luận và hình ảnh được tạo ra.

### Main Idea:
Re-Align giới thiệu một khung thống nhất nhằm thu hẹp khoảng cách giữa khả năng hiểu và tạo ảnh thông qua "structured reasoning-guided alignment". Giải pháp này bao gồm:
1.  **In-Context Chain-of-Thought (IC-CoT):** Một mô hình lý luận có cấu trúc phân tách rõ ràng hướng dẫn ngữ nghĩa (semantic guidance) và liên kết tham chiếu (reference association). Semantic guidance cung cấp một văn bản mục tiêu rõ ràng (dưới dạng chú thích ảnh đầu ra), giúp đơn giản hóa tác vụ, trong khi reference association phân tích vai trò của từng ảnh tham chiếu để ngăn chặn sự nhầm lẫn.
2.  **Chương trình huấn luyện Reinforcement Learning (RL) hiệu quả:** Sử dụng Group Relative Policy Optimization (GRPO) với một phần thưởng thay thế (surrogate reward) để đo lường mức độ căn chỉnh giữa văn bản lý luận có cấu trúc và hình ảnh được tạo ra. Chiến lược "reasoning-induced diversity" cũng được đề xuất để cải thiện sự đa dạng mẫu và ổn định quá trình huấn luyện.
3.  **Tập dữ liệu Re-Align-410K:** Một pipeline tự động để xây dựng và lọc dữ liệu chất lượng cao với các chú thích IC-CoT, hỗ trợ quá trình huấn luyện mô hình.

### Main Results:
Re-Align đạt hiệu suất vượt trội so với các phương pháp cạnh tranh có quy mô mô hình và tài nguyên tương đương trên cả hai nhiệm vụ tạo ảnh và chỉnh sửa ảnh theo ngữ cảnh. Các thử nghiệm cho thấy Re-Align cải thiện đáng kể khả năng căn chỉnh giữa lý luận có cấu trúc và hình ảnh được tạo ra, giải quyết vấn đề không khớp của các mô hình trước đây.

### Conclusion & Future Works:
Bài báo kết luận Re-Align là một framework mạnh mẽ cho In-Context Image Generation and Editing, đạt được hiệu suất tiên tiến (SOTA) bằng cách tận dụng cơ chế lý luận có cấu trúc (IC-CoT) và chiến lược huấn luyện dựa trên Reinforcement Learning. Các hướng nghiên cứu tiếp theo có thể bao gồm việc khám phá việc mở rộng IC-CoT cho các tác vụ đa phương thức phức tạp hơn, hoặc tinh chỉnh thêm các cơ chế phần thưởng và đa dạng trong RL để nâng cao hơn nữa chất lượng và sự phù hợp của hình ảnh được tạo ra.

### Brainstorming Space:
#### 1. Publish Papers:
1. Nghiên cứu cách áp dụng IC-CoT cho các tác vụ tạo video hoặc tạo mô hình 3D từ các prompt đan xen hình ảnh và văn bản.
2. Phát triển các chiến lược phần thưởng RL tiên tiến hơn, có thể tích hợp các yếu tố phản hồi từ con người để tinh chỉnh căn chỉnh lý luận-hình ảnh.
3. Khám phá việc kết hợp các mô hình nền tảng ngôn ngữ lớn (LLM) mạnh mẽ hơn với Re-Align để tăng cường khả năng lý luận ngữ nghĩa và hiểu ý định người dùng trong bối cảnh multimodal.

#### 2. Patent:
1. Một ứng dụng chỉnh sửa ảnh thông minh trên điện thoại di động cho phép người dùng nhập các prompt đan xen hình ảnh và văn bản phức tạp, sử dụng công nghệ Re-Align để tạo ra các chỉnh sửa chính xác và sáng tạo.
2. Một tính năng "chụp ảnh tổng hợp" trong ứng dụng camera điện thoại, cho phép người dùng kết hợp một ảnh chụp tức thời với các ảnh tham chiếu khác và văn bản để tạo ra một bố cục ảnh mới theo ngữ cảnh ngay trên thiết bị.
3. Hệ thống tạo biểu tượng cảm xúc (emoji) hoặc nhãn dán (sticker) cá nhân hóa cho ứng dụng nhắn tin trên điện thoại, cho phép người dùng mô tả hình ảnh mong muốn bằng văn bản và tham chiếu các ảnh hiện có để tạo ra biểu tượng độc đáo.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.05124](https://huggingface.co/papers/2601.05124) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.05124](https://arxiv.org/abs/2601.05124) |
| PDF Download | [https://arxiv.org/pdf/2601.05124.pdf](https://arxiv.org/pdf/2601.05124.pdf) |
| Github Repository | [https://github.com/hrz2000/realign](https://github.com/hrz2000/realign) |

--- 

## 18. ProFuse: Efficient Cross-View Context Fusion for Open-Vocabulary 3D Gaussian Splatting

**Tác giả:** Yen-Jen Chiou, Wei-Tse Cheng, Yuan-Fu Yang

**Xuất bản lúc:** 2026-01-08

**Tag:** 3D Gaussian Splatting, Open-Vocabulary, Cross-View Context Fusion, Semantic Understanding, Dense Correspondence

### Main Problem:
Các phương pháp hiểu cảnh 3D ngữ nghĩa mở sử dụng 3D Gaussian Splatting (3DGS) gặp khó khăn trong việc đảm bảo tính nhất quán giữa các góc nhìn (cross-view consistency) và sự gắn kết trong mặt nạ (intra-mask cohesion). Nhiều cách tiếp cận dựa vào chưng cất tín hiệu 2D có giám sát, dẫn đến thời gian huấn luyện lâu, chi phí tính toán cao và khả năng không khớp với nhúng ngôn ngữ gốc, cũng như sự thiếu ổn định khi truy vấn ngữ nghĩa từ các góc nhìn riêng lẻ.

### Main Idea:
ProFuse đề xuất một khuôn khổ hiệu quả, nhận biết ngữ cảnh để hiểu cảnh 3D ngữ nghĩa mở với 3DGS. Phương pháp này tăng cường tính nhất quán giữa các góc nhìn và sự gắn kết trong mặt nạ thông qua một thiết lập đăng ký trực tiếp (direct registration) với chi phí tối thiểu và không yêu cầu tinh chỉnh có giám sát kết xuất. Thay vì dựa vào một cảnh 3DGS đã được huấn luyện trước, ProFuse sử dụng giai đoạn tiền đăng ký (pre-registration) được hướng dẫn bởi sự tương ứng dày đặc (dense correspondence) để khởi tạo các Gaussians với hình học chính xác và đồng thời xây dựng các 3D Context Proposals thông qua phân cụm đa góc nhìn. Mỗi đề xuất mang một đặc trưng toàn cục được tổng hợp từ các nhúng thành phần và đặc trưng này được hợp nhất vào các Gaussians trong quá trình đăng ký trực tiếp để duy trì sự mạch lạc ngôn ngữ trên mỗi primitive giữa các góc nhìn mà không cần tối ưu hóa bổ sung.

### Main Results:
ProFuse đạt được khả năng hiểu cảnh 3DGS ngữ nghĩa mở mạnh mẽ. Quá trình gắn kết ngữ nghĩa hoàn thành trong khoảng năm phút cho mỗi cảnh, nhanh hơn 2 lần so với các phương pháp tiên tiến (SOTA). Phương pháp này cải thiện khả năng chọn đối tượng 3D, hiểu đám mây điểm ngữ nghĩa mở và hiệu quả huấn luyện trên các bộ dữ liệu tiêu chuẩn hiện có, đồng thời duy trì liên kết ngữ nghĩa không cần kết xuất một cách hiệu quả.

### Conclusion & Future Works:
ProFuse cung cấp một con đường gọn nhẹ và không cần huấn luyện để đạt được khả năng hiểu cảnh 3D ngữ nghĩa mở nhất quán, được xây dựng trực tiếp trên cơ chế đăng ký dựa trên sự tương ứng.

### Brainstorming Space:
#### 1. Publish Papers:
1. Nghiên cứu mở rộng phương pháp ProFuse để hỗ trợ các cảnh động và thay đổi theo thời gian, duy trì tính nhất quán ngữ nghĩa khi đối tượng di chuyển hoặc biến đổi.
2. Khám phá việc tích hợp các mô hình ngôn ngữ lớn để tạo ra các mô tả ngữ nghĩa 3D phong phú hơn và truy vấn tương tác phức tạp hơn trong khuôn khổ ProFuse.
3. Phát triển một phương pháp tự động điều chỉnh siêu tham số và ngưỡng cho quá trình tiền đăng ký dựa trên đặc điểm của từng cảnh để cải thiện tính mạnh mẽ của hệ thống.
#### 2. Patent:
1. Hệ thống lập bản đồ 3D ngữ nghĩa tức thì trên điện thoại di động, cho phép người dùng quét môi trường và truy vấn các đối tượng bằng ngôn ngữ tự nhiên mà không cần kết nối đám mây liên tục.
2. Công nghệ chụp ảnh và tái tạo 3D trên điện thoại thông minh với khả năng tự động chú thích ngữ nghĩa mở, cho phép người dùng lưu trữ và tìm kiếm các không gian thực tế dựa trên nội dung.
3. Ứng dụng thực tế tăng cường trên điện thoại di động sử dụng hiểu biết ngữ nghĩa 3D không cần huấn luyện bổ sung để neo các vật thể ảo vào các đối tượng vật lý được nhận diện bằng ngôn ngữ mở trong thời gian thực.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.04754](https://huggingface.co/papers/2601.04754) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.04754](https://arxiv.org/abs/2601.04754) |
| PDF Download | [https://arxiv.org/pdf/2601.04754.pdf](https://arxiv.org/pdf/2601.04754.pdf) |
| Github Repository | [https://github.com/chiou1203/ProFuse](https://github.com/chiou1203/ProFuse) |

--- 

## 19. Guardians of the Hair: Rescuing Soft Boundaries in Depth, Stereo, and Novel Views

**Tác giả:** Xiang Zhang, Yang Zhang, Lukas Mehl, Markus Gross, Christopher Schroers

**Xuất bản lúc:** 2026-01-06

**Tag:** Depth Estimation, Stereo Conversion, Novel View Synthesis, Soft Boundaries, Image Matting, Generative Models, 3D Vision

### Main Problem:
Các phương pháp thị giác 3D hiện đại gặp khó khăn đáng kể trong việc xử lý các ranh giới mềm (ví dụ: tóc, cấu trúc mỏng) trong ước lượng độ sâu, chuyển đổi stereo và tổng hợp góc nhìn mới. Những vùng này, nơi tiền cảnh và hậu cảnh pha trộn, thường dẫn đến độ sâu không chính xác, kết cấu bị suy giảm và hình học không nhất quán.

### Main Idea:
Bài báo giới thiệu Guardians of the Hair (HairGuard), một framework toàn diện được thiết kế để phục hồi các chi tiết ranh giới mềm trong các tác vụ thị giác 3D. HairGuard tích hợp một pipeline xử lý dữ liệu mới tận dụng các bộ dữ liệu matting hình ảnh để huấn luyện. Framework này bao gồm một mạng "depth fixer" với "gated residual module" để tự động xác định và tinh chỉnh độ sâu chính xác ở ranh giới mềm, một "generative scene painter" để lấp đầy các vùng bị che khuất và loại bỏ nhiễu, cùng với một "color fuser" với kiến trúc "dual skip" để kết hợp kết quả được warping và inpainted, nhằm bảo toàn chi tiết kết cấu mịn và đảm bảo hình học nhất quán cho tổng hợp góc nhìn mới.

### Main Results:
HairGuard đạt được hiệu suất vượt trội trong ước lượng độ sâu đơn ảnh, chuyển đổi ảnh/video stereo và tổng hợp góc nhìn mới. Các thử nghiệm rộng rãi cho thấy HairGuard cải thiện đáng kể khả năng nắm bắt chi tiết ranh giới mềm, khắc phục các vấn đề về độ sâu bị đứt đoạn, kết cấu bị suy giảm và hình học không nhất quán mà các phương pháp hiện có gặp phải.

### Conclusion & Future Works:
HairGuard đã thành công trong việc giải quyết thách thức của các ranh giới mềm trong thị giác 3D bằng cách kết hợp chiến lược xử lý dữ liệu thông minh và kiến trúc mạng chuyên biệt. Nó cung cấp một giải pháp plug-and-play để tinh chỉnh độ sâu và tổng hợp góc nhìn chất lượng cao, thiết lập một tiêu chuẩn mới cho việc xử lý các chi tiết tinh xảo này. Hướng nghiên cứu tiếp theo có thể khám phá việc mở rộng HairGuard sang các loại ranh giới mềm phức tạp hơn hoặc tích hợp với các mô hình nền tảng thế hệ mới để cải thiện khả năng tổng quát hóa.

### Brainstorming Space:
#### 1. Publish Papers:
. Nghiên cứu về việc áp dụng HairGuard để cải thiện độ chính xác của các mô hình AR/VR trong việc hiển thị các vật thể có ranh giới mềm theo thời gian thực.
. Khám phá việc sử dụng các mô hình ngôn ngữ lớn để tạo ra các chú thích tự động cho ranh giới mềm, giúp đào tạo các mô hình như HairGuard với ít dữ liệu matting hơn.
. Phát triển một phương pháp để đánh giá định lượng chất lượng của ranh giới mềm trong các tác vụ thị giác 3D, vượt ra ngoài các chỉ số độ sâu và kết cấu truyền thống.

#### 2. Patent:
. Hệ thống camera điện thoại thông minh tích hợp bộ xử lý HairGuard để cải thiện chất lượng ảnh chân dung và video có hiệu ứng bokeh, đặc biệt là quanh tóc và lông.
. Công nghệ chỉnh sửa video trên điện thoại di động sử dụng HairGuard để tăng cường hiệu ứng 3D và chuyển đổi stereo cho nội dung do người dùng tạo, mang lại trải nghiệm xem sâu hơn.
. Ứng dụng AR trên điện thoại di động sử dụng công nghệ depth fixer của HairGuard để định vị chính xác các vật thể ảo lên các vật thể thực có ranh giới mềm (ví dụ: đặt mũ ảo lên tóc người dùng) một cách liền mạch hơn.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.03362](https://huggingface.co/papers/2601.03362) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.03362](https://arxiv.org/abs/2601.03362) |
| PDF Download | [https://arxiv.org/pdf/2601.03362.pdf](https://arxiv.org/pdf/2601.03362.pdf) |
| Github Repository | N/A |

--- 

## 20. One Sample to Rule Them All: Extreme Data Efficiency in RL Scaling

**Tác giả:** Yiyuan Li, Zhen Huang, Yanan Wu, Weixun Wang, Xuefeng Li, Yijia Luo, Wenbo Su, Bo Zheng, Pengfei Liu

**Xuất bản lúc:** 2026-01-06

**Tag:** Reinforcement Learning (RL), Large Language Models (LLMs), Data Efficiency, One-shot Learning, Sample Engineering, Cross-Domain Generalization, Polymath Learning.

### Main Problem:
Các mô hình ngôn ngữ lớn (LLM) thường yêu cầu hàng nghìn mẫu chất lượng cao để huấn luyện bằng Reinforcement Learning (RL) nhằm phát huy khả năng suy luận. Vấn đề cốt lõi mà bài báo đề cập là làm thế nào để đạt được hiệu quả dữ liệu cực cao trong RL cho LLM, đặc biệt là liệu có thể cải thiện khả năng suy luận đa miền chỉ với một mẫu huấn luyện duy nhất, và cách tối ưu hóa việc lựa chọn hoặc tổng hợp mẫu này để đạt được tác động tối đa.

### Main Idea:
Bài báo giới thiệu "polymath learning", một khuôn khổ tập trung vào việc thiết kế một mẫu huấn luyện duy nhất có thể tạo ra tác động đa ngành, thách thức giả định về yêu cầu dữ liệu trong RL cho LLM. Ý tưởng chính là chứng minh rằng một mẫu suy luận toán học được chọn lọc một cách chiến lược hoặc được thiết kế tổng hợp có thể mang lại những cải thiện đáng kể về hiệu suất trên nhiều lĩnh vực (ví dụ: vật lý, hóa học, sinh học) thông qua RL. Bài báo đề xuất tập trung vào "sample engineering" (kỹ thuật mẫu) – lựa chọn và thiết kế mẫu chính xác – thay vì chỉ tăng khối lượng dữ liệu để mở khóa khả năng suy luận nâng cao.

### Main Results:
1. Một mẫu suy luận toán học duy nhất, được lựa chọn chiến lược, có thể tạo ra những cải thiện hiệu suất đáng kể trên nhiều lĩnh vực khác nhau, bao gồm vật lý, hóa học và sinh học, thông qua Reinforcement Learning.
2. Các kỹ năng toán học nổi bật, đặc biệt là đại số và tiền giải tích, gợi ý các đặc điểm của mẫu polymath tối ưu có ảnh hưởng đến khả năng suy luận.
3. Một mẫu tổng hợp được thiết kế đặc biệt, tích hợp các yếu tố đa ngành, cho hiệu suất vượt trội so với việc huấn luyện bằng các mẫu tự nhiên riêng lẻ.
4. Phương pháp tiếp cận này đạt được hiệu suất vượt trội so với việc huấn luyện với các bộ dữ liệu lớn hơn, chứng minh rằng chất lượng và thiết kế mẫu, thay vì số lượng, có thể là chìa khóa để mở khóa khả năng suy luận nâng cao trong các mô hình ngôn ngữ.

### Conclusion & Future Works:
Bài báo kết luận rằng việc tập trung vào chất lượng và thiết kế của mẫu huấn luyện ("sample engineering") có thể mang lại hiệu quả dữ liệu cực cao trong Reinforcement Learning cho LLM, cho phép khả năng suy luận đa miền chỉ với một mẫu duy nhất. Điều này gợi ý một sự thay đổi trong cách tiếp cận RL, từ việc chỉ tăng khối lượng dữ liệu sang kỹ thuật chính xác các mẫu huấn luyện. Hướng nghiên cứu tiếp theo bao gồm việc tối ưu hóa hơn nữa các đặc điểm của mẫu polymath lý tưởng và phát triển các kỹ thuật tổng hợp mẫu đa ngành hiệu quả.

### Brainstorming Space:
#### 1. Publish Papers:
1. Nghiên cứu sâu hơn về mối tương quan giữa các kỹ năng nhận thức trong một mẫu huấn luyện duy nhất và khả năng tổng quát hóa liên miền của LLM trên các lĩnh vực đa dạng hơn.
2. Phát triển một framework tự động để đánh giá và lựa chọn các "mẫu polymath" tối ưu từ một kho dữ liệu lớn dựa trên động lực học của quá trình huấn luyện RL.
3. Khám phá việc áp dụng "sample engineering" trong các mô hình đa phương thức (multimodal models) để xem xét liệu một mẫu kết hợp các loại dữ liệu khác nhau có thể tạo ra hiệu ứng tổng quát hóa tương tự không.

#### 2. Patent:
1. Hệ thống huấn luyện AI cá nhân hóa trên thiết bị di động, tự động xác định và sử dụng một mẫu dữ liệu "đa tài" nhỏ từ tương tác của người dùng để cải thiện khả năng suy luận của trợ lý ảo.
2. Công nghệ tạo ra các bài toán tổng hợp đa ngành theo thời gian thực dựa trên ngữ cảnh và sở thích của người dùng điện thoại, giúp tinh chỉnh mô hình ngôn ngữ mà không cần kết nối internet hay dữ liệu lớn.
3. Phương pháp tối ưu hóa bộ nhớ và hiệu suất của các mô hình ngôn ngữ trên điện thoại thông minh bằng cách liên tục cập nhật chúng chỉ với một "mẫu kỹ thuật" được lựa chọn thông minh thay vì tải về các bản cập nhật lớn.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.03111](https://huggingface.co/papers/2601.03111) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.03111](https://arxiv.org/abs/2601.03111) |
| PDF Download | [https://arxiv.org/pdf/2601.03111.pdf](https://arxiv.org/pdf/2601.03111.pdf) |
| Github Repository | N/A |

--- 

## 21. Memorization in 3D Shape Generation: An Empirical Study

**Tác giả:** Shu Pu, Boya Zeng, Kaichen Zhou, Mengyu Wang, Zhuang Liu

**Xuất bản lúc:** 2025-12-29

**Tag:** 3D Shape Generation, Memorization, Generative Models, Diffusion, Evaluation Framework, Latent Representations, Light Field Distance (LFD)

### Main Problem:
Vấn đề cốt lõi mà bài báo đề cập là liệu các mô hình sinh 3D có đang ghi nhớ các hình dạng huấn luyện hay không, điều này có thể dẫn đến rò rỉ dữ liệu, thiếu tính đa dạng và hạn chế khả năng khái quát hóa. Hiện tại, chưa có thước đo tiêu chuẩn nào để định lượng mức độ ghi nhớ trong các mô hình sinh 3D.

### Main Idea:
Bài báo thiết kế một khung đánh giá thực nghiệm để định lượng mức độ ghi nhớ trong các mô hình sinh 3D. Khung này sử dụng khoảng cách Light Field Distance (LFD) làm thước đo chính xác nhất để xác định sự sao chép hình dạng, kết hợp với thống kê z-score ZU (từ kiểm định Mann-Whitney U) để định lượng mức độ ghi nhớ cấp mô hình. Để tách biệt mức độ ghi nhớ khỏi chất lượng tạo hình, Fréchet Distance (FD) cũng được sử dụng. Sau đó, bài báo áp dụng khung này để đánh giá các phương pháp hiện có và tiến hành các thí nghiệm có kiểm soát với mô hình Vecset diffusion để nghiên cứu ảnh hưởng của các yếu tố thiết kế dữ liệu và mô hình đến việc ghi nhớ.

### Main Results:
- LFD được xác định là thước đo hiệu quả nhất (độ chính xác 78.4%) để phát hiện các bản sao hình dạng huấn luyện so với các thước đo khác.
- Các mô hình sinh 3D được huấn luyện trên các tập dữ liệu nhỏ hơn (ví dụ: một danh mục ShapeNet) cho thấy sự ghi nhớ rõ ràng, tạo ra các bản sao gần như chính xác, trong khi các mô hình sinh có điều kiện quy mô lớn hơn thể hiện khả năng ghi nhớ hạn chế và khả năng khái quát hóa tốt hơn.
- **Về phía dữ liệu:** Việc ghi nhớ phụ thuộc vào phương thức dữ liệu (hình ảnh kết xuất dễ ghi nhớ hơn hình dạng 3D) và tăng lên cùng với sự đa dạng của dữ liệu và mức độ điều kiện chi tiết hơn.
- **Về phía mô hình:** Mức độ ghi nhớ đạt đỉnh ở một quy mô hướng dẫn (guidance scale) vừa phải và có thể được giảm thiểu hiệu quả bằng cách tăng chiều dài Vecset tiềm ẩn và áp dụng tăng cường xoay đơn giản.
- Các chiến lược được đề xuất có thể giảm thiểu việc ghi nhớ mà không làm giảm chất lượng tạo hình.

### Conclusion & Future Works:
Bài báo giới thiệu một khung đánh giá và phân tích thực nghiệm về việc ghi nhớ trong các mô hình sinh 3D, cung cấp hiểu biết sâu sắc về các yếu tố ảnh hưởng đến nó. Các phát hiện gợi ý các chiến lược đơn giản nhưng hiệu quả, như tăng chiều dài Vecset và áp dụng tăng cường xoay, có thể giảm thiểu việc ghi nhớ trong khi vẫn duy trì chất lượng tạo hình. Những hiểu biết này có thể định hướng cho nghiên cứu trong tương lai về tổng hợp 3D có khả năng khái quát hóa tốt hơn.

### Brainstorming Space:
#### 1. Publish Papers:
- Nghiên cứu sự tương tác giữa các kỹ thuật giảm ghi nhớ khác nhau (ví dụ: Vecset length và rotation augmentation) để tìm ra sự kết hợp tối ưu.
- Mở rộng khung đánh giá để bao gồm việc ghi nhớ cấu trúc hoặc đặc điểm ngữ nghĩa của các hình dạng 3D, không chỉ là sự giống hệt về mặt thị giác.
- Phân tích cách các tập dữ liệu huấn luyện thiên lệch hoặc không cân bằng ảnh hưởng đến mức độ ghi nhớ và đề xuất các phương pháp đối phó.

#### 2. Patent:
- Hệ thống tạo hình 3D trên thiết bị di động với khả năng điều chỉnh thông số Vecset và áp dụng tăng cường xoay tự động để người dùng có thể tạo ra các vật thể 3D độc đáo, giảm thiểu trùng lặp với dữ liệu huấn luyện.
- Phương pháp phát hiện và cảnh báo rò rỉ dữ liệu 3D trong các ứng dụng thiết kế trên điện thoại bằng cách sử dụng LFD để so sánh các thiết kế mới với cơ sở dữ liệu đã có, bảo vệ tài sản trí tuệ.
- Ứng dụng di động cá nhân hóa avatar hoặc vật phẩm ảo 3D, nơi các thuật toán tích hợp tự động giảm thiểu sự giống nhau với các mẫu có sẵn bằng cách điều chỉnh các yếu tố như độ đa dạng dữ liệu và độ chi tiết điều kiện.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2512.23628](https://huggingface.co/papers/2512.23628) |
| ArXiv Abstract | [https://arxiv.org/abs/2512.23628](https://arxiv.org/abs/2512.23628) |
| PDF Download | [https://arxiv.org/pdf/2512.23628.pdf](https://arxiv.org/pdf/2512.23628.pdf) |
| Github Repository | N/A |

--- 

## 22. Multi-Scale Local Speculative Decoding for Image Generation

**Tác giả:** Elia Peruzzo, Guillaume Sautière, Amirhossein Habibian

**Xuất bản lúc:** 2026-01-08

**Tag:** Speculative Decoding, Image Generation, Autoregressive Models, Multi-Scale, Latency Reduction

### Main Problem:
Các mô hình Autoregressive (AR) đạt được thành công đáng kể trong tổng hợp hình ảnh nhưng bản chất tuần tự của chúng gây ra giới hạn đáng kể về độ trễ, đặc biệt khi kích thước chuỗi tăng nhanh chóng với độ phân giải cao, dẫn đến hàng nghìn token. Các phương pháp Speculative Decoding hiện có bị hạn chế bởi sự mơ hồ ở cấp độ token và thiếu nhận thức về không gian khi áp dụng cho tổng hợp hình ảnh.

### Main Idea:
Bài báo giới thiệu Multi-Scale Local Speculative Decoding (MuLo-SD), một framework mới kết hợp phác thảo đa độ phân giải với xác minh có nhận thức không gian để tăng tốc tạo hình ảnh AR. Phương pháp này sử dụng một mô hình phác thảo độ phân giải thấp kết hợp với các bộ lấy mẫu tăng cường (up-samplers) đã được học để đề xuất các token hình ảnh ứng cử viên. Các token này sau đó được mô hình đích độ phân giải cao xác minh song song. MuLo-SD tích hợp một cơ chế từ chối và lấy mẫu lại cục bộ, cho phép sửa lỗi phác thảo hiệu quả bằng cách tập trung vào các vùng lân cận không gian thay vì lấy mẫu lại toàn bộ chuỗi theo thứ tự raster-scan sau lần từ chối đầu tiên.

### Main Results:
MuLo-SD đạt được tốc độ tăng đáng kể – lên đến 1.7 lần – vượt trội so với các phương pháp Speculative Decoding cơ bản mạnh mẽ như EAGLE-2 và LANTERN về khả năng tăng tốc, đồng thời duy trì sự liên kết ngữ nghĩa và chất lượng cảm nhận tương đương. Những kết quả này được xác thực bằng cách sử dụng GenEval, DPG-Bench, và FID/HPSv2 trên bộ xác thực MS-COCO 5k. Các phân tích chuyên sâu làm nổi bật tác động của thiết kế up-sampling, gộp xác suất, và từ chối cũng như lấy mẫu lại cục bộ với mở rộng vùng lân cận. Phương pháp này đặt ra một tiêu chuẩn mới trong Speculative Decoding cho tổng hợp hình ảnh.

### Conclusion & Future Works:
MuLo-SD đại diện cho một bước tiến mới trong Speculative Decoding cho tổng hợp hình ảnh bằng cách giải quyết các hạn chế về độ trễ của các mô hình AR, đặc biệt trong lĩnh vực hình ảnh. Bằng cách tận dụng các thuộc tính cấu trúc của hình ảnh thông qua phác thảo đa độ phân giải và xác minh cục bộ, MuLo-SD giúp thu hẹp khoảng cách giữa hiệu quả và độ trung thực. Phương pháp này tích hợp tốt với các mô hình MLLM dự đoán next-token hiện có, khác với các phương pháp đa quy mô truyền thống yêu cầu lịch lấy mẫu tùy chỉnh.

### Brainstorming Space:
#### 1. Publish Papers:
*   Nghiên cứu tích hợp MuLo-SD với các phương pháp giải mã song song khác như ZipAR để khám phá tiềm năng tăng hiệu suất kết hợp trong tổng hợp hình ảnh.
*   Phát triển và so sánh các kiến trúc up-sampler đã học nâng cao hoặc kiến trúc drafter nhiều tầng cho MuLo-SD để cải thiện hơn nữa hiệu quả và chất lượng.
*   Mở rộng MuLo-SD để áp dụng cho tổng hợp video hoặc mô hình 3D, nơi các vấn đề về độ trễ do kích thước chuỗi lớn còn nghiêm trọng hơn.

#### 2. Patent:
*   Hệ thống và phương pháp tăng tốc tổng hợp hình ảnh trên thiết bị di động bằng cách sử dụng kiến trúc MuLo-SD, cho phép tạo ra hình ảnh chất lượng cao gần như theo thời gian thực trong các ứng dụng điện thoại.
*   Khung phần mềm tích hợp sẵn cho các hệ điều hành di động, tự động điều chỉnh độ phân giải của mô hình phác thảo MuLo-SD dựa trên tài nguyên sẵn có của điện thoại (ví dụ: pin, RAM) để tối ưu hóa hiệu suất và tiết kiệm năng lượng.
*   Công nghệ camera thông minh trên điện thoại có khả năng tạo ra các hiệu ứng hình ảnh hoặc cải thiện chất lượng ảnh chụp tức thì bằng cách sử dụng MuLo-SD để tăng tốc quá trình xử lý hình ảnh dựa trên AI.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.05149](https://huggingface.co/papers/2601.05149) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.05149](https://arxiv.org/abs/2601.05149) |
| PDF Download | [https://arxiv.org/pdf/2601.05149.pdf](https://arxiv.org/pdf/2601.05149.pdf) |
| Github Repository | N/A |

--- 

## 23. PyramidalWan: On Making Pretrained Video Model Pyramidal for Efficient Inference

**Tác giả:** Denis Korzhenkov, Adil Karjauv, Animesh Karnewar, Mohsen Ghafoorian, Amirhossein Habibian

**Xuất bản lúc:** 2026-01-08

**Tag:** Diffusion, Video Generation, Pyramidal Models, Efficient Inference, Finetuning, Step Distillation

### Main Problem:
Các mô hình khuếch tán video tiên tiến hiện nay đạt chất lượng sinh tạo ấn tượng nhưng quá trình suy luận nhiều bước vẫn rất tốn kém về mặt tính toán. Trong khi đó, các mô hình pyramidal video mã nguồn mở hiện có, dù được thiết kế để giảm chi phí tính toán bằng cách xử lý các cấp độ nhiễu khác nhau ở độ phân giải khác nhau, lại thường được huấn luyện từ đầu và có hiệu suất kém hơn so với các hệ thống hiện đại về độ chân thực của hình ảnh.

### Main Idea:
Bài báo đề xuất một quy trình để chuyển đổi một mô hình khuếch tán video đã được huấn luyện trước (pretrained diffusion model) thành mô hình pyramidal thông qua finetuning với chi phí thấp, mà không làm suy giảm chất lượng của video đầu ra. Cụ thể, nghiên cứu bắt đầu với mô hình Wan2.1-1.3B đã được huấn luyện trước, phân tách quá trình khuếch tán thành ba giai đoạn không gian-thời gian hoạt động ở các độ phân giải khác nhau và tinh chỉnh mô hình bằng hàm mất mát flow matching pyramidal. Ngoài ra, bài báo còn nghiên cứu và so sánh các chiến lược chưng cất bước (step distillation) khác nhau trong thiết lập pyramidal để tăng cường hơn nữa hiệu quả suy luận. Cuối cùng, một sự tổng quát hóa lý thuyết các phép toán chuyển đổi độ phân giải trong khung PyramidalFlow được trình bày, mở rộng sang các hàm upsampling và downsampling tùy ý dựa trên biến đổi trực giao.

### Main Results:
*   Bài báo chứng minh rằng một mô hình transformer khuếch tán video thông thường có thể được chuyển đổi hiệu quả thành một mô hình khuếch tán pyramidal không gian-thời gian với chi phí finetuning tối thiểu và không ảnh hưởng đến chất lượng.
*   Các mô hình pyramidal giảm đáng kể chi phí tính toán cho suy luận (ví dụ: từ 2x12,592 TFLOPs xuống 2x2,821 TFLOPs cho "Diffusion" và "Pyramidal diffusion").
*   Tiết kiệm 43% tốc độ xử lý cho lịch trình 2-2-1 so với 0-0-2, trong khi chỉ chậm hơn 13% so với 0-0-1.
*   Nghiên cứu có hệ thống về các kỹ thuật chưng cất bước trong thiết lập pyramidal đã được thực hiện, cung cấp những hiểu biết thực tế cho nhiều kịch bản huấn luyện.
*   Bài báo lần đầu tiên chứng minh rằng các mô hình Pyramidal Patchification (PPF) có thể được huấn luyện thành công cho việc tạo video với ít bước suy luận.
*   Các phép toán chuyển đổi độ phân giải trong PyramidalFlow được tổng quát hóa thành một lớp rộng hơn các hàm upsampling dựa trên biến đổi trực giao.

### Conclusion & Future Works:
Nghiên cứu này thành công trong việc giải quyết thách thức về chi phí tính toán cao của các mô hình khuếch tán video bằng cách chuyển đổi hiệu quả các mô hình đã được huấn luyện trước thành kiến trúc pyramidal thông qua finetuning tiết kiệm chi phí, đồng thời duy trì chất lượng đầu ra. Việc tổng quát hóa các phép toán chuyển đổi độ phân giải và nghiên cứu chưng cất bước mở ra nhiều hướng tiềm năng để tối ưu hóa hiệu suất hơn nữa.

### Brainstorming Space:
#### 1. Publish Papers:
1.  Nghiên cứu so sánh định lượng và định tính chi tiết giữa hiệu suất của PyramidalFlow và Pyramidal Patchification Flow (PPF) trong các kịch bản huấn luyện giới hạn tài nguyên và các bộ dữ liệu video đa dạng.
2.  Khám phá việc tích hợp các kiến trúc mô hình nền tảng khác (ví dụ: U-Net thay vì DiT) vào khung pyramidal được finetuning, đánh giá tác động của chúng lên hiệu quả và chất lượng tạo video.
3.  Phát triển một phương pháp chưng cất bước động cho các mô hình pyramidal, cho phép mô hình tự động điều chỉnh số lượng bước suy luận ở mỗi giai đoạn dựa trên độ phức tạp của nội dung video hoặc mục tiêu hiệu suất.

#### 2. Patent:
1.  Phương pháp tạo video hiệu quả trên thiết bị di động bằng cách sử dụng mô hình khuếch tán pyramidal đã được tinh chỉnh, tự động điều chỉnh độ phân giải xử lý dựa trên mức độ nhiễu của từng khung hình để tối ưu hóa hiệu suất và tuổi thọ pin trên điện thoại thông minh.
2.  Hệ thống phần mềm cho điện thoại thông minh tích hợp công nghệ Pyramidal Patchification Flow (PPF), cho phép tạo hoặc chỉnh sửa video chất lượng cao với thời gian xử lý cực nhanh bằng cách điều chỉnh kích thước kernel của lớp patchification theo thời gian thực để phù hợp với tài nguyên thiết bị.
3.  Công nghệ xử lý video trên chip điện thoại di động sử dụng các phép toán upsampling và downsampling dựa trên biến đổi trực giao đã được cấp bằng sáng chế để thực hiện chuyển đổi độ phân giải hiệu quả, giúp giảm thiểu độ trễ và tiêu thụ điện năng khi chạy các ứng dụng tạo video AI.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.04792](https://huggingface.co/papers/2601.04792) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.04792](https://arxiv.org/abs/2601.04792) |
| PDF Download | [https://arxiv.org/pdf/2601.04792.pdf](https://arxiv.org/pdf/2601.04792.pdf) |
| Github Repository | N/A |

--- 

## 24. AgentDevel: Reframing Self-Evolving LLM Agents as Release Engineering

**Tác giả:** Di Zhang

**Xuất bản lúc:** 2026-01-08

**Tag:** LLM Agents, Self-Improvement, Release Engineering, Software Development, Regression Testing, Auditable AI

### Main Problem:
Các phương pháp hiện có để cải thiện tác nhân LLM tự tiến hóa (self-evolving LLM agents) thường dẫn đến những cải tiến không ổn định và khó kiểm toán, gây khó khăn trong việc đảm bảo không có sự thoái hóa hiệu suất (non-regression) hoặc phân tích nguyên nhân lỗi qua các phiên bản.

### Main Idea:
Bài báo đề xuất AgentDevel, một khuôn khổ tái định hình việc cải thiện tác nhân LLM như là kỹ thuật phát hành phần mềm (release engineering). Thay vì để tác nhân tự cải thiện nội tại hoặc tìm kiếm trong nhiều biến thể đồng thời, AgentDevel ngoại hóa quá trình cải thiện vào một quy trình phát hành có nhận thức về lỗi thoái hóa.
AgentDevel duy trì một dòng phiên bản tác nhân chính tắc duy nhất và tập trung vào việc ngăn chặn thoái hóa là mục tiêu chính. Quy trình này bao gồm ba thiết kế cốt lõi:
1.  **Một LLM critic không biết về triển khai (implementation-blind)**: Mô tả các biểu hiện lỗi ở cấp độ triệu chứng mà không truy cập vào các chi tiết bên trong của tác nhân.
2.  **Chẩn đoán thực thi dựa trên script**: Tổng hợp các mẫu triệu chứng lỗi chủ đạo và tạo ra các đặc tả kỹ thuật có thể kiểm toán.
3.  **Kiểm soát "flip-centered gating"**: Ưu tiên các trường hợp `pass -> fail` (thoái hóa) và `fail -> pass` (sửa lỗi) làm bằng chứng chính để chấp nhận hoặc từ chối một bản phát hành ứng cử viên (Release Candidate - RC).

### Main Results:
Các thử nghiệm trên các điểm chuẩn nặng về thực thi cho thấy AgentDevel mang lại những cải tiến ổn định với số lượng thoái hóa ít hơn đáng kể, đồng thời tạo ra các "artifact" có thể tái tạo và kiểm toán được. AgentDevel cung cấp một kỷ luật phát triển thực tế để xây dựng, gỡ lỗi và phát hành các tác nhân LLM giống như quy trình phát triển phần mềm truyền thống.

### Conclusion & Future Works:
**Conclusion:** AgentDevel chứng minh rằng việc áp dụng các nguyên tắc kỹ thuật phát hành phần mềm vào quá trình cải thiện tác nhân LLM có thể dẫn đến các hệ thống ổn định hơn, dễ kiểm toán hơn và ít bị thoái hóa hơn, từ đó nâng cao độ tin cậy của các tác nhân LLM trong các ứng dụng thực tế.
**Future Works:** Bài báo gợi ý AgentDevel là một "kỷ luật phát triển thực tế" và không phụ thuộc vào điểm chuẩn cụ thể, cho thấy khả năng tiếp tục ứng dụng và tinh chỉnh nó trên nhiều lĩnh vực và bề mặt lỗi khác nhau.

### Brainstorming Space:
#### 1. Publish Papers:
-   Nghiên cứu cách tích hợp và tối ưu hóa các phương pháp học tăng cường (reinforcement learning) vào quy trình AgentDevel để tự động hóa việc tổng hợp các bản sửa lỗi trong RC.
-   Khám phá việc sử dụng các mô hình ngôn ngữ đa phương thức (multimodal LLM) làm critic để phân tích các trace execution phức tạp hơn, bao gồm cả yếu tố hình ảnh hoặc âm thanh.
-   Phát triển các tiêu chuẩn và công cụ định lượng mới cho "ổn định" và "khả năng kiểm toán" của tác nhân LLM trong môi trường sản xuất.

#### 2. Patent:
-   Hệ thống quản lý vòng đời tác nhân LLM trên điện thoại thông minh, tự động phát hiện lỗi, đề xuất bản sửa lỗi và kiểm tra thoái hóa trước khi cập nhật các tác nhân tích hợp trong hệ điều hành hoặc ứng dụng di động.
-   Phương pháp kiểm soát chất lượng tự động cho các tính năng AI mới trên điện thoại di động, nơi các bản cập nhật tính năng được đánh giá thông qua cơ chế "flip-centered gating" để đảm bảo không làm gián đoạn các chức năng hiện có.
-   Công nghệ "implementation-blind critic" dạng mô-đun dành cho các ứng dụng di động, cho phép các nhà phát triển độc lập đánh giá hiệu suất của tác nhân LLM mà không cần truy cập vào mã nguồn nhạy cảm của tác nhân đó.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.04620](https://huggingface.co/papers/2601.04620) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.04620](https://arxiv.org/abs/2601.04620) |
| PDF Download | [https://arxiv.org/pdf/2601.04620.pdf](https://arxiv.org/pdf/2601.04620.pdf) |
| Github Repository | N/A |

--- 

## 25. Scaling Behavior Cloning Improves Causal Reasoning: An Open Model for Real-Time Video Game Playing

**Tác giả:** Yuguang Yue, Irakli Salia, Samuel Hunt, Chris Green, Wenzhe Shi, Jonathan J Hunt

**Xuất bản lúc:** 2026-01-08

**Tag:** Behavior Cloning, Causal Reasoning, Video Game AI, Foundation Model, Real-Time Control, Multimodal AI, Scaling Laws

### Main Problem:
1. Các hệ thống học tăng cường (RL) hiện tại để chơi game thường được tùy chỉnh cho từng trò chơi cụ thể, yêu cầu môi trường huấn luyện và hàm thưởng được thiết kế cẩn thận, hạn chế tính tổng quát và khả năng mở rộng.
2. Behavior Cloning (BC) gặp phải các thách thức cơ bản là phân bố lệch (distributional shift) và nhầm lẫn nhân quả (causal confusion), làm giảm đáng kể hiệu suất.
3. Việc triển khai các mô hình đa phương thức lớn (VLM) cho điều khiển thời gian thực trên phần cứng tiêu dùng gặp khó khăn về độ trễ, chi phí và hiệu suất kém trong việc điều khiển game.

### Main Idea:
Bài báo giới thiệu một "công thức mở" để huấn luyện một mô hình nền tảng chơi game được thiết kế để suy luận theo thời gian thực trên GPU tiêu dùng. Phương pháp này dựa trên Behavior Cloning quy mô lớn, sử dụng một bộ dữ liệu khổng lồ (hơn 8300 giờ chơi game chất lượng cao của con người) và mã nguồn mở. Mô hình có khả năng chơi nhiều loại trò chơi 3D bằng cách sử dụng quan sát hình ảnh thô và tạo ra các hành động bàn phím và chuột theo thời gian thực. Bài báo cũng nghiên cứu một cách có hệ thống các quy luật mở rộng của Behavior Cloning để hiểu cách hiệu suất và khả năng suy luận nhân quả của mô hình thay đổi theo quy mô mô hình và dữ liệu. Mô hình Pixels2Play (P2P) được thiết kế là một mô hình transformer chỉ giải mã (decoder-only transformer) nhẹ, đa phương thức và có điều kiện văn bản, tích hợp bộ giải mã hành động tự hồi quy để xử lý không gian hành động phức tạp.

### Main Results:
1. Mô hình tốt nhất có khả năng chơi nhiều loại trò chơi 3D ở mức độ cạnh tranh với người chơi.
2. Việc tăng cả lượng dữ liệu huấn luyện và độ sâu mạng lưới dẫn đến mô hình học được chính sách nhân quả hơn đối với một số loại suy luận nhân quả, điều này được chứng minh cả trong một bài toán toy problem đơn giản và trong các mô hình quy mô lớn (lên đến 1.2 tỷ tham số).
3. Việc mở rộng cả quy mô mô hình và dữ liệu là một giải pháp thực tế để giải quyết các vấn đề về nhầm lẫn nhân quả trong Behavior Cloning.
4. Quan sát thấy mối quan hệ quy luật lũy thừa rõ ràng giữa tổn thất thử nghiệm và quy mô bộ dữ liệu.
5. Mô hình có thể chơi các trò chơi đơn giản không yêu cầu mức độ lập kế hoạch cao với hiệu suất tốt.
6. Thiết kế bộ giải mã hành động (action decoder) cho phép tăng tốc độ thực thi thời gian thực khoảng 5 lần so với việc dự đoán trực tiếp tất cả các token hành động.

### Conclusion & Future Works:
Kết luận chính là việc mở rộng quy mô Behavior Cloning (với dữ liệu và mô hình lớn hơn) cải thiện đáng kể khả năng suy luận nhân quả, cho phép phát triển một mô hình nền tảng chơi game AI có khả năng hoạt động theo thời gian thực trên phần cứng tiêu dùng. Hướng nghiên cứu tiếp theo được ngụ ý là việc tiếp tục khám phá các quy luật mở rộng để nâng cao hơn nữa hiệu suất và khả năng suy luận nhân quả, cũng như ứng dụng các mô hình này vào các trò chơi phức tạp hơn hoặc các môi trường tương tác khác, tận dụng bộ dữ liệu, mã nguồn và mô hình được phát hành công khai.

### Brainstorming Space:
#### 1. Publish Papers:
1. Nghiên cứu ảnh hưởng của các kiến trúc transformer khác nhau đến khả năng suy luận nhân quả và hiệu quả tính toán trong Behavior Cloning.
2. Khám phá việc tích hợp các phương pháp học tăng cường (RL) vào mô hình Behavior Cloning đã được huấn luyện để cải thiện khả năng thích ứng với môi trường mới.
3. Phân tích hiệu suất và khả năng suy luận nhân quả của mô hình khi được triển khai trong các trò chơi yêu cầu lập kế hoạch chiến lược phức tạp và dài hạn.

#### 2. Patent:
1. Hệ thống điều khiển trò chơi bằng AI thời gian thực trên điện thoại di động, sử dụng mô hình nền tảng tối ưu hóa để giảm độ trễ và tiêu thụ năng lượng.
2. Công nghệ tạo dữ liệu huấn luyện tự động cho Behavior Cloning, sử dụng VLM để chú thích hành động và hướng dẫn dựa trên video chơi game của người dùng trên điện thoại.
3. Ứng dụng AI để cá nhân hóa trải nghiệm chơi game trên thiết bị di động bằng cách học phong cách chơi của người dùng và điều chỉnh độ khó hoặc gợi ý hành động trong game.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.04575](https://huggingface.co/papers/2601.04575) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.04575](https://arxiv.org/abs/2601.04575) |
| PDF Download | [https://arxiv.org/pdf/2601.04575.pdf](https://arxiv.org/pdf/2601.04575.pdf) |
| Github Repository | [https://github.com/elefant-ai/open-p2p](https://github.com/elefant-ai/open-p2p) |

--- 

## 26. ReHyAt: Recurrent Hybrid Attention for Video Diffusion Transformers

**Tác giả:** Mohsen Ghafoorian, Amirhossein Habibian

**Xuất bản lúc:** 2026-01-07

**Tag:** Video Diffusion, Transformers, Hybrid Attention, Recurrent Neural Networks, Scalability, Video Generation, Attention Distillation

### Main Problem:
Các mô hình khuếch tán video dựa trên Transformer hiện đại đạt chất lượng tạo video tiên tiến nhưng phải đối mặt với độ phức tạp chú ý bậc hai (quadratic attention complexity), giới hạn nghiêm trọng khả năng mở rộng cho các chuỗi video dài hơn. Việc đào tạo lại từ đầu các mô hình dựa trên softmax hiện có với các cơ chế chú ý hiệu quả hơn là quá tốn kém và không thực tế.

### Main Idea:
Bài báo giới thiệu ReHyAt, một cơ chế chú ý lai đệ quy (Recurrent Hybrid Attention) kết hợp tính chính xác cao của chú ý softmax với hiệu quả của chú ý tuyến tính (linear attention). ReHyAt sử dụng thiết kế chú ý lai theo từng khối thời gian (temporally chunked) với các khối chồng lấp để mô hình hóa các phụ thuộc cục bộ quan trọng bằng softmax và các phụ thuộc toàn cầu bằng linear attention. Điều này cho phép tái cấu trúc đệ quy theo từng khối (chunk-wise recurrent reformulation) và sử dụng bộ nhớ không đổi. Một quy trình chưng cất (distillation) và tinh chỉnh nhẹ nhàng (lightweight fine-tuning) được đề xuất để chuyển đổi các mô hình softmax hai chiều tiên tiến hiện có thành dạng đệ quy hiệu quả với chi phí đào tạo giảm đáng kể.

### Main Results:
ReHyAt đạt được chất lượng video tiên tiến trên VBench và VBench-2.0, cũng như trong một nghiên cứu về sở thích của con người.
Nó giảm chi phí chú ý từ bậc hai xuống tuyến tính, mở khóa khả năng mở rộng thực tế cho việc tạo video thời lượng dài và trên thiết bị.
Phương pháp này giảm chi phí đào tạo xuống hai bậc độ lớn, chỉ còn khoảng 160 giờ GPU, trong khi vẫn cạnh tranh về chất lượng với các mô hình softmax hoàn chỉnh như Wan2.1.
ReHyAt cung cấp một công thức chi phí thấp để chuyển đổi các mô hình SOTA dựa trên softmax thành các RNN hiệu quả với tác động chất lượng không đáng kể chỉ trong vài trăm giờ GPU.

### Conclusion & Future Works:
ReHyAt giải quyết thành công các thách thức về khả năng mở rộng và chi phí trong các mô hình khuếch tán video bằng cách giới thiệu một cơ chế chú ý lai đệ quy hiệu quả. Phương pháp chưng cất và tinh chỉnh nhẹ của nó cung cấp một cách thực tế để tận dụng các mô hình softmax tiên tiến hiện có. Hướng nghiên cứu tương lai bao gồm việc áp dụng công thức này cho các mô hình softmax hai chiều tiên tiến tiếp theo, mở đường cho việc tạo video dài hơn và triển khai trên thiết bị.

### Brainstorming Space:
#### 1. Publish Papers:
1. Nghiên cứu ảnh hưởng của các chiến lược phân vùng khối và chồng lấp khác nhau trong ReHyAt đến chất lượng video và hiệu suất tính toán.
2. Khám phá việc tích hợp ReHyAt vào các kiến trúc mô hình khuếch tán không phải Transformer để đánh giá khả năng áp dụng rộng rãi của nó.
3. Phát triển một phương pháp thích ứng động cho ReHyAt để điều chỉnh tỷ lệ giữa chú ý softmax và linear attention dựa trên độ phức tạp của nội dung video.

#### 2. Patent:
1. Hệ thống tạo video AI trên thiết bị di động có khả năng tạo video chất lượng cao với thời lượng tùy ý bằng cách sử dụng cơ chế chú ý lai đệ quy của ReHyAt.
2. Phương pháp chuyển đổi mô hình học sâu hiệu quả tài nguyên để triển khai trên điện thoại thông minh, cho phép chưng cất các mô hình phức tạp thành kiến trúc chú ý lai đệ quy.
3. Công nghệ ứng dụng camera thông minh trên điện thoại có khả năng tạo hiệu ứng video hoặc chỉnh sửa thời gian thực bằng cách tận dụng khả năng xử lý tuyến tính và bộ nhớ không đổi của ReHyAt.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.04342](https://huggingface.co/papers/2601.04342) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.04342](https://arxiv.org/abs/2601.04342) |
| PDF Download | [https://arxiv.org/pdf/2601.04342.pdf](https://arxiv.org/pdf/2601.04342.pdf) |
| Github Repository | N/A |

--- 

## 27. Beyond Binary Preference: Aligning Diffusion Models to Fine-grained Criteria by Decoupling Attributes

**Tác giả:** Chenye Meng, Zejian Li, Zhongni Liu, Yize Li, Changle Xie, Kaixin Jia, Ling Yang, Huanghuang Deng, Shiying Ding, Shengyuan Zhang, Jiayi Li, Lingyun Sun

**Xuất bản lúc:** 2026-01-07

**Tag:** Diffusion, Alignment, Preference Optimization, Fine-grained Criteria, Deep Learning
### Main Problem:
Các phương pháp điều chỉnh mô hình Diffusion sau huấn luyện hiện tại dựa trên các tín hiệu đơn giản như phần thưởng vô hướng hoặc các ưu tiên nhị phân. Điều này hạn chế khả năng điều chỉnh theo chuyên môn phức tạp của con người, vốn có tính phân cấp và tinh chỉnh. Các khung này gặp khó khăn trong việc xử lý các tín hiệu đa chiều, rời rạc và không cân bằng của đánh giá chuyên gia, cũng như sự đồng tồn tại của các thuộc tính tích cực và tiêu cực trong cùng một mẫu.

### Main Idea:
Bài nghiên cứu đề xuất một khuôn khổ điều chỉnh hai giai đoạn để giải quyết vấn đề này. Đầu tiên, nhóm nghiên cứu xây dựng một tiêu chí đánh giá phân cấp, tinh chỉnh với sự cộng tác của các chuyên gia miền, phân tách chất lượng hình ảnh thành nhiều thuộc tính tích cực và tiêu cực được tổ chức theo cấu trúc cây. Sau đó, họ tiêm kiến thức miền vào một mô hình Diffusion phụ trợ thông qua Supervised Fine-Tuning. Giai đoạn thứ hai giới thiệu Complex Preference Optimization (CPO), mở rộng DPO để điều chỉnh mô hình Diffusion mục tiêu theo các tiêu chí phân cấp, không nhị phân. CPO tái cấu trúc bài toán điều chỉnh để đồng thời tối đa hóa xác suất của các thuộc tính tích cực và tối thiểu hóa xác suất của các thuộc tính tiêu cực bằng cách sử dụng mô hình phụ trợ. Phương pháp được minh họa trong lĩnh vực tạo tranh và huấn luyện CPO với một tập dữ liệu tranh được chú thích các thuộc tính tinh chỉnh. Ngoài ra, một chiến lược ổn định mới được đề xuất để giải quyết sự mất ổn định của quá trình tối ưu hóa ưu tiên bằng cách cân bằng các gradient từ các mẫu tích cực và tiêu cực.

### Main Results:
Các thử nghiệm rộng rãi chứng minh rằng CPO cải thiện đáng kể chất lượng tạo ảnh và sự phù hợp với chuyên môn của các chuyên gia. Chiến lược ổn định được đề xuất giúp tăng tốc độ huấn luyện hơn 10 lần so với phương pháp sử dụng hàm mất mát gốc. Công trình này xác nhận giá trị của đánh giá tinh chỉnh và mở ra những hướng đi mới cho việc điều chỉnh mô hình theo tiêu chí tinh chỉnh.

### Conclusion & Future Works:
Bài nghiên cứu đã thành công trong việc mở rộng các ưu tiên nhị phân đơn giản và đề xuất một tiêu chí đánh giá mới, phù hợp với con người, dựa trên các tiêu chí chuyên gia đa chiều, rời rạc và không cân bằng. CPO cho phép điều chỉnh mô hình Diffusion bằng cách tách rời các thuộc tính tích cực và tiêu cực bên trong các mẫu được tạo ra, đồng thời chiến lược ổn định mới giải quyết các bất ổn trong tối ưu hóa. Công trình này xác nhận giá trị của việc đánh giá tinh chỉnh và mở ra những con đường mới cho các mô hình điều chỉnh sau huấn luyện trong tương lai.

### Brainstorming Space:
#### 1. Publish Papers:
1. Nghiên cứu việc áp dụng CPO để tinh chỉnh các mô hình Diffusion cho việc tạo ra ảnh y tế hoặc ảnh kỹ thuật, nơi yêu cầu sự chính xác cao và tuân thủ các tiêu chí chuyên môn khắt khe.
2. Khám phá việc tự động học các cấu trúc phân cấp thuộc tính từ dữ liệu phản hồi thô của người dùng thay vì xây dựng thủ công bởi chuyên gia, giảm thiểu công sức chú thích dữ liệu.
3. Phát triển một phương pháp thích nghi CPO để xử lý các yêu cầu điều chỉnh thay đổi theo thời gian hoặc theo ngữ cảnh khác nhau, cho phép mô hình tạo ra hình ảnh linh hoạt hơn.
#### 2. Patent:
1. Một hệ thống AI tích hợp trong ứng dụng camera điện thoại cho phép người dùng chọn các "tiêu chí chất lượng nghệ thuật" (ví dụ: bố cục vàng, màu sắc hài hòa) để AI tự động cải thiện ảnh ngay sau khi chụp theo các thuộc tính đã được tinh chỉnh.
2. Công nghệ tạo hình đại diện hoặc sticker cá nhân hóa trên điện thoại, cho phép người dùng định nghĩa các thuộc tính cụ thể (ví dụ: mắt trong sáng, đường nét cân đối) để AI tạo ra các hình ảnh phù hợp và loại bỏ các yếu tố không mong muốn.
3. Một tính năng "chỉnh sửa ảnh chuyên nghiệp thông minh" trong ứng dụng chỉnh sửa ảnh di động, nơi người dùng có thể chỉ ra các thuộc tính tích cực muốn nhấn mạnh và các thuộc tính tiêu cực muốn loại bỏ (ví dụ: loại bỏ chi tiết lộn xộn, làm nổi bật chủ thể chính) để AI thực hiện các điều chỉnh tinh tế.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.04300](https://huggingface.co/papers/2601.04300) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.04300](https://arxiv.org/abs/2601.04300) |
| PDF Download | [https://arxiv.org/pdf/2601.04300.pdf](https://arxiv.org/pdf/2601.04300.pdf) |
| Github Repository | N/A |

--- 

## 28. Enhancing Object Detection with Privileged Information: A Model-Agnostic Teacher-Student Approach

**Tác giả:** Matthias Bartolo, Dylan Seychell, Gabriel Hili, Matthew Montebello, Carl James Debono, Saviour Formosa, Konstantinos Makantasis

**Xuất bản lúc:** 2026-01-05

**Tag:** Computer Vision, Object Detection, Learning Using Privileged Information (LUPI), Knowledge Distillation, Teacher-Student Learning

### Main Problem:
Vấn đề cốt lõi mà bài báo đề cập là nâng cao độ chính xác và khả năng tổng quát hóa của các bộ phát hiện đối tượng dựa trên học sâu mà không làm tăng độ phức tạp suy luận hoặc kích thước mô hình. Các phương pháp hiện tại thường đòi hỏi kiến trúc phức tạp, tài nguyên tính toán lớn và các bộ dữ liệu được chú thích rộng lớn và tốn kém, đồng thời chưa tận dụng hết thông tin chi tiết, mô tả phong phú có sẵn trong quá trình huấn luyện (được gọi là thông tin đặc quyền - privileged information) nhưng không có sẵn trong quá trình suy luận.

### Main Idea:
Bài báo giới thiệu một phương pháp luận tổng quát, độc lập với kiến trúc model, để tích hợp thông tin đặc quyền (như mask của hộp giới hạn, bản đồ nổi bật và tín hiệu độ sâu) vào các bộ phát hiện đối tượng dựa trên học sâu. Phương pháp này sử dụng kiến trúc thầy-trò (teacher-student architecture): mạng thầy truy cập cả đầu vào tiêu chuẩn và thông tin đặc quyền để học các biểu diễn phong phú hơn, trong khi mạng trò chỉ xử lý đầu vào tiêu chuẩn. Trong quá trình huấn luyện, mạng trò được khuyến khích tái tạo các biểu diễn tiềm ẩn của mạng thầy thông qua cơ chế chưng cất tri thức (knowledge distillation), qua đó gián tiếp hưởng lợi từ thông tin đặc quyền mà không cần trực tiếp truy cập chúng trong quá trình suy luận.

### Main Results:
Các thí nghiệm được thực hiện trên năm mô hình phát hiện đối tượng hiện đại và nhiều bộ dữ liệu công khai (bao gồm bộ dữ liệu phát hiện rác thải dựa trên UAV và Pascal VOC 2012) cho thấy:
- Các mô hình student được huấn luyện bằng LUPI liên tục vượt trội so với các phiên bản baseline của chúng.
- Đạt được sự tăng cường đáng kể về độ chính xác phát hiện mà không làm tăng độ phức tạp suy luận hoặc kích thước mô hình.
- Các cải thiện hiệu suất đặc biệt rõ rệt đối với các đối tượng có kích thước trung bình và lớn.
- Các nghiên cứu phân tích (ablation studies) tiết lộ rằng việc điều chỉnh trọng số trung gian cho sự hướng dẫn từ mạng thầy giúp cân bằng tối ưu quá trình học từ cả đầu vào đặc quyền và đầu vào tiêu chuẩn.

### Conclusion & Future Works:
Những phát hiện này khẳng định rằng khung LUPI cung cấp một chiến lược hiệu quả và thiết thực để nâng cao các hệ thống phát hiện đối tượng trong cả môi trường hạn chế tài nguyên và thực tế. Bài báo đã mở rộng đáng kể nghiên cứu trước đây bằng cách phân tích hiệu suất trên các quy mô đối tượng, các chỉ số COCO tiêu chuẩn, và các dạng thông tin đặc quyền khác nhau, cũng như các yếu tố thực tế như thời gian suy luận và kích thước mô hình. Hướng nghiên cứu tiếp theo có thể bao gồm việc khám phá các loại thông tin đặc quyền mới và các phương pháp chưng cất tri thức nâng cao để tối ưu hóa hơn nữa quá trình học của student.

### Brainstorming Space:
#### 1. Publish Papers:
1.  Nghiên cứu cách sử dụng các mô hình tạo sinh (generative models) để tự động tạo thông tin đặc quyền chất lượng cao từ dữ liệu tiêu chuẩn nhằm tăng cường huấn luyện phát hiện đối tượng.
2.  Khám phá việc áp dụng phương pháp LUPI đa miền (multi-domain LUPI) trong phát hiện đối tượng, nơi thông tin đặc quyền từ một miền (ví dụ: ảnh nhiệt) được sử dụng để cải thiện hiệu suất trong một miền khác (ví dụ: ảnh RGB).
3.  Phân tích tác động của các phương pháp lượng tử hóa (quantization methods) lên các mô hình student được huấn luyện bằng LUPI để đạt được hiệu suất tối ưu trên các thiết bị biên có tài nguyên hạn chế.

#### 2. Patent:
1.  Một hệ thống camera trên điện thoại thông minh tích hợp cảm biến độ sâu (ví dụ: LiDAR) để tạo thông tin đặc quyền trong quá trình huấn luyện, giúp cải thiện đáng kể khả năng nhận diện vật thể trong điều kiện ánh sáng yếu hoặc môi trường phức tạp.
2.  Phương pháp huấn luyện mô hình phát hiện khuyết tật sản phẩm trên dây chuyền sản xuất sử dụng điện thoại di động, trong đó thông tin đặc quyền về cấu trúc vật liệu được thu thập bằng cảm biến chuyên dụng trong quá trình huấn luyện, cho phép mô hình trên điện thoại phát hiện khuyết tật chính xác hơn.
3.  Công nghệ tối ưu hóa thuật toán nhận diện khuôn mặt trên điện thoại bằng cách sử dụng thông tin đặc quyền về tư thế đầu hoặc biểu cảm khuôn mặt từ camera 3D trong quá trình huấn luyện, giúp tăng cường độ chính xác và khả năng chống giả mạo của hệ thống bảo mật sinh trắc học trên thiết bị.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.02016](https://huggingface.co/papers/2601.02016) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.02016](https://arxiv.org/abs/2601.02016) |
| PDF Download | [https://arxiv.org/pdf/2601.02016.pdf](https://arxiv.org/pdf/2601.02016.pdf) |
| Github Repository | N/A |

--- 

## 29. VERSE: Visual Embedding Reduction and Space Exploration. Clustering-Guided Insights for Training Data Enhancement in Visually-Rich Document Understanding

**Tác giả:** Ignacio de Rodrigo, Alvaro J. Lopez-Lopez, Jaime Boal

**Xuất bản lúc:** 2026-01-08

**Tag:** Visually-rich Document Understanding (VrDU), Vision-Language Models (VLMs), Visual Embeddings, Clustering, Data Enhancement, Interpretability, Explainability

### Main Problem:
Vấn đề cốt lõi mà bài báo đề cập là làm thế nào để phân tích và cải thiện các mô hình Vision–Language (VLM) ứng dụng trong Visually-rich Document Understanding (VrDU). Cụ thể, khi sử dụng dữ liệu tổng hợp trong các lĩnh vực có mẫu thực tế hạn chế, chất lượng hình ảnh thường được đánh giá theo quan điểm con người (ví dụ: độ chân thực), nhưng điều này không đảm bảo tính hữu ích cho mô hình. Vấn đề là cần một phương pháp để đánh giá chất lượng dữ liệu thông qua biểu diễn nội bộ của mô hình, xác định các vùng gây lỗi trong không gian nhúng thị giác và hướng dẫn tạo dữ liệu bổ sung hiệu quả.

### Main Idea:
Bài báo giới thiệu VERSE (Visual Embedding Reduction and Space Exploration), một phương pháp luận được thiết kế để phân tích, diễn giải và tận dụng cấu trúc không gian nhúng thị giác của các VLM. VERSE cho phép trực quan hóa các biểu diễn tiềm ẩn để đánh giá khả năng của mô hình, xác định các vùng có vấn đề (các cụm lỗi) và hướng dẫn tạo dữ liệu tổng hợp nhằm nâng cao hiệu suất trong các cụm đó. Phương pháp này thay đổi mô hình đánh giá dữ liệu huấn luyện tổng hợp từ góc độ lấy con người làm trung tâm sang góc độ lấy mô hình làm trung tâm, dựa trên các biểu diễn nội bộ của mô hình.

### Main Results:
Các kết quả chính cho thấy VERSE giúp phát hiện ra các đặc điểm thị giác liên quan đến các cụm dễ gây lỗi. Việc huấn luyện lại mô hình với các mẫu chứa những đặc điểm này làm tăng đáng kể hiệu suất F1 mà không làm suy giảm khả năng tổng quát hóa. Hơn nữa, các mô hình chạy trên hệ thống nội bộ (on-premise) như Donut và Idefics2, khi được tối ưu hóa bằng VERSE, có thể đạt hoặc thậm chí vượt qua hiệu suất của các giải pháp SaaS hàng đầu như GPT-4 và Pixtral.

### Conclusion & Future Works:
VERSE là một phương pháp luận mới để phân tích không gian nhúng thị giác, cung cấp các hiểu biết sâu sắc dựa trên phân cụm để tăng cường dữ liệu huấn luyện trong Visually-rich Document Understanding. Nó giúp giải thích hành vi của mô hình, xác định các vùng lỗi và cải thiện hiệu suất thông qua việc tạo dữ liệu tổng hợp có mục tiêu.
Hướng nghiên cứu tương lai: Không được đề cập trực tiếp trong phần trích dẫn này của bài báo.

### Brainstorming Space:
#### 1. Publish Papers:
1. Nghiên cứu mở rộng VERSE để tích hợp phân tích không gian nhúng đa phương thức (thị giác, văn bản, bố cục) nhằm cung cấp cái nhìn toàn diện hơn về hoạt động của VLM trong VrDU.
2. Phát triển một hệ thống tự động hoàn toàn sử dụng kết quả phân tích cụm lỗi của VERSE để trực tiếp tạo ra dữ liệu tổng hợp mới, nhằm liên tục cải thiện hiệu suất mô hình.
3. Áp dụng phương pháp VERSE cho các lĩnh vực khác ngoài tài liệu, chẳng hạn như phân tích hình ảnh y tế hoặc hình ảnh địa lý, để tối ưu hóa việc tạo dữ liệu và hiệu suất mô hình trong các ngữ cảnh đó.

#### 2. Patent:
1. Hệ thống tối ưu hóa chụp ảnh tài liệu trên điện thoại thông minh, tích hợp phân tích không gian nhúng thị giác theo VERSE để đưa ra phản hồi thời gian thực về chất lượng ảnh và hướng dẫn người dùng chụp lại nếu ảnh nằm trong vùng lỗi tiềm ẩn của mô hình VrDU.
2. Công nghệ tạo dữ liệu huấn luyện tăng cường trên thiết bị di động, cho phép các nhà phát triển tạo ra các mẫu dữ liệu tổng hợp được tối ưu hóa bởi VERSE trực tiếp trên điện thoại thông minh để cải thiện các mô hình nhận dạng tài liệu trên thiết bị.
3. Giải pháp điều chỉnh mô hình AI nhận diện tài liệu theo ngữ cảnh chụp ảnh di động, sử dụng VERSE để phân tích các đặc điểm thị giác phổ biến từ ảnh chụp điện thoại (như bóng, nếp nhăn) và tự động tạo dữ liệu huấn luyện bổ sung để nâng cao độ chính xác của mô hình trên thiết bị.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.05125](https://huggingface.co/papers/2601.05125) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.05125](https://arxiv.org/abs/2601.05125) |
| PDF Download | [https://arxiv.org/pdf/2601.05125.pdf](https://arxiv.org/pdf/2601.05125.pdf) |
| Github Repository | [https://github.com/nachoDRT/VrDU-Doctor](https://github.com/nachoDRT/VrDU-Doctor) |

--- 

## 30. Learning User Preferences Through Interaction for Long-Term Collaboration

**Tác giả:** Shuhaib Mehri, Priyanka Kargupta, Tal August, Dilek Hakkani-Tür

**Xuất bản lúc:** 2026-01-06

**Tag:** Conversational Agents, User Preferences, Long-Term Collaboration, Memory, Reinforcement Learning

### Main Problem:
Vấn đề cốt lõi là các tác nhân hội thoại hiện tại gặp khó khăn trong việc học hỏi và thích ứng liên tục với sở thích của người dùng qua nhiều phiên tương tác. Điều này dẫn đến gánh nặng nhận thức cho người dùng khi phải lặp lại các tùy chọn của họ và cản trở việc cải thiện chất lượng hợp tác lâu dài giữa người và AI, do tác nhân không thể nhận ra và tận dụng thông tin có giá trị cho các tương tác trong tương lai.

### Main Idea:
Bài báo giới thiệu **MULTISESSIONCOLLAB**, một bộ tiêu chuẩn mới để đánh giá khả năng của tác nhân hội thoại trong việc học và tận dụng sở thích người dùng nhằm cải thiện chất lượng hợp tác trong nhiều phiên. Để giải quyết vấn đề này, các tác giả đề xuất các tác nhân cộng tác dài hạn được trang bị bộ nhớ, bộ nhớ này sẽ lưu giữ và tinh chỉnh sở thích người dùng khi kinh nghiệm tương tác tích lũy. Hơn nữa, bài báo trình bày một khung học tăng cường (RL) sử dụng tín hiệu học tập từ hành vi của trình mô phỏng người dùng trong MULTISESSIONCOLLAB để đào tạo tác nhân tạo ra các phản hồi toàn diện hơn và cập nhật bộ nhớ hiệu quả hơn.

### Main Results:
Các thử nghiệm sâu rộng đã chứng minh rằng việc trang bị bộ nhớ cho tác nhân giúp cải thiện sự hợp tác dài hạn, dẫn đến tỷ lệ hoàn thành nhiệm vụ cao hơn, tương tác hiệu quả hơn và giảm nỗ lực của người dùng. Phân tích hiệu suất qua các phiên cho thấy sự cải thiện liên tục, với những cải tiến rõ rệt nhất ở các phiên đầu và ổn định dần sau đó. Đáng chú ý, các tác nhân học sở thích qua tương tác có hiệu suất cạnh tranh với những tác nhân được cấp quyền truy cập trực tiếp vào sở thích người dùng thực, cho thấy bộ nhớ đã thu thập thông tin phong phú hơn về sở thích. Một nghiên cứu với người thật cũng xác nhận rằng bộ nhớ giúp cải thiện trải nghiệm người dùng trong các thiết lập thực tế, với người tham gia mô tả các tác nhân này là cá nhân hóa và chủ động hơn.

### Conclusion & Future Works:
Bài báo kết luận rằng việc trang bị bộ nhớ cho tác nhân hội thoại là một cách hiệu quả để học hỏi và áp dụng sở thích người dùng, từ đó cải thiện đáng kể chất lượng hợp tác dài hạn.
Về hướng nghiên cứu tiếp theo, nghiên cứu đã chỉ ra những thách thức trong việc khái quát hóa sở thích người dùng qua nhiều lĩnh vực (cross-domain preference generalization). Điều này mở ra hướng nghiên cứu để phát triển các phương pháp giúp tác nhân có thể áp dụng sở thích đã học được cho các loại nhiệm vụ hoặc ngữ cảnh khác nhau một cách linh hoạt hơn.

### Brainstorming Space:
#### 1. Publish Papers:
1.  Nghiên cứu các kiến trúc bộ nhớ động cho phép tác nhân tự động quyết định thông tin nào cần lưu trữ, thời gian lưu giữ và khi nào nên loại bỏ các sở thích ít liên quan.
2.  Phát triển các chiến lược học tăng cường tiên tiến để cải thiện khả năng khái quát hóa sở thích người dùng đã học qua nhiều lĩnh vực nhiệm vụ khác nhau.
3.  Khám phá các phương pháp để tác nhân chủ động gợi mở và làm rõ sở thích của người dùng khi có sự mơ hồ hoặc thiếu thông tin, thay vì chỉ phản ứng lại các chỉ dẫn.

#### 2. Patent:
1.  Hệ thống trợ lý cá nhân thông minh trên điện thoại có khả năng ghi nhớ và thích ứng liên tục với sở thích giao tiếp và phong cách làm việc của người dùng qua các phiên tương tác.
2.  Phương pháp tích hợp AI ghi nhớ sở thích người dùng vào các ứng dụng giải quyết vấn đề hoặc học tập trên điện thoại, cho phép tối ưu hóa trải nghiệm và hiệu quả hỗ trợ theo thời gian.
3.  Công nghệ điều chỉnh giao diện người dùng và cách hiển thị thông tin trên điện thoại dựa trên việc học hỏi sở thích cá nhân của người dùng qua lịch sử sử dụng ứng dụng đa phiên.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.02702](https://huggingface.co/papers/2601.02702) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.02702](https://arxiv.org/abs/2601.02702) |
| PDF Download | [https://arxiv.org/pdf/2601.02702.pdf](https://arxiv.org/pdf/2601.02702.pdf) |
| Github Repository | N/A |

--- 

## 31. Safety at One Shot: Patching Fine-Tuned LLMs with A Single Instance

**Tác giả:** Jiawen Zhang, Lipeng He, Kejia Chen, Jian Lou, Jian Liu, Xiaohu Yang, Ruoxi Jia

**Xuất bản lúc:** 2026-01-05

**Tag:** LLMs, Safety Alignment, Fine-tuning Attacks, One-shot Learning, Gradient Analysis, Bi-level Optimization
### Main Problem:
Việc tinh chỉnh (fine-tuning) các mô hình ngôn ngữ lớn (LLMs) có thể làm giảm đáng kể mức độ an toàn của chúng, cho phép tạo ra nội dung độc hại. Các phương pháp khôi phục an toàn hiện có đòi hỏi nhiều mẫu dữ liệu hoặc bộ hiệu chuẩn lớn, gây ra chi phí tính toán đáng kể, dẫn đến sự suy giảm về khả năng tiện ích của mô hình, và có thể chưa giải quyết triệt để các lỗ hổng. Vấn đề cốt lõi là làm thế nào để khôi phục hoàn toàn sự an toàn của mô hình một cách hiệu quả, với chi phí tối thiểu và không làm suy giảm tiện ích.

### Main Idea:
Bài báo đề xuất một phương pháp mới gọi là "vá lỗi an toàn một lần" (one-shot safety recovery), cho thấy rằng chỉ với một ví dụ an toàn được chọn lọc cẩn thận, có thể khôi phục hoàn toàn sự an toàn của LLM đã bị xâm phạm. Phương pháp này không làm mất đi tiện ích của mô hình và chỉ tốn chi phí tối thiểu. Các tác giả cũng giải thích cơ chế hoạt động bằng cách chỉ ra cấu trúc hạng thấp (low-rank structure) của gradient an toàn, cho thấy tín hiệu căn chỉnh nằm trong một không gian con nội tại hạng thấp và các hướng chủ đạo của không gian này gần như đối nghịch với các gradient có hại.

### Main Results:
*   Phương pháp vá lỗi an toàn một lần khôi phục hoàn toàn an toàn (ASR = 0, HS = 1.0) trên nhiều LLMs mã nguồn mở (Llama, Mistral, Qwen) và API mã nguồn đóng (GPT-4.1).
*   Phương pháp này duy trì hoàn hảo tiện ích của mô hình trên các tác vụ xuôi dòng (SQL, MMLU, MT-bench).
*   Đạt hiệu quả cao nhất với chi phí tính toán thấp nhất (chỉ 1-2 phút GPU bổ sung).
*   Sự khôi phục hiệu quả bất kể số lượng ví dụ độc hại được sử dụng trong tinh chỉnh hoặc kích thước của mô hình cơ bản.
*   Sự hội tụ đạt được chỉ trong vài epoch.
*   Phân tích cấu trúc hạng thấp của gradient an toàn giải thích lý do tại sao việc hiệu chỉnh hiệu quả như vậy là khả thi.

### Conclusion & Future Works:
Bài nghiên cứu kết luận rằng việc khôi phục an toàn cho LLM bị tinh chỉnh có thể thực hiện hiệu quả chỉ với một ví dụ an toàn duy nhất, phá vỡ quan niệm trước đây về yêu cầu dữ liệu lớn. Điều này đạt được mà không làm suy giảm tiện ích và với chi phí tối thiểu, được hỗ trợ bởi bằng chứng thực nghiệm mạnh mẽ và phân tích cấu trúc hạng thấp của gradient an toàn. Thông điệp cuối cùng là sự khả thi của một giải pháp hiệu quả và ít tốn kém cho các thách thức an toàn trong mô hình LLM-as-a-Service. Hướng nghiên cứu tiếp theo có thể bao gồm việc mở rộng các nguyên lý này sang các loại sai lệch khác hoặc các kịch bản tấn công tinh chỉnh phức tạp hơn.

### Brainstorming Space:
#### 1. Publish Papers:
1.  Nghiên cứu ứng dụng phương pháp vá lỗi một lần này để khôi phục các dạng sai lệch khác của LLM, chẳng hạn như định kiến xã hội hoặc thông tin sai lệch.
2.  Phân tích sâu hơn cấu trúc gradient và các không gian nội tại để xác định các đặc điểm chung của việc khôi phục an toàn hiệu quả trên các kiến trúc mô hình và miền tác vụ khác nhau.
3.  Khám phá việc tự động chọn lựa "ví dụ an toàn một lần" tối ưu thông qua các phương pháp học tăng cường hoặc tối ưu hóa meta-learning.

#### 2. Patent:
1.  Hệ thống bảo vệ LLM tích hợp trên điện thoại thông minh, tự động phát hiện và vá lỗi an toàn cho các ứng dụng dựa trên LLM bằng một ví dụ duy nhất khi có cập nhật hoặc phát hiện hành vi độc hại.
2.  Phương pháp tối ưu hóa tài nguyên trên thiết bị di động để thực hiện vá lỗi an toàn tức thì cho các mô hình ngôn ngữ cá nhân hóa (ví dụ: bàn phím thông minh, trợ lý ảo) chỉ với một mẫu dữ liệu được người dùng cung cấp.
3.  Công nghệ "SafePatch API" cho phép các nhà phát triển ứng dụng di động triển khai khả năng khôi phục an toàn cho LLM của họ chỉ bằng cách cung cấp một ví dụ an toàn, đảm bảo tuân thủ và độ tin cậy.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.01887](https://huggingface.co/papers/2601.01887) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.01887](https://arxiv.org/abs/2601.01887) |
| PDF Download | [https://arxiv.org/pdf/2601.01887.pdf](https://arxiv.org/pdf/2601.01887.pdf) |
| Github Repository | N/A |

--- 

## 32. LEMAS: Large A 150K-Hour Large-scale Extensible Multilingual Audio Suite with Generative Speech Models

**Tác giả:** Zhiyuan Zhao, Lijian Lin, Ye Zhu, Kai Xie, Yunfei Liu, Yu Li

**Xuất bản lúc:** 2026-01-04

**Tag:** Generative Speech Models, Multilingual Speech Synthesis, Speech Editing, Large-scale Multilingual Corpus, Word-level Timestamps, Flow-matching, Autoregressive Models

### Main Problem:
Vấn đề cốt lõi mà bài báo đề cập là giới hạn trong khả năng của các mô hình giọng nói sinh học trong môi trường đa ngôn ngữ. Hạn chế này chủ yếu do thách thức về dữ liệu: việc thu thập và tuyển chọn dữ liệu giọng nói đa ngôn ngữ quy mô lớn với chất lượng nhất quán và chú thích thời gian chi tiết là vô cùng khó khăn. Các kho ngữ liệu thu thập từ web hiện có cung cấp sự đảm bảo hạn chế về chất lượng dữ liệu và độ tin cậy của chú thích trong các thiết lập đa ngôn ngữ.

### Main Idea:
Bài báo giới thiệu **LEMAS-Dataset**, một kho ngữ liệu giọng nói đa ngôn ngữ mã nguồn mở lớn nhất (hơn 150,000 giờ trên 10 ngôn ngữ chính) với các dấu thời gian cấp từ chính xác, được xây dựng thông qua một quy trình xử lý dữ liệu hiệu quả để đảm bảo chất lượng cao. Để chứng minh tính hiệu quả của LEMAS-Dataset, nhóm nghiên cứu đã đào tạo hai mô hình nền tảng:
1.  **LEMAS-TTS:** Một mô hình tổng hợp giọng nói (TTS) không tự hồi quy dựa trên khung flow-matching. Nó khai thác quy mô lớn và sự đa dạng ngôn ngữ của bộ dữ liệu để đạt được tổng hợp đa ngôn ngữ zero-shot mạnh mẽ, sử dụng huấn luyện chống giọng điệu (accent-adversarial training) và CTC loss để giảm thiểu các vấn đề về giọng điệu đa ngôn ngữ và tăng cường độ ổn định tổng hợp.
2.  **LEMAS-Edit:** Một hệ thống chỉnh sửa giọng nói dựa trên kiến trúc chỉ bộ giải mã tự hồi quy. Nó xây dựng nhiệm vụ chỉnh sửa giọng nói dưới dạng điền mã thông báo bị che, tận dụng sự căn chỉnh cấp từ chính xác và áp dụng các chiến lược giải mã thích ứng để đạt được chỉnh sửa giọng nói liền mạch, ranh giới mượt mà với chuyển đổi tự nhiên.

### Main Results:
*   LEMAS-Dataset được phát hành là kho ngữ liệu giọng nói đa ngôn ngữ mã nguồn mở lớn nhất với dấu thời gian cấp từ chính xác, bao gồm hơn 150,000 giờ trên 10 ngôn ngữ, được xây dựng bằng quy trình căn chỉnh có khả năng mở rộng với ước tính độ tin cậy cấp từ.
*   Các mô hình được huấn luyện trên LEMAS-Dataset, cụ thể là LEMAS-TTS và LEMAS-Edit, mang lại hiệu suất tổng hợp và chỉnh sửa chất lượng cao, xác nhận chất lượng của bộ dữ liệu.
*   LEMAS-TTS đạt được khả năng tổng hợp đa ngôn ngữ zero-shot mạnh mẽ với khả năng dễ hiểu được cải thiện và tính nhất quán về giọng điệu.
*   LEMAS-Edit cho phép chỉnh sửa đa ngôn ngữ liền mạch, ranh giới mượt mà và hoạt động hiệu quả ngay cả trên âm thanh "in-the-wild" có tiếng ồn môi trường.

### Conclusion & Future Works:
Bài báo kết luận rằng việc thiếu kho ngữ liệu giọng nói đa ngôn ngữ quy mô lớn, chất lượng cao với các chú thích chi tiết là một nút thắt cổ chai lớn trong việc phát triển các mô hình giọng nói sinh học mạnh mẽ. Bằng cách giới thiệu LEMAS-Dataset và chứng minh hiệu quả của nó thông qua hai mô hình nền tảng (LEMAS-TTS và LEMAS-Edit), nghiên cứu này cung cấp một nguồn tài nguyên quý giá để thúc đẩy lĩnh vực này. Nhóm nghiên cứu hình dung rằng kho ngữ liệu đa ngôn ngữ được chú thích dấu thời gian phong phú, chi tiết này sẽ thúc đẩy những tiến bộ trong các hệ thống tạo giọng nói dựa trên lời nhắc (prompt-based speech generation systems) trong tương lai.

### Brainstorming Space:
#### 1. Publish Papers:
1.  Nghiên cứu ảnh hưởng của các kỹ thuật xử lý dữ liệu khác nhau trong quy trình xây dựng LEMAS-Dataset đến hiệu suất của các mô hình giọng nói sinh học.
2.  Khám phá việc tích hợp các mô hình ngôn ngữ lớn (LLMs) với LEMAS-TTS và LEMAS-Edit để cải thiện khả năng tạo và chỉnh sửa giọng nói dựa trên ngữ cảnh.
3.  Đánh giá hiệu quả của LEMAS-Dataset trong việc huấn luyện các mô hình nhận dạng giọng nói tự động (ASR) đa ngôn ngữ, đặc biệt là trong các ngôn ngữ ít tài nguyên.
#### 2. Patent:
1.  Hệ thống chỉnh sửa giọng nói trên điện thoại di động cho phép người dùng chọn và chỉnh sửa các từ cụ thể trong bản ghi âm giọng nói, tự động điều chỉnh ngữ điệu và khớp âm thanh để tạo ra một bản ghi liền mạch.
2.  Ứng dụng tổng hợp giọng nói đa ngôn ngữ tích hợp trên điện thoại, cho phép người dùng tạo bản sao giọng nói của mình bằng nhiều ngôn ngữ khác nhau chỉ từ một đoạn văn bản và mẫu giọng nói ngắn.
3.  Công nghệ tích hợp vào ứng dụng quay phim hoặc ghi âm trên điện thoại thông minh, tự động gắn dấu thời gian cấp từ cho mọi nội dung âm thanh và cung cấp tùy chọn tự động dịch hoặc chuyển ngữ theo thời gian thực.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.04233](https://huggingface.co/papers/2601.04233) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.04233](https://arxiv.org/abs/2601.04233) |
| PDF Download | [https://arxiv.org/pdf/2601.04233.pdf](https://arxiv.org/pdf/2601.04233.pdf) |
| Github Repository | N/A |

--- 

## 33. Towards Open-Vocabulary Industrial Defect Understanding with a Large-Scale Multimodal Dataset

**Tác giả:** TsaiChing Ni, ZhenQi Chen, YuanFu Yang

**Xuất bản lúc:** 2025-12-30

**Tag:** Multimodal Learning, Diffusion Model, Vision-Language Model (VLM), Industrial Defect Understanding, Large-Scale Dataset, Foundation Model, Open-Vocabulary
### Main Problem:
Vấn đề cốt lõi mà bài báo đề cập là những hạn chế của các hệ thống kiểm tra chất lượng tự động (AOI) hiện tại và các phương pháp học sâu chuyên biệt trong việc phát hiện lỗi công nghiệp. Các hệ thống này gặp phải tỷ lệ báo động sai cao, khả năng thích ứng kém với các mẫu lỗi mới, khó khái quát hóa qua nhiều ngữ cảnh sản xuất, và thiếu khả năng diễn giải ngữ nghĩa. Các mô hình ngôn ngữ thị giác (VLM) hiện có, được đào tạo chủ yếu trên hình ảnh tự nhiên, không có đủ kiến thức chuyên môn về các lỗi công nghiệp tinh vi, cục bộ và yêu cầu thuật ngữ miền cụ thể. Hơn nữa, thiếu dữ liệu lỗi công nghiệp đa phương thức quy mô lớn là một rào cản lớn.

### Main Idea:
Bài báo giới thiệu IMDD-1M, bộ dữ liệu lỗi công nghiệp đa phương thức quy mô lớn đầu tiên, bao gồm 1.000.000 cặp hình ảnh-văn bản được căn chỉnh, nhằm thúc đẩy học tập đa phương thức trong sản xuất và kiểm tra chất lượng. Bộ dữ liệu này chứa các lỗi thực tế độ phân giải cao, bao gồm hơn 60 loại vật liệu và hơn 400 loại lỗi, mỗi loại đi kèm với chú thích được chuyên gia xác minh và mô tả văn bản chi tiết. Dựa trên IMDD-1M, các tác giả đào tạo một mô hình nền tảng ngôn ngữ thị giác dựa trên khuếch tán (diffusion-based VLM) từ đầu, được điều chỉnh đặc biệt cho các kịch bản công nghiệp. Mô hình này phục vụ như một nền tảng tổng quát có thể được thích ứng hiệu quả với các miền chuyên biệt thông qua việc tinh chỉnh nhẹ nhàng (lightweight fine-tuning) và có khả năng tích hợp các khả năng phân biệt (discriminative) và tạo sinh (generative).

### Main Results:
IMDD-1M là bộ dữ liệu công nghiệp quy mô triệu mẫu đầu tiên với 1.24 triệu cặp hình ảnh-văn bản, bao gồm 421 loại lỗi trên 63 lĩnh vực sản xuất, vượt qua các bộ dữ liệu hiện có về quy mô gấp khoảng hai bậc độ lớn. Mô hình nền tảng dựa trên khuếch tán được đào tạo trên IMDD-1M có thể thích ứng hiệu quả với các miền chuyên biệt, đạt được hiệu suất tương đương với các mô hình chuyên gia chỉ với chưa đến 5% dữ liệu dành riêng cho tác vụ. Điều này nhấn mạnh tiềm năng của việc thích ứng mô hình nền tảng hiệu quả dữ liệu cho kiểm tra và tạo sinh trong công nghiệp.

### Conclusion & Future Works:
Bài báo kết luận rằng IMDD-1M và mô hình nền tảng ngôn ngữ thị giác dựa trên khuếch tán mà họ đề xuất mở đường cho trí tuệ sản xuất có khả năng mở rộng, thích ứng theo miền và dựa trên kiến thức. Mô hình nền tảng này, tích hợp khả năng tạo sinh và phân biệt, cung cấp một giải pháp tổng quát cho việc hiểu lỗi công nghiệp và có thể được điều chỉnh hiệu quả cho nhiều ứng dụng như phân loại, phân đoạn, truy xuất, chú thích và mô hình tạo sinh. Hướng nghiên cứu tiếp theo bao gồm việc tiếp tục phát triển và ứng dụng mô hình nền tảng này trong các môi trường công nghiệp thực tế.

### Brainstorming Space:
#### 1. Publish Papers:
1. Nghiên cứu phương pháp sử dụng IMDD-1M để tự động tạo ra các bài kiểm tra chất lượng tổng hợp cho các dây chuyền sản xuất mới nhằm rút ngắn thời gian phát triển sản phẩm.
2. Khám phá việc áp dụng mô hình ngôn ngữ thị giác được đào tạo trên IMDD-1M để hỗ trợ các kỹ thuật viên bảo trì bằng cách cung cấp mô tả lỗi và đề xuất sửa chữa dựa trên hình ảnh.
3. Phát triển một phương pháp thích ứng miền không giám sát (unsupervised domain adaptation) cho mô hình nền tảng IMDD-1M để xử lý hiệu quả hơn các dữ liệu lỗi từ các miền công nghiệp chưa từng thấy trước đây.

#### 2. Patent:
1. Một hệ thống kiểm tra chất lượng tự động tích hợp trực tiếp vào dây chuyền sản xuất điện thoại thông minh, sử dụng mô hình nền tảng đã tinh chỉnh từ IMDD-1M để nhận diện và phân loại các lỗi vi mô trên bo mạch chủ hoặc vỏ điện thoại.
2. Công nghệ tạo dữ liệu lỗi tổng hợp dựa trên IMDD-1M, cho phép nhà sản xuất điện thoại mô phỏng và tạo ra các kịch bản lỗi hiếm gặp để kiểm tra độ bền và độ tin cậy của sản phẩm mà không cần tạo ra lỗi thực tế.
3. Ứng dụng di động cho phép người dùng cuối chụp ảnh thiết bị điện thoại của họ, sau đó gửi đến một API đám mây sử dụng mô hình VLM được đào tạo trên IMDD-1M để chẩn đoán lỗi phần cứng và đề xuất dịch vụ sửa chữa phù hợp.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2512.24160](https://huggingface.co/papers/2512.24160) |
| ArXiv Abstract | [https://arxiv.org/abs/2512.24160](https://arxiv.org/abs/2512.24160) |
| PDF Download | [https://arxiv.org/pdf/2512.24160.pdf](https://arxiv.org/pdf/2512.24160.pdf) |
| Github Repository | [https://github.com/NinaNeon/IMDD-1M-Towards-Open-Vocabulary-Industrial-Defect-](https://github.com/NinaNeon/IMDD-1M-Towards-Open-Vocabulary-Industrial-Defect-) |

