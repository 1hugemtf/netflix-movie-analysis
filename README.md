# Netflix Movie Duration Analysis

A Python exploratory data analysis project investigating movie duration by release year, with genre highlighting to help interpret shorter films.

**Author:** Hamed Dhiaa  
**Tools:** Python, pandas, Matplotlib, Jupyter Notebook

## Project overview

Do movies in this Netflix dataset appear to be getting shorter? This notebook filters the catalogue to movies, identifies titles shorter than 60 minutes, and visualises duration against release year. Children's films, documentaries and stand-up titles are highlighted separately.

This is a learning project from my DataCamp coursework. The supplied exercise, dataset and illustration are retained in the original notebook; this repository documents the analysis and how to run it. It is not affiliated with Netflix.

## What the notebook does

1. Loads `netflix_data.csv` with pandas.
2. Filters the data to entries labelled `Movie`.
3. Selects title, country, genre, release year and duration.
4. Creates a subset of movies shorter than 60 minutes.
5. Colours Children titles red, Documentaries blue, Stand-Up green and other genres black.
6. Plots movie duration against release year.

## Dataset snapshot

- Catalogue entries: **7,787**
- Movie entries: **5,377**
- Movie release years: **1942–2021**
- Movies shorter than 60 minutes: **420**

These figures describe the supplied dataset, not the current Netflix catalogue. For movies, duration is measured in minutes. `release_year` refers to the title's release year; it is distinct from `date_added`.

## Interpretation and limitations

The original notebook ends with `answer = "maybe"`. The scatter plot is exploratory: it does not establish that movie runtimes are declining. Genre mix, the number of titles represented in each year, and catalogue selection can affect the apparent pattern. The notebook does not include a statistical trend test or an analysis that controls for genre.

## Run locally

Requires Python 3.10 or later.

```bash
git clone https://github.com/1hugemtf/netflix-movie-analysis.git
cd netflix-movie-analysis
python -m venv .venv
```

Activate the environment:

```powershell
# Windows PowerShell
.venv\Scripts\Activate.ps1
```

```bash
# macOS / Linux
source .venv/bin/activate
```

Install dependencies and open the notebook:

```bash
python -m pip install -r requirements.txt
python -m jupyterlab notebook.ipynb
```

Run the cells from top to bottom, keeping the CSV and image alongside the notebook.

## Files

| File | Purpose |
| --- | --- |
| `notebook.ipynb` | Original analysis notebook with saved output |
| `netflix_data.csv` | Supplied catalogue dataset |
| `redpopcorn.jpg` | Supplied notebook illustration |
| `requirements.txt` | Python dependencies |

## Possible next steps

- Compare annual median and mean movie duration alongside sample sizes.
- Examine trends within genres rather than across the entire catalogue.
- Add a plot legend and investigate missing values and text-encoding issues.

## Attribution

This repository contains a DataCamp learning exercise and supplied assets. No blanket open-source licence is applied to the third-party dataset, exercise text or image; their respective rights remain with their owners. Public availability does not establish unrestricted reuse rights.

## Connect

- [Portfolio](https://1huge-dhiaa.carrd.co)
- [LinkedIn](https://www.linkedin.com/in/dhiaa-hamed/)
