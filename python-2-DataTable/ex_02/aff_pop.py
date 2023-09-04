from load_csv import load
import matplotlib.pyplot as plt


def preprocess_population(pop_str):
    """
    Preprocesses the population string to convert it into
    a numeric value in standard form.

    Args:
        pop_str (str): Population string with or without
        the 'M' suffix for million.

    Returns:
        float: Numeric population value.
    """
    if pop_str.endswith("M"):
        return float(pop_str[:-1]) * 1e6
    elif pop_str.endswith("k"):
        return float(pop_str[:-1]) * 1e3
    else:
        return float(pop_str)


def main():
    """
    Loads population data from a CSV file, processes and
    plots(used for creating line plots)
    the population comparison of three countries.
    """
    data = load("population_total.csv")

    campus = "Germany"
    country = "France"
    home = "Hungary"

    germany_data = data[data['country'] == campus].iloc[:, 1:]
    france_data = data[data['country'] == country].iloc[:, 1:]
    hungary_data = data[data['country'] == home].iloc[:, 1:]

    germany_pop = germany_data.values.flatten()
    france_pop = france_data.values.flatten()
    hungary_pop = hungary_data.values.flatten()
    years = germany_data.columns.astype(int)

    germany_pop = [preprocess_population(pop) for pop in germany_pop]
    france_pop = [preprocess_population(pop) for pop in france_pop]
    hungary_pop = [preprocess_population(pop) for pop in hungary_pop]

    plt.plot(years, germany_pop, label=campus)
    plt.plot(years, france_pop, label=country)
    plt.plot(years, hungary_pop, label=home)

    plt.title("Population in {}, {} and {}".format(campus, country, home))
    plt.xlabel("Year")
    plt.xticks(range(1800, 2051, 40), range(1800, 2051, 40))
    plt.xlim(1800, 2040)
    plt.ylabel("Population")
    plt.legend()
    plt.tight_layout()
    max_pop = max(max(germany_pop), max(france_pop), max(hungary_pop))
    y_ticks = [i * 1e7 for i in range(int(max_pop / 1e7) + 1)]
    plt.yticks(y_ticks, ["{:,.0f}M".format(pop / 1e6) for pop in y_ticks])
    plt.show()


if __name__ == "__main__":
    main()
