# Prostate Cancer Classification according to Gleason Grading System using High-Resolution Net 


## Getting Stated

### Prerequisites
Before running the application, make sure you have the following installed:

- Python >= 3.8
- CUDA 11.6
- CUDAnn
- PyTorch 1.13
- A terminal (pwsh/zsh/cmd)

### Download and Extract Data
- Download the 'output' and 'data' folders from the specified link.
- Extract the folders in the `prostate_cancer_detection_hrnet_deploy/` directory.

### Installing Required Libraries
- Open the extracted folder in the terminal.
- Run the following command to install the required libraries: `pip install -r requirements.txt`. This may take a while.

### Splitting the Data
- Run the following command to split the data into train, test, and validation folders: `python docs/split.py`.
- Configure the input and output data directories in the `split.py` file.

### Running the User Interface (UI)
- Run the following command to start the User Interface (UI) for the application: `python main.py`.
- Open your browser and paste this URL: `http://127.0.0.1:5000/home`.
- Upload pictures from the test folder and the application will predict the output (e.g., Benign, Grade 3, Grade 4, Grade 5).

### Training the Model
- Run the following command to train the model: `python tools/train.py --cfg experiments/cls_hrnet_w48_sgd_lr5e-2_wd1e-4_bs32_x100.yaml`.
- Note: The model has already been trained until 100 epochs, so it will not train further. You can change the preferred number of epochs in the `.yaml` file (default: 100). If you don't have a powerful GPU, consider reducing the batch_size to 8 or 16 in the `.yaml` file.

### Validating the Model
- Run the following command to validate the model: `python tools/valid.py --cfg experiments/cls_hrnet_w48_sgd_lr5e-2_wd1e-4_bs32_x100.yaml --testModel output\imagenet\cls_hrnet_w48_sgd_lr5e-2_wd1e-4_bs32_x100\model_best.pth.tar`.
- It will show the accuracy of the pretrained model. In this case, the accuracy is 94.444%.

## Contributing
If you want to contribute to this project:

1. Fork the repository
2. Clone the repository to your local machine
3. Create a new branch with a descriptive name
4. Make changes and commit them to your branch
5. Push the changes to your forked repository
6. Submit a pull request to the main repository with a detailed explanation of your changes

## Author
- [khushaalan](https://github.com/khushaalan)

## License
This project is licensed under the MIT License

## Acknowledgments
- Project inspiration (https://github.com/HRNet/HRNet-Image-Classification)
- Dataset source (HKUM Dataset)
