import io
import time
import csv


import numpy as np
import picamera

import edgetpu.classification.engine

def get_labels_from_csv(file_path):
    labels = []
    with open(file_path, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            labels.append(row[0])
    print("The labels are: ", labels)
    return labels

def main(model_path):
    label_file_path = '../label/for_lt_20190731/label.csv'
    labels = get_labels_from_csv(label_file_path)
    engine = edgetpu.classification.engine.ClassificationEngine(model_path)
    with picamera.PiCamera() as camera:
        camera.resolution = (225, 225)
        # camera.resolution = (640, 480)
        camera.vflip = True
        camera.hflip = True
        camera.framerate = 30
        _, width, height, channels = engine.get_input_tensor_shape()
        camera.start_preview()
        try:
            stream = io.BytesIO()
            for foo in camera.capture_continuous(stream,
                                                 format='rgb',
                                                 use_video_port=True,
                                                 resize=(width, height)):
                stream.truncate()
                stream.seek(0)
                input = np.frombuffer(stream.getvalue(), dtype=np.uint8)
                start_ms = time.time()
                results = engine.ClassifyWithInputTensor(input, top_k=5)
                elapsed_ms = time.time() - start_ms
                if results:
                    # camera.annotate_text = "%s %.2f\n%.2fms" % (
                    #     labels[results[0][0]], results[0][1], elapsed_ms*1000.0)
                    if results[0][1] < 0.2:
                        label = ""
                        target_value = 0.0
                    else:
                        label = labels[results[0][0]]
                        target_value = results[0][1]
                    camera.annotate_text = "%s %.1f\n%.2fms" % (
                        label, target_value, elapsed_ms*1000.0)
                    print(results)
        finally:
            camera.stop_preview()

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('model_path', type=str)
    args = parser.parse_args()

    model_path = args.model_path
    main(model_path)
