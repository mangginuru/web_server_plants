import io
import torch
from efficientnet_pytorch import EfficientNet
from PIL import Image
import torchvision.transforms as transforms


def get_model():
    model = EfficientNet.from_pretrained(model_name="efficientnet-b7", num_classes=20)
    model.load_state_dict(torch.load('best_weights_b7_9.pt', map_location=torch.device('cpu')))
    model.eval()
    return model


def transform_image(image_bytes):
    my_transforms = transforms.Compose([transforms.Resize((224, 224)), 
                                        transforms.ToTensor(),
                                        transforms.Normalize(
                                        [0.485, 0.456, 0.406],
                                        [0.229, 0.224, 0.225])])
    image = Image.open(io.BytesIO(image_bytes))
    return my_transforms(image).unsqueeze(0)
