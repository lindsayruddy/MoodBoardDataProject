import pandas as pd
import numpy as np
from IPython.core.display import HTML


dataset = pd.read_csv("MoodBoardData.csv")


def sort(column, name):
    data = pd.DataFrame(columns = ["ImageLocation"])
    count = 0
    for index, row in dataset.iterrows():
        if row[name].lower() == column:
            data.loc[count] = row['ImageLocation']
            count = count + 1

    return data

def write_csvs_with_specs(color, cname, shade, sname, room, rname):
    final_data = pd.DataFrame(columns = ['ImageLocation'])

    # Color
    color_data = sort(color, cname)
    final_data = pd.concat([color_data,final_data],join='inner')

    # Shade
    shade_data = sort(shade, sname)
    final_data = pd.concat([shade_data,final_data], join='inner')

    # Room
    room_data = sort(room, rname)
    final_data = pd.concat([room_data,final_data], join='inner')

    #If we add a tag, add a line hear calling sort with the input and column name
    #Update parameters above

    # Final writing of CSV
    final_data = final_data.drop_duplicates(subset=['ImageLocation'])

    final_data.to_csv("final_data.csv")
    return final_data


def main():
    # we make our input lowercase here too to match above
    color = input("Choose a color: ").lower()
    shade = input("Choose a shade: ").lower()
    room = input("Choose a room: "). lower()
    #Ask user for more information here as we add more tags

    #Add these new tags to parameters here
    write_csvs_with_specs(color, "Color", shade, "Shade", room, "Room")
    # final = write_csvs_with_specs(color, shade, room)


if __name__ == "__main__":
    main()
