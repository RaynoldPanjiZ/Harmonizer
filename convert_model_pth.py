import torch
from src.train.harmonizer import module
# from src import model

ckpt_path = 'pretrained/checkpoint_60.ckpt'
pth_path = 'pretrained/harmonizer_new.pth'


ckpt = torch.load(ckpt_path)['model']

for k in list(ckpt.keys()):
    if 'module.model.' in k:
        ckpt[k[13:]] = ckpt[k]
        del ckpt[k]
# print(ckpt.keys())

harmonizer = module.Harmonizer()
harmonizer.load_state_dict(ckpt)
harmonizer.eval()

state = harmonizer.state_dict()
torch.save(state, pth_path)