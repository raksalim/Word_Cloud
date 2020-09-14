import matplotlib.pyplot as plt
import numpy as np
import os
from os import path
from PIL import Image
from wordcloud import WordCloud, ImageColorGenerator, STOPWORDS

from text_to_frequency_dict import sorted_frequency_dict

def masked_image_from_freq_dict(text_dict, given_mask):

    wc = WordCloud(background_color="white", max_words=200, mask=given_mask, contour_width=1, contour_color='purple')
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
text_document = open('black_panther_script', encoding="utf-8").read()

## .png taken from https://favpng.com/png_download/ukQPKw63
#mask = np.array(Image.open(path.join(d, "FAVPNG_united-states-we-can-do-it-rosie-the-riveter-clip-art_ukQPKw63.png")))


## black_panther.png taken from https://www.deviantart.com/camo-flauge/art/Black-Panther-Vibranium-Transparent-729173846
mask = np.array(Image.open(path.join(d, "black_panther_mask.png")))

masked_image_from_freq_dict(sorted_frequency_dict(text_document), mask)