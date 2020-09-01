import pandas as pd
import numpy as np
from IPython.core.display import HTML


dataset = pd.read_csv("MoodBoardData.csv")


def sort_color(color):
    color_data = pd.DataFrame(columns = ["Color","ImageLocation"])
    count = 0
    for index, row in dataset.iterrows():
        if row['Color'].lower() == color:
            color_data.loc[count] = [row['Color']] + [row['ImageLocation']]
            count = count + 1

    return color_data

## def sort_lightdark(shade):

## def sort_room(room):



def write_csvs_with_specs(color):
    final_data = pd.DataFrame(columns = ['ImageLocation'])

    # Color
    color_data = sort_color(color)
    final_data = pd.concat([color_data,final_data],join='inner')

    # Shade

    # Room

    final_data.to_csv("final_data.csv")
    return final_data


def main():
    color = raw_input("Choose a color: ")
    final = write_csvs_with_specs(color)


if __name__ == "__main__":
    main()
