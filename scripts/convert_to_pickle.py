from PIL import Image
import glob
import numpy as np
import pickle
import random, string
import os


def open_pickle_and_marge(path_to_pickle):
    print("Generating test data start")
    x_train_files = glob.glob(path_to_pickle + '/x_train_*.pickle')
    X = np.array([])
    Y = np.array([])

    for i, x_train_file in enumerate(x_train_files):
        suffix_and_extension = x_train_file.split("/")[-1].lstrip("x_train_")
        y_train_file = path_to_pickle + '/y_train_' + suffix_and_extension

        print(y_train_file)
        print(".", end="")

        with open(x_train_file, mode='rb') as f:
            x_train = pickle.load(f)

        with open(y_train_file, mode='rb') as f:
            y_train = pickle.load(f)

        if i == 0:
            X = np.array(x_train)
            Y = np.array(y_train)
        else:
            X = np.append(X, x_train, axis=0)
            Y = np.append(Y, y_train)
        del x_train, y_train
    print("")
    print("Generating test data finished")
    return X, Y


def get_random_str(n):
    randlst = [random.choice(string.ascii_letters + string.digits) for i in
               range(n)]
    return ''.join(randlst)


def save_pickle(save_path, x_train, y_train, suffix):
    with open(save_path + '/x_train_' + suffix + '.pickle', mode='wb') as f:
        pickle.dump(x_train, f)
    with open(save_path + '/y_train_' + suffix + '.pickle', mode='wb') as f:
        pickle.dump(y_train, f)


def generate_test_data_from_file_list(file_list):
    # X = np.empty((1, 224, 224, 3), dtype = np.float32)
    # Y = np.empty((1, 1), dtype = np.int)
    X = np.array([])
    Y = np.array([])

    for i, file in enumerate(file_list):
        print(".", end="")
        index = int(file.split("/")[-1].split("_")[1])
        image = Image.open(file)
        image = image.convert("RGB")
        data = np.asarray(image)
        if i == 0:
            X = np.array([data])
            Y = np.array([index])
        else:
            X = np.append(X, [data], axis=0)
            Y = np.append(Y, [index])
    print("")
    return X, Y


def generate_file_list_2d_from_file_path(path_to_images, file_prefix, compart_num):
    file_list = glob.glob(path_to_images + '/' + file_prefix + '*.jpg')
    return [file_list[i:i + compart_num] for i in range(0, len(file_list), compart_num)]


def main(path_to_images, class_num, compart_num, prefix):
    print("Generating test data start")
    for i in range(class_num):
        zero_filled_index = str(i).zfill(2)
        file_prefix = prefix + "_" + zero_filled_index
        file_list_2d = generate_file_list_2d_from_file_path(path_to_images,
                                                            file_prefix,
                                                            compart_num)
        for file_list in file_list_2d:
            x_train, y_train = generate_test_data_from_file_list(file_list)
            suffix = zero_filled_index + "_" + get_random_str(8)

            save_pickle(path_to_images, x_train, y_train, suffix)
            del x_train, y_train

    print("Generating test data finished")
    print("The pickle file putted to " + path_to_images)


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()

    parser.add_argument('path_to_images', type=str, help='File path to the images for training.')
    parser.add_argument('class_num', type=int, help='Total number of classes.')
    parser.add_argument('--compart_num', type=int, help='The number of images included per pickele file', default=100)
    parser.add_argument('--image_file_prefix', type=str, help='Target image file prefix.', default="pict")

    args = parser.parse_args()

    path_to_images = args.path_to_images

    main(args.path_to_images, args.class_num, args.compart_num, args.image_file_prefix)
