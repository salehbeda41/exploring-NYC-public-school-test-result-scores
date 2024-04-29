
```markdown
# NYC Public School SAT Performance Analysis

This project analyzes the performance of New York City (NYC) public schools in SAT exams. It answers three key questions regarding SAT scores, math performance, and borough-wise statistics.

## Dataset

The dataset used for this analysis is provided in `schools.csv`. It contains information about NYC public schools, including school names, borough, average scores in math, reading, and writing SAT sections, and the percentage of students tested. This dataset belongs to DataCamp and is used as part of the Associate Data Science track.

## Requirements

To run the analysis, you'll need Python installed on your system along with the pandas library.

```bash
pip install pandas
```

## Questions Answered

1. **Which NYC schools have the best math results?**
   - Identifies schools with at least 80% of the maximum possible score of 800 for math and lists them in descending order of average math scores.

2. **What are the top 10 performing schools based on the combined SAT scores?**
   - Ranks the top 10 schools based on the total combined SAT scores.

3. **Which single borough has the largest standard deviation in the combined SAT score?**
   - Determines the borough with the largest standard deviation in combined SAT scores and provides additional statistics such as the number of schools, average SAT score, and standard deviation.

## Usage

1. Clone the repository:

```bash
git clone https://github.com/salehbeda41/nyc-public-school-sat-analysis.git
```

2. Navigate to the project directory:

```bash
cd exploring-NYC-public-school-test-result-scores
```

3. Run the Python script:

```bash
python main.py
```

This will perform the analysis and print the results to the console.

## Contributing

Contributions are welcome! If you have any suggestions, improvements, or additional analysis ideas, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

This project is a part of the Associate Data Science track in DataCamp. The dataset used in this analysis belongs to DataCamp.
```