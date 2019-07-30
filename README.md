# できること
Edge TPU 上で動作する TFLite ファイルを作成、実行できます。

# 必要なもの
## 以下の機材やアカウント等が必要になります。
- [Edge TPU USB Accelerator](https://coral.withgoogle.com/products/accelerator/)
- Google colaboratory を実行できるブラウザ
- 普段お使いの Google アカウント (Google drive を使います。)
- Raspberry Pi (3B + で動作確認してます。)
	- サンプルは [Raspberry Pi camera module](https://www.raspberrypi.org/documentation/usage/camera/) 前提で作成してあります。
  - 適当なモニターがあると推論結果が見やすいので、Raspberry Pi に繋いでください。(一応コンソールにも結果が出ます。)


# 手順
## Google colaboratory に移動
- [こちら](https://colab.research.google.com/gist/TsukasaDEKA/86f9acd762f439dbe628cef3e3a5eaea/generate_tflite_file_for_raspberry_pi_exsample.ipynb)のリンクから Google colaboratory に移動します。
- 記載されてる手順に従って Edge TPU 用の TFLite ファイルを作成してください。

## Raspberry Pi で実行
- Raspberry Pi にモニター、Edge TPU、Raspberry Pi camera module、電源を接続してください。
- [こちらの手順](https://coral.withgoogle.com/docs/accelerator/get-started/) に従って Raspberry Pi をセッティングします。
- 以下のコマンドを実行し、git リポジトリをクローンします。

```
$ git clone https://github.com/TsukasaDEKA/edge_tpu_sample_by_deka.git
$ cd edge_tpu_sample_by_deka/for_raspberrypi
```

- 先ほど作成した Edge TPU 用の TFLite ファイルを Raspberry Pi に送ります。
- 以下のコマンドを実行します。

```
$ python3 conv_classification.py <Edge TPU 用の TFLite ファイルのパス + ファイル名>
```
