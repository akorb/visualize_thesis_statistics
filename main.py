import pandas as pd


LETTERS = 'data/letter_counts'
WORDS = 'data/word_counts'


def plot_file(input, output, title, sort_by, ascending=True, strip=None):
    df = pd.read_fwf(input, header=None)
    df.sort_values(by=sort_by, ascending=ascending, inplace=True)
    if strip:
        df = df.iloc[:strip]
    ax = df.plot.bar(x=1, y=0, rot=0, xlabel='', legend=None, title=title)
    fig = ax.get_figure()
    fig.tight_layout()
    fig.savefig(output)


def main():
    plot_file(input=LETTERS,
              output='letters.svg',
              sort_by=1,
              ascending=True,
              title='Histogram of letters')

    plot_file(input=WORDS,
              output='words.svg',
              sort_by=0,
              ascending=False,
              title='Histogram of words',
              strip=20)


if __name__ == '__main__':
    main()
