# how-to-scrape
Code to go along with [my article about Web Scraping](https://dev.to/nrrb/my-scraping-techniques-that-fetched-millions-of-rows-52j1).

This code is also available in a [Google Colab notebook](https://colab.research.google.com/drive/1qO3GrOUN6GzFYEgQxQPrn8cFs8h5gfRr?usp=sharing).

After you've cloned this repository locally, you can create a Python virtual environment on the command-line with:

```bash
python3 -m venv venv && source venv/bin/activate
```

When that completes, then install the libraries you need:

```bash
pip install -r requirements.txt
```

## Running the Code

If you just want to run the code and see the output, you can run one of the following:

```bash
python example_requests.py
python example_requests_csv.py
python example_requests_json.py
python example_requests_pandas.py
python example_requests_beautifulsoup.py
python example_requests_beautifulsoup_fail.py
python example_selenium_beautifulsoup.py
python example_requests_useragent.py
python example_selenium_useragent.py
python example_rate_limiting.py
python example_robots.py
```

If you'd like to try the code interactively and work with the data after the fact, I recommend using [IPython shell](https://pycon.switowski.com/05-repl/ipython/). You can run it with `ipython` and then paste in the code.

Alternately, [Jupyter Notebook](https://jupyter.org/install) is great too.

If you want to run the code that uses Selenium, you first need to install a `chromedriver` on your specific system:

* macOS - First install [Homebrew](https://homebrew.sh/), then run `brew install chromedriver` in a Terminal window.
* Windows - [tutorial](https://developer.chrome.com/docs/chromedriver/get-started)
* Linux - [tutorial](https://katekuehl.medium.com/installation-guide-for-google-chrome-chromedriver-and-selenium-in-a-python-virtual-environment-e1875220be2f)

Author:

Nicholas Bennett
[LinkedIn](https://www.linkedin.com/in/nicholasrrbennett) | [Github](https://github.com/nrrb/) | [Email](mailto:nicholasbennett.work@gmail.com)