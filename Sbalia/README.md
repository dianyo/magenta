
# ***Sbalia-台灣人工智慧實驗室音樂計畫***

### Nowadays Result
1. First album : [Sbalia]()
### Implement
##### First Album - Sbalia
1. fork google 的 magenta 音樂開源專案，該專案使用 tensorflow 建立深度學習的模型，大部分是使用 RNN 模型來做 seq2seq 的訓練，在這個專案裡提供許多不一樣的訓練模型，詳細模型介紹：[magenta/magenta/models](https://github.com/dianyo/magenta/tree/master/magenta/models)。
2. 在試過不同的模型後，決定在第一張專輯中，使用 melody_rnn 以及 performance_rnn 這兩種模型，訓練好的模型以及資料來源說明可以在 [Sbalila/pertrain](https://github.com/dianyo/magenta/tree/master/Sbalia/pretrain) 中找到。
3. 在這張專輯中有修改 magenta 原始 [code](https://github.com/dianyo/magenta/blob/master/magenta/models/melody_rnn/melody_rnn_create_dataset.py)，將 ignore polyphonic 這個參數設成 ```True```，讓讀入的 Midi 檔，就算在同一個時間軸有其他音符，也會拿最高音，不像原本 default 直接捨去這段資料。
4. 目前(第一張專輯)還未能達到電腦全自動作曲，在這張專輯中的曲子是融合電腦與人一同創作的結果，電腦提供大量旋律（melody），音樂創作者從中挑選適合或者是自己喜歡的音樂，使用我們的[演算法](https://github.com/dianyo/magenta/tree/master/Sbalia/chord_work)加入和弦，之後再用音樂軟體進行加工，改變音色、加入節奏樂器等。
</br>
<center>
<img src="https://raw.githubusercontent.com/dianyo/magenta/master/Sbalia/imgs/Sbalia.001.jpeg" width="450"/>
</center>

