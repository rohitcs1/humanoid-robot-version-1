from luma.core.interface.serial import i2c
from luma.oled.device import sh1106
from PIL import Image, ImageDraw, ImageFont
import time


class RobotFace:

    WIDTH = 128
    HEIGHT = 64

    def __init__(self):

        serial = i2c(port=1, address=0x3C)
        self.device = sh1106(serial)

        self.font = ImageFont.load_default()

    def clear(self):
        self.device.clear()

    def _show(self, img):
        self.device.display(img)

    def _draw_title(self, draw, text):

        bbox = draw.textbbox((0, 0), text, font=self.font)

        text_width = bbox[2] - bbox[0]

        x = (self.WIDTH - text_width) // 2

        draw.text(
            (x, 2),
            text.upper(),
            font=self.font,
            fill=255
        )

    def _play(self, frames, fps=10, duration=1):

        frame_delay = 1 / fps
        end_time = time.time() + duration

        while time.time() < end_time:

            for frame in frames:

                self._show(frame)
                time.sleep(frame_delay)

                if time.time() >= end_time:
                    break

    ########################################################
    # HAPPY
    ########################################################

    def happy(self, duration=1.5):

        frames = []

        for mouth in [0, 3, 6, 3]:

            img = Image.new("1", (128, 64))
            d = ImageDraw.Draw(img)

            self._draw_title(d, "Happy")

            d.ellipse((30, 18, 42, 30), fill=255)
            d.ellipse((86, 18, 98, 30), fill=255)

            d.arc(
                (38, 34 - mouth, 90, 58 + mouth),
                0,
                180,
                fill=255,
                width=2
            )

            frames.append(img)

        self._play(frames, fps=8, duration=duration)

    ########################################################
    # SAD
    ########################################################

    def sad(self, duration=1.5):

        frames = []

        for eye in [0, 1, 2, 1]:

            img = Image.new("1", (128, 64))
            d = ImageDraw.Draw(img)

            self._draw_title(d, "Sad")

            d.ellipse((30, 18 + eye, 42, 30 + eye), fill=255)
            d.ellipse((86, 18 + eye, 98, 30 + eye), fill=255)

            d.arc(
                (40, 36 - eye, 88, 58 - eye),
                180,
                360,
                fill=255,
                width=2
            )

            frames.append(img)

        self._play(frames, fps=8, duration=duration)

    ########################################################
    # ANGRY
    ########################################################

    def angry(self, duration=1.5):

        frames = []

        for i in [0, 2, 0]:

            img = Image.new("1", (128, 64))
            d = ImageDraw.Draw(img)

            self._draw_title(d, "Angry")

            d.line((25, 18 + i, 42, 22), fill=255, width=2)
            d.line((103, 18 + i, 86, 22), fill=255, width=2)

            d.ellipse((30, 24, 40, 34), fill=255)
            d.ellipse((88, 24, 98, 34), fill=255)

            d.arc(
                (42, 42, 86, 50),
                180,
                360,
                fill=255,
                width=2
            )

            frames.append(img)

        self._play(frames, fps=10, duration=duration)

    ########################################################
    # NEUTRAL
    ########################################################

    def neutral(self, duration=1):

        img = Image.new("1", (128, 64))
        d = ImageDraw.Draw(img)

        self._draw_title(d, "Neutral")

        d.ellipse((30, 20, 42, 32), fill=255)
        d.ellipse((86, 20, 98, 32), fill=255)

        d.line((46, 48, 82, 48), fill=255, width=2)

        self._play([img], fps=1, duration=duration)

    ########################################################
    # BLINK
    ########################################################

    def blink(self):

        frames = []

        img = Image.new("1", (128, 64))
        d = ImageDraw.Draw(img)

        self._draw_title(d, "Blink")

        d.ellipse((30, 20, 42, 32), fill=255)
        d.ellipse((86, 20, 98, 32), fill=255)

        frames.append(img)

        img = Image.new("1", (128, 64))
        d = ImageDraw.Draw(img)

        self._draw_title(d, "Blink")

        d.rectangle((30, 25, 42, 27), fill=255)
        d.rectangle((86, 25, 98, 27), fill=255)

        frames.append(img)

        img = Image.new("1", (128, 64))
        d = ImageDraw.Draw(img)

        self._draw_title(d, "Blink")

        d.line((30, 26, 42, 26), fill=255, width=2)
        d.line((86, 26, 98, 26), fill=255, width=2)

        frames.append(img)

        self._play(frames + frames[::-1], fps=18, duration=0.4)

    ########################################################
    # STARTUP SCREEN
    ########################################################

    def show_name(self):

        img = Image.new("1", (128, 64))
        d = ImageDraw.Draw(img)

        # Title
        self._draw_title(d, "ALPHA")

        # Subtitle (center)
        text = "AI ROBOT"

        bbox = d.textbbox((0, 0), text, font=self.font)
        text_width = bbox[2] - bbox[0]

        x = (self.WIDTH - text_width) // 2

        d.text(
            (x, 28),
            text,
            font=self.font,
            fill=255
        )

        self._show(img)
