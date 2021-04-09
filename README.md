# LINE Toochi-Kun for LTK: LINE for notifying the progress of the training of AI
This is still my small-personal utility :)

![S__20668421](https://user-images.githubusercontent.com/1684732/114170227-937f2380-996d-11eb-83fe-7b77a6cfcbf6.jpg)

## How to use
1. Get access token of LINE notify from https://notify-bot.line.me/my/
2. Put your token to create the LTK instance of the class(!!! Be careful not to accidentally publish it to the public !!!)

## Example
```python
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
```

## TODO(?)
- Add some nice methods for the notification during ML training process
