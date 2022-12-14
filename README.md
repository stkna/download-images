# download-images

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
