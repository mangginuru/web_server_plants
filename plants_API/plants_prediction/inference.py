import json
from plants_API.plants_prediction.commons import get_model, transform_image

model = get_model()
imagenet_class_index = json.load(open('image_class.json', encoding='utf-8'))


def get_prediction(image_bytes):
    try:
        tensor = transform_image(image_bytes=image_bytes)
        outputs = model.forward(tensor)
    except Exception:
        return 0, 'error'
    _, y_hat = outputs.max(1)
    predicted_idx = str(y_hat.item())
    return imagenet_class_index[predicted_idx]