# remove_bg.py
import cv2
import numpy as np

from src.rmbg.briarmbg import briarmbg_process, create_briarmbg_session


class RemoveBG:
    def __init__(self):
        self.session, self.device = create_briarmbg_session()
        self.remove = briarmbg_process

    def gen_image(self, rgb_np_img) -> np.ndarray:
        bgr_np_img = cv2.cvtColor(rgb_np_img, cv2.COLOR_RGB2BGR)
        output = self.remove(bgr_np_img, session=self.session, device=self.device)
        return cv2.cvtColor(output, cv2.COLOR_BGRA2RGBA)
