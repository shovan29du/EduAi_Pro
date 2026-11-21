#!/usr/bin/env python3
"""Depth pass, C1 R: fill in real, hand-checked data_table content for
the 69 C1 R lessons not covered by the earlier breadth-first batch.
Brings C1 R to full 70/70 coverage.

Examples use real, runnable R syntax.

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_c1_r_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_c1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


CHARTS: dict[str, dict] = {
    "r-c1-l1": {
        "data_table": table(["Term", "Meaning"], [
            ["RStudio", "An integrated development environment (IDE) for R"],
        ]),
    },
    "r-c1-l2": {
        "data_table": table(["Type", "Example"], [
            ["numeric", "3.14"], ["character", "'hello'"], ["logical", "TRUE"],
        ]),
        "formulae": ["x <- c(1, 2, 3)"],
    },
    "r-c1-l4": {
        "data_table": table(["Operator", "Purpose"], [
            ["<-", "Assignment"], ["==", "Equality comparison"],
        ]),
        "formulae": ["x <- 5", "print(x)"],
    },
    "r-c1-l5": {
        "data_table": table(["Type", "Example"], [
            ["numeric", "42"], ["character", "\"text\""], ["logical", "TRUE/FALSE"],
        ]),
    },
    "r-c1-l6": {
        "data_table": table(["Term", "Meaning"], [
            ["Vectorized operation", "Applying an operation to every element of a vector at once"],
        ]),
        "formulae": ["v <- c(1, 2, 3)", "v * 2  # 2 4 6"],
    },
    "r-c1-l7": {
        "data_table": table(["Syntax", "Result"], [
            ["v[2]", "The second element"], ["v[-1]", "All but the first element"],
        ]),
        "formulae": ["v <- c(10, 20, 30)", "v[2]  # 20"],
    },
    "r-c1-l8": {
        "data_table": table(["Term", "Meaning"], [
            ["Factor", "A variable representing categorical data with fixed levels"],
        ]),
        "formulae": ["f <- factor(c(\"low\", \"high\", \"low\"))"],
    },
    "r-c1-l9": {
        "data_table": table(["Structure", "Feature"], [
            ["List", "Can hold elements of different types"],
        ]),
        "formulae": ["my_list <- list(name=\"Sam\", age=20)"],
    },
    "r-c1-l10": {
        "data_table": table(["Structure", "Feature"], [
            ["Matrix", "A 2D array of the same data type"],
        ]),
        "formulae": ["m <- matrix(1:6, nrow=2)"],
    },
    "r-c1-l11": {
        "data_table": table(["Structure", "Feature"], [
            ["Data frame", "A table-like structure with columns of possibly different types"],
        ]),
        "formulae": ["df <- data.frame(name=c(\"A\",\"B\"), score=c(90,85))"],
    },
    "r-c1-l12": {
        "data_table": table(["Function", "Purpose"], [
            ["read.csv()", "Reads a CSV file into a data frame"],
        ]),
        "formulae": ["df <- read.csv(\"data.csv\")"],
    },
    "r-c1-l13": {
        "data_table": table(["Function", "Purpose"], [
            ["is.na()", "Checks for missing values"], ["na.omit()", "Removes rows with missing values"],
        ]),
        "formulae": ["is.na(c(1, NA, 3))"],
    },
    "r-c1-l14": {
        "data_table": table(["Operator", "Meaning"], [
            ["&", "Logical AND"], ["|", "Logical OR"],
        ]),
    },
    "r-c1-l15": {
        "data_table": table(["Keyword", "Purpose"], [
            ["if", "Runs code when a condition is true"], ["else", "Runs when the condition is false"],
        ]),
        "formulae": ["if (x > 0) {", "  print(\"positive\")", "} else {", "  print(\"non-positive\")", "}"],
    },
    "r-c1-l16": {
        "data_table": table(["Loop", "Example"], [
            ["for", "for (i in 1:5) print(i)"],
        ]),
        "formulae": ["for (i in 1:5) {", "  print(i)", "}"],
    },
    "r-c1-l17": {
        "data_table": table(["Function", "Purpose"], [
            ["sapply()", "Applies a function to each element, returns a vector"], ["lapply()", "Applies a function, returns a list"],
        ]),
        "formulae": ["sapply(1:5, function(x) x^2)"],
    },
    "r-c1-l18": {
        "data_table": table(["Keyword", "Purpose"], [
            ["function", "Defines a reusable block of code"],
        ]),
        "formulae": ["add <- function(a, b) {", "  return(a + b)", "}"],
    },
    "r-c1-l19": {
        "data_table": table(["Tool", "Use"], [
            ["R script (.R file)", "Saves and reuses code"], ["R console", "Runs commands interactively"],
        ]),
    },
    "r-c1-l20": {
        "data_table": table(["Command", "Purpose"], [
            ["?function_name", "Opens documentation for a function"],
        ]),
        "formulae": ["?mean"],
    },
    "r-c1-l21": {
        "data_table": table(["Type", "Example"], [
            ["Integer", "5L"], ["Double", "5.0"],
        ]),
    },
    "r-c1-l22": {
        "data_table": table(["Function", "Purpose"], [
            ["as.numeric()", "Converts to numeric"], ["as.character()", "Converts to character"],
        ]),
        "formulae": ["as.numeric(\"42\")"],
    },
    "r-c1-l23": {
        "data_table": table(["Convention", "Example"], [
            ["snake_case", "student_score"],
        ]),
    },
    "r-c1-l24": {
        "data_table": table(["Function", "Purpose"], [
            ["nchar()", "Counts characters in a string"],
        ]),
        "formulae": ["nchar(\"hello\")  # 5"],
    },
    "r-c1-l25": {
        "data_table": table(["Function", "Purpose"], [
            ["paste()", "Concatenates strings"], ["substr()", "Extracts a substring"],
        ]),
        "formulae": ["paste(\"Hello\", \"World\")"],
    },
    "r-c1-l26": {
        "data_table": table(["Function", "Purpose"], [
            ["Sys.Date()", "Gets the current date"],
        ]),
        "formulae": ["Sys.Date()"],
    },
    "r-c1-l27": {
        "data_table": table(["Symbol", "Purpose"], [
            ["#", "Marks a comment in R"],
        ]),
    },
    "r-c1-l28": {
        "data_table": table(["Function", "Purpose"], [
            ["library()", "Loads an installed package"],
        ]),
        "formulae": ["library(ggplot2)"],
    },
    "r-c1-l29": {
        "data_table": table(["Function", "Purpose"], [
            ["install.packages()", "Installs a package from CRAN"],
        ]),
        "formulae": ["install.packages(\"dplyr\")"],
    },
    "r-c1-l30": {
        "data_table": table(["Pane", "Purpose"], [
            ["Console", "Runs commands"], ["Environment", "Shows current variables"],
        ]),
    },
    "r-c1-l31": {
        "data_table": table(["Concept", "Benefit"], [
            ["R Project", "Keeps file paths relative and organized"],
        ]),
    },
    "r-c1-l32": {
        "data_table": table(["Function", "Purpose"], [
            ["read_excel()", "Reads an Excel file (from readxl package)"],
        ]),
        "formulae": ["library(readxl)", "df <- read_excel(\"data.xlsx\")"],
    },
    "r-c1-l33": {
        "data_table": table(["Function", "Purpose"], [
            ["write.csv()", "Saves a data frame to a CSV file"],
        ]),
        "formulae": ["write.csv(df, \"output.csv\")"],
    },
    "r-c1-l34": {
        "data_table": table(["Function", "Purpose"], [
            ["str()", "Shows the structure of an R object"],
        ]),
        "formulae": ["str(df)"],
    },
    "r-c1-l35": {
        "data_table": table(["Function", "Purpose"], [
            ["summary()", "Shows summary statistics for each column"],
        ]),
        "formulae": ["summary(df)"],
    },
    "r-c1-l36": {
        "data_table": table(["Function", "Purpose"], [
            ["mean()", "Average"], ["sd()", "Standard deviation"],
        ]),
        "formulae": ["mean(c(1,2,3,4))"],
    },
    "r-c1-l37": {
        "data_table": table(["Term", "Meaning"], [
            ["R Markdown", "Combines R code, output, and text into one document"],
        ]),
    },
    "r-c1-l38": {
        "data_table": table(["Element", "Purpose"], [
            ["Code chunk", "Embeds executable R code in a report"],
        ]),
    },
    "r-c1-l39": {
        "data_table": table(["Function", "Purpose"], [
            ["plot()", "Creates a scatter or line plot"], ["hist()", "Creates a histogram"],
        ]),
        "formulae": ["plot(x, y)"],
    },
    "r-c1-l40": {
        "data_table": table(["Argument", "Effect"], [
            ["main=", "Sets the plot title"], ["col=", "Sets the color"],
        ]),
        "formulae": ["plot(x, y, main=\"My Plot\", col=\"blue\")"],
    },
    "r-c1-l41": {
        "data_table": table(["Chart", "Function"], [
            ["Boxplot", "boxplot(data)"], ["Scatterplot", "plot(x, y)"],
        ]),
    },
    "r-c1-l42": {
        "data_table": table(["Syntax", "Effect"], [
            ["df[df$score > 80, ]", "Filters rows where score exceeds 80"],
        ]),
    },
    "r-c1-l43": {
        "data_table": table(["Function", "Purpose"], [
            ["order()", "Returns the sorted index order"],
        ]),
        "formulae": ["df[order(df$score), ]"],
    },
    "r-c1-l44": {
        "data_table": table(["Step", "Purpose"], [
            ["Removing duplicates", "Ensures each record is counted once"],
        ]),
    },
    "r-c1-l45": {
        "data_table": table(["Function", "Purpose"], [
            ["duplicated()", "Flags duplicate rows"],
        ]),
        "formulae": ["df[!duplicated(df), ]"],
    },
    "r-c1-l46": {
        "data_table": table(["Syntax", "Example"], [
            ["Default argument", "function(x, y=10)"],
        ]),
        "formulae": ["greet <- function(name=\"World\") {", "  paste(\"Hello,\", name)", "}"],
    },
    "r-c1-l47": {
        "data_table": table(["Concept", "Example"], [
            ["Base case", "Stops the recursion"],
        ]),
        "formulae": ["factorial <- function(n) {", "  if (n <= 1) return(1)", "  return(n * factorial(n - 1))", "}"],
    },
    "r-c1-l48": {
        "data_table": table(["Keyword", "Purpose"], [
            ["tryCatch", "Handles errors gracefully in R"],
        ]),
        "formulae": ["tryCatch({", "  1 / 0", "}, error = function(e) print(\"error\"))"],
    },
    "r-c1-l49": {
        "data_table": table(["Approach", "Performance"], [
            ["Vectorization", "Faster, operates on whole vectors at once"], ["Loop", "Slower for large data"],
        ]),
    },
    "r-c1-l50": {
        "data_table": table(["Function", "Purpose"], [
            ["rowSums()", "Sums each row"], ["colMeans()", "Averages each column"],
        ]),
    },
    "r-c1-l51": {
        "data_table": table(["Structure", "Feature"], [
            ["Array", "A multi-dimensional generalization of a matrix"],
        ]),
        "formulae": ["arr <- array(1:24, dim=c(2,3,4))"],
    },
    "r-c1-l52": {
        "data_table": table(["Function", "Returns"], [
            ["sapply()", "A simplified vector or matrix"], ["lapply()", "A list"],
        ]),
    },
    "r-c1-l53": {
        "data_table": table(["Term", "Meaning"], [
            ["Environment", "A structure holding variable bindings in R"],
        ]),
    },
    "r-c1-l54": {
        "data_table": table(["Term", "Meaning"], [
            ["S3 class", "R's simplest object-oriented system based on naming conventions"],
        ]),
    },
    "r-c1-l55": {
        "data_table": table(["Function", "Purpose"], [
            ["sample()", "Draws a random sample"],
        ]),
        "formulae": ["sample(1:6, 1)"],
    },
    "r-c1-l56": {
        "data_table": table(["Function", "Purpose"], [
            ["union()", "Combines two sets"], ["intersect()", "Common elements"],
        ]),
    },
    "r-c1-l57": {
        "data_table": table(["Function", "Purpose"], [
            ["grepl()", "Tests if a pattern matches a string"],
        ]),
        "formulae": ["grepl(\"^A\", \"Apple\")  # TRUE"],
    },
    "r-c1-l58": {
        "data_table": table(["Function", "Purpose"], [
            ["saveRDS()", "Saves a single R object to a file"], ["readRDS()", "Loads it back"],
        ]),
    },
    "r-c1-l59": {
        "data_table": table(["Resource", "Purpose"], [
            ["Vignette", "A long-form guide bundled with an R package"],
        ]),
        "formulae": ["vignette(\"dplyr\")"],
    },
    "r-c1-l60": {
        "data_table": table(["Function", "Purpose"], [
            ["traceback()", "Shows the call stack after an error"],
        ]),
    },
    "r-c1-l61": {
        "data_table": table(["Application", "Example"], [
            ["Setting up a first project", "Creating an R Project and running a starter script"],
        ]),
    },
    "r-c1-l62": {
        "data_table": table(["Application", "Example"], [
            ["Combining vector types", "Building a vector of mixed types and checking coercion"],
        ]),
    },
    "r-c1-l63": {
        "data_table": table(["Application", "Example"], [
            ["Confirming installation", "Running sessionInfo() to check the R version"],
        ]),
    },
    "r-c1-l64": {
        "data_table": table(["Application", "Example"], [
            ["Computing with variables", "Calculating a total from assigned values"],
        ]),
    },
    "r-c1-l65": {
        "data_table": table(["Application", "Example"], [
            ["Type checking", "Using class() to confirm a variable's data type"],
        ]),
    },
    "r-c1-l66": {
        "data_table": table(["Application", "Example"], [
            ["Vectorized arithmetic", "Doubling every value in a vector without a loop"],
        ]),
    },
    "r-c1-l67": {
        "data_table": table(["Application", "Example"], [
            ["Extracting a subset", "Pulling the first three elements of a vector"],
        ]),
    },
    "r-c1-l68": {
        "data_table": table(["Application", "Example"], [
            ["Working with factors", "Counting how many observations fall into each category"],
        ]),
    },
    "r-c1-l69": {
        "data_table": table(["Application", "Example"], [
            ["Building a list", "Storing a person's name, age, and scores in one list"],
        ]),
    },
    "r-c1-l70": {
        "data_table": table(["Application", "Example"], [
            ["Matrix operations", "Multiplying two matrices together"],
        ]),
    },
}


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["R"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_c1.json R: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} C1 R lessons (completing 70/70).")


if __name__ == "__main__":
    main()
