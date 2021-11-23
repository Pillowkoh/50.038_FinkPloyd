from types import FrameType
import opensmile
import audiofile
import pandas as pd
from os import listdir
from os.path import isfile, join

smile = opensmile.Smile(
    feature_set=opensmile.FeatureSet.ComParE_2016,
    feature_level=opensmile.FeatureLevel.LowLevelDescriptors
)

path = './archive/DEAM_audio/WAV_audio'
save_feature_path = './archive/features/opensmile_time_series/'

feature_set = pd.DataFrame()

file_data = [f for f in listdir(path) if isfile (join(path, f))]
for line in file_data:
    if ( line[-1:] == '\n' ):
        line = line[:-1]

    # Reading Song
    songname = path + '/' + line

    print(songname)
    y = smile.process_file(songname)

    save_path = save_feature_path+line.split('.')[0]+'.csv'
    y.to_csv(save_path, index=True)
    print(y)

# print(len(smile.feature_names))