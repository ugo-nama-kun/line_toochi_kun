from toochikun.toochikun import LineToochiKun

import datetime
import numpy
import matplotlib.pyplot as plt


def main():
    line = LineToochiKun(token="Use your token")
    # line.send_notify("hello~")
    # line.send_sticker()

    now = datetime.datetime.now()
    plt.plot(numpy.random.randn(1000))
    plt.savefig("data/img.png")
    line.send_image(
        report=str(now),
        image_path="data/img.png"
    )


if __name__ == "__main__":
    main()