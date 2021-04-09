from pathlib import Path

import requests



class LineToochiKun:
    def __init__(self, token: str):
        self._token = token
        self._url = 'https://notify-api.line.me/api/notify'
        self._headers = {'Authorization': f'Bearer {self._token}'}

    def send_notify(self, report: str):
        data = {'message': report}
        res = requests.post(self._url,
                            headers=self._headers,
                            data=data)
        return res

    def send_image(self, report: str, image_path: str):
        message = report
        image = image_path  # png or jpg
        payload = {'message': message}
        files = {'imageFile': open(image, 'rb')}
        res = requests.post(self._url,
                            headers=self._headers,
                            params=payload,
                            files=files)
        return res

    def send_sticker(self, report: str, sticker):
        message = report
        sticker_package_id = sticker.__class__.ID.value
        sticker_id = sticker.value
        payload = {
            'message': message,
            'stickerPackageId': sticker_package_id,
            'stickerId': sticker_id,
        }
        res = requests.post(self._url,
                            headers=self._headers,
                            params=payload, )
        return res
