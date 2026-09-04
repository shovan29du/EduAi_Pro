#!/usr/bin/env python3
"""Depth pass, C2 R: fill in real, hand-checked data_table/formulae
(real runnable R code) content for the 69 C2 R lessons not covered by
the earlier breadth-first batch. Brings C2 R to full 70/70 coverage.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c2_r_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c2.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "r-c2-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["Data frame", "A table-like structure with rows and typed columns"],
        ]),
        "formulae": ["df <- data.frame(x = 1:3, y = c(\"a\", \"b\", \"c\"))"],
    },
    "r-c2-l2": {
        "data_table": table(["Layer", "Purpose"], [
            ["Aesthetics (aes)", "Maps data variables to visual properties"], ["Geom", "Determines the type of plot shape drawn"],
        ]),
        "formulae": ["ggplot(df, aes(x, y)) + geom_point()"],
    },
    "r-c2-l4": {
        "data_table": table(["Operator", "Meaning"], [
            ["%>%", "The magrittr pipe, passes the left side as input to the right"], ["|>", "The native R pipe, functionally similar"],
        ]),
        "formulae": ["df %>% filter(x > 1) %>% summarize(mean(y))"],
    },
    "r-c2-l5": {
        "data_table": table(["Type", "Feature"], [
            ["tibble", "Modern data frame with cleaner printing and stricter subsetting"], ["Base data.frame", "R's original tabular structure"],
        ]),
        "formulae": ["library(tibble)\ntb <- tibble(x = 1:3, y = c(\"a\", \"b\", \"c\"))"],
    },
    "r-c2-l6": {
        "data_table": table(["Component", "Meaning"], [
            ["Grammar of graphics", "Builds plots from layered, composable components"],
        ]),
    },
    "r-c2-l7": {
        "data_table": table(["Geom", "Plot Type"], [
            ["geom_point", "Scatter plot"], ["geom_line", "Line chart"], ["geom_bar", "Bar chart"],
        ]),
        "formulae": ["ggplot(df, aes(x, y)) + geom_line()"],
    },
    "r-c2-l8": {
        "data_table": table(["Function", "Purpose"], [
            ["facet_wrap", "Splits a plot into small multiples by a categorical variable"],
        ]),
        "formulae": ["ggplot(df, aes(x, y)) + geom_point() + facet_wrap(~group)"],
    },
    "r-c2-l9": {
        "data_table": table(["Function", "Purpose"], [
            ["theme_minimal", "Applies a clean, minimal visual theme"], ["scale_color_manual", "Sets custom colors for a mapped variable"],
        ]),
        "formulae": ["ggplot(df, aes(x, y)) + geom_point() + theme_minimal()"],
    },
    "r-c2-l10": {
        "data_table": table(["Geom", "Use"], [
            ["geom_histogram", "Shows the distribution of a continuous variable"], ["geom_boxplot", "Shows quartiles and outliers"],
        ]),
        "formulae": ["ggplot(df, aes(x)) + geom_histogram(bins = 20)"],
    },
    "r-c2-l11": {
        "data_table": table(["Function", "Purpose"], [
            ["geom_smooth", "Adds a fitted trend line with confidence interval"],
        ]),
        "formulae": ["ggplot(df, aes(x, y)) + geom_point() + geom_smooth(method = \"lm\")"],
    },
    "r-c2-l12": {
        "data_table": table(["Function", "Purpose"], [
            ["ggsave", "Saves the last displayed plot to a file"],
        ]),
        "formulae": ["ggsave(\"plot.png\", width = 8, height = 5)"],
    },
    "r-c2-l13": {
        "data_table": table(["Function", "Purpose"], [
            ["read_csv", "Reads a CSV file into a tibble"],
        ]),
        "formulae": ["library(readr)\ndf <- read_csv(\"data.csv\")"],
    },
    "r-c2-l14": {
        "data_table": table(["Function", "Direction"], [
            ["pivot_longer", "Converts wide columns into long key-value rows"], ["pivot_wider", "Converts long rows into wide columns"],
        ]),
        "formulae": ["df %>% pivot_longer(cols = starts_with(\"y\"), names_to = \"year\", values_to = \"value\")"],
    },
    "r-c2-l15": {
        "data_table": table(["Function", "Purpose"], [
            ["str_detect", "Tests whether a string matches a pattern"], ["str_replace", "Replaces matched text in a string"],
        ]),
        "formulae": ["library(stringr)\nstr_detect(\"hello\", \"ell\")"],
    },
    "r-c2-l16": {
        "data_table": table(["Function", "Purpose"], [
            ["fct_relevel", "Reorders the levels of a categorical factor"],
        ]),
        "formulae": ["library(forcats)\nfct_relevel(f, \"low\", \"medium\", \"high\")"],
    },
    "r-c2-l17": {
        "data_table": table(["Function", "Purpose"], [
            ["map", "Applies a function to each element of a list, returning a list"],
        ]),
        "formulae": ["library(purrr)\nmap(1:3, ~ .x * 2)"],
    },
    "r-c2-l18": {
        "data_table": table(["Join", "Behavior"], [
            ["inner_join", "Keeps only matching rows from both tables"], ["left_join", "Keeps all rows from the left table"],
        ]),
        "formulae": ["left_join(df1, df2, by = \"id\")"],
    },
    "r-c2-l19": {
        "data_table": table(["Function", "Purpose"], [
            ["group_by + summarize", "Computes aggregate statistics for each group"],
        ]),
        "formulae": ["df %>% group_by(category) %>% summarize(avg = mean(value))"],
    },
    "r-c2-l20": {
        "data_table": table(["Function", "Purpose"], [
            ["filter", "Keeps rows matching a condition"], ["arrange", "Sorts rows by column values"],
        ]),
        "formulae": ["df %>% filter(value > 10) %>% arrange(desc(value))"],
    },
    "r-c2-l21": {
        "data_table": table(["Function", "Purpose"], [
            ["mutate", "Adds or transforms columns"], ["case_when", "Vectorized multi-condition logic"],
        ]),
        "formulae": ["df %>% mutate(category = case_when(value > 10 ~ \"high\", TRUE ~ \"low\"))"],
    },
    "r-c2-l22": {
        "data_table": table(["Function", "Purpose"], [
            ["lag / lead", "Accesses previous or next row's value within a group"],
        ]),
        "formulae": ["df %>% mutate(prev = lag(value))"],
    },
    "r-c2-l23": {
        "data_table": table(["Join", "Behavior"], [
            ["anti_join", "Keeps rows from the left table with no match in the right"],
        ]),
        "formulae": ["anti_join(df1, df2, by = \"id\")"],
    },
    "r-c2-l24": {
        "data_table": table(["Function", "Direction"], [
            ["pivot_longer", "Wide to long"], ["pivot_wider", "Long to wide"],
        ]),
    },
    "r-c2-l25": {
        "data_table": table(["Function", "Purpose"], [
            ["annotate", "Adds custom text or shapes directly to a plot"],
        ]),
        "formulae": ["ggplot(df, aes(x, y)) + geom_point() + annotate(\"text\", x = 1, y = 1, label = \"note\")"],
    },
    "r-c2-l26": {
        "data_table": table(["Package", "Purpose"], [
            ["patchwork", "Combines multiple ggplot2 plots into one layout"],
        ]),
        "formulae": ["library(patchwork)\np1 + p2"],
    },
    "r-c2-l27": {
        "data_table": table(["Package", "Purpose"], [
            ["plotly", "Converts static ggplot2 plots into interactive visualizations"],
        ]),
        "formulae": ["library(plotly)\nggplotly(p)"],
    },
    "r-c2-l28": {
        "data_table": table(["Component", "Purpose"], [
            ["ui", "Defines the app's layout and appearance"], ["server", "Defines the app's reactive logic"],
        ]),
        "formulae": ["shinyApp(ui = ui, server = server)"],
    },
    "r-c2-l29": {
        "data_table": table(["Concept", "Meaning"], [
            ["Reactive expression", "Automatically re-executes when its dependencies change"],
        ]),
    },
    "r-c2-l30": {
        "data_table": table(["Feature", "Purpose"], [
            ["Parameterized report", "An R Markdown document that generates different outputs from input parameters"],
        ]),
    },
    "r-c2-l31": {
        "data_table": table(["Function", "Purpose"], [
            ["lm", "Fits a linear regression model"],
        ]),
        "formulae": ["model <- lm(y ~ x, data = df)"],
    },
    "r-c2-l32": {
        "data_table": table(["Output", "Meaning"], [
            ["Coefficient", "The estimated effect of a predictor on the outcome"], ["R-squared", "The proportion of variance explained by the model"],
        ]),
        "formulae": ["summary(model)"],
    },
    "r-c2-l33": {
        "data_table": table(["Function", "Purpose"], [
            ["glm", "Fits generalized linear models, including logistic regression"],
        ]),
        "formulae": ["model <- glm(y ~ x, data = df, family = binomial)"],
    },
    "r-c2-l34": {
        "data_table": table(["Function", "Purpose"], [
            ["aov", "Performs analysis of variance across groups"],
        ]),
        "formulae": ["result <- aov(value ~ group, data = df)"],
    },
    "r-c2-l35": {
        "data_table": table(["Function", "Purpose"], [
            ["t.test", "Tests whether two group means differ significantly"],
        ]),
        "formulae": ["t.test(value ~ group, data = df)"],
    },
    "r-c2-l36": {
        "data_table": table(["Function", "Purpose"], [
            ["cor", "Computes the correlation coefficient between two variables"],
        ]),
        "formulae": ["cor(df$x, df$y)"],
    },
    "r-c2-l37": {
        "data_table": table(["Function", "Purpose"], [
            ["ts", "Creates a time series object from a numeric vector"],
        ]),
        "formulae": ["ts_data <- ts(values, frequency = 12, start = c(2020, 1))"],
    },
    "r-c2-l38": {
        "data_table": table(["Function", "Purpose"], [
            ["decompose", "Splits a time series into trend, seasonal, and residual components"],
        ]),
        "formulae": ["decompose(ts_data)"],
    },
    "r-c2-l39": {
        "data_table": table(["Term", "Meaning"], [
            ["S4 class", "R's formal OOP system with strict class definitions"],
        ]),
        "formulae": ["setClass(\"Point\", representation(x = \"numeric\", y = \"numeric\"))"],
    },
    "r-c2-l40": {
        "data_table": table(["Term", "Meaning"], [
            ["R6 class", "A reference-semantics OOP system similar to classes in other languages"],
        ]),
        "formulae": ["library(R6)\nPoint <- R6Class(\"Point\", public = list(x = NULL, y = NULL))"],
    },
    "r-c2-l41": {
        "data_table": table(["Function", "Purpose"], [
            ["map_dbl", "Applies a function and returns a numeric vector"],
        ]),
        "formulae": ["map_dbl(1:5, ~ .x ^ 2)"],
    },
    "r-c2-l42": {
        "data_table": table(["Function", "Purpose"], [
            ["safely", "Wraps a function to capture errors instead of stopping execution"],
        ]),
        "formulae": ["safe_log <- safely(log)\nsafe_log(-1)"],
    },
    "r-c2-l43": {
        "data_table": table(["Concept", "Meaning"], [
            ["Tidy evaluation", "Allows column names to be used unquoted inside tidyverse functions"],
        ]),
    },
    "r-c2-l44": {
        "data_table": table(["Function", "Purpose"], [
            ["dbConnect", "Opens a connection to a database"],
        ]),
        "formulae": ["library(DBI)\ncon <- dbConnect(RSQLite::SQLite(), \"app.db\")"],
    },
    "r-c2-l45": {
        "data_table": table(["Function", "Purpose"], [
            ["unnest_tokens", "Splits text into individual words for analysis"],
        ]),
        "formulae": ["library(tidytext)\ndf %>% unnest_tokens(word, text)"],
    },
    "r-c2-l46": {
        "data_table": table(["Function", "Purpose"], [
            ["st_read", "Reads spatial data files like shapefiles"],
        ]),
        "formulae": ["library(sf)\nshapes <- st_read(\"map.shp\")"],
    },
    "r-c2-l47": {
        "data_table": table(["File", "Purpose"], [
            ["DESCRIPTION", "Declares an R package's metadata and dependencies"],
        ]),
    },
    "r-c2-l48": {
        "data_table": table(["Function", "Purpose"], [
            ["expect_equal", "Asserts that two values are equal in a testthat test"],
        ]),
        "formulae": ["library(testthat)\ntest_that(\"addition works\", {\n  expect_equal(1 + 1, 2)\n})"],
    },
    "r-c2-l49": {
        "data_table": table(["Command", "Purpose"], [
            ["git init", "Initializes version control in an R project directory"],
        ]),
    },
    "r-c2-l50": {
        "data_table": table(["Function", "Purpose"], [
            ["parallel::mclapply", "Applies a function across cores in parallel"],
        ]),
    },
    "r-c2-l51": {
        "data_table": table(["Function", "Purpose"], [
            ["system.time", "Measures how long an R expression takes to run"],
        ]),
        "formulae": ["system.time(my_function())"],
    },
    "r-c2-l52": {
        "data_table": table(["Package", "Purpose"], [
            ["tidymodels", "A unified framework for building and evaluating machine learning models in R"],
        ]),
    },
    "r-c2-l53": {
        "data_table": table(["Function", "Purpose"], [
            ["vfold_cv", "Creates cross-validation folds for model evaluation"],
        ]),
    },
    "r-c2-l54": {
        "data_table": table(["Function", "Purpose"], [
            ["kmeans", "Groups data into a specified number of clusters"],
        ]),
        "formulae": ["kmeans(df, centers = 3)"],
    },
    "r-c2-l55": {
        "data_table": table(["Function", "Purpose"], [
            ["prcomp", "Performs principal component analysis for dimensionality reduction"],
        ]),
        "formulae": ["prcomp(df, scale. = TRUE)"],
    },
    "r-c2-l56": {
        "data_table": table(["Term", "Meaning"], [
            ["Bayesian statistics", "Updates probability estimates as new evidence becomes available"],
        ]),
    },
    "r-c2-l57": {
        "data_table": table(["Component", "Purpose"], [
            ["recipe", "Defines preprocessing steps for a model"], ["workflow", "Bundles a recipe and model together"],
        ]),
    },
    "r-c2-l58": {
        "data_table": table(["Practice", "Reason"], [
            ["Setting a random seed", "Ensures results are reproducible across runs"],
        ]),
        "formulae": ["set.seed(42)"],
    },
    "r-c2-l59": {
        "data_table": table(["Function", "Purpose"], [
            ["renv::init", "Creates an isolated, reproducible package environment for a project"],
        ]),
    },
    "r-c2-l60": {
        "data_table": table(["Platform", "Purpose"], [
            ["shinyapps.io", "Hosts and deploys Shiny web applications online"],
        ]),
    },
    "r-c2-l61": {
        "data_table": table(["Application", "Example"], [
            ["Updating a prior belief", "Combining a prior distribution with observed data"],
        ]),
    },
    "r-c2-l62": {
        "data_table": table(["Application", "Example"], [
            ["Cleaning messy text", "Removing whitespace and standardizing case in a string column"],
        ]),
        "formulae": ["str_trim(str_to_lower(x))"],
    },
    "r-c2-l63": {
        "data_table": table(["Application", "Example"], [
            ["Building a tidy dataset", "Reshaping raw data into one-variable-per-column format"],
        ]),
    },
    "r-c2-l64": {
        "data_table": table(["Application", "Example"], [
            ["Building a layered plot", "Combining geoms and themes into a polished visualization"],
        ]),
    },
    "r-c2-l65": {
        "data_table": table(["Application", "Example"], [
            ["Applying tidy data rules", "Reshaping a wide dataset into tidy long format"],
        ]),
    },
    "r-c2-l66": {
        "data_table": table(["Application", "Example"], [
            ["Chaining operations", "Combining filter, mutate, and summarize with the pipe"],
        ]),
    },
    "r-c2-l67": {
        "data_table": table(["Application", "Example"], [
            ["Choosing tibble vs data.frame", "Deciding based on printing behavior and strictness needs"],
        ]),
    },
    "r-c2-l68": {
        "data_table": table(["Application", "Example"], [
            ["Building a plot from scratch", "Layering aesthetics, geoms, and a theme"],
        ]),
    },
    "r-c2-l69": {
        "data_table": table(["Application", "Example"], [
            ["Mapping color to a variable", "Distinguishing groups visually within one plot"],
        ]),
    },
    "r-c2-l70": {
        "data_table": table(["Application", "Example"], [
            ["Creating small multiples", "Faceting a plot by a categorical variable for comparison"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["R"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c2.json R: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C2 R lessons (completing 70/70).")


if __name__ == "__main__":
    main()
