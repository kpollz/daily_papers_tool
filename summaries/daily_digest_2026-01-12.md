# 🤗 Daily Hugging Face Paper Digest - 2026-01-12

Báo cáo được tạo tự động vào lúc 2026-01-12 13:34:03 bằng mô hình `gemini-2.5-flash`.

## 📰 Summary of Papers

--- 

## 1. Thinking with Map: Reinforced Parallel Map-Augmented Agent for Geolocalization

**Tác giả:** Yuxiang Ji, Yong Wang, Ziyu Ma, Yiming Hu, Hailang Huang, Xuecai Hu, Guanhua Chen, Liaoni Wu, Xiangxiang Chu

**Xuất bản lúc:** 2026-01-08

**Tag:** Geolocalization, Large Vision-Language Models (LVLM), Agentic AI, Reinforcement Learning (RL), Map Tools, Parallel Thinking, Test-Time Scaling (TTS)

### I. Main Problem:
Vấn đề cốt lõi mà bài báo đề cập là bài toán định vị địa lý hình ảnh (image geolocalization), mục tiêu là dự đoán vị trí (vĩ độ và kinh độ) mà một hình ảnh được chụp ở bất cứ đâu trên Trái Đất, chỉ sử dụng các manh mối thị giác. Các phương pháp hiện có dựa trên mô hình ngôn ngữ thị giác lớn (LVLM) thường bỏ qua một chiến lược phổ biến mà con người sử dụng – đó là sử dụng bản đồ, dẫn đến những hạn chế về độ chính xác, khả năng diễn giải và khả năng khái quát hóa đối với hình ảnh thực tế, đồng thời dễ bị ảnh hưởng bởi hiện tượng "ảo giác" và sai lệch của LVLM.

### II. Main Idea:
Bài báo đề xuất phương pháp "Thinking with Map" bằng cách trang bị cho các mô hình LVLM khả năng sử dụng các công cụ bản đồ như con người để giải quyết bài toán định vị địa lý hình ảnh. Phương pháp này được thiết kế như một vòng lặp tác tử-trong-bản đồ (agent-in-the-map loop) bao gồm việc đề xuất giả thuyết vị trí, truy xuất thông tin bản đồ, kiểm tra chéo và hội tụ quyết định. Nó sử dụng một lược đồ tối ưu hóa hai giai đoạn:
1.  **Học tăng cường tác tử (Agentic Reinforcement Learning - RL):** Củng cố khả năng tác tử của mô hình để cải thiện hiệu quả lấy mẫu.
2.  **Mở rộng thời gian kiểm tra song song (Parallel Test-Time Scaling - TTS):** Cho phép mô hình khám phá nhiều đường dẫn ứng cử viên trước khi đưa ra dự đoán cuối cùng, điều này rất quan trọng cho định vị địa lý.
Các công cụ bản đồ được cung cấp bao gồm các giao diện API như tìm kiếm từ khóa POI (Point of Interest), tra cứu chi tiết POI, truy vấn bản đồ tĩnh và bản đồ vệ tinh, cho phép mô hình truy xuất và xác minh thông tin trong môi trường bản đồ có cấu trúc. Bài báo cũng giới thiệu MAPBench, một bộ dữ liệu đánh giá toàn diện gồm hình ảnh thực tế để kiểm tra phương pháp.

### III. Main Results:
*   Phương pháp đề xuất vượt trội so với các mô hình mã nguồn mở và mã nguồn đóng hiện có trên hầu hết các chỉ số.
*   Cụ thể, nó cải thiện độ chính xác Acc@500m từ 8.0% lên 22.1% so với Gemini-3-Pro (với chế độ có thông tin từ Google Search/Map).
*   MAPBench, một bộ dữ liệu đào tạo và đánh giá định vị địa lý toàn diện bao gồm các hình ảnh đường phố và POI đô thị thực tế của Trung Quốc, đã được giới thiệu.

### IV. Conclusion & Future Works:
Bài báo trình bày một tác tử tăng cường bản đồ sáng tạo cho bài toán định vị địa lý hình ảnh trên toàn cầu, trang bị cho mô hình khả năng "Thinking with Map". Bằng cách kết hợp học tăng cường tác tử để cải thiện hiệu quả lấy mẫu và mở rộng thời gian kiểm tra song song với trình xác minh để khám phá nhiều giả thuyết, phương pháp này vượt trội đáng kể so với các mô hình LVLM hiện có. Mặc dù không trực tiếp nêu rõ hướng nghiên cứu tiếp theo trong phần trích dẫn, việc thiết lập khung tác tử-trong-bản đồ mở ra tiềm năng cho các tác tử AI tương tác hiệu quả hơn với môi trường thực tế và xác minh thông tin một cách có căn cứ.

### V. Brainstorming Space:

#### 1. Publish Papers:
*   Nghiên cứu cách tích hợp các công cụ bản đồ 3D hoặc dữ liệu LiDAR vào khung "Thinking with Map" để cải thiện độ chính xác định vị trong môi trường phức tạp.
*   Khám phá việc áp dụng phương pháp "Thinking with Map" cho các tác vụ hiểu ngữ cảnh hình ảnh khác yêu cầu suy luận địa lý, chẳng hạn như nhận dạng danh lam thắng cảnh hoặc phân loại môi trường đô thị.
*   Phát triển một phương pháp học tăng cường tự giám sát cho tác tử bản đồ để liên tục cải thiện khả năng suy luận và sử dụng công cụ mà không cần chú thích thủ công.

#### 2. Patent:
*   Hệ thống định vị địa lý di động thông minh tích hợp công nghệ "Thinking with Map" để cung cấp thông tin vị trí chính xác hơn cho người dùng dựa trên hình ảnh chụp từ điện thoại, ngay cả khi tín hiệu GPS yếu hoặc không có.
*   Ứng dụng camera điện thoại có khả năng nhận dạng và hiển thị thông tin về các điểm quan tâm (POI) xung quanh người dùng thông qua phân tích hình ảnh và truy vấn bản đồ theo thời gian thực, tương tự như cách con người "suy nghĩ với bản đồ".
*   Phương pháp tối ưu hóa pin cho điện thoại thông minh bằng cách sử dụng "Thinking with Map" để lựa chọn công cụ định vị (GPS, Wi-Fi, hình ảnh) hiệu quả nhất dựa trên ngữ cảnh hình ảnh hiện tại, giảm thiểu việc tiêu thụ năng lượng không cần thiết.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.05432](https://huggingface.co/papers/2601.05432) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.05432](https://arxiv.org/abs/2601.05432) |
| PDF Download | [https://arxiv.org/pdf/2601.05432.pdf](https://arxiv.org/pdf/2601.05432.pdf) |
| Github Repository | [https://github.com/AMAP-ML/Thinking-with-Map](https://github.com/AMAP-ML/Thinking-with-Map) |

--- 

## 2. Chaining the Evidence: Robust Reinforcement Learning for Deep Search Agents with Citation-Aware Rubric Rewards

**Tác giả:** Jiajie Zhang, Xin Lv, Ling Feng, Lei Hou, Juanzi Li

**Xuất bản lúc:** 2026-01-09

**Tag:** Reinforcement Learning, LLM, Deep Search Agents, Reward Function, Citation-aware, Rubric Rewards

### I. Main Problem:
Các phương pháp học tăng cường (Reinforcement Learning - RL) hiện tại cho các tác nhân tìm kiếm sâu dựa trên LLM chủ yếu dựa vào phần thưởng kết quả nhị phân (binary outcome rewards). Các phần thưởng này không nắm bắt được tính toàn diện và tính xác thực của quy trình suy luận của tác nhân, dẫn đến các hành vi không mong muốn như khai thác lối tắt (shortcut exploitation) và ảo giác (hallucinations), làm giảm độ mạnh mẽ và hiệu suất của tác nhân.

### II. Main Idea:
Bài báo đề xuất Citation-aware Rubric Rewards (CaRR), một khung phần thưởng chi tiết mới cho các tác nhân tìm kiếm sâu, nhấn mạnh tính toàn diện của suy luận, tính nền tảng thực tế và tính kết nối của bằng chứng. CaRR phân rã các câu hỏi phức tạp thành các tiêu chí đánh giá (rubrics) một bước có thể kiểm chứng được. Các tác nhân phải thỏa mãn các rubrics này bằng cách xác định rõ ràng các thực thể ẩn, hỗ trợ chúng bằng các trích dẫn chính xác và xây dựng các chuỗi bằng chứng hoàn chỉnh liên kết đến câu trả lời dự đoán. Hơn nữa, bài báo giới thiệu Citation-aware Group Relative Policy Optimization (C-GRPO), một thuật toán RL mở rộng của GRPO, kết hợp CaRR và phần thưởng kết quả để huấn luyện các tác nhân tìm kiếm sâu mạnh mẽ, gán thêm phần thưởng rubrics có trọng số cho các quỹ đạo có phần thưởng kết quả là 1.

### III. Main Results:
Các thử nghiệm cho thấy C-GRPO liên tục vượt trội so với các phương pháp cơ sở RL chỉ dựa trên phần thưởng kết quả trên nhiều chuẩn tìm kiếm sâu. Phân tích cũng xác nhận rằng C-GRPO ngăn chặn hiệu quả việc khai thác lối tắt, thúc đẩy suy luận toàn diện và dựa trên bằng chứng được trích dẫn. Ngoài ra, các tác nhân được huấn luyện bằng C-GRPO thể hiện khả năng tổng quát hóa mạnh mẽ đối với các nhiệm vụ nghiên cứu sâu mở.

### IV. Conclusion & Future Works:
Bài báo đã thành công trong việc xác định các hạn chế chính của RL dựa trên phần thưởng kết quả đối với các tác nhân tìm kiếm sâu và đề xuất CaRR cùng C-GRPO như một giải pháp hiệu quả. Các phương pháp này giúp xây dựng các tác nhân tìm kiếm sâu mạnh mẽ hơn, có khả năng suy luận toàn diện, dựa trên bằng chứng và ít bị ảo giác. Hướng nghiên cứu tiếp theo có thể bao gồm việc tối ưu hóa quy trình tự động tạo rubrics hoặc mở rộng ứng dụng của CaRR và C-GRPO cho các dạng câu hỏi phức tạp hơn hoặc các miền kiến thức chuyên biệt.

### V. Brainstorming Space:
#### 1. Publish Papers:
*   Nghiên cứu việc tích hợp CaRR với các mô hình suy luận đa phương thức để tạo ra các tác nhân tìm kiếm sâu có khả năng đánh giá bằng chứng từ nhiều nguồn và định dạng khác nhau.
*   Khám phá cách áp dụng khung phần thưởng CaRR để cải thiện tính minh bạch và khả năng giải thích (explainability) của các hệ thống trả lời câu hỏi tự động.
*   Phân tích hiệu quả của CaRR khi được áp dụng trong môi trường tìm kiếm thực tế có độ nhiễu cao và dữ liệu không có cấu trúc tốt, so với dữ liệu tổng hợp.

#### 2. Patent:
*   Một hệ thống tìm kiếm thông minh trên điện thoại di động sử dụng phần thưởng CaRR để đánh giá và hiển thị "Chỉ số Độ tin cậy Bằng chứng" cho mọi câu trả lời, giúp người dùng ngay lập tức biết câu trả lời có được hỗ trợ bởi chuỗi bằng chứng toàn diện và trích dẫn đáng tin cậy hay không.
*   Tính năng "Gợi ý Xác Minh Thông tin" tích hợp trong trình duyệt web di động, sử dụng CaRR để tự động phân tích và đề xuất các rubrics (tiêu chí kiểm chứng) cho thông tin trên trang web, hỗ trợ người dùng xác minh tính chính xác của nội dung.
*   Ứng dụng "Trợ lý Nghiên cứu Cá nhân" trên điện thoại hoặc máy tính bảng, được đào tạo bằng C-GRPO, có khả năng thực hiện các tìm kiếm sâu cho các dự án cá nhân, tự động xây dựng và trình bày các báo cáo kèm theo bằng chứng được trích dẫn đầy đủ và theo dõi chuỗi suy luận.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.06021](https://huggingface.co/papers/2601.06021) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.06021](https://arxiv.org/abs/2601.06021) |
| PDF Download | [https://arxiv.org/pdf/2601.06021.pdf](https://arxiv.org/pdf/2601.06021.pdf) |
| Github Repository | [https://github.com/THUDM/CaRR](https://github.com/THUDM/CaRR) |

--- 

## 3. MMFormalizer: Multimodal Autoformalization in the Wild

**Tác giả:** Jing Xiong, Qi Han, Yunta Hsieh, Hui Shen, Huajian Xin, Chaofan Tao, Chenyang Zhao, Hengyuan Zhang, Taiqiang Wu, Zhen Zhang, Haochen Wang, Zhongwei Wan, Lingpeng Kong, Ngai Wong

**Xuất bản lúc:** 2026-01-06

**Tag:** Autoformalization, Multimodal, Formal Reasoning, Physics, Geometry, Deep Learning, Large Language Models (LLMs), LEAN, Dependent Type Theory.

### I. Main Problem:
Việc tự động hình thức hóa (autoformalization) các khái niệm toán học và vật lý từ ngôn ngữ tự nhiên thành các mệnh đề hình thức để máy tính có thể lập luận gặp phải những thách thức cơ bản trong môi trường thực tế ("in the wild"). Cụ thể, thế giới vật lý có tính đa phương thức, nơi vật lý đòi hỏi phải suy luận các ràng buộc ẩn (ví dụ: khối lượng, năng lượng) từ các yếu tố trực quan, điều mà các hệ thống hiện có dựa chủ yếu vào đầu vào ký hiệu chưa giải quyết được.

### II. Main Idea:
Bài báo đề xuất MMFORMALIZER, một khung tự động hình thức hóa đa phương thức mở rộng khả năng ra ngoài văn bản bằng cách tích hợp tính định vị thích ứng (adaptive grounding) với các thực thể từ các lĩnh vực toán học và vật lý thực tế. MMFORMALIZER xây dựng một cách đệ quy các mệnh đề hình thức từ các nguyên thủy được định vị bằng cảm nhận thông qua định vị đệ quy (recursive grounding) và hợp thành tiên đề (axiom composition), với sự chấm dứt đệ quy thích ứng (adaptive recursive termination) đảm bảo mọi sự trừu tượng đều được hỗ trợ bởi bằng chứng trực quan và được neo vào định vị chiều (dimensional grounding) hoặc tiên đề. Hệ thống này sử dụng lý thuyết kiểu phụ thuộc (dependent type theory) của LEAN để mã hóa cấu trúc chiều của các đại lượng vật lý, cho phép mô hình hóa các khái niệm vật lý phức tạp một cách chính xác.

### III. Main Results:
MMFORMALIZER được đánh giá trên một bộ dữ liệu chuẩn mới, PHYX-AF, bao gồm 115 mẫu được tuyển chọn từ MathVerse, PhyX, Synthetic Geometry và Analytic Geometry, bao quát các nhiệm vụ tự động hình thức hóa đa phương thức đa dạng. Kết quả cho thấy các mô hình tiên tiến như GPT-5 và Gemini-3-Pro đạt độ chính xác biên dịch và ngữ nghĩa cao nhất. Trong đó, GPT-5 đặc biệt xuất sắc trong lập luận vật lý, trong khi lĩnh vực hình học vẫn là thách thức lớn nhất. MMFORMALIZER là phương pháp tự động hình thức hóa đa phương thức đầu tiên có khả năng xử lý cơ học cổ điển (phát sinh từ Hamilton), cũng như thuyết tương đối, cơ học lượng tử và nhiệt động lực học.

### IV. Conclusion & Future Works:
MMFORMALIZER cung cấp một khung có khả năng mở rộng để tự động hình thức hóa đa phương thức một cách thống nhất, kết nối nhận thức và lập luận hình thức. Nó giải quyết thách thức cốt lõi là xác định các tiên đề cơ bản để định vị tự động hình thức hóa đa phương thức trong các môi trường thực tế, đặc biệt là trong vật lý. Bài báo đã mở rộng ranh giới của autoformalization để xử lý các hiện tượng vật lý phức tạp trong thế giới thực thông qua việc tích hợp các ràng buộc chiều và tiên đề.

### V. Brainstorming Space:
#### 1. Publish Papers:
*   Nghiên cứu mở rộng MMFORMALIZER để tích hợp dữ liệu cảm biến thời gian thực (ví dụ: video) nhằm tự động hình thức hóa các tình huống vật lý động.
*   Phát triển các phương pháp tinh chỉnh (fine-tuning) LLM chuyên biệt cho các miền vật lý cụ thể trong PHYX-AF để cải thiện độ chính xác và hiệu quả.
*   Khám phá việc sử dụng học tăng cường để tối ưu hóa quá trình hợp thành tiên đề và định vị đệ quy trong các hệ thống tự động hình thức hóa đa phương thức.
#### 2. Patent:
*   Một ứng dụng di động cho phép người dùng chụp ảnh sơ đồ vật lý hoặc cảnh quan thực tế và tự động tạo ra các biểu thức toán học hình thức có kiểm tra tính chiều, hỗ trợ giải toán vật lý trên điện thoại.
*   Hệ thống trợ lý ảo trên điện thoại thông minh có khả năng hiểu và hình thức hóa các yêu cầu vật lý đa phương thức (ví dụ: giọng nói và hình ảnh) thành các mệnh đề có thể chứng minh được, giúp học sinh và kỹ sư.
*   Công nghệ tích hợp vào các thiết bị thực tế tăng cường (AR) trên điện thoại để hiển thị các biểu thức vật lý hình thức và ràng buộc chiều trực tiếp lên các vật thể trong thế giới thực, hỗ trợ thiết kế kỹ thuật và giáo dục.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.03017](https://huggingface.co/papers/2601.03017) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.03017](https://arxiv.org/abs/2601.03017) |
| PDF Download | [https://arxiv.org/pdf/2601.03017.pdf](https://arxiv.org/pdf/2601.03017.pdf) |
| Github Repository | N/A |

--- 

## 4. The Molecular Structure of Thought: Mapping the Topology of Long Chain-of-Thought Reasoning

**Tác giả:** Qiguang Chen, Yantao Du, Ziniu Li, Jinhao Liu, Songyao Duan, Jiarui Guo, Minghao Liu, Jiaheng Liu, Tong Yang, Ge Zhang, Libo Qin, Wanxiang Che, Wenhao Huang

**Xuất bản lúc:** 2026-01-09

**Tag:** Large Language Models (LLMs), Chain-of-Thought (CoT) Reasoning, Long CoT, Molecular Structure, Fine-tuning, Distillation, Mole-Syn, Semantic Isomers

### I. Main Problem:
Các mô hình ngôn ngữ lớn (LLM) thường thất bại trong việc học suy luận chuỗi tư duy dài (Long CoT) hiệu quả từ sự bắt chước của con người hoặc các LLM không có Long CoT. Vấn đề cốt lõi là làm thế nào để các LLM có thể học và biểu diễn suy luận Long CoT một cách hiệu quả, vì các phương pháp fine-tuning và chắt lọc thông thường thường khiến mô hình mất tính nhất quán hoặc không thể chuyển giao các mẫu suy luận sang các tác vụ mới.

### II. Main Idea:
Bài báo đề xuất rằng các quỹ đạo Long CoT hiệu quả và có thể học được có cấu trúc ổn định giống phân tử, hình thành từ ba loại tương tác ("liên kết hóa học"): Deep-Reasoning (như liên kết cộng hóa trị), Self-Reflection (như liên kết hydrogen) và Self-Exploration (như lực van der Waals). Chất lượng cao của Long CoT đến từ thành phần và sự sắp xếp ổn định của các loại liên kết này. Các tác giả giới thiệu "Effective Semantic Isomers" và chỉ ra rằng chỉ các liên kết thúc đẩy sự hội tụ entropy nhanh mới hỗ trợ học Long CoT ổn định. Dựa trên những phát hiện này, bài báo trình bày Mole-Syn, một phương pháp đồ thị chuyển giao phân phối, hướng dẫn tổng hợp các cấu trúc Long CoT hiệu quả, cải thiện hiệu suất và sự ổn định của học tăng cường (RL).

### III. Main Results:
- Phân tích quỹ đạo được chắt lọc cho thấy các cấu trúc phân tử này xuất hiện từ quá trình fine-tuning Long CoT, không phải do bắt chước từ khóa đơn thuần.
- Chỉ các liên kết thúc đẩy sự hội tụ entropy nhanh mới hỗ trợ học Long CoT ổn định, trong khi sự cạnh tranh cấu trúc làm suy yếu quá trình huấn luyện.
- Mole-Syn, phương pháp tổng hợp cấu trúc mới, đã nâng cao hiệu suất và sự ổn định của RL trên sáu bộ benchmark khác nhau.
- Các quỹ đạo Long CoT hiệu quả thể hiện sự tổ chức ổn định, giống cấu trúc phân tử, trên nhiều mô hình và tác vụ, với hệ số tương quan Pearson vượt quá 0.9.
- Chỉ việc chắt lọc từ các LLM suy luận mạnh mới truyền đạt hiệu quả các cấu trúc Long CoT, trong khi chắt lọc từ các LLM hướng dẫn yếu với ICL hoặc fine-tuning trên dấu vết suy luận của con người chỉ mang lại lợi ích hạn chế.

### IV. Conclusion & Future Works:
Bài báo kết luận rằng suy luận Long CoT có thể được mô hình hóa như một cấu trúc phân tử với ba loại liên kết chính (Deep-Reasoning, Self-Reflection, Self-Exploration) giúp hiểu rõ quá trình học hiệu quả. Việc xác định Effective Semantic Isomers và việc chỉ các liên kết hội tụ entropy mới cho phép học ổn định là những phát hiện quan trọng. Mole-Syn được giới thiệu như một phương pháp hiệu quả để tổng hợp các cấu trúc này, cải thiện đáng kể hiệu suất và sự ổn định của học tăng cường. Hơn nữa, bài báo cũng thảo luận về lý do tại sao một cấu trúc phân tử bị suy yếu lại khó khôi phục, giải thích cách các LLM riêng tư bảo vệ cấu trúc Long CoT khỏi sự bắt chước dựa trên chắt lọc, và rằng các phương pháp như tóm tắt hay nén suy luận có thể phá vỡ cấu trúc này, hạn chế việc sao chép trái phép các quy trình suy luận nội bộ.

### V. Brainstorming Space:
#### 1. Publish Papers:
- Nghiên cứu tác động của các phương pháp nén dữ liệu và tóm tắt suy luận lên tính toàn vẹn của cấu trúc phân tử Long CoT và đề xuất các kỹ thuật bảo toàn cấu trúc trong quá trình này.
- Phát triển một framework tự động để khám phá và tạo ra các "Semantic Isomers" Long CoT tối ưu cho các miền vấn đề cụ thể, không chỉ dựa vào việc chắt lọc từ mô hình giáo viên.
- Điều tra khả năng tích hợp các nguyên tắc "liên kết phân tử" trực tiếp vào kiến trúc mô hình LLM hoặc cơ chế tự chú ý để tạo ra các mô hình Long CoT mạnh mẽ và ổn định hơn từ đầu.

#### 2. Patent:
- Hệ thống trợ lý AI di động tích hợp khả năng "tự phản chiếu" và "tự khám phá" dựa trên mô hình cấu trúc phân tử để giải quyết các yêu cầu đa bước và phức tạp của người dùng trên điện thoại thông minh.
- Công nghệ "bảo vệ trí tuệ suy luận" cho các thiết bị di động, sử dụng các cơ chế làm suy yếu có chủ đích cấu trúc "liên kết phân tử" của Long CoT khi có ý định trích xuất hoặc sao chép trái phép các mô hình suy luận.
- Ứng dụng hỗ trợ học tập và giải quyết vấn đề cá nhân trên điện thoại, phân tích các bước suy nghĩ của người dùng và đề xuất các "liên kết" Deep-Reasoning, Self-Reflection, Self-Exploration để cải thiện kỹ năng giải quyết vấn đề theo chuỗi dài.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.06002](https://huggingface.co/papers/2601.06002) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.06002](https://arxiv.org/abs/2601.06002) |
| PDF Download | [https://arxiv.org/pdf/2601.06002.pdf](https://arxiv.org/pdf/2601.06002.pdf) |
| Github Repository | N/A |

--- 

## 5. EnvScaler: Scaling Tool-Interactive Environments for LLM Agent via Programmatic Synthesis

**Tác giả:** Xiaoshuai Song, Haofei Chang, Guanting Dong, Yutao Zhu, Zhicheng Dou, Ji-Rong Wen

**Xuất bản lúc:** 2026-01-09

**Tag:** LLM Agents, Tool-Interactive Environments, Programmatic Synthesis, Environment Scaling.
### I. Main Problem:
Vấn đề cốt lõi là sự thiếu hụt các môi trường tương tác công cụ đa dạng và có khả năng mở rộng để huấn luyện tác nhân LLM. Các môi trường thực tế bị hạn chế truy cập, môi trường mô phỏng bằng LLM dễ bị ảo giác và không nhất quán, trong khi các sandbox được xây dựng thủ công thì khó mở rộng và có phạm vi hạn chế, thiếu cơ chế đánh giá chất lượng tự động và thường phụ thuộc vào các tập công cụ hoặc môi trường có sẵn.

### II. Main Idea:
Giải pháp đề xuất là EnvScaler, một framework tự động hóa để tổng hợp các môi trường tương tác công cụ có khả năng mở rộng thông qua tổng hợp lập trình. EnvScaler gồm hai thành phần chính:
-   **SkelBuilder:** Xây dựng các khung môi trường đa dạng bằng cách khám phá chủ đề từ các bộ tác vụ hiện có, mô hình hóa logic môi trường và tự động triển khai thành môi trường thực thi được, sau đó đánh giá chất lượng thông qua tương tác giữa tác nhân thử nghiệm và tác nhân kiểm tra.
-   **ScenGenerator:** Tạo ra nhiều kịch bản tác vụ cho mỗi môi trường, bao gồm tổng hợp dữ liệu trạng thái ban đầu của môi trường, thiết kế các tác vụ đầy thách thức và sinh các hàm xác thực trạng thái cuối cùng dựa trên quy tắc để xác minh việc hoàn thành nhiệm vụ.

### III. Main Results:
EnvScaler đã tổng hợp 191 môi trường và khoảng 7K kịch bản, được áp dụng để huấn luyện mô hình Qwen3 series thông qua Supervised Fine-Tuning (SFT) và Reinforcement Learning (RL). Kết quả trên ba benchmark cho thấy EnvScaler cải thiện đáng kể khả năng của LLM trong việc giải quyết các tác vụ phức tạp liên quan đến tương tác đa lượt, đa công cụ. Phân tích thêm về phạm vi, quy mô môi trường và chiến lược huấn luyện cung cấp những hiểu biết sâu sắc về cách các môi trường tổng hợp thúc đẩy việc học công cụ và khả năng tổng quát hóa cho tác nhân LLM.

### IV. Conclusion & Future Works:
Bài báo kết luận bằng việc giới thiệu EnvScaler như một framework tự động hóa, có khả năng mở rộng để tổng hợp các môi trường tương tác công cụ. Các đóng góp chính bao gồm đề xuất SkelBuilder để tổng hợp các khung môi trường thực thi được, ScenGenerator để tạo dữ liệu trạng thái, các tác vụ đầy thách thức và xác minh quỹ đạo dựa trên quy tắc cho mỗi môi trường, cùng với bằng chứng thực nghiệm trên ba benchmark xác nhận hiệu quả của EnvScaler trong việc nâng cao khả năng của LLM trong các môi trường phức tạp liên quan đến tương tác đa lượt, đa công cụ.

### V. Brainstorming Space:
#### 1. Publish Papers:
1.  Nghiên cứu mở rộng SkelBuilder để tự động tạo ra các môi trường tương tác phức tạp hơn với các loại ràng buộc logic đa dạng và kiểm định chặt chẽ hơn.
2.  Phát triển một phương pháp ScenGenerator nâng cao để tạo ra các kịch bản nhiệm vụ khó khăn hơn và có khả năng thích ứng với hành vi của tác nhân LLM theo thời gian thực.
3.  Khám phá việc tích hợp EnvScaler với các phương pháp huấn luyện tác nhân LLM tiên tiến (như IRL - Inverse Reinforcement Learning) để tối ưu hóa việc học sử dụng công cụ và khả năng ra quyết định.

#### 2. Patent:
1.  Hệ thống tự động tạo môi trường thử nghiệm ứng dụng di động cho các tác nhân AI, mô phỏng tương tác người dùng và kiểm tra chức năng đa kịch bản trên điện thoại thông minh.
2.  Phương pháp sinh chương trình tự động để tạo các API và cơ sở dữ liệu ảo cho việc phát triển và kiểm thử tính năng mới của ứng dụng điện thoại thông minh.
3.  Công cụ lập trình tổng hợp các kịch bản kiểm tra tự động cho trợ lý ảo trên điện thoại, đảm bảo khả năng phản hồi và tương tác hiệu quả với các ứng dụng khác theo quy tắc định trước.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.05808](https://huggingface.co/papers/2601.05808) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.05808](https://arxiv.org/abs/2601.05808) |
| PDF Download | [https://arxiv.org/pdf/2601.05808.pdf](https://arxiv.org/pdf/2601.05808.pdf) |
| Github Repository | N/A |

--- 

## 6. Can We Predict Before Executing Machine Learning Agents?

**Tác giả:** Jingsheng Zheng, Jintian Zhang, Yujie Luo, Yuren Mao, Yunjun Gao, Lun Du, Huajun Chen, Ningyu Zhang

**Xuất bản lúc:** 2026-01-09

**Tag:** Autonomous ML Agents, Execution Bottleneck, World Models, LLMs, Data-centric Solution Preference, Predict-then-Verify, FOREAGENT

### I. Main Problem:
Vấn đề cốt lõi là "Execution Bottleneck" (nút thắt cổ chai về thực thi) trong chu trình "Generate-Execute-Feedback" của các tác nhân học máy tự động. Việc đánh giá giả thuyết dựa vào quá trình thực thi vật lý tốn kém và chậm, thường mất hàng giờ, gây cản trở nghiêm trọng đến quá trình khám phá khoa học và tối ưu hóa tác nhân.

### II. Main Idea:
Bài báo đề xuất một phương pháp để vượt qua giới hạn thực thi vật lý bằng cách nội hóa các ưu tiên thực thi để thay thế các kiểm tra thời gian chạy tốn kém bằng suy luận dự đoán tức thời, lấy cảm hứng từ World Models. Cụ thể, nghiên cứu chính thức hóa nhiệm vụ "Data-centric Solution Preference" nơi mô hình phải dự đoán hiệu suất tương đối của hai giải pháp thuật toán dựa trên báo cáo phân tích dữ liệu mà không cần thực thi vật lý. Các mô hình ngôn ngữ lớn (LLMs) được sử dụng làm "Implicit World Model" và được tăng cường đầu vào bằng "Verified Data Analysis Report" để cho phép suy luận và dự đoán hiệu suất. Khung này được tích hợp vào FOREAGENT, một tác nhân sử dụng vòng lặp "Predict-then-Verify" để tách rời quá trình khám phá khỏi thực thi.

### III. Main Results:
Nghiên cứu đã xây dựng một bộ dữ liệu toàn diện gồm 18.438 cặp so sánh. Các LLMs thể hiện khả năng dự đoán đáng kể, với DeepSeek-V3.2-Thinking đạt độ chính xác 61.5% trong nhiệm vụ Data-centric Solution Preference, vượt trội hơn đáng kể so với đoán ngẫu nhiên (50.0%) và các phương pháp heuristic dựa trên độ phức tạp (50.8%), đồng thời thể hiện độ tin cậy được hiệu chỉnh tốt. FOREAGENT, áp dụng khung này, đạt được khả năng tăng tốc hội tụ gấp 6 lần và cải thiện hiệu suất +6% so với các phương pháp cơ sở dựa trên thực thi, đồng thời mở rộng không gian tìm kiếm lên 3.2 lần. Mã nguồn và bộ dữ liệu sẽ được công bố rộng rãi.

### IV. Conclusion & Future Works:
LLMs có khả năng dự đoán đáng kể về hiệu suất giải pháp thuật toán trước khi thực thi, giúp giải quyết nút thắt cổ chai trong các tác nhân học máy tự động. Việc tích hợp khả năng này vào FOREAGENT cho phép tăng tốc đáng kể và cải thiện hiệu suất. Hướng nghiên cứu tiếp theo bao gồm việc sử dụng bộ dữ liệu mã nguồn mở về các quỹ đạo thực thi đã được xác minh để huấn luyện các mô hình phần thưởng có khả năng mở rộng nhằm đẩy nhanh quá trình triển khai và tối ưu hóa học tăng cường trên các khung tác nhân đa dạng.

### V. Brainstorming Space:
#### 1. Publish Papers:
*   Nghiên cứu so sánh hiệu quả của các kiến trúc LLM khác nhau và chiến lược prompt trong nhiệm vụ Data-centric Solution Preference trên nhiều miền dữ liệu đa dạng.
*   Phát triển các phương pháp tự động hóa hoàn toàn việc tạo "Verified Data Analysis Report" mà không cần sự can thiệp của con người hoặc phụ thuộc vào LLM khác để xác minh.
*   Áp dụng mô hình "Predict-then-Verify" vào các bài toán điện toán tốn kém khác ngoài việc thực thi tác nhân ML, như mô phỏng khoa học hoặc khám phá thuốc.
#### 2. Patent:
*   Hệ thống hỗ trợ phát triển ứng dụng di động thông minh, sử dụng LLM để dự đoán hiệu suất của các đoạn mã tối ưu hóa thuật toán trước khi biên dịch, giảm thời gian phát triển trên thiết bị di động.
*   Công nghệ tối ưu hóa tài nguyên trên điện thoại thông minh, nơi các tác vụ học máy cục bộ được đánh giá trước bởi một mô hình dự đoán nhẹ để chọn ra giải pháp ít tốn pin và hiệu quả nhất cho thiết bị.
*   Hệ thống chẩn đoán và sửa lỗi tự động cho ứng dụng di động, sử dụng mô hình dự đoán để nhận diện các kịch bản lỗi tiềm ẩn và đề xuất giải pháp tối ưu mà không cần chạy thử nghiệm tốn kém trên điện thoại.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.05930](https://huggingface.co/papers/2601.05930) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.05930](https://arxiv.org/abs/2601.05930) |
| PDF Download | [https://arxiv.org/pdf/2601.05930.pdf](https://arxiv.org/pdf/2601.05930.pdf) |
| Github Repository | [https://github.com/zjunlp/predict-before-execute](https://github.com/zjunlp/predict-before-execute) |

--- 

## 7. Illusions of Confidence? Diagnosing LLM Truthfulness via Neighborhood Consistency

**Tác giả:** Haoming Xu, Ningyuan Zhao, Yunzhi Yao, Weihong Xu, Hongru Wang, Xinle Deng, Shumin Deng, Jeff Z. Pan, Huajun Chen, Ningyu Zhang

**Xuất bản lúc:** 2026-01-09

**Tag:** LLM Truthfulness, Neighborhood Consistency, Belief Robustness, Contextual Interference, Structure-Aware Training, Self-Consistency, Cognitive Stress Testing.

### I. Main Problem:
Vấn đề cốt lõi mà bài báo đề cập là các Large Language Models (LLM), dù có khả năng vượt trội, vẫn mắc phải những lỗi dai dẳng về tính đúng đắn (truthfulness), bao gồm việc tạo ra thông tin sai lệch (hallucination) và thể hiện sự tự tin thái quá, đặc biệt khi phải hoạt động dưới sự nhiễu loạn ngữ cảnh trong các ứng dụng thực tế (như RAG, cộng tác đa tác nhân). Các phương pháp đánh giá hiện tại, chủ yếu dựa vào độ tin cậy "điểm-điểm" (point-wise confidence) như Self-Consistency, không đủ sâu sắc và che giấu trạng thái niềm tin dễ vỡ của LLM, khiến các sự thật được trả lời với sự tự nhất quán hoàn hảo vẫn có thể sụp đổ nhanh chóng dưới sự can thiệp ngữ cảnh nhẹ.

### II. Main Idea:
Bài báo đề xuất Neighbor-Consistency Belief (NCB) như một thước đo cấu trúc về độ bền vững của niềm tin (belief robustness), đánh giá sự nhất quán của phản hồi trên một "khu vực lân cận khái niệm" (conceptual neighborhood) bao gồm các tiền đề, hàm ý logic và liên kết chuyên đề của một sự thật. NCB được xây dựng dựa trên suy luận Bayesian, ước tính xác suất niềm tin ở trạng thái có cấu trúc (Sstruct - niềm tin bền vững và nhất quán) so với trạng thái không có cấu trúc (Sunstruct - sự ghi nhớ đơn lẻ, dễ vỡ). Để xác thực hiệu quả của NCB, nghiên cứu giới thiệu một giao thức "kiểm tra căng thẳng nhận thức" (cognitive stress-testing protocol) mới, mô phỏng các kịch bản đối nghịch như áp lực xã hội từ các tác nhân khác (Peer Quantity) và ảnh hưởng từ các nguồn thông tin gây hiểu lầm (Source Credibility) để thăm dò sự ổn định của đầu ra LLM dưới nhiễu ngữ cảnh. Cuối cùng, nghiên cứu đề xuất Structure-Aware Training (SAT) nhằm tối ưu hóa cấu trúc niềm tin bất biến theo ngữ cảnh và giảm độ mong manh của tri thức.

### III. Main Results:
*   Các thí nghiệm trên nhiều LLM cho thấy dữ liệu có NCB cao thể hiện khả năng chống chịu nhiễu ngữ cảnh tốt hơn đáng kể so với dữ liệu có NCB thấp, xác nhận NCB là một chỉ số hiệu quả cho niềm tin bền vững.
*   Nghiên cứu chỉ ra rằng ngay cả các sự thật được LLM trả lời với sự nhất quán hoàn hảo (self-consistency = 1.0) cũng có thể sụp đổ nhanh chóng dưới sự can thiệp ngữ cảnh nhẹ (độ chính xác giảm mạnh từ 100% xuống 33.8% trong nghiên cứu thí điểm).
*   Structure-Aware Training (SAT) đã giảm độ mong manh của tri thức được học (brittleness of learned knowledge) khoảng 30% so với các phương pháp cơ bản, chứng tỏ khả năng tối ưu hóa cấu trúc niềm tin bất biến theo ngữ cảnh.

### IV. Conclusion & Future Works:
Kết luận của nghiên cứu là niềm tin bền vững của LLM là một thuộc tính mang tính cấu trúc, không chỉ đơn thuần là sự tự tin theo từng điểm. Điều này nhấn mạnh sự cần thiết của việc đánh giá và đào tạo nhận biết cấu trúc (structure-aware evaluation and training) để xây dựng các LLM đáng tin cậy hơn. Hướng nghiên cứu tiếp theo có thể bao gồm việc mở rộng định nghĩa về "khu vực lân cận khái niệm" và khám phá các phương pháp phức tạp hơn để xây dựng tập dữ liệu Neighbor-Enriched, cũng như nghiên cứu các giới hạn khác.

### V. Brainstorming Space:
#### 1. Publish Papers:
*   Nghiên cứu tác động của các loại nhiễu ngữ cảnh khác nhau (ví dụ: thông tin sai lệch có chủ ý, lỗi dữ liệu hệ thống) lên độ bền vững của niềm tin LLM, được đo bằng NCB.
*   Phát triển các chiến lược Structure-Aware Training tiên tiến hơn, tích hợp các kỹ thuật kiến trúc mạng nơ-ron hoặc học tăng cường để cải thiện khả năng duy trì niềm tin trong các tác vụ suy luận phức tạp.
*   Khám phá cách áp dụng NCB để đánh giá và cải thiện khả năng suy luận đa bước của LLM, nơi sự nhất quán giữa các bước trung gian là rất quan trọng để đảm bảo tính đúng đắn của kết quả cuối cùng.

#### 2. Patent:
*   Hệ thống kiểm tra độ bền vững của thông tin LLM trên điện thoại, trong đó ứng dụng tạo ra các "câu hỏi hàng xóm" ngầm để xác nhận tính nhất quán của thông tin trước khi hiển thị cho người dùng.
*   Tính năng "nhắc nhở sự thật có cấu trúc" trên trợ lý ảo di động, cảnh báo người dùng khi thông tin được LLM cung cấp có độ NCB thấp và dễ bị ảnh hưởng bởi ngữ cảnh gây nhiễu, đề xuất tìm kiếm thêm thông tin xác thực.
*   Phương pháp đào tạo LLM trên thiết bị di động, tối ưu hóa cấu trúc tri thức cục bộ để giảm thiểu sự "mong manh" của thông tin khi người dùng tương tác trong các ngữ cảnh thay đổi liên tục và bộ nhớ bị giới hạn.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.05905](https://huggingface.co/papers/2601.05905) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.05905](https://arxiv.org/abs/2601.05905) |
| PDF Download | [https://arxiv.org/pdf/2601.05905.pdf](https://arxiv.org/pdf/2601.05905.pdf) |
| Github Repository | [https://github.com/zjunlp/belief](https://github.com/zjunlp/belief) |

--- 

## 8. Orient Anything V2: Unifying Orientation and Rotation Understanding

**Tác giả:** Zehan Wang, Ziang Zhang, Jiayang Xu, Jialei Wang, Tianyu Pang, Chao Du, HengShuang Zhao, Zhou Zhao

**Xuất bản lúc:** 2026-01-09

**Tag:** Computer Vision, 3D Object Orientation, Object Rotation, Rotational Symmetry, Foundation Model, Generative Models, Zero-shot Learning, 6DoF Pose Estimation.

### I. Main Problem:
Mô hình Orient Anything V1 gặp hạn chế trong việc hiểu sâu về xoay của vật thể, đặc biệt là với các vật thể có đối xứng xoay và không thể ước tính trực tiếp các xoay tương đối giữa các khung hình. Các hạn chế này xuất phát từ việc V1 chỉ định nghĩa hướng dựa trên một mặt trước duy nhất, bỏ qua các đối xứng xoay đa dạng và gặp khó khăn với dữ liệu huấn luyện thực tế bị mất cân bằng và chất lượng không đồng đều.

### II. Main Idea:
Bài báo giới thiệu Orient Anything V2, một mô hình nền tảng được nâng cấp để thống nhất việc hiểu hướng 3D và xoay của vật thể từ ảnh đơn hoặc cặp ảnh. Các cải tiến chính bao gồm bốn đổi mới cốt lõi:
1.  **Dữ liệu mở rộng và chất lượng cao:** Phát triển một công cụ dữ liệu có thể mở rộng, sử dụng các mô hình tạo sinh để tổng hợp 600K tài sản 3D với độ phủ danh mục rộng và phân bố cân bằng.
2.  **Hệ thống chú thích mạnh mẽ:** Sử dụng hệ thống chú thích "model-in-the-loop" hiệu quả để xác định từ 0 đến N mặt trước hợp lệ cho mỗi vật thể, nắm bắt được các đối xứng xoay.
3.  **Mục tiêu học tập nhận biết đối xứng:** Áp dụng mục tiêu "symmetry-aware, periodic distribution fitting" để mô hình hóa hiệu quả đối xứng xoay, dự đoán tất cả các hướng mặt trước có thể có.
4.  **Kiến trúc đa khung hình:** Mở rộng kiến trúc mô hình để hỗ trợ đầu vào đa khung hình, cho phép dự đoán trực tiếp các xoay tương đối của vật thể.

### III. Main Results:
Orient Anything V2 đạt được hiệu suất vượt trội (state-of-the-art) trong các tác vụ zero-shot:
*   Đạt hiệu suất zero-shot hàng đầu trong ước tính hướng.
*   Thiết lập kỷ lục mới trong ước tính xoay zero-shot (ước tính tư thế 6DoF).
*   Xử lý và dự đoán chính xác các đối xứng xoay khác nhau.
*   Thể hiện khả năng tổng quát hóa mạnh mẽ trên 11 bộ dữ liệu benchmark phổ biến, mở rộng đáng kể phạm vi ứng dụng của việc ước tính hướng.
*   Bộ dữ liệu tổng hợp cuối cùng chứa 600K tài sản, gấp 12 lần so với bộ dữ liệu hiện có, với chất lượng chú thích cao hơn đáng kể.

### IV. Conclusion & Future Works:
Orient Anything V2 là một mô hình nền tảng được nâng cấp đáng kể, thống nhất hiểu biết về hướng và xoay của vật thể 3D. Bằng cách giải quyết các hạn chế về dữ liệu và mô hình của phiên bản trước, V2 đạt được khả năng nhận biết đối xứng xoay và ước tính xoay tương đối, nâng cao đáng kể hiệu suất zero-shot và khả năng tổng quát hóa. Hướng nghiên cứu tiếp theo có thể tập trung vào việc áp dụng rộng rãi hơn mô hình này trong các ứng dụng robot, lái xe tự hành và thực tế tăng cường/thực tế ảo.

### V. Brainstorming Space:
#### 1. Publish Papers:
*   Nghiên cứu cách tích hợp mô hình Orient Anything V2 với dữ liệu đa phương thức để cải thiện khả năng ước tính hướng và xoay trong các điều kiện môi trường phức tạp.
*   Khám phá tiềm năng của Orient Anything V2 trong việc tự động tạo ra các mô hình 3D có độ chính xác cao từ hình ảnh 2D, đặc biệt tập trung vào việc tái tạo đối xứng xoay.
*   Điều tra việc sử dụng Orient Anything V2 để cải thiện khả năng điều khiển robot tự động trong các tác vụ thao tác vật thể đòi hỏi độ chính xác cao về hướng và xoay.

#### 2. Patent:
*   Hệ thống camera điện thoại thông minh có khả năng tự động nhận diện đối xứng xoay của vật thể chính trong khung hình và đề xuất các góc chụp hoặc bố cục ảnh tối ưu để chụp được tất cả các hướng mặt trước hợp lệ.
*   Ứng dụng chỉnh sửa video trên điện thoại cho phép người dùng dễ dàng căn chỉnh hoặc xoay các vật thể trong video, giữ nguyên tính nhất quán về hướng và xoay ngay cả khi vật thể có đối xứng, dựa trên khả năng hiểu xoay tương đối của Orient Anything V2.
*   Chức năng "Smart Focus" trong camera điện thoại sử dụng Orient Anything V2 để không chỉ nhận diện vật thể mà còn hiểu hướng 3D và đối xứng xoay của nó, cho phép lấy nét thông minh và theo dõi vật thể một cách ổn định ngay cả khi nó xoay trong không gian.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.05573](https://huggingface.co/papers/2601.05573) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.05573](https://arxiv.org/abs/2601.05573) |
| PDF Download | [https://arxiv.org/pdf/2601.05573.pdf](https://arxiv.org/pdf/2601.05573.pdf) |
| Github Repository | [https://github.com/SpatialVision/Orient-Anything-V2](https://github.com/SpatialVision/Orient-Anything-V2) |

--- 

## 9. Qwen3-VL-Embedding and Qwen3-VL-Reranker: A Unified Framework for State-of-the-Art Multimodal Retrieval and Ranking

**Tác giả:** Mingxin Li, Yanzhao Zhang, Dingkun Long, Keqin Chen, Sibo Song, Shuai Bai, Zhibo Yang, Pengjun Xie, An Yang, Dayiheng Liu, Jingren Zhou, Junyang Lin

**Xuất bản lúc:** 2026-01-08

**Tag:** Multimodal Retrieval, Multimodal Ranking, Embedding, Reranker, Qwen3-VL, Foundation Model

### I. Main Problem:
Vấn đề cốt lõi mà bài báo đề cập là sự gia tăng mạnh mẽ của nội dung đa phương thức trên internet, đòi hỏi các hệ thống tìm kiếm tiên tiến có khả năng hiểu và kết nối các khái niệm ngữ nghĩa trên nhiều phương thức dữ liệu khác nhau (văn bản, hình ảnh, tài liệu hình ảnh, video), vượt ra ngoài các phương pháp tìm kiếm chỉ dựa trên văn bản truyền thống.

### II. Main Idea:
Bài báo giới thiệu bộ mô hình Qwen3-VL-Embedding và Qwen3-VL-Reranker, một khung thống nhất dựa trên mô hình nền tảng Qwen3-VL, cung cấp giải pháp đầu cuối cho tìm kiếm đa phương thức có độ chính xác cao.
*   **Qwen3-VL-Embedding:** Sử dụng mô hình bi-encoder và quy trình huấn luyện đa giai đoạn từ tiền huấn luyện tương phản quy mô lớn đến chắt lọc mô hình reranking để tạo ra các vector nhúng ngữ nghĩa phong phú, ánh xạ các phương thức đa dạng vào một không gian biểu diễn thống nhất. Mô hình hỗ trợ Matryoshka Representation Learning cho phép kích thước embedding linh hoạt và xử lý đầu vào lên tới 32k token.
*   **Qwen3-VL-Reranker:** Sử dụng kiến trúc cross-encoder với cơ chế cross-attention để ước tính độ liên quan chi tiết giữa các cặp truy vấn và tài liệu.
Cả hai dòng mô hình đều kế thừa khả năng đa ngôn ngữ của Qwen3-VL (hơn 30 ngôn ngữ) và được phát hành với kích thước 2B và 8B tham số.

### III. Main Results:
Các đánh giá thực nghiệm cho thấy:
*   Dòng Qwen3-VL-Embedding đạt kết quả dẫn đầu trên các benchmark đánh giá embedding đa phương thức. Cụ thể, Qwen3-VL-Embedding-8B đạt tổng điểm 77.8 trên MMEB-V2, xếp hạng nhất trong số tất cả các mô hình (tính đến tháng 1 năm 2026).
*   Mô hình thể hiện hiệu quả trong các nhiệm vụ truy xuất đa phương thức khác nhau, bao gồm truy xuất hình ảnh-văn bản, hỏi đáp trực quan và đối sánh video-văn bản.
*   Trong đánh giá chỉ văn bản, Qwen3-VL-Embedding-8B đạt điểm nhiệm vụ trung bình 67.9 trên benchmark MTEB Multilingual.
*   Mô hình reranking Qwen3-VL-Reranker cũng mang lại kết quả cạnh tranh, với phiên bản 8B cải thiện kết quả xếp hạng thêm 4.1 điểm so với phiên bản 2B trên nhiều nhiệm vụ.
*   Nghiên cứu cũng bao gồm phân tích ảnh hưởng của các yếu tố chính đóng góp vào hiệu suất vượt trội của dòng Qwen3-VL-Embedding.

### IV. Conclusion & Future Works:
Bài báo kết luận rằng bộ mô hình Qwen3-VL-Embedding và Qwen3-VL-Reranker cung cấp một khung làm việc thống nhất và hiệu quả cho tìm kiếm và xếp hạng đa phương thức hiện đại. Phần tiếp theo của báo cáo sẽ tổng hợp các phát hiện chính và thảo luận về các hướng nghiên cứu đầy hứa hẹn trong tương lai, tuy nhiên chi tiết cụ thể không có trong đoạn văn trích dẫn này.

### V. Brainstorming Space:
#### 1. Publish Papers:
*   Nghiên cứu so sánh chi tiết hiệu quả của Matryoshka Representation Learning với các phương pháp nén embedding khác trong môi trường đa phương thức.
*   Khám phá ứng dụng của Qwen3-VL-Embedding trong việc cải thiện hệ thống gợi ý cá nhân hóa cho nội dung đa phương thức trên các nền tảng lớn.
*   Phân tích tác động của chiến lược tổng hợp dữ liệu đối với hiệu suất của các mô hình nhúng và reranking đa phương thức trong các kịch bản hiếm dữ liệu.

#### 2. Patent:
*   Hệ thống tìm kiếm thông minh trên điện thoại di động cho phép người dùng tìm kiếm bằng cách kết hợp giọng nói, hình ảnh và văn bản để truy vấn thông tin phức tạp.
*   Phương pháp tối ưu hóa bộ nhớ cho các ứng dụng đa phương tiện trên điện thoại, sử dụng các embedding có kích thước linh hoạt từ Qwen3-VL-Embedding.
*   Công nghệ "Trợ lý thị giác" trên điện thoại thông minh có khả năng trả lời các câu hỏi về nội dung hình ảnh hoặc tài liệu bằng cách hiểu ngữ cảnh đa phương thức.
*   Giải pháp cá nhân hóa trải nghiệm duyệt web và ứng dụng trên điện thoại thông minh bằng cách sử dụng Qwen3-VL-Reranker để xếp hạng các kết quả tìm kiếm đa phương thức dựa trên hành vi người dùng.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.04720](https://huggingface.co/papers/2601.04720) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.04720](https://arxiv.org/abs/2601.04720) |
| PDF Download | [https://arxiv.org/pdf/2601.04720.pdf](https://arxiv.org/pdf/2601.04720.pdf) |
| Github Repository | [https://github.com/QwenLM/Qwen3-VL-Embedding](https://github.com/QwenLM/Qwen3-VL-Embedding) |

--- 

## 10. AgentOCR: Reimagining Agent History via Optical Self-Compression

**Tác giả:** Lang Feng, Fuchao Yang, Feng Chen, Xin Cheng, Haiyang Xu, Zhenglin Wan, Ming Yan, Bo An

**Xuất bản lúc:** 2026-01-08

**Tag:** LLM Agents, Nén văn bản, Xử lý ngữ cảnh dài, Thị giác máy tính, Tự nén, Reinforcement Learning

### I. Main Problem:
Các hệ thống agent dựa trên mô hình ngôn ngữ lớn (LLM), được huấn luyện bằng học tăng cường (RL) qua nhiều lượt tương tác, đang gặp phải nút thắt nghiêm trọng. Lịch sử tương tác bằng văn bản ngày càng tăng nhanh làm cạn kiệt ngân sách token, tăng mức sử dụng bộ nhớ, gây ra độ trễ suy luận và chi phí tính toán lớn, đặc biệt khi xử lý các ngữ cảnh dài trong quá trình huấn luyện.

### II. Main Idea:
Bài báo giới thiệu AgentOCR, một framework giải quyết vấn đề bằng cách tái hình dung lịch sử agent thông qua "nén quang học tự động" (optical self-compression). AgentOCR khai thác mật độ thông tin vượt trội của các token thị giác bằng cách biểu diễn toàn bộ lịch sử quan sát-hành động đã tích lũy dưới dạng một hình ảnh được kết xuất nhỏ gọn. Để đảm bảo khả năng mở rộng trong các lượt chạy nhiều vòng, AgentOCR đề xuất hai cơ chế chính:
1.  **Segment Optical Caching:** Phân tách lịch sử thành các đoạn có thể hash và duy trì bộ nhớ đệm hình ảnh để loại bỏ việc kết xuất lại các đoạn trùng lặp.
2.  **Agentic Self-Compression:** Agent chủ động đưa ra tỷ lệ nén và được huấn luyện bằng phần thưởng nhận biết nén để thích nghi cân bằng giữa thành công nhiệm vụ và hiệu quả token.

### III. Main Results:
AgentOCR bảo toàn hơn 95% hiệu suất của các agent dựa trên văn bản trong khi giảm đáng kể mức tiêu thụ token (hơn 50%, và lên đến 80% ở các đỉnh token). Điều này dẫn đến hiệu quả token và bộ nhớ nhất quán. Phân tích sâu hơn xác nhận rằng "segment optical caching" tăng tốc độ kết xuất lên 20 lần và "self-compression" đạt được sự cân bằng chiến lược hiệu quả. Các kết quả này được chứng minh trên các benchmark agentic đầy thách thức như ALFWorld và QA dựa trên tìm kiếm.

### IV. Conclusion & Future Works:
AgentOCR cung cấp một giải pháp hiệu quả cho thách thức về lịch sử tương tác dài trong các hệ thống agent LLM bằng cách chuyển đổi thông tin văn bản thành biểu diễn hình ảnh nén. Với "segment optical caching" và "agentic self-compression", AgentOCR đạt được sự cân bằng tối ưu giữa hiệu suất và hiệu quả tài nguyên. Hướng nghiên cứu tương lai có thể bao gồm việc phát triển các chiến lược nén và tự nén nâng cao hơn hoặc tích hợp AgentOCR vào các kiến trúc agent phức tạp hơn.

### V. Brainstorming Space:
#### 1. Publish Papers:
1.  Nghiên cứu khả năng mở rộng của AgentOCR để xử lý lịch sử agent cực kỳ dài thông qua các phương pháp kết xuất hình ảnh phân cấp.
2.  Khám phá việc tích hợp "optical self-compression" vào các mô hình thị giác ngôn ngữ đa phương thức để cải thiện khả năng hiểu ngữ cảnh.
3.  Phát triển một phương pháp huấn luyện thích ứng cho "agentic self-compression" để tối ưu hóa tỷ lệ nén dựa trên độ phức tạp động của nhiệm vụ.
#### 2. Patent:
1.  Hệ thống quản lý bộ nhớ thông minh cho trợ lý ảo trên điện thoại, tự động chuyển đổi lịch sử trò chuyện thành hình ảnh nén để tiết kiệm tài nguyên và tăng tốc độ phản hồi.
2.  Ứng dụng ghi chú hoặc nhật ký trên điện thoại sử dụng công nghệ "optical self-compression" để lưu trữ các văn bản dài dưới dạng hình ảnh, tối ưu hóa không gian và tốc độ tìm kiếm.
3.  Tính năng duyệt web hiệu quả trên điện thoại thông minh, nơi lịch sử tương tác và nội dung trang web được nén quang học, giảm tải cho bộ nhớ và băng thông mạng.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.04786](https://huggingface.co/papers/2601.04786) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.04786](https://arxiv.org/abs/2601.04786) |
| PDF Download | [https://arxiv.org/pdf/2601.04786.pdf](https://arxiv.org/pdf/2601.04786.pdf) |
| Github Repository | N/A |

--- 

## 11. VideoAR: Autoregressive Video Generation via Next-Frame & Scale Prediction

**Tác giả:** Longbin Ji, Xiaoxiong Liu, Junyuan Shang, Shuohuan Wang, Yu Sun, Hua Wu, Haifeng Wang

**Xuất bản lúc:** 2026-01-09

**Tag:** Autoregressive Video Generation, Next-Frame Prediction, Multi-scale Prediction, VideoAR, Spatio-temporal modeling

### I. Main Problem:
Các mô hình tạo video hiện tại dựa trên Diffusion và Flow-matching tuy đạt chất lượng cao nhưng tốn kém về mặt tính toán và khó mở rộng. Các phương pháp Autoregressive (AR) cho tạo video còn ít được khám phá và đối mặt với ba thách thức chính: sự không khớp giữa mô hình không gian và thời gian, sự lan truyền lỗi tích lũy qua các chuỗi token video dài, và khả năng kiểm soát không gian-thời gian còn hạn chế, dẫn đến độ phân giải thấp và chất lượng suy giảm.

### II. Main Idea:
Bài báo giới thiệu VideoAR, một khung Visual Autoregressive (VAR) quy mô lớn đầu tiên cho tạo video, kết hợp dự đoán khung hình tiếp theo đa tỷ lệ với mô hình autoregressive. VideoAR phân tách sự phụ thuộc không gian và thời gian bằng cách tích hợp mô hình VAR nội khung với dự đoán khung hình tiếp theo mang tính nhân quả, được hỗ trợ bởi bộ mã hóa 3D đa tỷ lệ hiệu quả. Để cải thiện tính nhất quán dài hạn, VideoAR đề xuất Multi-scale Temporal RoPE, Cross-Frame Error Correction và Random Frame Mask, nhằm giảm thiểu sự lan truyền lỗi và ổn định tính nhất quán thời gian. Một quy trình huấn luyện trước nhiều giai đoạn được sử dụng để căn chỉnh dần dần việc học không gian và thời gian qua các độ phân giải và thời lượng tăng dần.

### III. Main Results:
VideoAR đạt được kết quả dẫn đầu trong số các mô hình autoregressive, cải thiện điểm FVD trên UCF-101 từ 99.5 xuống 88.6 (VideoAR-L đạt 90.3 gFVD). Nó cũng giảm số bước suy luận hơn 10 lần và đạt điểm VBench là 81.74, cạnh tranh với các mô hình dựa trên Diffusion lớn hơn nhiều lần. Những kết quả này chứng minh VideoAR đã thu hẹp khoảng cách hiệu suất giữa các mô hình autoregressive và Diffusion, cung cấp một nền tảng tạo video có khả năng mở rộng, hiệu quả và nhất quán về mặt thời gian. VideoAR có thể tạo video 4 giây ở độ phân giải 384x672 với độ chân thực cao và tính nhất quán thời gian mạnh mẽ.

### IV. Conclusion & Future Works:
VideoAR thiết lập một nền tảng hiệu quả, có khả năng mở rộng và nhất quán về mặt thời gian cho nghiên cứu tạo video trong tương lai, thu hẹp đáng kể khoảng cách hiệu suất giữa các mô hình autoregressive và Diffusion. Các đóng góp chính bao gồm việc giới thiệu VideoAR, đề xuất Multi-scale Temporal RoPE và hai chiến lược huấn luyện hiệu quả (Cross-Frame Error Correction, Random Frame Mask) để tăng cường mô hình hóa không gian-thời gian, cùng với bộ mã hóa và Transformer backbone được huấn luyện trước hiệu quả đạt kết quả SOTA.

### V. Brainstorming Space:
#### 1. Publish Papers:
1. Nghiên cứu sự kết hợp của kiến trúc VideoAR với các kỹ thuật nén video thích ứng để đạt được việc tạo video chất lượng cao trên băng thông hạn chế.
2. Khám phá việc tích hợp VideoAR với các mô hình ngôn ngữ lớn (LLM) để tạo ra các kịch bản video phức tạp và câu chuyện động từ mô tả văn bản chi tiết hơn.
3. Điều tra khả năng mở rộng mô hình VideoAR để tạo ra video tương tác trong thời gian thực, nơi người dùng có thể điều chỉnh các yếu tố động trong khi video đang được tạo.

#### 2. Patent:
1. Một hệ thống tạo video cá nhân hóa trên điện thoại di động, cho phép người dùng nhập mô tả văn bản để tạo các đoạn video ngắn chất lượng cao với độ nhất quán thời gian cao, sử dụng kiến trúc VideoAR nén và tối ưu hóa cho thiết bị di động.
2. Phương pháp cải thiện chất lượng video được quay trên điện thoại thông minh bằng cách sử dụng công nghệ VideoAR để sửa lỗi truyền qua khung hình và tăng cường độ mượt mà của chuyển động, đặc biệt cho các cảnh quay hành động hoặc có độ rung.
3. Ứng dụng di động cho phép người dùng tạo các hiệu ứng video động (ví dụ: thêm các đối tượng hoặc chuyển động nhất quán vào video hiện có) dựa trên mô tả văn bản, sử dụng mô hình VideoAR được triển khai dưới dạng dịch vụ đám mây hoặc tối ưu hóa cho chip AI trên điện thoại.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.05966](https://huggingface.co/papers/2601.05966) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.05966](https://arxiv.org/abs/2601.05966) |
| PDF Download | [https://arxiv.org/pdf/2601.05966.pdf](https://arxiv.org/pdf/2601.05966.pdf) |
| Github Repository | N/A |

--- 

## 12. Goal Force: Teaching Video Models To Accomplish Physics-Conditioned Goals

**Tác giả:** Nate Gillman, Yinghua Zhou, Zitian Tang, Evan Luo, Arjan Chakravarthy, Daksh Aggarwal, Michael Freeman, Charles Herrmann, Chen Sun

**Xuất bản lúc:** 2026-01-09

**Tag:** Video Generation, World Models, Neural Physics Simulator, Planning, Goal-Conditioned Control, Physics-aware AI

### I. Main Problem:
Vấn đề cốt lõi mà bài báo đề cập là việc xác định mục tiêu chính xác cho các mô hình tạo video (world models) vẫn còn khó khăn. Các hướng dẫn bằng văn bản thường quá trừu tượng để nắm bắt các sắc thái vật lý, trong khi hình ảnh mục tiêu lại không khả thi để chỉ định cho các nhiệm vụ động. Điều này cản trở khả năng của các mô hình này trong việc lập kế hoạch cho các nhiệm vụ vật lý phức tạp, đa bước.

### II. Main Idea:
Bài báo giới thiệu Goal Force, một khuôn khổ mới cho phép người dùng xác định mục tiêu thông qua các vector lực rõ ràng và động lực học trung gian, phản ánh cách con người hình dung các nhiệm vụ vật lý. Mô hình được huấn luyện trên một tập dữ liệu tổng hợp các nguyên tắc nhân quả cơ bản (như va chạm đàn hồi và domino đổ) để học cách truyền lực qua thời gian và không gian. Phương pháp này sử dụng một tín hiệu điều khiển vật lý đa kênh mới (lực trực tiếp, lực mục tiêu và khối lượng) để huấn luyện mô hình video tạo ra một chuỗi nhân quả vật lý cần thiết để đạt được lực mục tiêu đã chỉ định, hoạt động như một bộ mô phỏng vật lý thần kinh (neural physics simulator) ngầm định mà không cần trình mô phỏng bên ngoài khi suy luận.

### III. Main Results:
Mô hình thể hiện khả năng tổng quát hóa zero-shot đáng kể đối với các kịch bản phức tạp, thực tế, bao gồm thao tác công cụ và chuỗi nhân quả đa đối tượng, mặc dù chỉ được huấn luyện trên dữ liệu vật lý đơn giản. Kết quả cho thấy mô hình học được cách truyền lực qua thời gian và không gian, xử lý các chuỗi sự kiện. Điều này bao gồm khả năng sử dụng công cụ zero-shot, chẳng hạn như suy luận cách sử dụng gậy golf để truyền lực mong muốn vào bóng. Điều này gợi ý rằng mô hình không chỉ ghi nhớ các mẫu mà còn hoạt động như một bộ mô phỏng vật lý thần kinh ngầm định, cho phép lập kế hoạch chính xác, nhận biết vật lý mà không cần dựa vào các công cụ bên ngoài.

### IV. Conclusion & Future Works:
Goal Force cung cấp một phương pháp mới để dạy các mô hình video lập kế hoạch một chuỗi tương tác vật lý để đạt được một lực mục tiêu cụ thể, thay đổi cách mục tiêu có thể được chỉ định trong các mô hình thế giới. Bằng cách nối đất tạo video trong các tương tác vật lý cơ bản, các mô hình có thể phát triển thành các bộ mô phỏng vật lý thần kinh ngầm định. Tương lai có thể bao gồm việc tích hợp các lực mục tiêu này vào các công cụ lập kế hoạch hình ảnh để chỉ định mục tiêu ngoài văn bản và phát triển các mô hình thế giới tương tác có khả năng vật lý hơn. Mã nguồn, trọng số mô hình, dữ liệu huấn luyện và dữ liệu benchmark đều được công khai.

### V. Brainstorming Space:
#### 1. Publish Papers:
*   Nghiên cứu về các phương pháp hiệu quả để tạo dữ liệu tổng hợp đa dạng hơn, phức tạp hơn nhằm nâng cao khả năng tổng quát hóa của Goal Force trong các kịch bản vật lý khó lường.
*   Phát triển một kiến trúc mô hình kết hợp Goal Force với khả năng học tăng cường (Reinforcement Learning) để cho phép robot thực hiện các nhiệm vụ thao tác phức tạp trong thế giới thực dựa trên các mục tiêu lực.
*   Khám phá cách Goal Force có thể được sử dụng để tạo ra các môi trường ảo tương tác có tính vật lý cao cho mục đích huấn luyện AI hoặc phát triển trò chơi.
#### 2. Patent:
*   Hệ thống chỉnh sửa video di động cho phép người dùng chỉ định lực tác động mục tiêu lên các vật thể trong video, sau đó AI sẽ tự động tạo ra một chuỗi hoạt ảnh vật lý phù hợp, tạo ra hiệu ứng động thực tế.
*   Ứng dụng thiết kế trò chơi di động hỗ trợ người dùng tạo ra các kịch bản tương tác phức tạp bằng cách chỉ định các "lực mục tiêu" cho nhân vật hoặc vật thể, giúp AI tự động tạo ra các hành động tiền đề để đạt được mục tiêu đó.
*   Công nghệ thực tế tăng cường (AR) trên điện thoại cho phép người dùng "tác động lực" ảo lên các vật thể kỹ thuật số trong môi trường thực tế, với AI mô phỏng kết quả vật lý của lực đó, ví dụ, đẩy một vật thể ảo và xem nó tương tác với các vật thể khác.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.05848](https://huggingface.co/papers/2601.05848) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.05848](https://arxiv.org/abs/2601.05848) |
| PDF Download | [https://arxiv.org/pdf/2601.05848.pdf](https://arxiv.org/pdf/2601.05848.pdf) |
| Github Repository | N/A |

--- 

## 13. SmartSearch: Process Reward-Guided Query Refinement for Search Agents

**Tác giả:** Tongyu Wen, Guanting Dong, Zhicheng Dou

**Xuất bản lúc:** 2026-01-08

**Tag:** Search Agent, Large Language Models, Information Retrieval, RAG, Process Reward, Query Refinement

### I. Main Problem:
Các tác nhân tìm kiếm dựa trên Mô hình Ngôn ngữ Lớn (LLM) đã cho thấy nhiều hứa hẹn, nhưng chất lượng của các truy vấn tìm kiếm trung gian thường bị bỏ qua. Điều này dẫn đến các truy vấn không chính xác, gây ra kết quả truy xuất không mong muốn và cuối cùng hạn chế hiệu quả tổng thể của tác nhân tìm kiếm. Các phương pháp hiện có chưa đủ hiệu quả trong việc cải thiện chất lượng truy vấn trung gian và thường ưu tiên việc sử dụng thông tin hơn là tối ưu hóa các mẫu truy xuất.

### II. Main Idea:
Bài báo giới thiệu SmartSearch, một khung công tác được xây dựng trên hai cơ chế chính để tối ưu hóa chất lượng truy vấn tìm kiếm và nâng cao khả năng tìm kiếm thông tin chuyên sâu của tác nhân:
1.  **Process rewards:** Cung cấp giám sát chi tiết về chất lượng của từng truy vấn tìm kiếm trung gian thông qua Đánh giá Tín dụng Hai cấp độ (Dual-Level Credit Assessment), bao gồm đánh giá dựa trên quy tắc cho tính mới của truy vấn và đánh giá dựa trên mô hình cho tính hữu ích của truy vấn. Cơ chế này cung cấp cả điểm số và phản hồi bằng văn bản.
2.  **Query refinement:** Thúc đẩy tối ưu hóa việc tạo truy vấn bằng cách chọn lọc tinh chỉnh các truy vấn chất lượng thấp và tạo lại các vòng tìm kiếm tiếp theo dựa trên những tinh chỉnh này.
Để tác nhân tìm kiếm dần dần nội hóa khả năng cải thiện chất lượng truy vấn dưới sự hướng dẫn của phần thưởng quá trình, nhóm nghiên cứu đã thiết kế khung học tập theo chương trình ba giai đoạn:
1.  **Query Quality Screened Imitation Learning:** Học tập bắt chước có chọn lọc dữ liệu huấn luyện chất lượng cao.
2.  **Query Generation Alignment:** Điều chỉnh khả năng tạo truy vấn thông qua DPO (Direct Preference Optimization).
3.  **Query-Aware Policy Optimization:** Tối ưu hóa chính sách nhận thức về truy vấn bằng Học tăng cường (Reinforcement Learning).

### III. Main Results:
SmartSearch liên tục vượt trội hơn các phương pháp cơ sở hiện có trên sáu nhiệm vụ tập trung vào kiến thức và khám phá web đầy thách thức. Các phân tích định lượng bổ sung xác nhận những cải thiện đáng kể của nó về cả hiệu quả tìm kiếm và chất lượng truy vấn. Kết quả cũng làm nổi bật đóng góp quan trọng của hai cơ chế chính và ba giai đoạn học tập theo chương trình trong việc nâng cao hiệu quả và chất lượng truy vấn tìm kiếm.

### IV. Conclusion & Future Works:
Nghiên cứu này tiên phong trong việc tối ưu hóa chất lượng các truy vấn tìm kiếm trung gian thông qua hướng dẫn của phần thưởng quá trình, từ đó cải thiện khả năng tìm kiếm thông tin của các tác nhân tìm kiếm. SmartSearch, với các cơ chế phần thưởng quá trình và tinh chỉnh truy vấn, cùng với khung học tập theo chương trình ba giai đoạn, đã chứng minh hiệu quả vượt trội. Văn bản được trích xuất không đề cập rõ ràng đến các hướng nghiên cứu trong tương lai.

### V. Brainstorming Space:
#### 1. Publish Papers:
*   Nghiên cứu mở rộng cơ chế "process rewards" để đánh giá và cải thiện chất lượng các bước trung gian trong các tác vụ lý luận phức tạp khác ngoài tìm kiếm.
*   Khám phá các phương pháp học tăng cường và mô hình thưởng thay thế để tối ưu hóa việc tạo truy vấn, tập trung vào sự đa dạng và khả năng thích ứng của truy vấn.
*   Áp dụng kỹ thuật "query refinement" vào các hệ thống RAG tĩnh hoặc động để cải thiện chất lượng truy xuất thông tin trong các ứng dụng chuyên biệt.

#### 2. Patent:
*   Một trợ lý tìm kiếm thông minh tích hợp vào hệ điều hành di động, tự động phân tích và tinh chỉnh các truy vấn tìm kiếm của người dùng theo thời gian thực dựa trên ngữ cảnh và lịch sử tương tác để tối ưu hóa kết quả.
*   Hệ thống tối ưu hóa truy vấn tìm kiếm nội bộ cho ứng dụng di động doanh nghiệp, sử dụng cơ chế thưởng theo quá trình để cải thiện hiệu quả truy xuất dữ liệu chuyên biệt từ các cơ sở tri thức nội bộ.
*   Tiện ích mở rộng trình duyệt di động sử dụng AI để dự đoán và đề xuất các phiên bản truy vấn tìm kiếm đã được tinh chỉnh trước khi người dùng gửi, nhằm cung cấp kết quả chính xác và liên quan hơn, giảm số lần tìm kiếm lại.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.04888](https://huggingface.co/papers/2601.04888) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.04888](https://arxiv.org/abs/2601.04888) |
| PDF Download | [https://arxiv.org/pdf/2601.04888.pdf](https://arxiv.org/pdf/2601.04888.pdf) |
| Github Repository | [https://github.com/MYVAE/SmartSearch?tab=readme-ov-file](https://github.com/MYVAE/SmartSearch?tab=readme-ov-file) |

--- 

## 14. CaricatureGS: Exaggerating 3D Gaussian Splatting Faces With Gaussian Curvature

**Tác giả:** Eldad Matmon, Amit Bracha, Noam Rotstein, Ron Kimmel

**Xuất bản lúc:** 2026-01-06

**Tag:** 3D Gaussian Splatting, Caricature, Facial Animation, Geometric Deformation, Pseudo-Ground Truth, Deep Learning

### I. Main Problem:
Vấn đề cốt lõi là tạo ra các hình ảnh biếm họa 3D khuôn mặt chân thực và có thể điều khiển được trong khi vẫn giữ nguyên danh tính, đây vẫn là một thách thức mở. Các phương pháp dựa trên lưới truyền thống khi kết hợp với ánh xạ texture thường tạo ra các kết quả không tự nhiên và quá mịn màng. Hơn nữa, việc biến dạng trực tiếp các Gaussians để tạo biếm họa dẫn đến chất lượng thấp do khoảng cách miền (domain gap) giữa biểu cảm tự nhiên và biếm họa, và thiếu dữ liệu huấn luyện biếm họa chân thực.

### II. Main Idea:
Bài báo giới thiệu CaricatureGS, một framework mới kết hợp sự cường điệu hình học dựa trên độ cong Gaussian với 3D Gaussian Splatting (3DGS) để tạo ra các avatar biếm họa 3D chân thực.
1.  **Cường điệu hóa bề mặt:** Bắt đầu bằng cách trích xuất lưới FLAME từ video đa góc nhìn, sau đó giải phương trình Poisson có trọng số độ cong để thu được dạng lưới bị cường điệu hóa.
2.  **Tạo dữ liệu huấn luyện:** Để giải quyết việc thiếu dữ liệu biếm họa thực, phương pháp tổng hợp hình ảnh biếm họa "pseudo-ground-truth" (GT\*) bằng cách làm biến dạng từng khung hình đầu vào sang biểu diễn 2D đã cường điệu hóa tương ứng, sử dụng các phép biến đổi affine cục bộ.
3.  **Huấn luyện 3DGS:** Đề xuất một lược đồ huấn luyện xen kẽ giữa giám sát từ hình ảnh thực và hình ảnh GT\* được tổng hợp. Điều này cho phép một tập hợp Gaussians duy nhất mô hình hóa cả avatar tự nhiên và avatar biếm họa, khắc phục khoảng cách miền và cải thiện độ chân thực. Một mặt nạ không gian được áp dụng để bảo vệ các cấu trúc nhỏ (như tóc) trong các bước GT\*.
4.  **Kiểm soát và hiệu quả:** Giới thiệu một phép nội suy hiệu quả giữa bề mặt gốc và bề mặt bị cường điệu hóa để đạt được biến dạng thời gian thực, cho phép kiểm soát liên tục cường độ biếm họa và hỗ trợ chỉnh sửa cục bộ.

### III. Main Results:
*   CaricatureGS tạo ra các avatar biếm họa 3D chân thực, được kiểm soát hình học và giữ nguyên danh tính.
*   Phương pháp này vượt trội so với các công trình trước đây trong cả đánh giá định lượng và định tính về độ chân thực hình ảnh, tính nhất quán cấu trúc và bảo toàn danh tính.
*   Hỗ trợ kiểm soát liên tục cường độ biếm họa thông qua nội suy tuyến tính hiệu quả, với độ lệch giới hạn so với các giải pháp dạng đóng.
*   Cung cấp khả năng biến dạng theo thời gian thực và chỉnh sửa cục bộ (ví dụ: phóng đại kích thước mũi) mà không ảnh hưởng đến các vùng không liên quan.
*   Thành công trong việc kết hợp sự trung thực hình học dựa trên độ cong với 3DGS để tạo ra biếm họa chân thực.

### IV. Conclusion & Future Works:
CaricatureGS là đại diện 3DGS động đầu tiên cho phép kết xuất biếm họa chân thực trong khi vẫn giữ nguyên danh tính dưới các biến dạng biếm họa. Văn bản được trích xuất không nêu rõ các hướng nghiên cứu trong tương lai.

### V. Brainstorming Space:
#### 1. Publish Papers:
1.  Nghiên cứu mở rộng CaricatureGS để tạo ra các hình ảnh biếm họa không chỉ khuôn mặt mà còn toàn thân người, tích hợp các cử chỉ và chuyển động cơ thể.
2.  Phát triển một phương pháp CaricatureGS tương tác theo thời gian thực, cho phép người dùng điều chỉnh trực tiếp các đặc điểm biếm họa thông qua giao diện đồ họa.
3.  Áp dụng CaricatureGS để tạo ra các nhân vật hoạt hình hoặc avatar có phong cách độc đáo, học hỏi từ các nghệ sĩ biếm họa để tự động hóa quá trình sáng tạo.

#### 2. Patent:
1.  Một ứng dụng di động cho phép người dùng chụp ảnh selfie và tự động tạo ra hình ảnh hoặc video biếm họa 3D của chính họ, với khả năng điều chỉnh mức độ cường điệu.
2.  Công nghệ tích hợp CaricatureGS vào các nền tảng mạng xã hội hoặc ứng dụng gọi video, cho phép người dùng hiển thị avatar biếm họa 3D của mình trong các cuộc trò chuyện.
3.  Hệ thống AI trên điện thoại có khả năng phân tích biểu cảm khuôn mặt theo thời gian thực và áp dụng hiệu ứng biếm họa 3D động cho avatar người dùng trong các môi trường thực tế tăng cường (AR).

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.03319](https://huggingface.co/papers/2601.03319) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.03319](https://arxiv.org/abs/2601.03319) |
| PDF Download | [https://arxiv.org/pdf/2601.03319.pdf](https://arxiv.org/pdf/2601.03319.pdf) |
| Github Repository | N/A |

--- 

## 15. GenCtrl -- A Formal Controllability Toolkit for Generative Models

**Tác giả:** Emily Cheng, Carmen Amo Alonso, Federico Danieli, Arno Blaas, Luca Zappella, Pau Rodriguez, Xavier Suau

**Xuất bản lúc:** 2026-01-09

**Tag:** Generative Models, Controllability, Control Theory, Formal Verification, PAC Algorithms, LLMs, Text-to-Image

### I. Main Problem:
Nhu cầu kiểm soát chi tiết các mô hình sinh sản đang tăng lên, nhưng các phương pháp hiện có ngầm giả định khả năng kiểm soát của mô hình mà không có công cụ hình thức để xác minh. Điều này dẫn đến sự không chắc chắn về giới hạn cơ bản của các kỹ thuật kiểm soát hiện tại và thiếu một khung lý thuyết áp dụng cho các mô hình sinh sản phi tuyến tính, phức tạp với đầu ra rời rạc.

### II. Main Idea:
Bài báo đề xuất một khung lý thuyết dựa trên lý thuyết điều khiển để đánh giá khả năng kiểm soát của các mô hình sinh sản. Phương pháp này coi tương tác giữa người và mô hình là một quá trình điều khiển, đề xuất một thuật toán mới để ước tính các tập hợp có thể điều khiển được (controllable sets) với đảm bảo xác suất (PAC bounds). Khung này không phụ thuộc vào kiến trúc mô hình và có thể xử lý các không gian đầu vào/đầu ra rời rạc hoặc liên tục, giải quyết thách thức của các "discrete bottleneck" trong các hệ thống sinh sản.

### III. Main Results:
- Giới thiệu một khung lý thuyết điều khiển để định lượng một cách nghiêm ngặt các tập hợp có thể truy cập được (reachable sets) và có thể kiểm soát được (controllable sets) cho các mô hình sinh sản, cung cấp ngôn ngữ chính thức đầu tiên để mô tả các giới hạn vận hành.
- Phát triển các thuật toán Monte Carlo với đảm bảo PAC (probably-approximately correct) để ước tính các tập hợp này, các thuật toán này không phụ thuộc vào phân phối, chỉ giả định tính giới hạn của thuộc tính đầu ra và hoạt động cho bất kỳ hệ thống điều khiển phi tuyến tính nào.
- Phân tích thực nghiệm trên LLM và mô hình text-to-image cho thấy khả năng kiểm soát của mô hình rất "mong manh" và phụ thuộc nhiều vào bối cảnh thử nghiệm, không được đảm bảo, nhấn mạnh sự cần thiết của các phân tích cụ thể cho từng trường hợp.
- Cung cấp một bộ công cụ mã nguồn mở GenCtrl để cộng đồng nghiên cứu dễ dàng phân tích khả năng kiểm soát.

### IV. Conclusion & Future Works:
Bài báo kêu gọi một sự thay đổi tư duy, xem khả năng kiểm soát của mô hình sinh sản là một đối tượng phân tích rõ ràng, không phải là giả định ngầm. Công trình này đặt nền tảng có nguyên tắc hơn cho AI có thể kiểm soát được trong tương lai, nhấn mạnh sự cần thiết của các phân tích khả năng kiểm soát chặt chẽ, cụ thể cho từng trường hợp.

### V. Brainstorming Space:
#### 1. Publish Papers:
1. Nghiên cứu sâu hơn về các yếu tố cụ thể (ví dụ: kích thước mô hình, tập dữ liệu huấn luyện) ảnh hưởng đến sự "mong manh" của khả năng kiểm soát ở các mô hình sinh sản khác nhau.
2. Phát triển các chiến lược kiểm soát (ví dụ: kỹ thuật nhắc lệnh, tinh chỉnh) được tối ưu hóa dựa trên các ước tính tập hợp có thể điều khiển được của GenCtrl, thay vì chỉ thử và sai.
3. Mở rộng khung GenCtrl để đánh giá khả năng kiểm soát của các hệ thống AI tổng hợp phức tạp hơn, nơi nhiều mô hình tương tác với nhau trong một quy trình đa bước.

#### 2. Patent:
1. Một hệ thống tích hợp cho điện thoại thông minh cho phép người dùng kiểm tra trước phạm vi đầu ra khả thi của một trợ lý AI sinh sản (ví dụ: tạo ảnh, soạn tin nhắn) dựa trên đầu vào của họ, đảm bảo kết quả nằm trong giới hạn mong muốn.
2. Công nghệ điều chỉnh động các tham số kiểm soát của mô hình AI trên thiết bị di động (ví dụ: độ "sáng tạo" của văn bản, kiểu hình ảnh) dựa trên phản hồi của người dùng và khả năng kiểm soát ước tính theo thời gian thực để đạt được mục tiêu cụ thể.
3. Một giao diện người dùng trên điện thoại cho phép trực quan hóa "biên giới kiểm soát" của mô hình sinh sản, giúp người dùng hiểu rõ hơn về những gì AI có thể và không thể tạo ra một cách đáng tin cậy cho một tác vụ nhất định.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.05637](https://huggingface.co/papers/2601.05637) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.05637](https://arxiv.org/abs/2601.05637) |
| PDF Download | [https://arxiv.org/pdf/2601.05637.pdf](https://arxiv.org/pdf/2601.05637.pdf) |
| Github Repository | N/A |

--- 

## 16. Over-Searching in Search-Augmented Large Language Models

**Tác giả:** Roy Xie, Deepak Gopinath, David Qiu, Dong Lin, Haitian Sun, Saloni Potdar, Bhuwan Dhingra

**Xuất bản lúc:** 2026-01-09

**Tag:** Search-Augmented LLMs, Over-Searching, Abstention, Retrieval, TPC

### I. Main Problem:
Các mô hình ngôn ngữ lớn (LLMs) được tăng cường tìm kiếm thường gặp phải tình trạng "over-searching" – tức là vô ích gọi công cụ tìm kiếm ngay cả khi nó không cải thiện chất lượng phản hồi, dẫn đến kém hiệu quả về tính toán và gây ra lỗi hallucination do tích hợp ngữ cảnh không liên quan. Vấn đề này đặc biệt nghiêm trọng với các truy vấn không thể trả lời hoặc không rõ ràng, nơi các hệ thống đáng tin cậy nên từ chối đưa ra câu trả lời dứt khoát.

### II. Main Idea:
Bài nghiên cứu thực hiện một đánh giá có hệ thống về hiện tượng "over-searching" trên nhiều khía cạnh bao gồm các loại truy vấn, danh mục mô hình, điều kiện truy xuất và hội thoại nhiều lượt. Để định lượng "over-searching", các tác giả giới thiệu một chỉ số đánh giá mới là Tokens Per Correctness (TPC) nhằm nắm bắt sự đánh đổi giữa hiệu suất và chi phí cho các LLMs tăng cường tìm kiếm. Cuối cùng, bài báo khám phá các phương pháp giảm thiểu ở cả cấp độ truy vấn và truy xuất, đồng thời phát hành bộ dữ liệu OverSearchQA để thúc đẩy nghiên cứu liên tục về LLMs tăng cường tìm kiếm hiệu quả.

### III. Main Results:
Các phát hiện chính bao gồm:
1.  Tìm kiếm nói chung cải thiện độ chính xác câu trả lời cho các truy vấn có thể trả lời nhưng lại làm giảm khả năng từ chối trả lời cho các truy vấn không thể trả lời.
2.  "Over-searching" rõ rệt hơn ở các mô hình suy luận phức tạp và hệ thống nghiên cứu sâu, bị trầm trọng hơn bởi việc truy xuất thông tin nhiễu, và tích lũy qua các lượt trong hội thoại nhiều lượt.
3.  Thành phần của bằng chứng được truy xuất rất quan trọng, vì sự hiện diện của bằng chứng tiêu cực (negative evidence) giúp cải thiện khả năng từ chối trả lời.
4.  Chỉ số Tokens Per Correctness (TPC) tăng đơn điệu khi số lượt tìm kiếm tối đa tăng lên, cho thấy chi phí tích lũy nhanh hơn so với mức tăng độ chính xác, vì các tìm kiếm bổ sung không cải thiện độ chính xác câu trả lời cũng như không ngăn chặn sự suy giảm khả năng từ chối trả lời.

### IV. Conclusion & Future Works:
Mặc dù các LLMs tăng cường tìm kiếm vượt trội trong các tác vụ đòi hỏi kiến thức, chúng vẫn thường xuyên "over-search", gây ra chi phí và tiềm ẩn lỗi hallucination. Bài nghiên cứu đã đánh giá có hệ thống vấn đề này và đề xuất chỉ số TPC để định lượng nó. Các chiến lược giảm thiểu được khám phá nhưng chưa giải quyết được hoàn toàn khả năng tìm kiếm hợp lý của mô hình. Bài báo cung cấp bộ dữ liệu OverSearchQA để thúc đẩy nghiên cứu về khả năng từ chối và hiệu quả tìm kiếm.

### V. Brainstorming Space:
#### 1. Publish Papers:
*   Nghiên cứu các thuật toán dự đoán động thời điểm dừng tìm kiếm dựa trên độ tự tin của mô hình và tính chất của truy vấn để tối ưu hóa chi phí.
*   Phát triển các phương pháp đào tạo để LLMs tăng cường tìm kiếm tự động nhận diện và ưu tiên "bằng chứng tiêu cực" trong quá trình truy xuất nhằm cải thiện khả năng từ chối trả lời.
*   Khám phá việc tích hợp cơ chế phản hồi người dùng trong các cuộc hội thoại nhiều lượt để hướng dẫn LLMs giảm thiểu "over-searching" và cải thiện sự rõ ràng của câu hỏi.
#### 2. Patent:
*   Hệ thống trợ lý ảo trên điện thoại thông minh sử dụng chỉ số TPC để tự động điều chỉnh số lượt tìm kiếm tối đa, tiết kiệm pin và giảm thời gian phản hồi cho các truy vấn của người dùng.
*   Ứng dụng di động tích hợp tính năng cảnh báo thông minh, thông báo cho người dùng khi một truy vấn có khả năng gây ra "over-searching" và đề xuất làm rõ hoặc từ chối tìm kiếm để tối ưu hóa trải nghiệm.
*   Công nghệ quản lý tài nguyên trên thiết bị di động cho phép các ứng dụng AI đánh giá chi phí tìm kiếm dựa trên tính chất truy vấn và mức độ quan trọng của thông tin, chủ động điều chỉnh hoặc ngừng tìm kiếm để bảo vệ hiệu năng hệ thống.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.05503](https://huggingface.co/papers/2601.05503) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.05503](https://arxiv.org/abs/2601.05503) |
| PDF Download | [https://arxiv.org/pdf/2601.05503.pdf](https://arxiv.org/pdf/2601.05503.pdf) |
| Github Repository | [https://github.com/ruoyuxie/OversearchQA](https://github.com/ruoyuxie/OversearchQA) |

--- 

## 17. DR-LoRA: Dynamic Rank LoRA for Mixture-of-Experts Adaptation

**Tác giả:** Guanzhi Deng, Bo Li, Ronghao Chen, Huacan Wang, Linqi Song, Lijie Wen

**Xuất bản lúc:** 2026-01-08

**Tag:** LoRA, Mixture-of-Experts (MoE), Parameter-Efficient Fine-Tuning (PEFT), Dynamic Rank Adaptation

### I. Main Problem:
Các phương pháp điều chỉnh tham số hiệu quả (PEFT) hiện có, như LoRA, áp dụng cùng một hạng (rank) cho tất cả các chuyên gia (experts) trong mô hình Mixture-of-Experts (MoE) Large Language Models (LLMs). Cách tiếp cận đồng nhất này bỏ qua sự chuyên biệt chức năng vốn có của các chuyên gia MoE, dẫn đến việc phân bổ tài nguyên không phù hợp: các chuyên gia liên quan đến nhiệm vụ bị thiếu tài nguyên trong khi các chuyên gia ít liên quan nhận các tham số dư thừa, từ đó hạn chế hiệu suất và khả năng thích ứng của mô hình trên các tác vụ downstream.

### II. Main Idea:
Bài báo đề xuất DR-LoRA, một framework LoRA hạng động, tự động tăng hạng LoRA của các chuyên gia trong quá trình fine-tuning dựa trên nhu cầu cụ thể của từng tác vụ. DR-LoRA sử dụng cơ chế Chấm điểm mức độ nổi bật của chuyên gia (Expert Saliency Scoring) tích hợp hai tín hiệu: tần suất định tuyến của chuyên gia (tần suất được chọn) và tầm quan trọng của hạng LoRA (cường độ học tập). Các chuyên gia có điểm nổi bật cao hơn sẽ được ưu tiên mở rộng hạng, cho phép tự động hình thành một phân bố hạng không đồng nhất, phù hợp với tác vụ mục tiêu. Phương pháp này bắt đầu với hạng khởi tạo nhỏ và tăng dần hạng cho các chuyên gia có nhu cầu cao trong một "growth window" được xác định.

### III. Main Results:
Các thử nghiệm trên nhiều bộ dữ liệu benchmark đã chứng minh rằng DR-LoRA luôn vượt trội so với LoRA tiêu chuẩn và các chiến lược phân bổ tĩnh cũng như các phương pháp dựa trên cắt tỉa (pruning) dưới cùng một ngân sách tham số. DR-LoRA đạt được hiệu suất tác vụ vượt trội và sử dụng tham số hiệu quả hơn, với các phân tích xác nhận khả năng phân bổ năng lực hiệu quả, phù hợp với tác vụ.

### IV. Conclusion & Future Works:
DR-LoRA giải quyết hiệu quả vấn đề phân bổ tài nguyên không khớp trong việc thích ứng mô hình MoE bằng LoRA đồng nhất bằng cách giới thiệu một phương pháp điều chỉnh hạng động. Bằng cách điều chỉnh động khả năng thích ứng của từng chuyên gia dựa trên nhu cầu của tác vụ, DR-LoRA đạt được hiệu suất vượt trội và sử dụng tham số tối ưu hơn, chứng minh tiềm năng lớn trong việc tinh chỉnh các mô hình MoE LLMs một cách hiệu quả.

### V. Brainstorming Space:
#### 1. Publish Papers:
1. Nghiên cứu các phương pháp chấm điểm mức độ nổi bật của chuyên gia khác, kết hợp các tín hiệu học tập và cấu trúc mô hình để tối ưu hóa việc phân bổ hạng LoRA.
2. Mở rộng DR-LoRA để hỗ trợ fine-tuning đa nhiệm, trong đó hạng của các chuyên gia được điều chỉnh động cho nhiều tác vụ đồng thời.
3. Phân tích sâu hơn về mối quan hệ giữa sự chuyên biệt của chuyên gia và phân bố hạng LoRA được hình thành bởi DR-LoRA để hiểu rõ hơn về các cơ chế học tập.

#### 2. Patent:
1. Hệ thống quản lý tài nguyên AI trên điện thoại di động tự động điều chỉnh năng lực học tập của các module AI (ví dụ: hạng LoRA) dựa trên tần suất sử dụng ứng dụng và hiệu suất tác vụ hiện tại, tiết kiệm pin.
2. Công nghệ tối ưu hóa thuật toán LoRA tích hợp trên chip di động, cho phép các mô hình ngôn ngữ lớn trên thiết bị tự động điều chỉnh hạng của các expert để phù hợp với các yêu cầu cụ thể của người dùng và các tác vụ khác nhau (ví dụ: dịch thuật, tóm tắt).
3. Phương pháp thích ứng mô hình AI cá nhân hóa trên thiết bị di động, sử dụng Expert Saliency Scoring để ưu tiên và mở rộng khả năng của các chuyên gia MoE liên quan nhất đến hành vi và sở thích của người dùng, mang lại trải nghiệm AI mượt mà hơn.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.04823](https://huggingface.co/papers/2601.04823) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.04823](https://arxiv.org/abs/2601.04823) |
| PDF Download | [https://arxiv.org/pdf/2601.04823.pdf](https://arxiv.org/pdf/2601.04823.pdf) |
| Github Repository | N/A |

--- 

## 18. IIB-LPO: Latent Policy Optimization via Iterative Information Bottleneck

**Tác giả:** Huilin Deng, Hongchen Luo, Yue Zhu, Long Li, Zhuoyue Chen, Xinghao Zhao, Ming Li, Jihai Zhang, Mengchang Wang, Yang Cao, Yu Kang

**Xuất bản lúc:** 2026-01-09

Summary generation failed.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.05870](https://huggingface.co/papers/2601.05870) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.05870](https://arxiv.org/abs/2601.05870) |
| PDF Download | [https://arxiv.org/pdf/2601.05870.pdf](https://arxiv.org/pdf/2601.05870.pdf) |
| Github Repository | N/A |

--- 

## 19. Router-Suggest: Dynamic Routing for Multimodal Auto-Completion in Visually-Grounded Dialogs

**Tác giả:** Sandeep Mishra, Devichand Budagam, Anubhab Mandal, Bishal Santra, Pawan Goyal, Manish Gupta

**Xuất bản lúc:** 2026-01-09

**Tag:** Multimodal Auto-Completion, Dynamic Routing, Vision-Language Models, Dialog Systems

### I. Main Problem:
Vấn đề cốt lõi mà bài báo đề cập là việc thiếu hụt một hệ thống hoàn thành tự động (auto-completion) hiệu quả trong các cuộc hội thoại đa phương thức (multimodal dialogs) có ngữ cảnh thị giác. Các hệ thống hoàn thành tự động chỉ dựa trên văn bản (Text-only Auto-Completion - TAC) không thể nắm bắt đúng ý định của người dùng khi thông tin hình ảnh đóng vai trò quan trọng, dẫn đến dự đoán không chính xác và trải nghiệm người dùng kém hiệu quả, đặc biệt trong các ứng dụng như trợ lý kỹ thuật số, chatbot hay công cụ thiết kế.

### II. Main Idea:
Bài báo giới thiệu khái niệm Multimodal Auto-Completion (MAC), một tác vụ dự đoán các ký tự sắp tới trong các cuộc trò chuyện trực tiếp dựa trên văn bản đã gõ một phần và các tín hiệu thị giác. Để giải quyết thách thức này, các tác giả đề xuất **Router-Suggest**, một framework định tuyến động. Router-Suggest tự động lựa chọn giữa các mô hình chỉ dựa trên văn bản (textual models) và các mô hình ngôn ngữ thị giác (Vision-Language Models - VLMs) tùy thuộc vào ngữ cảnh hội thoại, đặc biệt là mức độ quan trọng của yếu tố thị giác. Router-Suggest sử dụng một bộ định tuyến thần kinh nhẹ (lightweight neural router) được huấn luyện bằng phương pháp tối ưu hóa chi phí để cân bằng giữa độ chính xác và độ trễ. Để hỗ trợ tác vụ MAC, bài báo xây dựng các bộ dữ liệu benchmark mới bằng cách điều chỉnh MM-Dialog và ImageChat, sử dụng GPT-4V để lọc các cuộc hội thoại có liên quan trực quan mạnh mẽ.

### III. Main Results:
Router-Suggest đạt được tốc độ nhanh hơn từ 2.3 lần đến 10 lần so với VLM có hiệu suất tốt nhất. Nghiên cứu người dùng (user study) chỉ ra rằng các mô hình ngôn ngữ thị giác (VLMs) vượt trội đáng kể so với các mô hình chỉ dựa trên văn bản về mức độ hài lòng của người dùng, giúp tiết kiệm đáng kể công sức gõ phím và cải thiện chất lượng hoàn thành văn bản trong các cuộc hội thoại nhiều lượt.

### IV. Conclusion & Future Works:
Các phát hiện của bài báo nhấn mạnh sự cần thiết của ngữ cảnh đa phương thức trong các tác vụ hoàn thành tự động để tạo ra các trợ lý thông minh hơn và nhận biết người dùng tốt hơn. Bài báo công khai mã nguồn và các bộ dữ liệu benchmark để thúc đẩy nghiên cứu trong lĩnh vực này, hướng tới các hệ thống hội thoại có khả năng dự đoán người dùng một cách trực quan và hiệu quả.

### V. Brainstorming Space:
#### 1. Publish Papers:
1. Nghiên cứu mở rộng Router-Suggest để tích hợp nhiều mô hình đa phương thức hơn, không chỉ dừng lại ở văn bản và hình ảnh, mà còn cả âm thanh và video.
2. Phát triển các chiến lược định tuyến động tiên tiến hơn, có khả năng học hỏi và thích ứng theo thời gian thực dựa trên phản hồi của người dùng và các yếu tố ngữ cảnh phức tạp.
3. Khám phá các phương pháp tối ưu hóa Router-Suggest cho các thiết bị biên (edge devices) với tài nguyên hạn chế, tập trung vào việc giảm kích thước mô hình và độ trễ mà vẫn duy trì hiệu suất.
#### 2. Patent:
1. Một hệ thống hoàn thành tự động tin nhắn trên điện thoại di động có khả năng phân tích hình ảnh đính kèm hoặc được hiển thị trên màn hình để đưa ra các gợi ý văn bản phù hợp theo ngữ cảnh thị giác.
2. Công nghệ hoàn thành tự động cho các ứng dụng chỉnh sửa ảnh hoặc thiết kế đồ họa trên điện thoại, tự động gợi ý mô tả, hashtag hoặc chỉnh sửa dựa trên nội dung hình ảnh và văn bản nhập liệu.
3. Hệ thống trợ lý ảo trên điện thoại thông minh tích hợp tính năng định tuyến động để tối ưu hóa việc hoàn thành tự động đa phương thức, chuyển đổi linh hoạt giữa các mô hình nhẹ và mô hình phức tạp tùy theo độ phức tạp của ngữ cảnh và yêu cầu về tốc độ phản hồi.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.05851](https://huggingface.co/papers/2601.05851) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.05851](https://arxiv.org/abs/2601.05851) |
| PDF Download | [https://arxiv.org/pdf/2601.05851.pdf](https://arxiv.org/pdf/2601.05851.pdf) |
| Github Repository | N/A |

--- 

## 20. AnyDepth: Depth Estimation Made Easy

**Tác giả:** Zeyu Ren, Zeyu Zhang, Wukai Li, Qingxiang Liu, Hao Tang

**Xuất bản lúc:** 2026-01-06

**Tag:** Depth Estimation, Monocular, Zero-shot, Transformer, Lightweight, Efficiency, Data Quality

### I. Main Problem:
Các phương pháp ước tính độ sâu đơn ảnh hiện tại, mặc dù có tiến bộ đáng kể, nhưng phụ thuộc nhiều vào các bộ dữ liệu quy mô lớn và bộ giải mã phức tạp (như DPT), dẫn đến hạn chế về hiệu quả và khả năng tổng quát hóa. Cụ thể, kiến trúc phức tạp của DPT với việc hợp nhất đặc trưng đa nhánh, các thao tác căn chỉnh và nội suy song tuyến tính cố định gây ra độ phức tạp không cần thiết, số lượng tham số lớn, tốc độ suy luận chậm, và làm mất chi tiết không gian tinh vi. Hơn nữa, các phương pháp dựa trên dữ liệu thuần túy gặp phải vấn đề về chi phí thu thập dữ liệu lớn và sự xuất hiện của các mẫu nhiễu, làm giảm chất lượng huấn luyện.

### II. Main Idea:
Bài báo đề xuất AnyDepth, một khung làm việc nhẹ và tập trung vào dữ liệu để ước tính độ sâu đơn ảnh zero-shot. Các ý tưởng chính bao gồm:
1.  **Kiến trúc hiệu quả:** Sử dụng DINOv3 làm bộ mã hóa hình ảnh để trích xuất các đặc trưng dày đặc chất lượng cao. Thiết kế Simple Depth Transformer (SDT) làm bộ giải mã nhỏ gọn, dựa trên transformer. SDT sử dụng quy trình hợp nhất và nâng mẫu đặc trưng một đường duy nhất để giảm chi phí tính toán của việc hợp nhất đặc trưng đa tỷ lệ, đồng thời duy trì độ chính xác cao hơn và giảm đáng kể số lượng tham số. Nó cũng tích hợp Spatial Detail Enhancer (SDE) để bảo toàn chi tiết không gian và sử dụng bộ nâng mẫu động có thể học được (DySample) thay vì nội suy song tuyến tính cố định.
2.  **Cải thiện chất lượng dữ liệu:** Đề xuất một chiến lược lọc dựa trên chất lượng để loại bỏ các mẫu có hại, từ đó giảm kích thước bộ dữ liệu mà vẫn cải thiện chất lượng huấn luyện tổng thể.

### III. Main Results:
1.  Khung làm việc AnyDepth vượt trội so với DPT về độ chính xác trên năm bộ tiêu chuẩn.
2.  Bộ giải mã SDT giảm khoảng 85%-89% số lượng tham số so với DPT trong khi đạt được độ chính xác cao hơn.
3.  AnyDepth giảm đáng kể chi phí tính toán (FLOPs) và thời gian suy luận so với DPT, đặc biệt ở độ phân giải cao hơn, thể hiện sự cân bằng vượt trội giữa hiệu quả và độ chính xác.
4.  Chiến lược lọc mẫu giúp giảm kích thước bộ dữ liệu nhưng vẫn cải thiện chất lượng huấn luyện tổng thể.
5.  AnyDepth đạt được hiệu suất ấn tượng trên nhiều cảnh trong nhà và ngoài trời.

### IV. Conclusion & Future Works:
Bài báo nhấn mạnh tầm quan trọng của việc cân bằng giữa thiết kế mô hình và chất lượng dữ liệu để đạt được ước tính độ sâu zero-shot hiệu quả và có khả năng tổng quát hóa cao. Từ đó, gợi mở hướng nghiên cứu tiếp theo về việc tiếp tục tối ưu hóa sự cân bằng này.

### V. Brainstorming Space:
#### 1. Publish Papers:
1.  Nghiên cứu ảnh hưởng của các chiến lược lọc dữ liệu dựa trên chất lượng khác nhau đối với hiệu suất và độ bền vững của mô hình ước tính độ sâu.
2.  Phát triển các phương pháp kết hợp kiến trúc bộ mã hóa và bộ giải mã nhẹ của AnyDepth với các kỹ thuật học tự giám sát để cải thiện khả năng tổng quát hóa zero-shot hơn nữa.
3.  Áp dụng nguyên lý "hợp nhất và nâng mẫu một đường" của SDT vào các tác vụ dự đoán dày đặc khác như phân đoạn ngữ nghĩa hoặc ước tính tư thế cơ thể người.
#### 2. Patent:
1.  Hệ thống camera điện thoại thông minh tích hợp AI để tự động ước tính độ sâu ảnh, cho phép điều chỉnh lấy nét sau khi chụp và tạo hiệu ứng xóa phông tự nhiên cho ảnh chân dung.
2.  Phương pháp xử lý ảnh trên thiết bị di động để cải thiện chất lượng hình ảnh thực tế tăng cường (AR) bằng cách sử dụng thông tin độ sâu ước tính nhanh chóng và hiệu quả từ ảnh đơn.
3.  Công nghệ tối ưu hóa tài nguyên trên điện thoại thông minh cho các ứng dụng thị giác máy tính, sử dụng mô hình ước tính độ sâu nhẹ của AnyDepth để thực hiện các tác vụ nhận diện vật thể và đo khoảng cách với tiêu thụ pin thấp.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.02760](https://huggingface.co/papers/2601.02760) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.02760](https://arxiv.org/abs/2601.02760) |
| PDF Download | [https://arxiv.org/pdf/2601.02760.pdf](https://arxiv.org/pdf/2601.02760.pdf) |
| Github Repository | [https://github.com/AIGeeksGroup/AnyDepth](https://github.com/AIGeeksGroup/AnyDepth) |

