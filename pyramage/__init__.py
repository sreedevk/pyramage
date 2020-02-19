import numpy as np
import sys
import matplotlib.pyplot as plt

class Pyramage:
    @staticmethod
    def get_local_pixels(image, current_ri, current_ci, depth=2):
        local_pixels = []
        local_pixel_values = np.array([])
        for iter_idx in range(1, depth):
            current_lpix = {
                'left': {
                    'ownrow': [current_ri, current_ci-iter_idx],
                    'upperrow': [current_ri-iter_idx, current_ci-iter_idx],
                    'lowerrow': [current_ri+iter_idx, current_ci-iter_idx]
                },
                'right': {
                    'ownrow': [current_ri, current_ci+iter_idx],
                    'upperrow': [current_ri-iter_idx, current_ci+iter_idx],
                    'lowerrow': [current_ri+iter_idx, current_ci+iter_idx]
                },
                'straight': {
                    'upperrow': [current_ri-iter_idx, current_ci],
                    'lowerrow': [current_ri+iter_idx, current_ci]
                }
            }

        if current_ci > iter_idx:
            local_pixels.extend([current_lpix['left']['ownrow']])
        if current_ci < (np.size(image, 1) - iter_idx):
            local_pixels.extend([current_lpix['right']['ownrow']])
        if current_ri > iter_idx:
            local_pixels.extend([current_lpix['straight']['upperrow']])
            if current_ci > iter_idx:
                local_pixels.extend([current_lpix['left']['upperrow']])
            if current_ci < (np.size(image, 1) - iter_idx):
                local_pixels.extend([current_lpix['right']['upperrow']])
        if current_ri < (np.size(image, 1) - iter_idx):
            local_pixels.extend([current_lpix['straight']['lowerrow']])
            if current_ci > iter_idx:
                local_pixels.extend([current_lpix['left']['lowerrow']])
            if current_ci < (np.size(image, 1) - iter_idx):
                local_pixels.extend([current_lpix['right']['lowerrow']])

        for pixel_coord in local_pixels:
            local_pixel_values = np.append(local_pixel_values, [image[pixel_coord[0]][pixel_coord[1]]])
        return local_pixel_values



    @staticmethod
    def generate_random_image(image_size):
        return np.random.random((image_size, image_size))

    @staticmethod
    def adjust_pixels(image_pixdat, scan_depth=2):
        for ridx, row in enumerate(image_pixdat):
            for cidx, _ in enumerate(row):
                image_pixdat[ridx][cidx] = np.average(
                    Pyramage.get_local_pixels(image_pixdat, ridx, cidx, scan_depth)
                )
        return image_pixdat

    @staticmethod
    def generate_perlin_image(img_size=100, perlin_depth=4, color_map='terrain'):
        IMG = Pyramage.generate_random_image(img_size)
        IMG = Pyramage.adjust_pixels(IMG, perlin_depth)
        plt.imshow(IMG, cmap=color_map)
        plt.show()
