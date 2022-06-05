import cfp_dataloader as cfp
from deepface import DeepFace

# ff = cfp.ff()
# diff, same = ff.loadcurrentfold()
# print(same)
fp = cfp.fp()
# _, same = fp.loadcurrentfold()
# print(same)

result = DeepFace.verify('./cfp-dataset/Data/Images/001/frontal/01.jpg', './cfp-dataset/Data/Images/001/profile/01.jpg',
                         detector_backend='retinaface', enforce_detection=False)
print(result)
#deepface test
# def deepfacetest():
#     result = DeepFace.verify('./cfp-dataset/Data/Images/001/frontal/01.jpg', './cfp-dataset/Data/Images/001/profile/01.jpg')