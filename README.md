# できること
Edge TPU 上で動作する TFLite ファイルに変換できます。

# 必要なもの
## 以下の機材やアカウント等が必要になります。
- [Edge TPU USB Accelerator](https://coral.withgoogle.com/products/accelerator/)
- Google colaboratory を実行できるブラウザ
- 普段お使いの Google アカウント (Google drive を使います。)
- Raspberry Pi (3B + で動作確認してます。)
	- サンプルは [Raspberry Pi camera module](https://www.raspberrypi.org/documentation/usage/camera/) 前提で作成してあります。


# 手順
## Google colaboratory に移動
- [こちら](https://colab.research.google.com/gist/TsukasaDEKA/86f9acd762f439dbe628cef3e3a5eaea/generate_tflite_file_for_raspberry_pi_exsample.ipynb)のリンクから Google colaboratory に移動します。
- 記載されてる手順に従って Edge TPU 用の TFLite ファイルを作成してください。

## Raspberry Pi で実行
- [こちらの手順](https://coral.withgoogle.com/docs/accelerator/get-started/) に従って Raspberry Pi をセッティングする。
- 以下のコマンドを実行し、git リポジトリをクローンする。

```
$ git clone https://github.com/TsukasaDEKA/edge_tpu_sample_by_deka.git
```
