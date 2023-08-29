from load_csv import load
import matplotlib.pyplot as plt


def main():
    """
    Load life expectancy data, filter for Germany, and display a line graph.

    Loads the life expectancy dataset from a CSV file, filters the data for
    Germany, and displays a line graph showing the life expectancy in Germany
    over the years. The x-axis of the graph includes year labels from
    1800 to 2080, with every 40th year label displayed and rotated for clarity.
    The graph includes a title, axis labels, legend, and grid.
    """
    dataset = load("life_expectancy_years.csv")
    germany_data = dataset[dataset['country'] == 'Germany']
    years = germany_data.columns[1:]
    life_expectancy = germany_data.values[0][1:]

    plt.plot(years, life_expectancy, marker='o', label='Germany')
    plt.title('Life Expectancy in Germany Over the Years')
    plt.xlabel('Year')
    plt.ylabel('Life Expectancy')
    plt.xticks(years[::40], rotation=45)  # Display every 40 years
    plt.legend()
    plt.grid()
    plt.tight_layout()  # Ensures labels fit nicely
    plt.show()


if __name__ == "__main__":
    main()
