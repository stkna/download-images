# download-images

```
This is a Python script that downloads images from a list of URLs. The URLs are stored in a text file called lista_urls.txt, and the images are saved in a directory called imagenes.

The script first creates the imagenes directory if it doesn't already exist. Then, it opens the lista_urls.txt file in read mode and reads each line in the file. If the line is not empty, the script generates a file name using a counter and downloads the image at the URL specified in the line. The image is saved in the imagenes directory with the generated file name. The counter is incremented after each iteration so that each image has a unique file name.
```

### Github Action - How it works

```
This is a GitHub Action that uses Python to run a script called download-img.py. The Action is triggered when a new commit is pushed to the main branch and the file lista_urls.txt is changed.

When the Action runs, it will do the following:

1. Check out the latest version of the repository
2. Set up a Python environment with version 3.8
3. Run the download-img.py script
4. Upload the imagenes directory as an artifact

It is not clear from the code what the download-img.py script does, but it likely downloads images from a list of URLs specified in the lista_urls.txt file.
```
