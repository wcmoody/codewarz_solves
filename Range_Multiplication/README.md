# Range_Multiplication

# Description

<p>You are given a file with 3 numbers per line, separated by spaces. For each line in the input file, print a list of all numbers from the 1st to the 3rd number (non-inclusive) that are multiples of both the first and second number.</p>

## Sample Input:

```
$ cat sample.txt
3 6 9
2 4 40
3 5 1000
```
## Expected Output:

```
$ ./solve.py sample.txt
[6]
[4, 8, 12, 16, 20, 24, 28, 32, 36]
[15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 180, 195, 210, 225, 240, 255, 270, 285, 300, 315, 330, 345, 360, 375, 390, 405, 420, 435, 450, 465, 480, 495, 510, 525, 540, 555, 570, 585, 600, 615, 630, 645, 660, 675, 690, 705, 720, 735, 750, 765, 780, 795, 810, 825, 840, 855, 870, 885, 900, 915, 930, 945, 960, 975, 990]
```
## Expected SHA1 Hash:

```
cee4b38bcfbec028aff1bd5a31738e0ec9c61263
```
