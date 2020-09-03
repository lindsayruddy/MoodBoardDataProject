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

def sort_shade(shade):
    shade_data = pd.DataFrame(columns = ["Shade", "ImageLocation"])
    count = 0
    for index, row in dataset.iterrows():
        if row['Shade'].lower() == shade:
            shade_data.loc[count] = [row['Shade']] + [row['ImageLocation']]
            count = count + 1

    return shade_data

def sort_room(room):
    room_data = pd.DataFrame(columns = ["Room", "ImageLocation"])
    count = 0
    for index, row in dataset.iterrows():
        if row['Room'].lower() == room:
            room_data.loc[count] = [row['Room']] + [row['ImageLocation']]
            count = count + 1

    return room_data


def write_csvs_with_specs(color, shade, room):
    final_data = pd.DataFrame(columns = ['ImageLocation'])

    # Color
    color_data = sort_color(color)
    final_data = pd.concat([color_data,final_data],join='inner')

    # Shade
    shade_data = sort_shade(shade)
    final_data = pd.concat([shade_data,final_data], join='inner')

    # Room
    room_data = sort_room(room)
    final_data = pd.concat([room_data,final_data], join='inner')

    final_data = final_data.drop_duplicates(subset=['ImageLocation'])
    final_data.to_csv("final_data.csv")
    return final_data


def main():
    # we make our input lowercase here too to match above
    color = input("Choose a color: ").lower()
    shade = input("Choose a shade: ").lower()
    room = input("Choose a room: "). lower()
    write_csvs_with_specs(color, shade, room)
    final = write_csvs_with_specs(color, shade, room)


if __name__ == "__main__":
    main()
