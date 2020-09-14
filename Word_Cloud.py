import matplotlib.pyplot as plt
import numpy as np
import os
from os import path
from PIL import Image
from wordcloud import WordCloud, ImageColorGenerator, STOPWORDS

from text_to_frequency_dict import sorted_frequency_dict

def masked_image_from_freq_dict(text_dict, given_mask):

    wc = WordCloud(background_color="white", max_words=200, mask=given_mask, contour_width=1, contour_color='black')
    # generate word cloud
    wc.generate_from_frequencies(text_dict)

    #image_colors = ImageColorGenerator(given_mask)
    # show
    #.recolor(color_func=image_colors),
    plt.imshow(wc, interpolation="bilinear")
    plt.axis("off")
    plt.show()


# get data directory (using getcwd() is needed to support running example in generated IPython notebook)
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

# script taken from ham4corpus
hamilton_full_text = open('Michelle_Obama_Speech.txt', encoding="utf-8").read()
#print(sorted_frequency_dict(hamilton_full_text))

## .png taken from https://www.vhv.rs/viewpic/hTwmwoh_michelle-obama-png-michelle-obama-black-and-white/
michelle_obama_mask = np.array(Image.open(path.join(d, "filelibertarian-party-ballot-access-locator-map-1996-united-united-states-of-america-png-6000_3710.png")))

masked_image_from_freq_dict(sorted_frequency_dict(hamilton_full_text), michelle_obama_mask)