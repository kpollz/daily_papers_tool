# 🤗 Daily Hugging Face Paper Digest - 2026-01-06

Báo cáo được tạo tự động vào lúc 2026-01-07 11:08:22 bằng mô hình `gemini-2.5-flash`.

## 📰 Summary of Papers

--- 

## 1. Can LLMs Predict Their Own Failures? Self-Awareness via Internal Circuits

**Tác giả:** Amirhosein Ghasemabadi, Di Niu

**Xuất bản lúc:** 2025-12-23

### Main Problem:
Các mô hình ngôn ngữ lớn (LLM) có khả năng tạo ra các phản hồi trôi chảy và phức tạp nhưng thường không nhận ra lỗi của chính mình hoặc các thông tin bịa đặt (hallucinations). Khoảng cách giữa khả năng tạo văn bản mạnh mẽ và khả năng tự xác minh yếu này hạn chế độ tin cậy, an toàn và hiệu quả của việc triển khai LLM, đặc biệt trong các tình huống yêu cầu suy luận dài hạn hoặc kiểm soát chi phí tính toán. Các phương pháp hiện có thường dựa vào các thẩm phán bên ngoài, tính nhất quán đa mẫu hoặc tự phê bình dựa trên văn bản, nhưng chúng đều phát sinh chi phí tính toán bổ sung hoặc tương quan yếu với độ chính xác thực sự.

### Main Idea:
Bài nghiên cứu giới thiệu Gnosis, một cơ chế tự nhận thức nhẹ cho phép các LLM đã được huấn luyện (frozen LLMs) thực hiện tự xác minh nội tại bằng cách giải mã tín hiệu từ các trạng thái ẩn (hidden states) và các mẫu chú ý (attention patterns) trong quá trình suy luận. Gnosis hoạt động như một quan sát viên thụ động, nén các dấu vết nội bộ của mô hình thành các mô tả có kích thước cố định, sau đó dự đoán điểm số chính xác. Kiến trúc của Gnosis được thiết kế để chi phí suy luận không phụ thuộc vào độ dài chuỗi, chỉ thêm khoảng 5 triệu tham số và có chi phí tính toán không đáng kể.

### Main Results:
Gnosis đã chứng minh hiệu suất vượt trội so với các phương pháp cơ sở nội bộ mạnh mẽ và các thẩm phán bên ngoài lớn về cả độ chính xác và độ hiệu chuẩn (calibration).
*   Trên các bộ tiêu chuẩn bao gồm suy luận toán học (Math-Reasoning), hỏi đáp miền mở (Open-Domain QA) và kiến thức học thuật (Academic Knowledge), Gnosis luôn vượt trội hơn các mô hình thưởng Skywork 8B và thẩm phán Gemini 2.5 Pro trên các mô hình nền từ 1.7B đến 20B tham số.
*   Gnosis chỉ thêm khoảng 5 triệu tham số, nhỏ hơn nhiều lần so với các trình xác minh bên ngoài có hàng tỷ tham số, nhưng vẫn đạt được hiệu suất tiên tiến.
*   Gnosis có khả năng khái quát hóa zero-shot sang các thế hệ một phần (partial generations), cho phép phát hiện sớm các quỹ đạo suy luận thất bại và kiểm soát tài nguyên tính toán.
*   Các kết quả cho thấy các dấu hiệu đáng tin cậy về độ chính xác là nội tại đối với quá trình tạo ra phản hồi và có thể được trích xuất một cách hiệu quả mà không cần giám sát từ bên ngoài.

### Conclusion & Future Works:
Các kết quả cho thấy các dấu hiệu đáng tin cậy về độ chính xác là nội tại đối với quá trình tạo ra phản hồi của LLM và có thể được trích xuất một cách hiệu quả mà không cần giám sát từ bên ngoài. Khả năng tự nhận thức nội tại này của Gnosis mang lại tiềm năng cho việc phát hiện sớm các lỗi suy luận, mở rộng hiệu quả trên các kích thước mô hình và miền khác nhau, cũng như triển khai thực tế các hệ thống ngôn ngữ yêu cầu độ tin cậy cao và kiểm soát tài nguyên tính toán một cách hiệu quả.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2512.20578](https://huggingface.co/papers/2512.20578) |
| ArXiv Abstract | [https://arxiv.org/abs/2512.20578](https://arxiv.org/abs/2512.20578) |
| PDF Download | [https://arxiv.org/pdf/2512.20578.pdf](https://arxiv.org/pdf/2512.20578.pdf) |
| Github Repository | [https://github.com/Amirhosein-gh98/Gnosis](https://github.com/Amirhosein-gh98/Gnosis) |

--- 

## 2. K-EXAONE Technical Report

**Tác giả:** Eunbi Choi, Kibong Choi, Seokhee Hong, Junwon Hwang, Hyojin Jeon, Hyunjik Jo, Joonkee Kim, Seonghwan Kim, Soyeon Kim, Sunkyoung Kim, Yireun Kim, Yongil Kim, Haeju Lee, Jinsik Lee, Kyungmin Lee, Sangha Park, Heuiyeen Yeen, Hwan Chang, Stanley Jungkyu Choi, Yejin Choi, Jiwon Ham, Kijeong Jeon, Geunyeong Jeong, Gerrard Jeongwon Jo, Yonghwan Jo, Jiyeon Jung, Naeun Kang, Dohoon Kim, Euisoon Kim, Hayeon Kim, Hyosang Kim, Hyunseo Kim, Jieun Kim, Minu Kim, Myoungshin Kim, Unsol Kim, Youchul Kim, YoungJin Kim, Chaeeun Lee, Chaeyoon Lee, Changhun Lee, Dahm Lee, Edward Hwayoung Lee, Honglak Lee, Jinsang Lee, Jiyoung Lee, Sangeun Lee, Seungwon Lim, Solji Lim, Woohyung Lim, Chanwoo Moon, Jaewoo Park, Jinho Park, Yongmin Park, Hyerin Seo, Wooseok Seo, Yongwoo Song, Sejong Yang, Sihoon Yang, Chang En Yea, Sihyuk Yi, Chansik Yoon, Dongkeun Yoon, Sangyeon Yoon, Hyeongu Yun

**Xuất bản lúc:** 2026-01-05

### Main Problem:
Thị trường phát triển mô hình ngôn ngữ lớn (LLM) toàn cầu đang có sự cạnh tranh gay gắt, với nhu cầu về các mô hình có hiệu suất vượt trội. Tuy nhiên, Hàn Quốc đối mặt với những thách thức riêng biệt về cơ sở hạ tầng, như thiếu trung tâm dữ liệu chuyên dụng và chip AI, làm hạn chế khả năng phát triển các mô hình quy mô lớn. Các nỗ lực trước đây tập trung vào các mô hình nhỏ hơn, hiệu quả về chi phí. Vấn đề cốt lõi là làm thế nào để xây dựng một mô hình nền tảng mạnh mẽ và đáng tin cậy, đạt hiệu suất hàng đầu trên quy mô toàn cầu, bất chấp những hạn chế về cơ sở hạ tầng. Ngoài ra, việc mở rộng khả năng đa ngôn ngữ và tăng cường năng lực suy luận cũng là những thách thức quan trọng.

### Main Idea:
LG AI Research đã phát triển K-EXAONE, một mô hình ngôn ngữ đa ngôn ngữ quy mô lớn, được xây dựng trên kiến trúc Mixture-of-Experts (MoE) với tổng số 236 tỷ tham số, trong đó 23 tỷ tham số được kích hoạt trong quá trình suy luận. Mô hình này hỗ trợ cửa sổ ngữ cảnh 256K token và bao gồm sáu ngôn ngữ: tiếng Hàn, tiếng Anh, tiếng Tây Ban Nha, tiếng Đức, tiếng Nhật và tiếng Việt. K-EXAONE tích hợp các cải tiến kiến trúc như thiết kế MoE thưa tinh chỉnh, cơ chế chú ý lai (hybrid attention) kết hợp chú ý toàn cục và chú ý cửa sổ trượt, và một module Multi-Token Prediction (MTP) để hỗ trợ đào tạo phụ trợ và tăng tốc suy luận. Bộ mã hóa (tokenizer) đã được thiết kế lại với kích thước từ vựng tăng lên (150K) và chiến lược SuperBPE để cải thiện hiệu quả mã hóa và khả năng mở rộng đa ngôn ngữ. Quá trình tiền huấn luyện ba giai đoạn được áp dụng, sử dụng bộ dữ liệu chất lượng cao, mở rộng phạm vi ngôn ngữ thông qua tổng hợp dữ liệu có mục tiêu và tổng hợp dữ liệu tăng cường suy luận. Mô hình cũng áp dụng quy trình mở rộng độ dài ngữ cảnh hai giai đoạn (từ 8K lên 256K token) bằng cách sử dụng tập dữ liệu Rehearsal để duy trì hiệu suất ngữ cảnh ngắn và tập dữ liệu Synthetic Reasoning để tăng cường khả năng suy luận.

### Main Results:
K-EXAONE thể hiện hiệu suất cạnh tranh, ngang bằng với các mô hình mã nguồn mở có kích thước tương tự trên một bộ tiêu chuẩn đánh giá toàn diện, bao gồm các khả năng suy luận, tác tử, tổng quát, tiếng Hàn và đa ngôn ngữ. Cụ thể, mô hình đạt được kết quả ấn tượng trên tám hạng mục đánh giá chính: kiến thức thế giới (MMLU-PRO), toán học (AIME 2025), lập trình (LiveCodeBench v6), sử dụng công cụ tác tử (τ2-Bench), tuân thủ hướng dẫn (IFBench), tiếng Hàn (KoBALT), đa ngôn ngữ (MMMLU) và an toàn (KGC-Safety). Thiết kế lại bộ mã hóa đã cải thiện hiệu quả mã hóa trung bình khoảng 30% trên các miền văn bản khác nhau. Trong quá trình suy luận, K-EXAONE sử dụng khối MTP để tự phác thảo, đạt được tốc độ giải mã nhanh hơn khoảng 1,5 lần so với giải mã tự hồi quy tiêu chuẩn. Mô hình cũng duy trì hiệu suất ngữ cảnh ngắn tốt sau quá trình mở rộng độ dài ngữ cảnh lên 256K token nhờ vào việc sử dụng Rehearsal Dataset.

### Conclusion & Future Works:
K-EXAONE là một bước tiến quan trọng của LG AI Research trong việc phát triển một mô hình nền tảng đạt hiệu suất tiên phong, giải quyết các thách thức về cơ sở hạ tầng AI tại Hàn Quốc thông qua sự hỗ trợ của chính phủ. Với kiến trúc MoE sáng tạo, khả năng hỗ trợ đa ngôn ngữ rộng rãi và kỹ thuật huấn luyện tiên tiến, K-EXAONE đã đạt được hiệu suất cạnh tranh trên phạm vi toàn cầu. Mô hình được định vị là một mô hình nền tảng AI độc quyền mạnh mẽ, sẵn sàng cho nhiều ứng dụng công nghiệp và nghiên cứu, nhằm thúc đẩy AI vì một cuộc sống tốt đẹp hơn. Phần trích dẫn không nêu rõ các hướng nghiên cứu tiếp theo mà chủ yếu tập trung vào mô tả các đặc tính và kết quả hiện tại của mô hình.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.01739](https://huggingface.co/papers/2601.01739) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.01739](https://arxiv.org/abs/2601.01739) |
| PDF Download | [https://arxiv.org/pdf/2601.01739.pdf](https://arxiv.org/pdf/2601.01739.pdf) |
| Github Repository | [https://github.com/LG-AI-EXAONE/K-EXAONE](https://github.com/LG-AI-EXAONE/K-EXAONE) |

--- 

## 3. NextFlow: Unified Sequential Modeling Activates Multimodal Understanding and Generation

**Tác giả:** Huichao Zhang, Liao Qu, Yiheng Liu, Hang Chen, Yangyang Song, Yongsheng Dong, Shikun Sun, Xian Li, Xu Wang, Yi Jiang, Hu Ye, Bo Chen, Yiming Gao, Peng Liu, Akide Liu, Zhipeng Yang, Qili Deng, Linjie Xing, Jiyang Liu, Zhao Wang, Yang Zhou, Mingcong Liu, Yi Zhang, Qian He, Xiwei Hu, Zhongqi Qi, Jie Shao, Zhiye Fu, Shuai Wang, Fangmin Chen, Xuezhi Chai, Zhihua Wu, Yitong Wang, Zehuan Yuan, Daniel K. Du, Xinglong Wu

**Xuất bản lúc:** 2026-01-05

### Main Problem:
Các mô hình ngôn ngữ lớn (LLMs) và mô hình khuếch tán (Diffusion Models) hiện tại vẫn tách biệt, dẫn đến việc các mô hình khuếch tán thiếu khả năng suy luận và học theo ngữ cảnh của LLMs, trong khi các LLMs đa phương thức truyền thống thường chỉ giới hạn ở khả năng nhận thức. Các kiến trúc lai AR-Diffusion gặp vấn đề về chi phí mã hóa lại và hạn chế tích hợp đa phương thức sâu sắc. Các mô hình tự hồi quy thuần túy như Chameleon gặp phải hai vấn đề chính: chi phí tính toán lớn và tốc độ chậm khi tạo hình ảnh độ phân giải cao (hơn 10 phút cho ảnh 1024x1024) do sử dụng phương pháp quét raster truyền thống, và biểu diễn hình ảnh thiếu mật độ ngữ nghĩa cao, làm hạn chế hiệu suất trong các tác vụ hiểu đa phương thức.

### Main Idea:
Bài báo giới thiệu NextFlow, một mô hình transformer tự hồi quy chỉ dựa trên bộ giải mã (decoder-only) được huấn luyện trên 6 nghìn tỷ token rời rạc xen kẽ văn bản và hình ảnh. NextFlow kích hoạt khả năng hiểu và tạo đa phương thức thống nhất, bao gồm chỉnh sửa hình ảnh, nội dung xen kẽ và tạo video. Để giải quyết vấn đề hiệu quả, NextFlow sử dụng phương pháp dự đoán theo tỉ lệ tiếp theo (next-scale prediction) cho tạo hình ảnh (thay vì quét raster), tạo nội dung hình ảnh từ cấu trúc thô đến chi tiết tinh vi. Để khắc phục khoảng cách ngữ nghĩa, NextFlow áp dụng trình mã hóa tokenizer dual-codebook để tách biệt các đặc trưng ngữ nghĩa và mức pixel. Mô hình được huấn luyện với công thức mạnh mẽ để giải quyết sự bất ổn định của tạo đa tỉ lệ, và giới thiệu chiến lược prefix-tuning cho học tăng cường (Reinforcement Learning) để tối ưu hóa cấu trúc tổng thể. Một bộ giải mã khuếch tán tùy chọn cũng được tích hợp để tinh chỉnh đầu ra rời rạc, nâng cao độ chân thực của hình ảnh.

### Main Results:
NextFlow có thể tạo ra hình ảnh 1024x1024 chỉ trong 5 giây, nhanh hơn nhiều lần so với các mô hình AR tương đương dựa trên quét raster. Mô hình đạt hiệu suất dẫn đầu trong số các mô hình thống nhất và cạnh tranh với các mô hình khuếch tán chuyên biệt về chất lượng hình ảnh. Với 7 tỷ tham số, NextFlow đạt hiệu suất cạnh tranh trên các tiêu chuẩn văn bản-thành-hình ảnh và vượt trội hơn các mô hình chuyên biệt trong chỉnh sửa hình ảnh. Kiến trúc thống nhất hỗ trợ các tác vụ xen kẽ văn bản-hình ảnh, có khả năng thực hiện suy luận Chain-of-Thought (CoT) để tinh chỉnh lời nhắc và học theo ngữ cảnh (in-context learning) cho chỉnh sửa hình ảnh zero-shot. NextFlow hiệu quả cao, yêu cầu ít hơn 6 lần FLOPs trong quá trình suy luận so với các mô hình khuếch tán dựa trên MMDiT ở độ phân giải 1024x1024.

### Conclusion & Future Works:
NextFlow chứng minh rằng một mô hình tự hồi quy thống nhất có thể cạnh tranh với các mô hình khuếch tán tiên tiến về chất lượng hình ảnh, đồng thời giữ được khả năng suy luận của LLMs. Mô hình giải quyết thành công các nút thắt về hiệu quả và mật độ ngữ nghĩa trong các mô hình đa phương thức thống nhất. Thông tin về các hướng nghiên cứu tiếp theo không được cung cấp trong đoạn văn trích dẫn.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.02204](https://huggingface.co/papers/2601.02204) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.02204](https://arxiv.org/abs/2601.02204) |
| PDF Download | [https://arxiv.org/pdf/2601.02204.pdf](https://arxiv.org/pdf/2601.02204.pdf) |
| Github Repository | [https://github.com/ByteVisionLab/NextFlow](https://github.com/ByteVisionLab/NextFlow) |

--- 

## 4. DreamID-V:Bridging the Image-to-Video Gap for High-Fidelity Face Swapping via Diffusion Transformer

**Tác giả:** Xu Guo, Fulong Ye, Xinghui Li, Pengqi Tu, Pengze Zhang, Qichao Sun, Songtao Zhao, Xiangwang Hou, Qian He

**Xuất bản lúc:** 2026-01-04

### Main Problem:
Video Face Swapping (VFS) hiện tại gặp khó khăn trong việc duy trì độ tương đồng danh tính (identity similarity), bảo toàn thuộc tính (attribute preservation) như tư thế, biểu cảm, ánh sáng, nền và thông tin động, cũng như tính nhất quán thời gian (temporal consistency). Các phương pháp Image Face Swapping (IFS) tiên tiến, dù đạt hiệu suất tốt về danh tính và thuộc tính, khi áp dụng trực tiếp cho video thường gây ra hiện tượng nhấp nháy (flickering) và rung lắc (jittering). Các phương pháp VFS hiện có cải thiện tính nhất quán thời gian nhưng vẫn còn kém xa IFS về khả năng bảo toàn danh tính và thuộc tính. Ngoài ra, có sự hạn chế về các bộ dữ liệu đánh giá (benchmarks) toàn diện cho VFS.

### Main Idea:
Bài nghiên cứu đề xuất DreamID-V, một framework toàn diện nhằm thu hẹp khoảng cách giữa IFS và VFS để đạt được trao đổi khuôn mặt video độ chân thực cao. Giải pháp bao gồm ba trụ cột chính:
1.  **SyncID-Pipe:** Một pipeline dữ liệu mới giúp chuyển giao ưu điểm của IFS sang lĩnh vực video. Nó tiền huấn luyện một Identity-Anchored Video Synthesizer (IVS) điều khiển bằng tư thế, sử dụng cơ chế Adaptive Pose-Attention để đưa thông tin tư thế vào các mô hình nền tảng video First-Last-Frame. IVS sau đó được kết hợp với các mô hình IFS để xây dựng các bộ dữ liệu "bidirectional ID quadruplets" nhằm cung cấp giám sát rõ ràng trong huấn luyện. Pipeline này cũng bao gồm chiến lược thích ứng biểu cảm và cơ chế tái tạo nền để đảm bảo tính phù hợp của dữ liệu.
2.  **DreamID-V Framework:** Là framework trao đổi khuôn mặt video đầu tiên dựa trên Diffusion Transformer (DiT). Nó sử dụng module Modality-Aware Conditioning (MC) cốt lõi để đưa các điều kiện đa phương thức một cách phân biệt, cho phép tách rời điều kiện và hợp nhất tính năng.
3.  **Các Cơ chế Huấn luyện Nâng cao:** Để tăng cường tính chân thực của hình ảnh và tính nhất quán danh tính trong các kịch bản khó khăn, framework thiết kế cơ chế Synthetic-to-Real Curriculum và chiến lược Identity-Coherence Reinforcement Learning.
Ngoài ra, bài báo giới thiệu **IDBench-V**, một bộ dữ liệu đánh giá toàn diện mới bao gồm nhiều cảnh đa dạng cho nhiệm vụ trao đổi khuôn mặt video.

### Main Results:
Dựa trên đoạn trích dẫn, các kết quả chính được công bố là:
*   DreamID-V vượt trội hơn các phương pháp hiện đại (state-of-the-art) khác trong các thử nghiệm rộng rãi, cả về định lượng và định tính.
*   Framework thể hiện tính linh hoạt đặc biệt, có thể dễ dàng thích ứng với nhiều nhiệm vụ liên quan đến trao đổi khuôn mặt khác nhau.
*   IDBench-V được giới thiệu như một bộ dữ liệu đánh giá toàn diện, phục vụ cho việc đánh giá các phương pháp VFS trong các điều kiện đa dạng.

### Conclusion & Future Works:
Bài nghiên cứu đã phát triển một framework toàn diện, bao gồm một pipeline dữ liệu mới (SyncID-Pipe), một kiến trúc mô hình đột phá (DreamID-V dựa trên DiT) và một bộ dữ liệu đánh giá mới (IDBench-V), để giải quyết những thách thức cố hữu trong Video Face Swapping. DreamID-V đã chứng minh hiệu suất tạo video vượt trội so với các phương pháp hiện đại và thể hiện tính linh hoạt đáng kể, có khả năng thích ứng linh hoạt với các nhiệm vụ liên quan đến trao đổi khuôn mặt khác. Đoạn trích dẫn không đi sâu vào các công việc tương lai cụ thể, nhưng framework đã đặt nền móng vững chắc cho việc phát triển VFS chất lượng cao hơn và mở ra nhiều hướng nghiên cứu tiềm năng.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.01425](https://huggingface.co/papers/2601.01425) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.01425](https://arxiv.org/abs/2601.01425) |
| PDF Download | [https://arxiv.org/pdf/2601.01425.pdf](https://arxiv.org/pdf/2601.01425.pdf) |
| Github Repository | [https://github.com/bytedance/DreamID-V](https://github.com/bytedance/DreamID-V) |

--- 

## 5. VAR RL Done Right: Tackling Asynchronous Policy Conflicts in Visual Autoregressive Generation

**Tác giả:** Shikun Sun, Liao Qu, Huichao Zhang, Yiheng Liu, Yangyang Song, Xian Li, Xu Wang, Yi Jiang, Daniel K. Du, Xinglong Wu, Jia Jia

**Xuất bản lúc:** 2026-01-05

### Main Problem:
Vấn đề cốt lõi mà bài báo đề cập là "xung đột chính sách không đồng bộ" (asynchronous policy conflicts) trong các mô hình Visual Autoregressive (VAR) khi được tối ưu hóa bằng Học Tăng Cường (RL). Các mô hình VAR hoạt động với cấu trúc đầu vào không đồng nhất (lưới token rời rạc với hình dạng không gian thay đổi và số lượng token truy vấn biến động) qua các bước tạo ảnh khác nhau. Sự không đồng nhất này dẫn đến quá trình huấn luyện RL không ổn định, hội tụ chậm và căn chỉnh dưới mức tối ưu, đặc biệt khi áp dụng các phương pháp như Group Relative Policy Optimization (GRPO) trực tiếp vào các mô hình VAR chuyển đổi văn bản thành hình ảnh.

### Main Idea:
Bài nghiên cứu đề xuất một framework mới để tăng cường Group Relative Policy Optimization (GRPO) nhằm giải quyết một cách rõ ràng các xung đột chính sách không đồng bộ trong mô hình VAR. Framework này tích hợp ba thành phần hiệp đồng:
1.  **Value as Middle Return (VMR):** Một phần thưởng trung gian ổn định được thiết kế để hướng dẫn quá trình tạo ảnh ở giai đoạn đầu, cung cấp phản hồi dày đặc, độ biến thiên thấp và đảm bảo tính tối ưu của tập hợp chính sách. Nó phân tách mục tiêu RL toàn chuỗi thành một bài toán tối ưu hóa hai giai đoạn, giảm thiểu xung đột giữa các bước.
2.  **Per-Action Normalization Weighting (PANW):** Một lược đồ điều chỉnh trọng số động theo bước thời gian để phân bổ tín dụng chính xác. Nó chuẩn hóa đóng góp của mỗi bước bằng số lượng token truy vấn, giúp cân bằng gradient trên các tỷ lệ khác nhau và cải thiện sự ổn định.
3.  **Mask Propagation (MP):** Một thuật toán lan truyền mask mới, lấy cảm hứng từ nguyên tắc Reward Feedback Learning (ReFL), được thiết kế để cô lập hiệu ứng tối ưu hóa cả về mặt không gian và thời gian đối với các token có trách nhiệm chính tạo ra phần thưởng cuối cùng.

### Main Results:
Các phát hiện chính cho thấy framework được đề xuất đã cải thiện đáng kể chất lượng mẫu và độ phù hợp với mục tiêu so với baseline GRPO thông thường. Cụ thể, phương pháp này:
-   Thể hiện sự ổn định vượt trội trong quá trình huấn luyện và tăng tốc độ hội tụ so với GRPO vanilla.
-   Đạt được những cải thiện đáng kể về chất lượng mẫu và độ phù hợp với mục tiêu trên các benchmark hiển thị văn bản.
-   Đạt được kết quả vượt trội so với điểm khởi đầu TokenFlow-T2I và đạt được kết quả tiên tiến (state-of-the-art) so với các baseline tập trung vào diffusion.
-   Bài nghiên cứu cung cấp chẩn đoán và hình thức hóa các xung đột chính sách không đồng bộ trong RL cho VAR, chứng minh vai trò quan trọng của VMR, PANW và MP trong việc cân bằng gradient và tăng cường phân bổ tín dụng theo không gian-thời gian.

### Conclusion & Future Works:
Bài nghiên cứu kết luận rằng việc cấu trúc đúng đắn mục tiêu Học Tăng Cường và cân bằng các cập nhật trên các bước không đồng nhất là rất quan trọng để đạt được sự căn chỉnh đáng tin cậy giữa văn bản và hình ảnh trong các mô hình Visual Autoregressive. Mặc dù văn bản được trích dẫn không đề cập rõ ràng đến các hướng nghiên cứu trong tương lai, bài báo đã thiết lập một framework RL hệ thống đầu tiên cho VAR chuyển đổi văn bản thành hình ảnh, nhấn mạnh rằng việc sử dụng RL trong các mô hình AR dự đoán theo thang đo tiếp theo vẫn còn là một lĩnh vực ít được khám phá, đặc biệt là việc giải quyết các thách thức cấu trúc cốt lõi do việc tạo token song song đa tỷ lệ gây ra.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.02256](https://huggingface.co/papers/2601.02256) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.02256](https://arxiv.org/abs/2601.02256) |
| PDF Download | [https://arxiv.org/pdf/2601.02256.pdf](https://arxiv.org/pdf/2601.02256.pdf) |
| Github Repository | N/A |

--- 

## 6. GARDO: Reinforcing Diffusion Models without Reward Hacking

**Tác giả:** Haoran He, Yuxiao Ye, Jie Liu, Jiajun Liang, Zhiyong Wang, Ziyang Yuan, Xintao Wang, Hangyu Mao, Pengfei Wan, Ling Pan

**Xuất bản lúc:** 2025-12-30

### Main Problem:
Vấn đề cốt lõi là hiện tượng "reward hacking" (hack phần thưởng) khi tinh chỉnh các mô hình khuếch tán (diffusion models) thông qua học tăng cường (RL) trực tuyến. Điều này phát sinh do việc sử dụng phần thưởng proxy (proxy reward) không hoàn hảo, chỉ phản ánh một phần mục tiêu thực sự, dẫn đến việc các mô hình tối ưu hóa điểm số proxy nhưng chất lượng hình ảnh thực tế suy giảm và sự đa dạng trong tạo mẫu bị mất. Các giải pháp hiện có sử dụng KL regularization để ngăn chặn "reward hacking" lại làm giảm hiệu quả lấy mẫu và cản trở khả năng khám phá các vùng có phần thưởng cao mới.

### Main Idea:
Bài nghiên cứu đề xuất một khuôn khổ đa năng mang tên GARDO (Gated and Adaptive Regularization with Diversity-aware Optimization) để giải quyết các yêu cầu cạnh tranh về hiệu quả lấy mẫu, khám phá và giảm thiểu "reward hacking". Các ý tưởng chính của GARDO bao gồm:
1.  **Gated Regularization (Điều hòa có cổng):** Không áp dụng điều hòa phổ biến cho tất cả các mẫu, mà chỉ chọn lọc xử phạt một tập hợp con các mẫu có độ không chắc chắn cao về phần thưởng. Độ không chắc chắn này được định lượng bằng sự không đồng nhất giữa một tập hợp các hàm phần thưởng.
2.  **Adaptive Regularization (Điều hòa thích ứng):** Cơ chế điều hòa thích ứng, trong đó mô hình tham chiếu được cập nhật định kỳ để phù hợp với khả năng của chính sách trực tuyến, đảm bảo mục tiêu điều hòa luôn phù hợp và hỗ trợ khám phá liên tục.
3.  **Diversity-aware Optimization (Tối ưu hóa nhận biết đa dạng):** Khuếch đại phần thưởng cho các mẫu chất lượng cao đồng thời thể hiện sự đa dạng cao, khuyến khích bao phủ các chế độ (mode coverage) mà không làm mất ổn định quá trình tối ưu hóa.

### Main Results:
Các thử nghiệm rộng rãi trên nhiều phần thưởng proxy khác nhau và các chỉ số đo lường chưa từng thấy (hold-out unseen metrics) cho thấy GARDO:
*   Giảm thiểu thành công hiện tượng "reward hacking".
*   Nâng cao tính đa dạng trong việc tạo ra mẫu.
*   Không làm giảm hiệu quả lấy mẫu (sample efficiency).
*   Không cản trở khả năng khám phá (exploration).
Điều này làm nổi bật tính hiệu quả và mạnh mẽ của phương pháp.

### Conclusion & Future Works:
Bài nghiên cứu kết luận rằng GARDO là một phương pháp hiệu quả và mạnh mẽ, có khả năng cân bằng thành công giữa các yêu cầu cạnh tranh về hiệu quả lấy mẫu, khám phá, đa dạng, đồng thời giảm thiểu "reward hacking" trong quá trình tinh chỉnh các mô hình tạo ảnh. (Đoạn văn trích dẫn không đề cập rõ ràng đến các hướng nghiên cứu trong tương lai).

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2512.24138](https://huggingface.co/papers/2512.24138) |
| ArXiv Abstract | [https://arxiv.org/abs/2512.24138](https://arxiv.org/abs/2512.24138) |
| PDF Download | [https://arxiv.org/pdf/2512.24138.pdf](https://arxiv.org/pdf/2512.24138.pdf) |
| Github Repository | [https://github.com/tinnerhrhe/GARDO](https://github.com/tinnerhrhe/GARDO) |

--- 

## 7. VINO: A Unified Visual Generator with Interleaved OmniModal Context

**Tác giả:** Junyi Chen, Tong He, Zhoujie Fu, Pengfei Wan, Kun Gai, Weicai Ye

**Xuất bản lúc:** 2026-01-05

### Main Problem:
Các pipeline tạo hình ảnh và video hiện tại bị phân mảnh, đòi hỏi các mô hình riêng biệt cho từng nhiệm vụ như tạo từ văn bản sang hình ảnh, từ văn bản sang video và chỉnh sửa hình ảnh. Mặc dù các mô hình ngôn ngữ lớn đa phương thức (multimodal LLMs) cung cấp khả năng nhận thức hợp nhất, chúng vẫn dựa vào các mô hình khuếch tán hoặc bộ giải mã bên ngoài để tạo hình ảnh độ phân giải cao. Ngoài ra, các mô hình hiện tại gặp khó khăn trong việc xử lý đồng thời các tín hiệu đa phương thức khác nhau, dẫn đến xung đột ngữ nghĩa hoặc điều kiện không nhất quán, đặc biệt khi có sự khác biệt giữa các lệnh mô tả phong phú và các hướng dẫn chỉnh sửa ngắn gọn.

### Main Idea:
VINO đề xuất một trình tạo hình ảnh hợp nhất có khả năng tạo và chỉnh sửa hình ảnh và video trong một khuôn khổ duy nhất bằng cách sử dụng một backbone khuếch tán chia sẻ được điều kiện hóa bởi văn bản, hình ảnh và video. Nó kết hợp một mô hình ngôn ngữ-thị giác (VLM) với một Bộ biến đổi khuếch tán đa phương thức (MMDiT), nơi các đầu vào đa phương thức được mã hóa thành các token điều kiện xen kẽ và sau đó được sử dụng để hướng dẫn quá trình khuếch tán. Kiến trúc này bao gồm các token truy vấn có thể học được tại đầu vào VLM để cải thiện khả năng điều kiện và ổn định, cùng với cơ chế đánh dấu ranh giới token để liên kết nhất quán các biểu diễn ngữ nghĩa (VLM) và tiềm ẩn (VAE) của các tham chiếu trực quan. Một chiến lược huấn luyện đa giai đoạn cũng được giới thiệu để dần dần mở rộng một mô hình tạo video cơ bản thành một trình tạo đa tác vụ có khả năng xử lý cả đầu vào và đầu ra hình ảnh và video.

### Main Results:
VINO thể hiện chất lượng hình ảnh mạnh mẽ, tuân thủ hướng dẫn một cách trung thực, cải thiện khả năng bảo toàn tham chiếu và thuộc tính, và cho phép chỉnh sửa đa danh tính dễ kiểm soát hơn. Các cơ chế đề xuất giúp cải thiện khả năng điều kiện đa phương thức, ổn định quá trình tối ưu hóa và giảm thiểu việc hoán đổi danh tính cũng như rò rỉ thuộc tính trong các cảnh tham chiếu đa phương thức phức tạp. Mô hình cung cấp một con đường khả thi hơn để tạo hình ảnh hợp nhất và có khả năng mở rộng so với các pipeline khuếch tán chuyên biệt hiện có.

### Conclusion & Future Works:
Bài báo trình bày VINO như một khuôn khổ khả thi cho việc tạo hình ảnh hợp nhất và có khả năng mở rộng. Nó nhấn mạnh tiềm năng của tính toán xen kẽ, trong ngữ cảnh như một nền tảng cho việc tạo hình ảnh đa mục đích, gợi mở hướng phát triển cho các hệ thống tạo hình ảnh tổng quát hơn trong tương lai.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.02358](https://huggingface.co/papers/2601.02358) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.02358](https://arxiv.org/abs/2601.02358) |
| PDF Download | [https://arxiv.org/pdf/2601.02358.pdf](https://arxiv.org/pdf/2601.02358.pdf) |
| Github Repository | [https://github.com/SOTAMak1r/VINO-code](https://github.com/SOTAMak1r/VINO-code) |

--- 

## 8. InfiniteVGGT: Visual Geometry Grounded Transformer for Endless Streams

**Tác giả:** Shuai Yuan, Yantai Yang, Xiaotian Yang, Xupeng Zhang, Zhonghao Zhao, Lingming Zhang, Zhipeng Zhang

**Xuất bản lúc:** 2026-01-05

### Main Problem:
Vấn đề cốt lõi là sự khó khăn trong việc đạt được khả năng hiểu hình học 3D trực quan quy mô lớn, liên tục cho các luồng dữ liệu vô tận. Các mô hình ngoại tuyến hiện có, như VGGT, không phù hợp cho các hệ thống trực tiếp do tính chất xử lý theo lô và yêu cầu bộ nhớ GPU lớn. Các kiến trúc trực tuyến, dù được thiết kế cho hoạt động thời gian thực, lại gặp phải vấn đề tích lũy bộ nhớ KV không giới hạn, dẫn đến chi phí tính toán và bộ nhớ cao không bền vững, hoặc nén trạng thái ngầm định làm mất thông tin quan trọng và gây ra hiện tượng trôi dạt dữ liệu thảm khốc qua các chuỗi dài. Một thách thức lớn nữa là sự dư thừa token cấp độ cao trong bộ nhớ KV của các quỹ đạo camera liên tục, khiến kích thước bộ nhớ tăng nhanh. Các phương pháp cắt tỉa truyền thống không thể áp dụng được với các kernel tối ưu hóa như FlashAttention vì chúng dựa vào việc truy cập trọng số chú ý, điều mà các kernel này bỏ qua để đạt tốc độ.

### Main Idea:
InfiniteVGGT đề xuất một kiến trúc transformer hình học trực quan nhân quả mới với khái niệm "bộ nhớ cuộn". Giải pháp này sử dụng bộ nhớ KV có giới hạn nhưng thích ứng và luôn thể hiện tốt. InfiniteVGGT áp dụng một chiến lược cắt tỉa không cần huấn luyện và không phụ thuộc vào cơ chế chú ý, dựa trên độ tương đồng cosine của khóa làm tiêu chí quan trọng của token, để loại bỏ thông tin lỗi thời và dư thừa một cách thông minh, từ đó "cuộn" bộ nhớ về phía trước với mỗi khung hình mới. Phương pháp này hoàn toàn tương thích với FlashAttention. Bộ nhớ cuộn này hoạt động bằng cách liên tục và động làm mới nội dung thông qua một chiến lược duy trì đa cấp, tập trung vào việc bảo toàn các token riêng lẻ thay vì xóa toàn bộ khung hình, và được quản lý bởi một ngân sách token động, phân bổ theo từng lớp kiến trúc, đảm bảo dấu chân bộ nhớ GPU bị giới hạn. Nghiên cứu cũng giới thiệu benchmark Long3D để đánh giá nghiêm ngặt khả năng ước tính hình học 3D liên tục trên các chuỗi dài đến khoảng 10.000 khung hình.

### Main Results:
InfiniteVGGT đạt được hiệu suất vượt trội so với các phương pháp streaming hiện có về độ ổn định dài hạn. Nó cho phép streaming với chân trời vô hạn đồng thời thực hiện tái tạo mạnh mẽ, vô hạn mà không gặp phải tình trạng tràn bộ nhớ. Nghiên cứu đã chứng minh khả năng độc đáo này trên các benchmark chuỗi dài. Ngoài ra, việc giới thiệu benchmark Long3D đã cung cấp một nền tảng đánh giá định nghĩa cho nghiên cứu tương lai về hiểu và tái tạo hình học 3D dài hạn, lấp đầy một khoảng trống quan trọng trong lĩnh vực này. Benchmark này lần đầu tiên cho phép đánh giá nghiêm ngặt ước tính hình học 3D liên tục trên các chuỗi khoảng 10.000 khung hình.

### Conclusion & Future Works:
Nghiên cứu này giới thiệu InfiniteVGGT, một kiến trúc bộ nhớ vô hạn cho việc hiểu hình học 3D liên tục, được xây dựng trên một hệ thống bộ nhớ tường minh, động và có thể giải thích được. InfiniteVGGT đạt được hiệu suất tiên tiến trên các benchmark chuỗi dài và có khả năng độc đáo là tái tạo mạnh mẽ, vô hạn mà không bị tràn bộ nhớ. Cuối cùng, benchmark Long3D mới được giới thiệu nhằm mục đích đánh giá nghiêm ngặt hiệu suất dài hạn, cung cấp một nền tảng đánh giá cuối cùng cho nghiên cứu tương lai trong lĩnh vực hiểu hình học 3D dài hạn.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.02281](https://huggingface.co/papers/2601.02281) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.02281](https://arxiv.org/abs/2601.02281) |
| PDF Download | [https://arxiv.org/pdf/2601.02281.pdf](https://arxiv.org/pdf/2601.02281.pdf) |
| Github Repository | [https://github.com/AutoLab-SAI-SJTU/InfiniteVGGT](https://github.com/AutoLab-SAI-SJTU/InfiniteVGGT) |

--- 

## 9. Recursive Language Models

**Tác giả:** Alex L. Zhang, Tim Kraska, Omar Khattab

**Xuất bản lúc:** 2025-12-31

### Main Problem:
Các mô hình ngôn ngữ lớn (LLMs) hiện đại có giới hạn về độ dài ngữ cảnh và chất lượng suy giảm đáng kể khi ngữ cảnh dài hơn ("context rot"), ngay cả trong giới hạn cho phép của chúng. Điều này gây khó khăn cho việc xử lý các nhắc nhở (prompts) dài tùy ý, đặc biệt là trong các tác vụ yêu cầu hàng triệu token. Các phương pháp hiện có như tóm tắt (compaction) thường không đủ biểu cảm và bỏ qua các chi tiết quan trọng.

### Main Idea:
Bài báo đề xuất Mô hình ngôn ngữ đệ quy (Recursive Language Models - RLMs) như một chiến lược suy luận tổng quát để mở rộng đáng kể độ dài ngữ cảnh hiệu quả của LLMs. Ý tưởng chính là coi các nhắc nhở dài như một phần của "môi trường bên ngoài" mà LLM có thể tương tác một cách tượng trưng, thay vì nạp trực tiếp vào mạng lưới thần kinh. RLMs khởi tạo một môi trường lập trình REPL (Read-Eval-Print Loop) nơi prompt được đặt làm giá trị của một biến. LLM sau đó có thể viết mã để kiểm tra, phân tách nhắc nhở, quan sát các hiệu ứng phụ từ việc thực thi mã và tự gọi lại một cách đệ quy trên các đoạn mã con.

### Main Results:
RLMs thành công trong việc xử lý các đầu vào có độ dài lớn hơn đến hai bậc so với cửa sổ ngữ cảnh của mô hình cơ sở (lên đến hơn 10 triệu token).
- So với các LLM cơ sở và các phương pháp xử lý ngữ cảnh dài thông thường (tóm tắt, tác nhân công cụ truy xuất, tác nhân tạo mã), RLMs vượt trội về chất lượng trên bốn tác vụ ngữ cảnh dài đa dạng, bao gồm Deep Research, Information Aggregation, Code Repository Understanding và một tác vụ suy luận cặp tổng hợp.
- RLMs duy trì hiệu suất mạnh mẽ với sự suy giảm ít nghiêm trọng hơn đáng kể khi độ dài đầu vào và độ phức tạp tác vụ tăng lên (như minh họa trên S-NIAH, OOLONG và OOLONG-Pairs).
- Chi phí cho mỗi truy vấn của RLMs tương đương hoặc thậm chí rẻ hơn so với các phương pháp khác. Ví dụ, trên BrowseComp-Plus (1K), RLM (GPT-5) có chi phí trung bình là 0.99 USD và vượt trội hơn các đường cơ sở tóm tắt và truy xuất hơn 29%.

### Conclusion & Future Works:
RLMs cung cấp một giải pháp hiệu quả và có thể mở rộng để LLMs xử lý các ngữ cảnh cực dài, vượt qua các giới hạn của cửa sổ ngữ cảnh truyền thống và hiệu suất kém dần ("context rot"). Phương pháp này mang lại hiệu suất vượt trội và chi phí cạnh tranh. Văn bản trích dẫn không đề cập rõ ràng đến các hướng nghiên cứu trong tương lai.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2512.24601](https://huggingface.co/papers/2512.24601) |
| ArXiv Abstract | [https://arxiv.org/abs/2512.24601](https://arxiv.org/abs/2512.24601) |
| PDF Download | [https://arxiv.org/pdf/2512.24601.pdf](https://arxiv.org/pdf/2512.24601.pdf) |
| Github Repository | [https://github.com/alexzhang13/rlm/tree/main](https://github.com/alexzhang13/rlm/tree/main) |

--- 

## 10. Falcon-H1R: Pushing the Reasoning Frontiers with a Hybrid Model for Efficient Test-Time Scaling

**Tác giả:** Falcon LLM Team, Iheb Chaabane, Puneesh Khanna, Suhail Mohmad, Slim Frikha, Shi Hu, Abdalgader Abubaker, Reda Alami, Mikhail Lubinets, Mohamed El Amine Seddik, Hakim Hacid

**Xuất bản lúc:** 2026-01-05

### Main Problem:
Các mô hình ngôn ngữ lớn (LLM) gặp khó khăn trong việc cân bằng hiệu suất suy luận cao với chi phí suy luận (inference cost) thấp, đặc biệt khi áp dụng các phương pháp Test-Time Scaling (TTS) vốn tốn kém tài nguyên. Vấn đề cốt lõi là làm thế nào để đạt được khả năng suy luận cạnh tranh với các mô hình ngôn ngữ nhỏ (SLM) mà vẫn đảm bảo hiệu quả về chi phí và tài nguyên.

### Main Idea:
Bài nghiên cứu giới thiệu Falcon-H1R, một mô hình 7B tham số được tối ưu hóa cho suy luận, sử dụng kiến trúc lai Transformer-Mamba để đạt hiệu suất suy luận cạnh tranh với các mô hình lớn hơn. Mô hình này được huấn luyện thông qua Supervised Fine-Tuning (SFT) trên dữ liệu được tuyển chọn kỹ lưỡng và Reinforcement Learning (RL) với phương pháp GRPO. Falcon-H1R được thiết kế để nâng cao hiệu quả Test-Time Scaling (TTS) bằng cách kết hợp suy luận nhanh, hiệu quả token và độ chính xác cao, đặc biệt khi tích hợp phương pháp DeepConf để tối ưu hóa việc tạo chuỗi suy luận song song và dừng sớm.

### Main Results:
Falcon-H1R-7B đạt hiệu suất suy luận vượt trội hoặc ngang bằng các mô hình SOTA lớn hơn từ 2 đến 7 lần, thể hiện hiệu quả tham số cao. Mô hình đạt độ chính xác mạnh mẽ trên nhiều bộ benchmark suy luận, bao gồm 88.1% trên AIME24, 83.1% trên AIME25, 64.9% trên HMMT25, 36.3% trên AMO-Bench và 68.6% trên LiveCodeBenchv6, cạnh tranh với các mô hình SOTA lớn hơn như GPT-OSS-20B và Qwen3-32B. Khi áp dụng Test-Time Scaling với DeepConf, Falcon-H1R-7B cải thiện đáng kể cả độ chính xác và hiệu quả chi phí. Ví dụ, trên AIME25, mô hình đạt 96.7% độ chính xác đồng thời giảm 38% số lượng token sử dụng so với DeepSeek-R1-0528-Qwen3-8B. Điều này đến từ việc tối ưu hóa đồng thời độ chính xác cao, hiệu quả token và tốc độ suy luận trong môi trường tư duy song song.

### Conclusion & Future Works:
Falcon-H1R chứng minh rằng các mô hình nhỏ gọn, thông qua các lựa chọn kiến trúc lai mục tiêu và chiến lược huấn luyện cẩn thận (bao gồm SFT và RL), có thể mang lại khả năng suy luận mạnh mẽ, có thể mở rộng và hiệu quả về mặt chi phí. Mô hình này được coi là một nền tảng hiệu quả cho các tác vụ suy luận đòi hỏi cả độ chính xác cao và khả năng mở rộng, đặc biệt trong các kịch bản cần tạo ra chuỗi suy luận dài và Test-Time Scaling song song.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.02346](https://huggingface.co/papers/2601.02346) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.02346](https://arxiv.org/abs/2601.02346) |
| PDF Download | [https://arxiv.org/pdf/2601.02346.pdf](https://arxiv.org/pdf/2601.02346.pdf) |
| Github Repository | N/A |

--- 

## 11. SimpleMem: Efficient Lifelong Memory for LLM Agents

**Tác giả:** Jiaqi Liu, Yaofeng Su, Peng Xia, Siwei Han, Zeyu Zheng, Cihang Xie, Mingyu Ding, Huaxiu Yao

**Xuất bản lúc:** 2026-01-05

### Main Problem:
Các tác nhân LLM hiện tại gặp khó khăn trong tương tác dài hạn do giới hạn cửa sổ ngữ cảnh và hệ thống bộ nhớ không hiệu quả, dẫn đến sự dư thừa thông tin đáng kể và chi phí token cao. Các phương pháp hiện có hoặc lưu trữ toàn bộ lịch sử tương tác, gây ra tình trạng "phồng ngữ cảnh" và suy giảm hiệu suất, hoặc dựa vào suy luận lặp lại để lọc nhiễu, nhưng lại tốn kém về mặt tính toán và token. Vấn đề cốt lõi là hiệu quả truy xuất kém và sử dụng token thấp.

### Main Idea:
Bài nghiên cứu giới thiệu SimpleMem, một khuôn khổ bộ nhớ hiệu quả cho các tác nhân LLM dựa trên nén ngữ nghĩa không mất mát. SimpleMem giải quyết vấn đề bằng một quy trình ba giai đoạn:
1.  **Semantic Structured Compression**: Áp dụng cơ chế lọc nhận biết entropy để chắt lọc các tương tác phi cấu trúc thành các đơn vị bộ nhớ nén, được lập chỉ mục đa chiều (nhúng ngữ nghĩa dày đặc, đặc điểm từ vựng thưa thớt và siêu dữ liệu ký hiệu).
2.  **Recursive Memory Consolidation**: Một quá trình không đồng bộ tích hợp các đơn vị liên quan vào các biểu diễn trừu tượng cấp cao hơn để giảm sự dư thừa và duy trì cấu trúc bộ nhớ nhỏ gọn, lấy cảm hứng từ sự củng cố bộ nhớ sinh học.
3.  **Adaptive Query-Aware Retrieval**: Điều chỉnh động phạm vi truy xuất dựa trên độ phức tạp của truy vấn để xây dựng ngữ cảnh chính xác và hiệu quả token cho quá trình suy luận tiếp theo.

### Main Results:
SimpleMem thể hiện hiệu suất vượt trội so với các phương pháp cơ sở:
*   Đạt được cải thiện F1 trung bình 26.4% so với các phương pháp cơ sở như Mem0.
*   Giảm mức tiêu thụ token thời gian suy luận tới 30 lần so với các mô hình ngữ cảnh đầy đủ.
*   Thể hiện sự cân bằng vượt trội giữa hiệu suất và hiệu quả, đạt độ chính xác cao với mức tiêu thụ token tối thiểu (khoảng 550 token).
*   Vượt trội hơn các phương pháp hiện có về độ chính xác, hiệu quả truy xuất và chi phí suy luận.

### Conclusion & Future Works:
SimpleMem thiết lập một tiêu chuẩn mới về hiệu quả bộ nhớ cho các tác nhân LLM thông qua nén ngữ nghĩa có cấu trúc, tổ chức bộ nhớ nguyên tắc, củng cố và truy xuất thích ứng. Khung này cải thiện đáng kể hiệu quả thông tin dưới ngân sách ngữ cảnh và token cố định. Văn bản trích dẫn không đề cập cụ thể đến các hướng nghiên cứu trong tương lai.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.02553](https://huggingface.co/papers/2601.02553) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.02553](https://arxiv.org/abs/2601.02553) |
| PDF Download | [https://arxiv.org/pdf/2601.02553.pdf](https://arxiv.org/pdf/2601.02553.pdf) |
| Github Repository | [https://github.com/aiming-lab/SimpleMem](https://github.com/aiming-lab/SimpleMem) |

--- 

## 12. Talk2Move: Reinforcement Learning for Text-Instructed Object-Level Geometric Transformation in Scenes

**Tác giả:** Jing Tan, Zhaoyang Zhang, Yantao Shen, Jiarui Cai, Shuo Yang, Jiajun Wu, Wei Xia, Zhuowen Tu, Stefano Soatto

**Xuất bản lúc:** 2026-01-05

### Main Problem:
Vấn đề cốt lõi mà bài báo đề cập là việc khó khăn trong thao tác không gian đối tượng trong các cảnh ảnh bằng ngôn ngữ tự nhiên. Các hệ thống tạo đa phương thức hiện có, đặc biệt là các phương pháp chỉnh sửa dựa trên văn bản, gặp khó khăn trong việc thực hiện các phép biến đổi hình học ở cấp độ đối tượng như dịch chuyển, xoay hoặc thay đổi kích thước. Điều này là do sự khan hiếm của dữ liệu giám sát theo cặp và giới hạn của việc tối ưu hóa cấp độ pixel, khiến việc kiểm soát không gian không chính xác và đòi hỏi sự can thiệp thủ công hoặc chuyên môn về đồ họa.

### Main Idea:
Bài báo giới thiệu TALK2MOVE, một khung làm việc dựa trên học tăng cường (RL) sử dụng mô hình khuếch tán để thực hiện các phép biến đổi không gian cấp độ đối tượng theo hướng dẫn bằng văn bản. Giải pháp này sử dụng Group Relative Policy Optimization (GRPO) để khám phá các hành động hình học thông qua các lượt triển khai đa dạng được tạo từ ảnh đầu vào và các biến thể văn bản nhẹ, loại bỏ nhu cầu về dữ liệu theo cặp tốn kém. TALK2MOVE thiết kế một mô hình phần thưởng không gian hướng đối tượng để đánh giá trực tiếp hành vi dịch chuyển, xoay và thay đổi kích thước, giúp các biến đổi dễ hiểu và nhất quán. Để tăng hiệu quả học tập, phương pháp này cũng sử dụng đánh giá bước ngoài chính sách (off-policy step evaluation) và lấy mẫu bước chủ động (active step sampling) để tập trung vào các giai đoạn biến đổi thông tin, đồng thời giới thiệu cơ chế thoát sớm để tăng tốc quá trình tạo lượt triển khai.

### Main Results:
TALK2MOVE đạt được các phép biến đổi đối tượng chính xác, nhất quán và trung thực về ngữ nghĩa. Các thử nghiệm trên các bộ dữ liệu được chọn lọc đã chứng minh rằng TALK2MOVE đạt kết quả vượt trội so với các phương pháp chỉnh sửa được hướng dẫn bằng văn bản hiện có về cả độ chính xác không gian và tính mạch lạc của cảnh. Phương pháp này hiệu quả về dữ liệu so với các phương pháp dựa trên SFT, giảm đáng kể sự phụ thuộc vào các chú thích theo cặp tốn kém và cải thiện hiệu quả đào tạo lên gấp 2 lần thông qua việc lấy mẫu bước chủ động.

### Conclusion & Future Works:
TALK2MOVE là khung làm việc dựa trên học tăng cường đầu tiên giải quyết bài toán biến đổi hình học cấp độ đối tượng được hướng dẫn bằng văn bản, cung cấp một giao diện trực quan và dễ tiếp cận cho người dùng. Mặc dù đã đạt được những kết quả vượt trội về độ chính xác không gian và tính mạch lạc, các hướng nghiên cứu trong tương lai có thể bao gồm việc mở rộng quy mô bộ dữ liệu cho các biến đổi hình học và tiếp tục cải thiện hiệu quả tính toán của quá trình đào tạo GRPO.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.02356](https://huggingface.co/papers/2601.02356) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.02356](https://arxiv.org/abs/2601.02356) |
| PDF Download | [https://arxiv.org/pdf/2601.02356.pdf](https://arxiv.org/pdf/2601.02356.pdf) |
| Github Repository | [https://github.com/sparkstj/Talk2Move](https://github.com/sparkstj/Talk2Move) |

--- 

## 13. Confidence Estimation for LLMs in Multi-turn Interactions

**Tác giả:** Caiqi Zhang, Ruihan Yang, Xiaochen Zhu, Chengzu Li, Tiancheng Hu, Yijiang River Dong, Deqing Yang, Nigel Collier

**Xuất bản lúc:** 2026-01-05

### Main Problem:
Nghiên cứu hiện tại về ước lượng độ tin cậy của các Mô hình Ngôn ngữ Lớn (LLM) chủ yếu tập trung vào các cài đặt tương tác một lượt (single-turn). Động lực của độ tin cậy của mô hình trong các cuộc hội thoại đa lượt, nơi ngữ cảnh tích lũy và sự mơ hồ dần được giải quyết, vẫn chưa được khám phá rộng rãi. Việc ước lượng độ tin cậy đáng tin cậy trong cài đặt đa lượt là rất quan trọng cho nhiều ứng dụng hạ nguồn như các tác nhân tự trị và hệ thống có sự tham gia của con người, nhưng các phương pháp hiện tại không hiệu quả trong việc theo dõi sự tiến triển này.

### Main Idea:
Bài nghiên cứu này trình bày một nghiên cứu hệ thống đầu tiên về ước lượng độ tin cậy trong các tương tác đa lượt. Công trình thiết lập một khuôn khổ đánh giá chính thức dựa trên hai tiêu chí chính: hiệu chuẩn từng lượt (per-turn calibration) và tính đơn điệu của độ tin cậy (monotonicity of confidence) khi có thêm thông tin. Để thực hiện điều này, các tác giả giới thiệu các chỉ số mới, bao gồm Lỗi hiệu chuẩn dự kiến được chuẩn hóa theo độ dài thông tin (InfoECE), và một mô hình "Hinter-Guesser" mới để tạo các bộ dữ liệu đánh giá có kiểm soát. Bài báo đề xuất P(SUFFICIENT), một phương pháp dò hỏi dựa trên logit, đánh giá độ tin cậy bằng cách hỏi liệu thông tin hiện tại có đủ để suy ra rằng một câu trả lời là duy nhất và chính xác hay không, đặc biệt hữu ích trong các tình huống câu hỏi ban đầu không rõ ràng. Các phương pháp ước lượng độ tin cậy khác được đánh giá bao gồm phương pháp verbalized (VANILLA-VERB, COT-VERB) và phương pháp self-consistency (SC).

### Main Results:
Các thử nghiệm cho thấy các kỹ thuật độ tin cậy được sử dụng rộng rãi gặp khó khăn trong việc duy trì hiệu chuẩn hoặc thể hiện tính đơn điệu nhất quán khi các cuộc hội thoại tiến triển. Phương pháp P(SUFFICIENT) được đề xuất chứng tỏ hiệu suất tốt hơn một cách tương đối về cả hiệu chuẩn và tính đơn điệu, mặc dù nhiệm vụ này vẫn còn nhiều không gian để cải thiện. Các mô hình thể hiện tính đơn điệu mạnh mẽ hơn khi độ tin cậy được đánh giá dựa trên câu trả lời đúng thực tế chứ không phải câu trả lời tạm thời của mô hình. P(SUFFICIENT) hiệu quả hơn trong việc phân biệt các thông tin tăng thêm có ý nghĩa so với các đoạn hội thoại không cung cấp giá trị thông tin. Phân tích cũng tiết lộ rằng tín hiệu độ tin cậy có hành vi rất khác nhau giữa đối thoại đa lượt và tóm tắt một lượt, nhấn mạnh tầm quan trọng của cấu trúc tương tác của đối thoại đối với việc ước lượng độ tin cậy của mô hình.

### Conclusion & Future Works:
Công trình này cung cấp một phương pháp luận nền tảng để phát triển các tác nhân hội thoại đáng tin cậy và đáng tin cậy hơn. Các phát hiện làm nổi bật rằng độ tin cậy trong tương tác đa lượt là một mục tiêu riêng biệt và cần thiết để đạt được hành vi LLM đáng tin cậy và định hướng quyết định. Mặc dù P(SUFFICIENT) cải thiện hiệu suất, nhiệm vụ ước lượng độ tin cậy trong tương tác đa lượt vẫn còn xa mới được giải quyết, gợi ý nhiều hướng nghiên cứu tiếp theo để phát triển các phương pháp hiệu quả hơn.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.02179](https://huggingface.co/papers/2601.02179) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.02179](https://arxiv.org/abs/2601.02179) |
| PDF Download | [https://arxiv.org/pdf/2601.02179.pdf](https://arxiv.org/pdf/2601.02179.pdf) |
| Github Repository | N/A |

--- 

## 14. KV-Embedding: Training-free Text Embedding via Internal KV Re-routing in Decoder-only LLMs

**Tác giả:** Yixuan Tang, Yi Yang

**Xuất bản lúc:** 2026-01-03

### Main Problem:
Vấn đề cốt lõi mà bài báo đề cập là hai thách thức cấu trúc khi sử dụng các mô hình ngôn ngữ lớn (LLM) chỉ có bộ giải mã (decoder-only LLM) làm xương sống nhúng văn bản trong môi trường không cần huấn luyện (training-free):
1.  **Sự bất đối xứng thông tin:** Cơ chế chú ý nhân quả (causal attention) hạn chế các token ở vị trí đầu truy cập vào ngữ cảnh sau đó trong chuỗi, khiến chúng không nhận thức được toàn bộ nội dung.
2.  **Thiên vị trong biểu diễn:** Mục tiêu dự đoán token tiếp theo (next-token prediction objective) khiến các biểu diễn bị thiên về tạo sinh hơn là nén ngữ nghĩa, làm giảm chất lượng nhúng.

### Main Idea:
Bài báo đề xuất KV-Embedding, một khuôn khổ không cần huấn luyện nhằm giải quyết các hạn chế trên thông qua việc định tuyến lại trạng thái KV nội bộ trong LLM:
1.  **Định tuyến lại trạng thái Key-Value (KV) nội bộ:** Phương pháp này khai thác quan sát rằng các trạng thái Key và Value (KV) của token cuối cùng ở mỗi lớp mã hóa một cái nhìn nén của chuỗi. Bằng cách định tuyến lại các trạng thái này và tiền xử lý chúng như một tiền tố nội bộ vào cơ chế chú ý, tất cả các token có thể truy cập ngữ cảnh cấp độ chuỗi trong một lần truyền tiến duy nhất.
2.  **Chiến lược lựa chọn lớp tự động:** Để đảm bảo khả năng áp dụng không phụ thuộc vào mô hình, bài báo giới thiệu một chiến lược lựa chọn lớp tự động dựa trên chiều nội tại (intrinsic dimensionality), giúp xác định các lớp tối ưu để định tuyến lại KV, nơi các biểu diễn thể hiện độ nén tối đa.
3.  **Nhắc nhở hướng nén ngữ nghĩa:** Sử dụng một template nhắc nhở đặc biệt được thiết kế để định hướng biểu diễn của token cuối cùng về phía chắt lọc bản chất ngữ nghĩa của đầu vào, từ đó giảm thiểu thiên vị dự đoán.

### Main Results:
-   **Hiệu suất vượt trội:** KV-Embedding vượt trội hơn các phương pháp không cần huấn luyện hiện có tới 10% trên bộ benchmark MTEB, sử dụng các mô hình nền tảng như Qwen, Mistral và Llama.
-   **Hiệu suất ổn định với ngữ cảnh dài:** Phương pháp duy trì hiệu suất mạnh mẽ trên các chuỗi dài tới 4.096 token trên benchmark LoCoV1, một kịch bản mà các phương pháp cơ sở thường suy giảm do sự loãng ngữ cảnh.
-   **Không gian nhúng cải thiện:** Phân tích thêm xác nhận rằng phương pháp tạo ra một không gian nhúng đẳng hướng hơn với sự liên kết và đồng nhất được cải thiện.
-   **Giải pháp hiệu quả và có thể mở rộng:** Các kết quả chứng minh rằng việc thao tác trạng thái nội bộ mang lại một giải pháp hiệu quả và có thể mở rộng để tận dụng LLM làm mô hình nhúng văn bản.

### Conclusion & Future Works:
KV-Embedding thiết lập một trạng thái nghệ thuật mới cho việc nhúng văn bản không cần huấn luyện thông qua việc định tuyến lại KV nội bộ. Khung công tác này duy trì khả năng áp dụng không phụ thuộc vào mô hình nhờ chiến lược lựa chọn lớp tự động dựa trên chiều nội tại. Các tác giả hy vọng công trình này khuyến khích khám phá sâu hơn về các cơ chế nội bộ của LLM để học biểu diễn, chứng minh rằng thao tác trạng thái nội bộ là một giải pháp thay thế hiệu quả cho việc sửa đổi đầu vào.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.01046](https://huggingface.co/papers/2601.01046) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.01046](https://arxiv.org/abs/2601.01046) |
| PDF Download | [https://arxiv.org/pdf/2601.01046.pdf](https://arxiv.org/pdf/2601.01046.pdf) |
| Github Repository | N/A |

--- 

## 15. CPPO: Contrastive Perception for Vision Language Policy Optimization

**Tác giả:** Ahmad Rezaei, Mohsen Gholami, Saeed Ranjbar Alvar, Kevin Cannons, Mohammad Asiful Hossain, Zhou Weimin, Shunbo Zhou, Yong Zhang, Mohammad Akbari

**Xuất bản lúc:** 2026-01-01

### Main Problem:
Các mô hình VLM (Vision-Language Models) thường thể hiện hiệu suất suy luận đa phương thức yếu hơn so với các mô hình ngôn ngữ thuần túy. Việc mở rộng học tăng cường (RL) sang suy luận đa phương thức đòi hỏi cải thiện cả khía cạnh nhận thức (perception) và suy luận (reasoning). Các phương pháp trước đây để giải quyết vấn đề này chủ yếu dựa vào phần thưởng nhận thức tường minh nhưng gặp khó khăn trong việc tách biệt các token nhận thức khỏi các token suy luận. Cụ thể, các thách thức bao gồm việc cần thêm các mô hình LLM, dữ liệu ground-truth, ép buộc tách biệt giữa nhận thức và suy luận trong đầu ra của mô hình, hoặc áp dụng phần thưởng một cách không chọn lọc cho tất cả các token. Những cách tiếp cận này có thể làm gián đoạn quá trình suy luận tự nhiên, tốn kém về mặt tính toán, không mở rộng được, dễ bị "reward hacking", hoặc sử dụng các hàm mất mát không ổn định (ví dụ: KL divergence không giới hạn) và áp dụng chúng không đồng đều cho tất cả các token.

### Main Idea:
CPPO (Contrastive Perception Policy Optimization) là một phương pháp tối ưu hóa chính sách dựa trên học tăng cường để tinh chỉnh các mô hình VLM. CPPO giải quyết vấn đề bằng cách phát hiện các token nhận thức thông qua sự thay đổi entropy trong các đầu ra của mô hình dưới các hình ảnh đầu vào bị nhiễu loạn. Cụ thể, các token có entropy tăng mạnh nhất dưới sự nhiễu loạn loại bỏ thông tin được xác định là token nhận thức, vì phân phối của chúng thể hiện thông tin tương hỗ cao nhất với hình ảnh. CPPO sau đó mở rộng hàm mục tiêu của RL với một hàm mất mát nhận thức tương phản (Contrastive Perception Loss - CPL). CPL yêu cầu sự nhất quán dưới các nhiễu loạn giữ thông tin và sự nhạy cảm dưới các nhiễu loạn loại bỏ thông tin. CPL là một hàm mất mát tương phản không có giám sát, không yêu cầu giám sát Chain-of-Thought (CoT) bổ sung hoặc các mô hình độc quyền. Nó được áp dụng dưới dạng hàm mất mát tương phản InfoNCE, sử dụng phân phối xác suất token với hình ảnh gốc làm neo, hình ảnh nhiễu loạn giữ thông tin làm mẫu tích cực và hình ảnh nhiễu loạn loại bỏ thông tin làm mẫu tiêu cực. Quan trọng là, CPL chỉ được áp dụng cho các token nhận thức từ các "rollout" đúng, đảm bảo rằng các neo tương ứng với các token nhận thức chính xác và đã được xác minh.

### Main Results:
- CPPO vượt trội hơn các phương pháp thưởng nhận thức trước đây.
- CPPO tránh được việc sử dụng các mô hình bổ sung, làm cho quá trình đào tạo hiệu quả và có khả năng mở rộng hơn.
- CPPO thành công trong việc tách biệt và cải thiện khả năng nhận thức và suy luận của chính sách VLM.
- CPPO giới thiệu một phương pháp phát hiện token nhận thức dựa trên entropy, cho phép chính sách VLM tự xác định các token nhận thức của mình bằng cách phân tích phân phối đầu ra của nó.
- CPPO đề xuất CPL, một hàm mất mát tương phản không giám sát, dành riêng cho nhận thức để tối ưu hóa chính sách VLM.

### Conclusion & Future Works:
Bài nghiên cứu giới thiệu CPPO như một giải pháp dựa trên học tăng cường để tinh chỉnh các mô hình VLM, cải thiện khả năng suy luận đa phương thức bằng cách cung cấp cơ chế hiệu quả để disentangle và tối ưu hóa cả nhận thức và suy luận. CPPO vượt trội so với các phương pháp trước đó nhờ khả năng tự động xác định token nhận thức và áp dụng hàm mất mát tương phản không giám sát một cách có mục tiêu, giúp việc đào tạo hiệu quả và dễ mở rộng. Mặc dù văn bản trích dẫn không đề cập rõ ràng đến các công trình tương lai, phương pháp được đề xuất về hàm mất mát tương phản cấp token được áp dụng cụ thể cho các token phụ thuộc vào thị giác mở ra một hướng nghiên cứu mới trong việc tối ưu hóa chính sách VLM.

### Overview Figure

![Overview Figure](papers\2026-01-06\2601.00501_overview.png)

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.00501](https://huggingface.co/papers/2601.00501) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.00501](https://arxiv.org/abs/2601.00501) |
| PDF Download | [https://arxiv.org/pdf/2601.00501.pdf](https://arxiv.org/pdf/2601.00501.pdf) |
| Github Repository | N/A |

--- 

## 16. DiffProxy: Multi-View Human Mesh Recovery via Diffusion-Generated Dense Proxies

**Tác giả:** Renke Wang, Zhenyu Zhang, Ying Tai, Jian Yang

**Xuất bản lúc:** 2026-01-05

### Main Problem:
Vấn đề chính trong việc phục hồi lưới người từ nhiều góc nhìn là các bộ dữ liệu thế giới thực chứa các chú thích ground-truth không hoàn hảo, gây sai lệch cho quá trình huấn luyện mô hình. Ngược lại, dữ liệu tổng hợp mặc dù có sự giám sát chính xác nhưng lại phải đối mặt với khoảng cách miền (domain gap) đáng kể so với dữ liệu thực. Sự khan hiếm dữ liệu đa góc nhìn được chú thích còn làm trầm trọng thêm vấn đề tổng quát hóa giữa các bộ dữ liệu. Các phương pháp hiện có dựa trên dữ liệu tổng hợp thường sử dụng kỹ thuật ngẫu nhiên hóa miền (domain randomization) nhưng vẫn khó khắc phục hoàn toàn khoảng cách miền, đặc biệt đối với các phương pháp hồi quy trực tiếp.

### Main Idea:
Bài nghiên cứu đề xuất DiffProxy, một framework mới lạ để tạo ra các "proxy" người nhất quán từ nhiều góc nhìn cho việc phục hồi lưới. Giải pháp cốt lõi của DiffProxy là tận dụng các ưu tiên tạo sinh dựa trên mô hình khuếch tán (diffusion-based generative priors) để bắc cầu giữa việc huấn luyện trên dữ liệu tổng hợp và khả năng tổng quát hóa trong thế giới thực. Các đổi mới chính bao gồm:
1.  Một cơ chế đa điều kiện (multi-conditional mechanism) để tạo ra các proxy người nhất quán từ nhiều góc nhìn và được căn chỉnh từng pixel.
2.  Một module tinh chỉnh bàn tay (hand refinement module) tích hợp các gợi ý trực quan linh hoạt để nâng cao chi tiết cục bộ, đặc biệt ở cấp độ ngón tay.
3.  Một phương pháp nhân tỷ lệ trong thời gian kiểm tra nhận biết độ không chắc chắn (uncertainty-aware test-time scaling) để tăng cường sự mạnh mẽ cho các trường hợp thách thức trong quá trình tối ưu hóa.
Framework được huấn luyện độc quyền trên dữ liệu tổng hợp quy mô lớn và hoạt động theo hai giai đoạn: (i) Tạo Proxy người, tạo ra các tương ứng mật độ pixel-to-surface; (ii) Phục hồi lưới người, bằng cách khớp mô hình SMPL-X với các proxy này thông qua tối ưu hóa tái chiếu. Mô hình khuếch tán cũng cho phép ước tính độ không chắc chắn trên từng pixel để điều chỉnh trọng số tối ưu hóa.

### Main Results:
DiffProxy, được huấn luyện hoàn toàn trên dữ liệu tổng hợp và không yêu cầu bất kỳ cặp chú thích hình ảnh-lưới thực nào, đạt được hiệu suất hiện đại (state-of-the-art) trên năm bộ benchmark thế giới thực. Phương pháp này thể hiện khả năng tổng quát hóa zero-shot mạnh mẽ, đặc biệt trong các kịch bản thách thức với sự che khuất (occlusions) và các góc nhìn một phần (partial views).

### Conclusion & Future Works:
DiffProxy là một phương pháp tiên phong tận dụng các mô hình khuếch tán được huấn luyện trước để tạo ra các tương ứng mật độ nhất quán từ nhiều góc nhìn, từ đó giải quyết các thách thức về chú thích sai lệch và khoảng cách miền trong phục hồi lưới người. Bằng cách huấn luyện độc quyền trên dữ liệu tổng hợp quy mô lớn, DiffProxy đạt được khả năng tổng quát hóa mạnh mẽ và hiệu suất vượt trội trên các bộ dữ liệu thực tế mà không cần huấn luyện trên dữ liệu thực. (Không có thông tin cụ thể về các hướng nghiên cứu tiếp theo trong đoạn trích này).

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.02267](https://huggingface.co/papers/2601.02267) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.02267](https://arxiv.org/abs/2601.02267) |
| PDF Download | [https://arxiv.org/pdf/2601.02267.pdf](https://arxiv.org/pdf/2601.02267.pdf) |
| Github Repository | [https://github.com/wrk226/DiffProxy](https://github.com/wrk226/DiffProxy) |

--- 

## 17. COMPASS: A Framework for Evaluating Organization-Specific Policy Alignment in LLMs

**Tác giả:** Dasol Choi, DongGeon Lee, Brigitta Jesica Kartono, Helena Berndt, Taeyoun Kwon, Joonwon Jang, Haon Park, Hwanjo Yu, Minsuk Kahng

**Xuất bản lúc:** 2026-01-05

### Main Problem:
1.  Các mô hình ngôn ngữ lớn (LLM) đang được triển khai trong các ứng dụng doanh nghiệp quan trọng (như y tế, tài chính), nơi việc tuân thủ các chính sách cụ thể của tổ chức là vô cùng cần thiết.
2.  Các đánh giá an toàn hiện có chỉ tập trung vào các mối nguy hại chung (như độc hại, bạo lực, phát ngôn thù địch) và không có các giao thức đánh giá tiêu chuẩn cho việc tuân thủ chính sách đặc thù của từng tổ chức.
3.  Điều này tạo ra một lỗ hổng trong việc đảm bảo LLM tuân thủ các quy tắc "allowlist" (được phép) và "denylist" (bị cấm) do tổ chức định nghĩa, dẫn đến rủi ro về thông tin sai lệch, vi phạm quy định và tổn hại cho người dùng.

### Main Idea:
1.  Đề xuất COMPASS (Company/Organization Policy Alignment Assessment), một khuôn khổ có hệ thống và có khả năng mở rộng đầu tiên để đánh giá sự tuân thủ chính sách cụ thể của tổ chức trong các LLM.
2.  COMPASS nhận đầu vào là tập hợp các chính sách allowlist và denylist của một tổ chức (được diễn đạt bằng ngôn ngữ tự nhiên) cùng với mô tả ngữ cảnh tổ chức.
3.  Khuôn khổ này tự động tạo ra các truy vấn đánh giá bao gồm:
    *   Truy vấn cơ bản (base queries) để kiểm tra tuân thủ thông thường.
    *   Truy vấn trường hợp biên (edge queries) được thiết kế để kiểm tra giới hạn của chính sách, bao gồm cả các trường hợp đối kháng (adversarial) để phát hiện từ chối sai (false positive) hoặc không từ chối (false negative).
4.  Sau đó, COMPASS sử dụng một LLM làm trọng tài để đánh giá phản hồi của chatbot và xác định xem chúng có tuân thủ chính sách hay không.

### Main Results:
1.  Áp dụng COMPASS cho tám kịch bản ngành đa dạng, tạo ra và xác thực 5.920 truy vấn kiểm tra cả tuân thủ định kỳ và khả năng chống chịu đối kháng.
2.  Đánh giá bảy mô hình hiện đại cho thấy một sự bất đối xứng cơ bản: các mô hình xử lý đáng tin cậy các yêu cầu hợp lệ (allowlist) với độ chính xác trên 95 phần trăm.
3.  Tuy nhiên, các mô hình thất bại nghiêm trọng trong việc thực thi các lệnh cấm (denylist), chỉ từ chối 13-40 phần trăm các vi phạm denylist đối kháng.
4.  Khoảng cách này gia tăng đáng kể trong các điều kiện đối kháng, với một số mô hình từ chối dưới 5 phần trăm các trường hợp biên vi phạm chính sách.
5.  Những kết quả này chứng minh rằng các LLM hiện tại thiếu sự mạnh mẽ cần thiết cho các triển khai nhạy cảm về chính sách.

### Conclusion:
1.  Các LLM hiện tại thiếu độ bền vững cần thiết cho các triển khai quan trọng về chính sách.
2.  COMPASS được thiết lập như một khuôn khổ đánh giá thiết yếu cho an toàn AI cấp tổ chức.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.01836](https://huggingface.co/papers/2601.01836) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.01836](https://arxiv.org/abs/2601.01836) |
| PDF Download | [https://arxiv.org/pdf/2601.01836.pdf](https://arxiv.org/pdf/2601.01836.pdf) |
| Github Repository | [https://github.com/AIM-Intelligence/COMPASS](https://github.com/AIM-Intelligence/COMPASS) |

--- 

## 18. SWE-Lego: Pushing the Limits of Supervised Fine-tuning for Software Issue Resolving

**Tác giả:** Chaofan Tao, Jierun Chen, Yuxin Jiang, Kaiqi Kou, Shaowei Wang, Ruoyu Wang, Xiaohui Li, Sidi Yang, Yiming Du, Jianbo Dai, Zhiming Mao, Xinyu Wang, Lifeng Shang, Haoli Bai

**Xuất bản lúc:** 2026-01-04

### Main Problem:
Vấn đề cốt lõi mà bài báo đề cập là làm thế nào để nâng cao giới hạn của phương pháp tinh chỉnh có giám sát (SFT) đơn giản và nhẹ nhàng để giải quyết các vấn đề kỹ thuật phần mềm (SWE), thay vì phụ thuộc vào các phương pháp huấn luyện phức tạp và tốn kém tài nguyên (như mid-training, học tăng cường hoặc kết hợp các phương pháp này). Ngoài ra, các nỗ lực SFT trước đây thường thiếu bộ dữ liệu chất lượng cao bao gồm môi trường thực thi và các trường hợp lỗi thực tế cần thiết để tạo ra các lộ trình đa dạng và chất lượng.

### Main Idea:
Bài báo đề xuất SWE-Lego, một phương pháp tinh chỉnh có giám sát (SFT) được thiết kế để đạt hiệu suất tiên tiến nhất trong giải quyết các vấn đề kỹ thuật phần mềm. SWE-Lego bao gồm ba khối xây dựng chính:
1.  **Bộ dữ liệu SWE-Lego:** Một bộ sưu tập 32 nghìn trường hợp nhiệm vụ chất lượng cao và 18 nghìn lộ trình đã được xác thực, kết hợp dữ liệu thực tế và tổng hợp để bổ sung cho nhau về chất lượng và số lượng. Dữ liệu này được xây dựng từ hơn 3000 kho lưu trữ thực tế và được xác thực nghiêm ngặt để ngăn chặn các kỹ thuật gian lận (như Git hacking).
2.  **Quy trình SFT tinh chỉnh:** Bao gồm "che lỗi từng bước" (loại trừ các token liên quan đến lỗi thực thi khỏi tính toán mất mát) và "học theo độ khó" (huấn luyện mô hình trên các tác vụ dễ hơn trước khi chuyển sang các tác vụ khó hơn).
3.  **Mở rộng tại thời điểm kiểm tra (TTS):** Nghiên cứu các chiến lược TTS hiệu quả nhất cho các tác vụ SWE bằng cách mở rộng tuần tự (tăng số lượt tương tác tối đa) và mở rộng song song (nhiều lần chạy với lựa chọn bằng trình xác minh), đồng thời tìm ra các chiến lược tối ưu.

### Main Results:
*   Các mô hình SWE-Lego đạt hiệu suất tiên tiến nhất trong số các mô hình mã nguồn mở có kích thước tương đương trên SWE-bench Verified.
*   SWE-Lego-Qwen3-8B đạt 42.2% chỉ với SFT và tăng lên 49.6% với TTS@16.
*   SWE-Lego-Qwen3-32B đạt 52.6% chỉ với SFT và tăng lên 58.8% với TTS@16.
*   Kết quả này được thực hiện dựa trên đánh giá không gian lận Git, tránh các kết quả bị thổi phồng.
*   Phân tích chi tiết hiệu suất cho thấy bộ dữ liệu SWE-Lego mang lại mức tăng đáng kể 25.6%, quy trình SFT tinh chỉnh đóng góp thêm 3.8% và TTS đóng góp 6.2%, tổng cộng nâng mô hình Qwen3-32B từ 23.2% lên 58.8%.

### Conclusion & Future Works:
SWE-Lego chứng minh rằng một quy trình SFT được thiết kế tỉ mỉ có thể cạnh tranh hoặc vượt trội hơn hiệu suất của các phương pháp huấn luyện phức tạp và tốn kém hơn. Bài nghiên cứu hy vọng SWE-Lego có thể cung cấp một mô hình hậu huấn luyện có thể tái sản xuất và nhẹ nhàng để xây dựng các tác nhân SWE hiệu quả. Dữ liệu và các mô hình liên quan của công trình này sẽ được mở nguồn cho nghiên cứu tương lai trong cộng đồng.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.01426](https://huggingface.co/papers/2601.01426) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.01426](https://arxiv.org/abs/2601.01426) |
| PDF Download | [https://arxiv.org/pdf/2601.01426.pdf](https://arxiv.org/pdf/2601.01426.pdf) |
| Github Repository | [https://github.com/SWE-Lego/SWE-Lego](https://github.com/SWE-Lego/SWE-Lego) |

--- 

## 19. Toward Stable Semi-Supervised Remote Sensing Segmentation via Co-Guidance and Co-Fusion

**Tác giả:** Yi Zhou, Xuechao Zou, Shun Zhang, Kai Li, Shiying Wang, Jingming Chen, Congyan Lang, Tengfei Cao, Pin Tao, Yuanchun Shi

**Xuất bản lúc:** 2025-12-28

### Main Problem:
Phân đoạn ngữ nghĩa ảnh vệ tinh bán giám sát (semi-supervised remote sensing image semantic segmentation) gặp phải vấn đề cốt lõi là "pseudo-label drift", nơi "confirmation bias" dẫn đến sự tích lũy lỗi trong quá trình huấn luyện. Các mô hình được giám sát hoàn toàn đòi hỏi chú thích cấp pixel tốn kém và mất thời gian, dẫn đến tình trạng khan hiếm nhãn dữ liệu. Các phương pháp bán giám sát hiện có dễ bị trôi nhãn giả và gặp khó khăn trong việc phân biệt các danh mục ngữ nghĩa tương tự hoặc xác định ranh giới đối tượng chính xác, đặc biệt trong các cảnh ảnh vệ tinh phức tạp và khi nhãn dữ liệu cực kỳ khan hiếm.

### Main Idea:
Bài nghiên cứu đề xuất Co2S, một khuôn khổ phân đoạn ảnh vệ tinh bán giám sát ổn định. Co2S kết hợp một cách hiệp đồng các thông tin tiên nghiệm từ các mô hình thị giác-ngôn ngữ (vision-language models) và các mô hình tự giám sát (self-supervised models). Cụ thể, kiến trúc bao gồm hai mô hình nền tảng thị giác dựa trên ViT không đồng nhất, được khởi tạo với CLIP và DINOv3 được huấn luyện trước, nhằm giảm thiểu sự tích lũy lỗi và pseudo-label drift. Co2S giới thiệu cơ chế "explicit-implicit semantic co-guidance" sử dụng nhúng văn bản và các truy vấn có thể học được để cung cấp hướng dẫn cấp độ lớp tường minh và ngầm định. Ngoài ra, chiến lược "global-local feature collaborative fusion" được phát triển để kết hợp thông tin ngữ cảnh toàn cục từ CLIP với các chi tiết cục bộ từ DINOv3, cho phép mô hình tạo ra kết quả phân đoạn có độ chính xác cao.

### Main Results:
Các thử nghiệm rộng rãi trên sáu bộ dữ liệu ảnh vệ tinh phổ biến khác nhau đã chứng minh tính ưu việt của phương pháp Co2S. Co2S liên tục đạt được hiệu suất hàng đầu trên các giao thức phân vùng khác nhau và trong các kịch bản đa dạng. Khung này cho thấy hiệu quả vượt trội so với các phương pháp bán giám sát hiện có, đặc biệt trong các trường hợp chú thích cực kỳ khan hiếm.

### Conclusion & Future Works:
Co2S là một khuôn khổ ổn định cho phân đoạn ngữ nghĩa ảnh vệ tinh bán giám sát, giải quyết vấn đề pseudo-label drift thông qua việc kết hợp priors từ các mô hình thị giác-ngôn ngữ và tự giám sát, sử dụng cơ chế co-guidance và co-fusion.
Hướng nghiên cứu tiếp theo không được đề cập trực tiếp trong đoạn văn được trích dẫn.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2512.23035](https://huggingface.co/papers/2512.23035) |
| ArXiv Abstract | [https://arxiv.org/abs/2512.23035](https://arxiv.org/abs/2512.23035) |
| PDF Download | [https://arxiv.org/pdf/2512.23035.pdf](https://arxiv.org/pdf/2512.23035.pdf) |
| Github Repository | [https://github.com/XavierJiezou/Co2S](https://github.com/XavierJiezou/Co2S) |

--- 

## 20. OpenNovelty: An LLM-powered Agentic System for Verifiable Scholarly Novelty Assessment

**Tác giả:** Ming Zhang, Kexin Tan, Yueyuan Huang, Yujiong Shen, Chunchun Ma, Li Ju, Xinran Zhang, Yuhui Wang, Wenqing Jing, Jingyi Deng, Huayu Sha, Binze Hu, Jingqi Tong, Changhao Jiang, Yage Geng, Yuankai Ying, Yue Zhang, Zhangyue Yin, Zhiheng Xi, Shihan Dou, Tao Gui, Qi Zhang, Xuanjing Huang

**Xuất bản lúc:** 2026-01-04

Dưới đây là tóm tắt bài nghiên cứu dựa trên tiêu đề và đoạn văn trích dẫn:

### Main Problem:
Vấn đề cốt lõi mà bài báo đề cập là những thách thức trong việc đánh giá tính mới của các bài nộp học thuật trong quá trình đánh giá ngang hàng. Việc bùng nổ các ấn phẩm học thuật đã đặt áp lực lớn lên hệ thống đánh giá, khiến người đánh giá thiếu thời gian và năng lượng để thực hiện các đánh giá kỹ lưỡng, công bằng. Việc đánh giá tính mới đặc biệt khó khăn do lượng tài liệu khổng lồ, khó khăn trong việc xác minh tuyên bố thông qua phân tích chi tiết và tính chủ quan trong phán đoán. Các phương pháp dựa trên Mô hình Ngôn ngữ Lớn (LLM) hiện có cũng còn hạn chế, bao gồm việc LLM có thể "ảo giác" các tài liệu không tồn tại, chỉ so sánh tiêu đề và tóm tắt, hoặc bị giới hạn bởi cửa sổ ngữ cảnh.

### Main Idea:
Bài báo giới thiệu OpenNovelty, một hệ thống đại diện được hỗ trợ bởi LLM, được thiết kế để cung cấp phân tích tính mới minh bạch, có thể truy xuất nguồn gốc và dựa trên bằng chứng cho các bài nộp học thuật quy mô lớn. Triết lý thiết kế cốt lõi của OpenNovelty là làm cho "Tính mới có thể xác minh được" bằng cách không dựa vào kiến thức tham số của LLM mà thay vào đó, truy xuất các bài báo thực tế và thực hiện so sánh toàn văn ở cấp độ đóng góp để đảm bảo mọi phán đoán đều có bằng chứng. Hệ thống này hoạt động qua bốn giai đoạn: (1) trích xuất nhiệm vụ cốt lõi và các tuyên bố đóng góp để tạo truy vấn; (2) truy xuất các công trình trước đây có liên quan thông qua công cụ tìm kiếm ngữ nghĩa; (3) xây dựng một phân loại có hệ thống về các công trình liên quan đến nhiệm vụ cốt lõi và thực hiện so sánh toàn văn ở cấp độ đóng góp; và (4) tổng hợp tất cả các phân tích thành một báo cáo tính mới có cấu trúc với các trích dẫn và đoạn bằng chứng rõ ràng.

### Main Results:
Hệ thống OpenNovelty đã được triển khai để phân tích hơn 500 bài nộp ICLR 2026, với tất cả các báo cáo tính mới được công khai trên trang web của dự án. Phân tích sơ bộ cho thấy hệ thống có khả năng xác định các công trình trước đây có liên quan, bao gồm cả những bài báo có liên quan chặt chẽ mà các tác giả có thể đã bỏ qua. Bằng cách dựa tất cả các đánh giá tính mới vào các bài báo thực tế được truy xuất, kèm theo các trích dẫn rõ ràng và đoạn bằng chứng, OpenNovelty tránh được vấn đề "ảo giác" thường gặp trong các phương pháp dựa trên LLM đơn giản. Khung phân tích tính mới của OpenNovelty tích hợp việc trích xuất đóng góp, truy xuất ngữ nghĩa, xây dựng phân loại dựa trên LLM và so sánh cấp độ đóng góp vào một quy trình tự động hoàn toàn, cung cấp cho người đánh giá một ngữ cảnh có cấu trúc để hiểu vị trí của mỗi bài báo trong lĩnh vực nghiên cứu.

### Conclusion & Future Works:
OpenNovelty hướng tới việc trang bị cho cộng đồng nghiên cứu một công cụ có khả năng mở rộng để thúc đẩy quá trình đánh giá ngang hàng công bằng, nhất quán và dựa trên bằng chứng. Nhóm nghiên cứu có kế hoạch mở rộng phân tích này lên hơn 2.000 bài nộp trong các giai đoạn tiếp theo. Các hạn chế liên quan đến việc trích xuất công thức toán học và nội dung hình ảnh cũng sẽ được giải quyết trong các cải tiến sau này.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.01576](https://huggingface.co/papers/2601.01576) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.01576](https://arxiv.org/abs/2601.01576) |
| PDF Download | [https://arxiv.org/pdf/2601.01576.pdf](https://arxiv.org/pdf/2601.01576.pdf) |
| Github Repository | [https://github.com/january-blue/OpenNovelty](https://github.com/january-blue/OpenNovelty) |

--- 

## 21. Selective Imperfection as a Generative Framework for Analysis, Creativity and Discovery

**Tác giả:** Markus J. Buehler

**Xuất bản lúc:** 2025-12-30

### Main Problem:
Vấn đề cốt lõi mà bài nghiên cứu đề cập là làm thế nào để hiểu và khai thác các nguyên tắc tạo sinh chung giữa cấu trúc vật chất và logic sáng tác âm nhạc để thúc đẩy phân tích, sáng tạo và khám phá. Cụ thể, thách thức là tạo ra sự đổi mới trong khoa học và nghệ thuật khi các ràng buộc hiện có không thể được thỏa mãn, đòi hỏi phải mở rộng không gian cấu hình khả thi, và phát triển các hệ thống Trí tuệ Nhân tạo (AI) có khả năng phát minh thay vì chỉ nội suy.

### Main Idea:
Bài báo giới thiệu "materiomusic" như một khuôn khổ tạo sinh, liên kết các cấu trúc phân cấp của vật chất với logic cấu tạo của âm nhạc. Ý tưởng chính là sử dụng các ánh xạ thuận nghịch giữa các cấu trúc vật lý (ví dụ: phổ phân tử, mạng lưới ba chiều) và các cấu trúc âm nhạc (ví dụ: âm điệu, hòa âm) theo cách được nền tảng vật lý. Trong khuôn khổ này, âm thanh đóng vai trò là một công cụ khoa học, nơi việc lắng nghe trở thành một chế độ "nhìn thấy" và sáng tác âm nhạc trở thành bản thiết kế cho vật chất. Khái niệm "khiếm khuyết có chọn lọc" (selective imperfection) được đề xuất như một cơ chế để khôi phục sự cân bằng giữa tính mạch lạc và khả năng thích ứng, cho phép sự đổi mới xuất hiện khi các ràng buộc không thể được đáp ứng trong các mức độ tự do hiện có.

### Main Results:
*   Phân tích định lượng tất cả 2^12 thang âm nhạc cho thấy các hệ thống có ý nghĩa văn hóa tập trung trong một "hành lang" có độ entropy trung bình và khuyết tật trung bình, song song với điểm tối ưu Hall-Petch trong khoa học vật liệu, nơi mật độ khuyết tật trung gian tối đa hóa độ bền của vật liệu.
*   Các mô hình AI dựa trên bầy đàn (swarm-based AI) có thể sáng tác âm nhạc thể hiện các đặc điểm cấu trúc giống con người, như kết nối mạng lưới "thế giới nhỏ" (small-world connectivity), tích hợp module và sự mạch lạc tầm xa, cho thấy một lộ trình vượt ra ngoài nội suy để hướng tới sự phát minh.
*   Khuôn khổ materiomusic hỗ trợ thiết kế protein de novo đa phương thức và các hệ thống AI có khả năng sáng tạo thông qua động lực học tập thể.
*   Các ánh xạ được xây dựng là thuận nghịch và bảo toàn cấu trúc nội tại, cho phép dịch các cấu trúc vật lý thành âm thanh để khám phá và ngược lại, sử dụng không gian âm nhạc để thiết kế các dạng vật chất mới.

### Conclusion & Future Works:
Bài nghiên cứu kết luận rằng khoa học và nghệ thuật là những hành động tạo sinh trong việc "xây dựng thế giới" dưới các ràng buộc, với dao động (vibration) đóng vai trò là ngữ pháp chung tổ chức cấu trúc trên nhiều quy mô. "Khiếm khuyết có chọn lọc" phục vụ như thuật toán cho phép vũ trụ tự sáng tác. Hướng nghiên cứu tiếp theo bao gồm việc phát triển materiomusic như một ngôn ngữ tự nhiên cho sự sáng tạo, thống nhất các phân tử, vật liệu và âm thanh, cũng như tiếp tục khai thác AI tác nhân để trở thành đối tác sáng tạo, vượt ra ngoài nội suy để đạt được những phát minh mới.

### Overview Figure

![Overview Figure](papers\2026-01-06\2601.00863_overview.png)

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.00863](https://huggingface.co/papers/2601.00863) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.00863](https://arxiv.org/abs/2601.00863) |
| PDF Download | [https://arxiv.org/pdf/2601.00863.pdf](https://arxiv.org/pdf/2601.00863.pdf) |
| Github Repository | [https://github.com/lamm-mit/MusicAnalysis](https://github.com/lamm-mit/MusicAnalysis) |

--- 

## 22. IMA++: ISIC Archive Multi-Annotator Dermoscopic Skin Lesion Segmentation Dataset

**Tác giả:** Kumar Abhishek, Jeremy Kawahara, Ghassan Hamarneh

**Xuất bản lúc:** 2025-12-25

### Main Problem:
Vấn đề cốt lõi mà bài báo đề cập là sự thiếu hụt các bộ dữ liệu phân đoạn tổn thương da (SLS) đa người chú thích quy mô lớn, công khai và có nhãn người chú thích, đặc biệt cho ảnh soi da (dermoscopic). Các bộ dữ liệu SLS hiện có thường chỉ cung cấp một mặt nạ phân đoạn cho mỗi ảnh hoặc quá nhỏ (ví dụ: ISIC 2019-Seg chỉ có 100 ảnh với 3 phân đoạn mỗi ảnh) để nghiên cứu hiệu quả các tác vụ cụ thể của người chú thích. Việc phân đoạn tổn thương da vốn đã là một nhiệm vụ thách thức do các yếu tố như hiện vật hình ảnh, sự đa dạng về kích thước, hình dạng, tông màu da, độ tương phản và ranh giới tổn thương không rõ ràng, tất cả đều ảnh hưởng đến việc xác định một "chân lý mặt đất" duy nhất.

### Main Idea:
Bài báo giới thiệu ISIC MultiAnnot++ (IMA++), một bộ dữ liệu phân đoạn tổn thương da đa người chú thích công khai và quy mô lớn, được tổng hợp từ Kho lưu trữ ISIC. IMA++ được thiết kế để giải quyết sự thiếu hụt các bộ dữ liệu đa người chú thích bằng cách cung cấp nhiều phân đoạn cho mỗi ảnh cùng với siêu dữ liệu chi tiết, bao gồm trình độ kỹ năng của người chú thích và công cụ phân đoạn được sử dụng. Bộ dữ liệu này mô phỏng các kịch bản chú thích thực tế, nơi nhiều người chú thích đóng góp vào một tập hợp con các hình ảnh, tạo ra một biểu đồ hai phía không đầy đủ giữa tập hợp ảnh và tập hợp người chú thích. Bài báo cũng cung cấp các mặt nạ phân đoạn đồng thuận được tạo ra bằng hai thuật toán đồng thuận cho các ảnh có nhiều phân đoạn.

### Main Results:
IMA++ là bộ dữ liệu phân đoạn tổn thương da (SLS) công khai lớn nhất hiện có, với tổng cộng 17.684 mặt nạ phân đoạn trên 14.967 ảnh soi da. Trong số đó, 2.394 ảnh soi da có từ 2 đến 5 phân đoạn mỗi ảnh, được tạo bởi 16 người chú thích. Khi bổ sung các mặt nạ phân đoạn đồng thuận, tổng số phân đoạn trong bộ dữ liệu tăng lên 22.472. Bộ dữ liệu này nắm bắt một phạm vi rộng các phong cách phân đoạn, phản ánh sự khác biệt về sở thích của người chú thích, công cụ được sử dụng và mức độ kỹ năng. IMA++ là bộ dữ liệu đầu tiên và lớn nhất cung cấp thông tin về công cụ và trình độ kỹ năng của người chú thích, cho phép khám phá cách các yếu tố này ảnh hưởng đến sự biến thiên của phân đoạn.

### Conclusion & Future Works:
IMA++ là một bộ dữ liệu có giá trị cho các nhà nghiên cứu làm việc trên nhiều vấn đề mở, bao gồm phân loại và phân đoạn tổn thương da. Nó đặc biệt hữu ích cho việc mô hình hóa sở thích phân đoạn đa người chú thích, mô hình hóa sự đồng thuận của chuyên gia, tìm hiểu sự phân bố các phân đoạn, khám phá các phong cách phân đoạn cơ bản từ mặt nạ đa người chú thích, và nghiên cứu sự đồng thuận giữa các chuyên gia. Hơn nữa, nó hỗ trợ phân tích hình ảnh da đa phương thức (ảnh soi da và siêu dữ liệu phong phú) và đa nhiệm vụ (chẩn đoán, phân đoạn, dự đoán IAA). Các hướng nghiên cứu tiếp theo đã sử dụng hoặc có thể sử dụng IMA++ bao gồm việc đánh giá việc khám phá các phong cách chú thích duy nhất và kiểm tra mối liên hệ thống kê giữa mức độ đồng thuận phân đoạn giữa các người chú thích và mức độ ác tính của tổn thương da, cũng như khả năng dự đoán mức độ đồng thuận từ ảnh trực tiếp.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2512.21472](https://huggingface.co/papers/2512.21472) |
| ArXiv Abstract | [https://arxiv.org/abs/2512.21472](https://arxiv.org/abs/2512.21472) |
| PDF Download | [https://arxiv.org/pdf/2512.21472.pdf](https://arxiv.org/pdf/2512.21472.pdf) |
| Github Repository | [https://github.com/sfu-mial/IMAplusplus](https://github.com/sfu-mial/IMAplusplus) |

--- 

## 23. Prithvi-Complimentary Adaptive Fusion Encoder (CAFE): unlocking full-potential for flood inundation mapping

**Tác giả:** Saurabh Kaushik, Lalit Maurya, Beth Tellman

**Xuất bản lúc:** 2026-01-05

### Main Problem:
Các mô hình Geo-Foundation Models (GFMs) hiện tại, đặc biệt là Prithvi GFM, gặp khó khăn trong việc vượt trội hơn baseline U-Net trong tác vụ lập bản đồ ngập lụt, do hạn chế trong việc nắm bắt các chi tiết cục bộ quan trọng. Hơn nữa, kiến trúc của Prithvi GFM nguyên bản chỉ hỗ trợ sáu kênh đầu vào, giới hạn khả năng ứng dụng của nó với dữ liệu đa kênh và đa phương thức.

### Main Idea:
Bài nghiên cứu đề xuất Prithvi-Complementary Adaptive Fusion Encoder (CAFE), một mô hình kết hợp bộ mã hóa Prithvi GFM đã được huấn luyện trước với một nhánh CNN song song được tăng cường bởi các Convolutional Attention Modules (CAM). Prithvi-CAFE sử dụng các adapter để tinh chỉnh nhanh và hiệu quả Prithvi, đồng thời thực hiện hợp nhất đa cấp, đa tỷ lệ các đặc trưng của CNN. Phương pháp này cho phép xử lý bất kỳ số lượng kênh đầu vào nào, nắm bắt các chi tiết cục bộ quan trọng trong khi vẫn giữ được các phụ thuộc tầm xa, bằng cách phân chia các kênh đầu vào thành hai tập bổ sung cho Transformer và CNN.

### Main Results:
Prithvi-CAFE đạt được kết quả hàng đầu (SoTA) trên hai bộ dữ liệu lập bản đồ ngập lụt: Sen1Flood11 và FloodPlanet.
- Trên dữ liệu thử nghiệm Sen1Flood11, Prithvi-CAFE đạt IoU 83.41, vượt trội so với Prithvi gốc (IoU 82.50) và các GFM khác (TerraMind 82.90, DOFA 81.54, spectralGPT 81.02).
- Trên địa điểm thử nghiệm tách biệt của Sen1Flood11, Prithvi-CAFE đạt IoU 81.37, vượt xa baseline U-Net (70.57) và Prithvi gốc (72.42).
- Trên FloodPlanet, Prithvi-CAFE đạt IoU 64.70, cũng vượt trội so với U-Net (60.14), Terramind (62.33), DOFA (59.15) và Prithvi 2.0 (61.91).

### Conclusion & Future Works:
Mô hình Prithvi-CAFE đơn giản nhưng hiệu quả cho thấy tiềm năng mạnh mẽ trong việc cải thiện các tác vụ phân đoạn, đặc biệt là khi dữ liệu đa kênh và đa phương thức cung cấp thông tin bổ sung và các chi tiết cục bộ là rất quan trọng. Nghiên cứu này mở rộng khả năng của Prithvi GFM vượt ra ngoài sáu kênh phổ ban đầu để xử lý hiệu quả bất kỳ số lượng kênh nào và tạo ra các bản đồ lũ lụt đáng tin cậy. Mã nguồn của Prithvi-CAFE đã được công bố trên GitHub.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.02315](https://huggingface.co/papers/2601.02315) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.02315](https://arxiv.org/abs/2601.02315) |
| PDF Download | [https://arxiv.org/pdf/2601.02315.pdf](https://arxiv.org/pdf/2601.02315.pdf) |
| Github Repository | [https://github.com/Sk-2103/Prithvi-CAFE](https://github.com/Sk-2103/Prithvi-CAFE) |

--- 

## 24. Project Ariadne: A Structural Causal Framework for Auditing Faithfulness in LLM Agents

**Tác giả:** Sourena Khanzadeh

**Xuất bản lúc:** 2026-01-05

### Main Problem:
Khi các tác nhân Mô hình Ngôn ngữ Lớn (LLM agents) ngày càng đảm nhận các quyết định tự động có rủi ro cao, sự minh bạch trong quy trình lập luận của chúng trở thành một mối quan ngại an toàn cấp bách. Mặc dù các dấu vết Chain-of-Thought (CoT) cho phép agent tạo ra các lập luận dễ đọc, nhưng không rõ liệu các dấu vết này có phải là các động lực tạo ra trung thực (faithful generative drivers) cho đầu ra của mô hình hay chỉ đơn thuần là các biện minh hậu kiểm (post-hoc rationalizations). Vấn đề này được gọi là "Khoảng cách Trung thực (Faithfulness Gap)" hoặc "Sự Tách rời Nhân quả (Causal Decoupling)", thể hiện một thất bại cơ bản trong AI Giải thích được (XAI) khi "suy nghĩ" nội bộ của agent không liên kết nhân quả với hành động cuối cùng.

### Main Idea:
Bài nghiên cứu giới thiệu Project Ariadne, một khung XAI mới sử dụng Mô hình Nhân quả Cấu trúc (Structural Causal Models - SCMs) và logic phản thực tế (counterfactual logic) để kiểm tra tính toàn vẹn nhân quả của lập luận của agent. Không giống như các phương pháp giải thích hiện có dựa vào sự tương đồng văn bản ở mức bề mặt, Project Ariadne thực hiện các "can thiệp cứng (hard interventions)" (do-calculus) vào các nút lập luận trung gian—hệ thống đảo ngược logic, phủ định các tiền đề và đảo ngược các tuyên bố thực tế—để đo lường "Độ nhạy Nhân quả (Causal Sensitivity)" (phi) của câu trả lời cuối cùng. Khung này định lượng tính trung thực bằng "Điểm nhạy cảm nhân quả (Causal Sensitivity Score)" dựa trên sự khác biệt ngữ nghĩa giữa câu trả lời gốc và câu trả lời phản thực tế sau khi can thiệp.

### Main Results:
Các đánh giá thực nghiệm trên các mô hình hiện đại cho thấy một "Khoảng cách Trung thực" dai dẳng. Bài nghiên cứu xác định và phát hiện một chế độ thất bại phổ biến được gọi là "Sự Tách rời Nhân quả", trong đó các agent thể hiện "mật độ vi phạm (violation density)" (rho) lên đến 0.77 trong các lĩnh vực thực tế và khoa học. Trong những trường hợp này, các agent đưa ra các kết luận giống hệt nhau mặc dù có logic nội bộ mâu thuẫn, chứng minh rằng dấu vết lập luận của chúng hoạt động như "Nhà hát Lập luận (Reasoning Theater)" trong khi việc ra quyết định bị chi phối bởi các tiên nghiệm tham số tiềm ẩn. "Mật độ vi phạm" cao nhất trong Lập luận Khoa học (rho = 0.96), trong khi các nhiệm vụ Logic Toán học cho thấy độ nhạy cao hơn đáng kể (phi trung bình = 0.329), cho thấy tính nhân quả sâu sắc hơn.

### Conclusion & Future Works:
Các phát hiện cho thấy các kiến trúc agent hiện tại vốn dĩ dễ bị giải thích không trung thực. Project Ariadne cung cấp một khung chẩn đoán để phát hiện các vi phạm tính trung thực. Bài nghiên cứu đề xuất "Điểm Ariadne (Ariadne Score)" như một tiêu chuẩn mới để đánh giá sự phù hợp giữa logic đã nêu và hành động của mô hình. Điều này có thể định hướng cho các nghiên cứu và phát triển trong tương lai nhằm cải thiện tính trung thực và minh bạch của các agent LLM.

### Overview Figure

![Overview Figure](papers\2026-01-06\2601.02314_overview.png)

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2601.02314](https://huggingface.co/papers/2601.02314) |
| ArXiv Abstract | [https://arxiv.org/abs/2601.02314](https://arxiv.org/abs/2601.02314) |
| PDF Download | [https://arxiv.org/pdf/2601.02314.pdf](https://arxiv.org/pdf/2601.02314.pdf) |
| Github Repository | [https://github.com/skhanzad/AridadneXAI](https://github.com/skhanzad/AridadneXAI) |

--- 

## 25. M-ErasureBench: A Comprehensive Multimodal Evaluation Benchmark for Concept Erasure in Diffusion Models

**Tác giả:** Ju-Hsuan Weng, Jia-Wei Liao, Cheng-Fu Chou, Jun-Cheng Chen

**Xuất bản lúc:** 2025-12-28

### Main Problem:
Các mô hình khuếch tán văn bản thành hình ảnh có thể tạo ra nội dung có hại hoặc có bản quyền. Các phương pháp xóa bỏ khái niệm hiện có chủ yếu tập trung vào việc xóa khái niệm từ các lời nhắc văn bản, bỏ qua các phương thức nhập liệu khác như nhúng học được và latent đảo ngược. Những phương thức này trở thành bề mặt tấn công, nơi các khái niệm đã bị xóa có thể tái xuất hiện, với Tỷ lệ tái tạo khái niệm (CRR) vượt quá 90% trong thiết lập hộp trắng. Điều này cho thấy các phương pháp hiện tại chủ yếu làm gián đoạn sự liên kết văn bản-hình ảnh thay vì loại bỏ hoàn toàn các khái niệm.

### Main Idea:
Bài nghiên cứu giới thiệu M-ErasureBench, một khuôn khổ đánh giá đa phương thức mới, toàn diện để chấm điểm các phương pháp xóa bỏ khái niệm trên ba phương thức nhập liệu: lời nhắc văn bản, nhúng học được và latent đảo ngược. Đối với hai phương thức sau, nghiên cứu đánh giá cả truy cập hộp trắng và hộp đen, tạo ra năm kịch bản đánh giá. Để giải quyết các lỗ hổng, bài nghiên cứu đề xuất IRECE (Inference-time Robustness Enhancement for Concept Erasure), một mô-đun cắm-và-chạy giúp định vị các khái niệm mục tiêu thông qua cơ chế chú ý chéo và làm nhiễu các latent liên quan trong quá trình khử nhiễu, mà không cần huấn luyện lại.

### Main Results:
Phân tích cho thấy các phương pháp hiện có đạt hiệu suất xóa bỏ mạnh mẽ đối với lời nhắc văn bản nhưng phần lớn thất bại dưới các nhúng học được và latent đảo ngược, với CRR vượt quá 90% trong thiết lập hộp trắng. IRECE đã chứng minh rằng nó khôi phục khả năng chống chịu một cách nhất quán, giảm CRR tới 40% trong kịch bản đảo ngược latent hộp trắng khó khăn nhất, đồng thời duy trì chất lượng hình ảnh. M-ErasureBench cung cấp tiêu chuẩn đánh giá toàn diện đầu tiên về xóa bỏ khái niệm ngoài lời nhắc văn bản.

### Conclusion & Future Works:
M-ErasureBench là tiêu chuẩn đánh giá đa phương thức toàn diện đầu tiên cho việc xóa bỏ khái niệm trong các mô hình khuếch tán. Nghiên cứu này làm nổi bật các lỗ hổng của các phương pháp hiện có đối với các phương thức tấn công thời gian suy luận ngoài văn bản. Cùng với IRECE, một mô-đun plug-and-play giúp tăng cường khả năng chống chịu mà không cần huấn luyện lại, nghiên cứu cung cấp các biện pháp bảo vệ thiết thực để xây dựng các mô hình tạo sinh đáng tin cậy hơn và an toàn hơn.

### Các đường dẫn liên quan

| Nền tảng | Đường dẫn |
| :--- | :--- |
| Hugging Face | [https://huggingface.co/papers/2512.22877](https://huggingface.co/papers/2512.22877) |
| ArXiv Abstract | [https://arxiv.org/abs/2512.22877](https://arxiv.org/abs/2512.22877) |
| PDF Download | [https://arxiv.org/pdf/2512.22877.pdf](https://arxiv.org/pdf/2512.22877.pdf) |
| Github Repository | N/A |

