import pandas as pd
import numpy as np

dataset = pd.read_csv("MoodBoardData.csv")


def sort_color(color):
    # creating a dataframe to add all matching rows to
    color_data = pd.DataFrame(columns = ["Color","ImageLocation"])
    # so that we dont overwrite the rows when we add to it
    count = 0
    # Here we are iterating through the rows to check if the input color is
    # the color of our dataset row
    for index, row in dataset.iterrows():
        if row['Color'] == color:
            # we make them all lowercase here so that a user doesnt input a lowercase
            # that is the same type that still doesnt come up
            color_data.loc[count] = [row['Color'].lower()] + [row['ImageLocation']]
            count = count + 1

    return color_data

## def sort_shade(shade):

## def sort_room(room):



def write_csvs_with_specs(color):
    final_data = pd.DataFrame(columns = ['ImageLocation'])

    # Color
    color_data = sort_color(color)
    final_data = pd.concat([color_data,final_data],join='inner')

    # Shade

    # Room

    final_data.to_csv("final_data.csv")



def main():
    # we make our input lowercase here too to match above
    color = input("Choose a color: ").lower()

    write_csvs_with_specs(color)


if __name__ == "__main__":
    main()
