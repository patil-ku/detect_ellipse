# detect_ellipse
Simple script that will detect an ellipse in a given image and find the coordinates to generate it. 

# What it does:
Essentially, feed it an image which has an ellipse in it, it will output a picture of the closest ellipse the program could find, and then generate coordinates for that ellipse. The formula is for an ellipse in it's standard form: 
```
((x - x0)^2 / a^2) + ((y - y0)^2 / b^2) = 1

Where,
(x0,y0) are the coordinates of the ellipse center,
a is the semi-major axis length,
b is the semi-minor axis length.
```

## Installation and running the code:

- Make sure you have python installed.
- Clone this repository using `git clone git@github.com:patil-ku/detect_ellipse.git` OR
- Just download the zip and extract it. You should find the download button 
- In a directory where you will run this code, install a virtual environment using the command:
  
  ```
  virtualenv venv
  ```
- Activate this venv once created:
  
  ```
  source venv/bin/activate
  ```
- Install the required package:
  
  ```
  pip install -r requirements.txt
  ```
At this point, you have successfully installed everything, and you are good to run the code.
- Run the code:

  ```
  python get_equation.py
  ```
- Make sure you update the path variable in the code `image_path` to reflect where your file is kept in the system.
- Once the image is generated press `0` to close the image.
- Program should output required results after this.
  
