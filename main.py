from sticker import CherryCoco


import datetime
import numpy
import matplotlib.pyplot as plt

from toochikun.toochikun import LineToochiKun


def main():
    line = LineToochiKun(token="Your Token")

    # send message notification
    line.send_notify("hello~")

    # send image
    now = datetime.datetime.now()
    plt.plot(numpy.random.randn(1000))
    plt.savefig("data/img.png")
    line.send_image(
        report=str(now),
        image_path="data/img.png"
    )

    # send sticker
    res = line.send_sticker(
        report=str(now),
        sticker=CherryCoco.merry_christmas
    )


if __name__ == "__main__":
    main()