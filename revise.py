import torch
# import torchvision.models as models
from torchvision.models import resnet50

# 加载 ResNet50 模型，但不使用预训练参数
model = resnet50(weights=None)

# 加载你已经下载的模型权重 resnet50-0676ba61.pth
pth_file = "/home/codespace/.cache/torch/hub/checkpoints/resnet50-0676ba61.pth"
state_dict = torch.load(pth_file)

# 将权重加载到模型中
model.load_state_dict(state_dict)

# (可选) 如果你想对模型权重进行修改
# 例如，修改 conv1 的权重
# with torch.no_grad():
#     model.conv1.weight *= 2  # 将卷积层的权重乘以 2 作为示例ls


# 保存修改后的模型权重
torch.save(model.state_dict(), "/home/codespace/.cache/torch/hub/checkpoints/resnet50-0676ba61.pth")
