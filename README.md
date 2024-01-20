# PNG to ICO Converter

## Readme
1. [Readme: Italiano](./README_IT.md)
2. [Readme: English](./README.md)

## Description
This program is a converter from PNG to ICO. It allows you to select a PNG file and convert it to an ICO file. ICO is a file format used for icons in Windows operating systems.

## Dependencies
- PyQt5
- pillow

## Usage
1. Install the necessary dependencies:
```
pip install PyQt5
pip install pillow
```

2. Run the program:
```
python converter.pyw
```

3. In the main window of the program, click on the "Convert from PNG to ICO" button.

4. A file dialog window will appear to select a PNG file to convert. Select the desired file and click "Open".

5. A check will be performed to verify if the selected file is indeed a PNG file. If it's not, an error message will be displayed.

6. Next, a file dialog window will appear to select the save location for the converted ICO file. Select the desired location and click "Save".

7. The PNG file will be converted to an ICO file and a confirmation message will be displayed with the save location of the ICO file.

## Compiling the program

1. Install the necessary dependencies:
```shell
pip install pyinstaller
```

2. Once PyInstaller is installed, you can use it to create an executable from your Python script. The file `version_info.txt` contains information about the executable to be created. Here is an example command to create an executable on Windows:

```shell
pyinstaller --onefile --windowed --icon=img/logo.ico --name=PNGtoICO --version-file=version_info.txt converter.pyw
```

## Executable

In the `build` folder, you will find the file `PNGtoICO.zip`, which contains the executable version of the `converter.pyw` script.

## Screenshot

![Screenshot PNGtoICO](img/screenshot.png)
