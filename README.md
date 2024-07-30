# 1. Folder Structure

.
├── docs
├── model                                                                 # trained model, saved all code the models
│   └── 2018-11-22_14-44_se_resnext50_16x4d_usgn_64_gaze_xVal0
├── pulsepytools                                                          # the PULSE's pulsepytools: 2.0.0 (64f8103770ae19dd8c5324e61459b72a27fa0a4e)
├── tests
│   ├── configuration.py
│   └── test_inference.py
├── usgazenet                                                             # the us gaze data
|   ├── __init__.py
|   ├── classifier.py
|   ├── config
|   ├── datasets.py
|   ├── eval.py
|   ├── model.py
|   ├── models
|   ├── retrain.py
│   ├── salretrain.py
│   └── train.py
│
├── requirements.txt
└── readme.md
