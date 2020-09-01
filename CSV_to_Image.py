import pandas as pd
import random

from PIL import Image
import cv2

def take_6(dataset):
    cols = len(dataset)
    #print(cols)
    count = 0
    for i in range(0,6):
        num = random.randint(0, cols - 1)
        img = cv2.imread(dataset['ImageLocation'][num])
        location = 'finalImage/image{}.jpg'.format(count)
        #print(location)
        cv2.imwrite(str(location), img)
        count = count + 1
#print(data['ImageLocation'][0])


def main():
    data = pd.read_csv("final_data.csv")
    take_6(data)


if __name__ == "__main__":
    main()
