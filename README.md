# Histogram Automation for Statistical Analysis
A Python tool that automates the creation of histograms and frequency distribution tables from datasets, following theoretical statistical analysis methodology.
## Live Coding Session
Watch the full development process: [YouTube Link - Coming Soon]
## Academic Context
**Institution:** Faculty of Computer and Information Sciences, Ain Shams University  
**Course:** CIS 240 - Statistical Analysis  
**Special Thanks:** Dr. Diaa for the excellent teaching and guidance throughout this course
## Features
- Automatically calculates statistical measures (min, max, range, sample size)
- Determines optimal number of subintervals using √n method
- Computes frequency and relative frequency distributions
- Generates side-by-side frequency table and histogram visualization
- Handles decimal precision automatically based on dataset
## Technologies
- **Python 3.13**
- **Matplotlib** (visualization only)
- No pandas, no numpy - pure Python implementation
## Methodology
The project follows standard statistical histogram construction steps:
1. Find minimum and maximum data points
2. Calculate range (max - min)
3. Determine subintervals using √n (rounded up)
4. Calculate interval width: Range / Number of subintervals
5. Create interval boundaries with consistent decimal precision
6. Count frequencies for each interval
7. Generate frequency table and histogram
## Usage
1. Prepare your dataset as a CSV file (comma-separated values)
2. Update the filename in the code:
```py
file = open("dataset_1.csv", "rt")
```
3. Run the script:
```bash
python histogram_generator.py
```
## Input Format
The dataset should be a CSV file with comma-separated numerical values:
```csv
2.0,3.0,0.3,3.3,1.3,0.4,0.2,6.0,5.5,6.5,2.5,2.3...
```
## Output
- Console output with all statistical measures
- Interactive matplotlib window displaying:
- Frequency distribution table (left)
![table_pic](attachments/table)
- Histogram visualization (right)
![histogram_pic](attachments/histogram)
## Example Output
The tool generates a comprehensive view with:
- Intervals column showing data ranges
- Frequency counts for each interval
- Relative frequencies (as decimals)
- Visual histogram with proper binning
## Educational Context
This project was developed as part of a theoretical statistical analysis course, demonstrating the practical implementation of histogram construction principles taught in statistics classes.
## License
MIT License - Feel free to use for educational purposes
## Contributing
This is an educational project, but suggestions and improvements are welcome!

---

_Developed as part of Statistical Analysis coursework - demonstrating core concepts without relying on high-level data science libraries._