#!/usr/bin/env python3
"""Depth pass, M1 R: fill in real, hand-checked data_table and
formulae (runnable code) content for the 119 M1 R lessons not
covered by the earlier breadth-first batch. Brings M1 R to full
120/120 coverage.

Structure: l1-l100 are unique graduate-level topics spanning
functional/OOP R programming, package development, the tidyverse
internals, advanced statistical modeling, and domain-specific R
applications (genomics, finance, ecology); l101-l120 are "Worked
Analysis" companions reusing the data_table/formulae of l1-l20
(direct 1:1 mapping). l3 was already completed by an earlier
breadth-first batch (data_table only, no formulae there), so its
data_table is hard-coded here for reuse (it falls within l1-l20, so
it is also reused for l103).

Idempotent: only fills in fields that aren't already set.

Re-run after editing:
    python3 backend/scripts/add_m1_r_completion.py
"""
from __future__ import annotations

import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
SYLLABUS_PATH = BASE_DIR / "syllabus" / "level_m1.json"


def table(headers, rows):
    return {"headers": headers, "rows": rows}


_L3_SOURCE = table(["Term", "Meaning"], [
    ["Environment", "A container mapping variable names to values, R's core scoping mechanism"],
    ["Closure", "A function bundled with the environment in which it was created"],
])

CHARTS: dict[str, dict] = {
    "r-m1-l1": {"data_table": table(["Term", "Meaning"], [
        ["Specialized domain R", "Uses R's statistical ecosystem tailored to a specific applied field"],
    ]), "formulae": ["library(tidyverse)"]},
    "r-m1-l2": {"data_table": table(["Term", "Meaning"], [
        ["testthat", "R's standard framework for writing and running unit tests"],
    ]), "formulae": ["testthat::test_that('adds', { expect_equal(1 + 1, 2) })"]},
    "r-m1-l4": {"data_table": table(["Term", "Meaning"], [
        ["Functional programming", "Treats functions as first-class values passed to and returned from other functions"],
    ]), "formulae": ["Map(function(x) x^2, 1:5)"]},
    "r-m1-l5": {"data_table": table(["Term", "Meaning"], [
        ["Vectorized function", "Operates on whole vectors at once instead of looping element by element"],
    ]), "formulae": ["square <- function(x) x^2\nsquare(1:5)"]},
    "r-m1-l6": {"data_table": table(["Term", "Meaning"], [
        ["S3 class", "R's simplest object system, dispatching methods based on an object's class attribute"],
    ]), "formulae": ["obj <- structure(list(x=1), class='myclass')\nprint.myclass <- function(o, ...) cat('x =', o$x)"]},
    "r-m1-l7": {"data_table": table(["System", "Feature"], [
        ["S4", "Formal classes with strict validation and multiple dispatch"],
        ["R6", "Reference-semantics classes similar to conventional OOP"],
    ]), "formulae": ["setClass('Point', representation(x='numeric', y='numeric'))"]},
    "r-m1-l8": {"data_table": table(["Term", "Meaning"], [
        ["testthat unit testing", "Verifies individual R functions behave correctly in isolation"],
    ]), "formulae": ["test_that('multiplication works', {\n  expect_equal(2 * 2, 4)\n})"]},
    "r-m1-l9": {"data_table": table(["Term", "Meaning"], [
        ["CI for R packages", "Automatically runs R CMD check and tests on every commit"],
    ]), "formulae": ["# .github/workflows/R-CMD-check.yaml\nuses: r-lib/actions/check-r-package@v2"]},
    "r-m1-l10": {"data_table": table(["Term", "Meaning"], [
        ["R package structure", "Organizes R code, docs, and tests into an installable, shareable unit"],
    ]), "formulae": ["usethis::create_package('mypkg')"]},
    "r-m1-l11": {"data_table": table(["Term", "Meaning"], [
        ["Package vignette", "A long-form document demonstrating how to use a package's functions"],
    ]), "formulae": ["usethis::use_vignette('intro')"]},
    "r-m1-l12": {"data_table": table(["Tool", "Purpose"], [
        ["profvis", "Visualizes where an R script spends its execution time"],
    ]), "formulae": ["profvis::profvis({ Sys.sleep(1) })"]},
    "r-m1-l13": {"data_table": table(["Term", "Meaning"], [
        ["Rcpp", "Lets R call compiled C++ functions for performance-critical code"],
    ]), "formulae": ["Rcpp::cppFunction('int add(int x, int y) { return x + y; }')"]},
    "r-m1-l14": {"data_table": table(["Package", "Purpose"], [
        ["parallel / future", "Run R computations across multiple cores or machines"],
    ]), "formulae": ["library(future)\nplan(multisession)"]},
    "r-m1-l15": {"data_table": table(["Term", "Meaning"], [
        ["Large dataset memory management", "Uses chunked or out-of-memory techniques for data too big for RAM"],
    ]), "formulae": ["library(data.table)\ndt <- fread('big.csv')"]},
    "r-m1-l16": {"data_table": table(["Tool", "Purpose"], [
        ["browser()", "Pauses execution at a point in an R function for interactive debugging"],
    ]), "formulae": ["f <- function(x) { browser(); x + 1 }"]},
    "r-m1-l17": {"data_table": table(["Term", "Meaning"], [
        ["Git for R projects", "Tracks changes to R scripts and package source over time"],
    ]), "formulae": ["usethis::use_git()"]},
    "r-m1-l18": {"data_table": table(["Package", "Purpose"], [
        ["Stan / brms", "Fit full Bayesian models using Hamiltonian Monte Carlo sampling"],
    ]), "formulae": ["library(brms)\nfit <- brm(y ~ x, data = df)"]},
    "r-m1-l19": {"data_table": table(["Term", "Meaning"], [
        ["Reproducibility", "Ensures an R analysis produces the same result when re-run later"],
    ]), "formulae": ["set.seed(42)"]},
    "r-m1-l20": {"data_table": table(["Component", "Purpose"], [
        ["End-to-end analysis report", "Integrates data cleaning, modeling, and reporting into one reproducible document"],
    ]), "formulae": ["rmarkdown::render('report.Rmd')"]},
    "r-m1-l21": {"data_table": table(["Term", "Meaning"], [
        ["data.table", "A high-performance package for fast data manipulation on large datasets"],
    ]), "formulae": ["library(data.table)\ndt[x > 5, .(mean(y)), by = group]"]},
    "r-m1-l22": {"data_table": table(["Term", "Meaning"], [
        ["Tidy evaluation", "Lets tidyverse functions accept unquoted column names as expressions"],
    ]), "formulae": ["library(rlang)\nf <- function(data, var) { var <- enquo(var); dplyr::select(data, !!var) }"]},
    "r-m1-l23": {"data_table": table(["Term", "Meaning"], [
        ["rlang metaprogramming", "Manipulates R expressions and quosures programmatically"],
    ]), "formulae": ["library(rlang)\nexpr(1 + 2)"]},
    "r-m1-l24": {"data_table": table(["Term", "Meaning"], [
        ["Custom ggplot2 extension", "Adds a new geom or stat layer to extend ggplot2's grammar of graphics"],
    ]), "formulae": ["library(ggplot2)\nggplot(mtcars, aes(wt, mpg)) + geom_point()"]},
    "r-m1-l25": {"data_table": table(["Term", "Meaning"], [
        ["grid graphics", "R's low-level graphics system underlying ggplot2 and lattice"],
    ]), "formulae": ["library(grid)\ngrid.rect()"]},
    "r-m1-l26": {"data_table": table(["Term", "Meaning"], [
        ["Reactive programming (Shiny)", "Automatically re-runs dependent outputs when their inputs change"],
    ]), "formulae": ["library(shiny)\nserver <- function(input, output) {\n  output$plot <- renderPlot({ plot(input$n) })\n}"]},
    "r-m1-l27": {"data_table": table(["Term", "Meaning"], [
        ["Shiny module", "Packages reusable UI and server logic into a self-contained component"],
    ]), "formulae": ["mod_ui <- function(id) { ns <- NS(id); tagList() }"]},
    "r-m1-l28": {"data_table": table(["Term", "Meaning"], [
        ["Shiny Server deployment", "Hosts a Shiny app so multiple users can access it over the web"],
    ]), "formulae": ["rsconnect::deployApp('myapp')"]},
    "r-m1-l29": {"data_table": table(["Package", "Purpose"], [
        ["lme4 / nlme", "Fit mixed-effects models with random and fixed effects"],
    ]), "formulae": ["library(lme4)\nfit <- lmer(y ~ x + (1 | group), data = df)"]},
    "r-m1-l30": {"data_table": table(["Package", "Purpose"], [
        ["mgcv", "Fits generalized additive models with smooth, nonlinear terms"],
    ]), "formulae": ["library(mgcv)\nfit <- gam(y ~ s(x), data = df)"]},
    "r-m1-l31": {"data_table": table(["Package", "Purpose"], [
        ["survival", "Fits and analyzes time-to-event (survival) models"],
    ]), "formulae": ["library(survival)\nfit <- survfit(Surv(time, status) ~ 1, data = df)"]},
    "r-m1-l32": {"data_table": table(["Package", "Purpose"], [
        ["forecast / fable", "Fit and forecast time series models like ARIMA and ETS"],
    ]), "formulae": ["library(forecast)\nfit <- auto.arima(ts_data)"]},
    "r-m1-l33": {"data_table": table(["Term", "Meaning"], [
        ["Kalman filter", "Recursively estimates a system's hidden state from noisy sequential observations"],
    ]), "formulae": ["library(dlm)\nmod <- dlmModPoly(order = 1)"]},
    "r-m1-l34": {"data_table": table(["Term", "Meaning"], [
        ["Hierarchical model", "Models data with nested grouping structure, sharing information across groups"],
    ]), "formulae": ["library(lme4)\nlmer(y ~ x + (1 | school/class), data = df)"]},
    "r-m1-l35": {"data_table": table(["Package", "Purpose"], [
        ["sf / gstat", "Handle spatial vector data and geostatistical interpolation"],
    ]), "formulae": ["library(sf)\npts <- st_as_sf(df, coords = c('lon', 'lat'))"]},
    "r-m1-l36": {"data_table": table(["Package", "Purpose"], [
        ["tmap / leaflet", "Create static and interactive maps in R"],
    ]), "formulae": ["library(leaflet)\nleaflet() %>% addTiles()"]},
    "r-m1-l37": {"data_table": table(["Package", "Purpose"], [
        ["igraph", "Analyzes and visualizes network/graph-structured data"],
    ]), "formulae": ["library(igraph)\ng <- graph_from_data_frame(edges)"]},
    "r-m1-l38": {"data_table": table(["Package", "Purpose"], [
        ["quanteda", "Provides fast text mining and quantitative NLP tools"],
    ]), "formulae": ["library(quanteda)\ncorp <- corpus(texts)"]},
    "r-m1-l39": {"data_table": table(["Term", "Meaning"], [
        ["Sentiment analysis pipeline", "Classifies text by its expressed emotional polarity"],
    ]), "formulae": ["library(tidytext)\nget_sentiments('bing')"]},
    "r-m1-l40": {"data_table": table(["Package", "Purpose"], [
        ["stm", "Fits structural topic models discovering latent themes in text"],
    ]), "formulae": ["library(stm)\nmod <- stm(docs, K = 10)"]},
    "r-m1-l41": {"data_table": table(["Package", "Purpose"], [
        ["tidymodels", "A tidyverse-consistent framework for building machine learning pipelines"],
    ]), "formulae": ["library(tidymodels)\nrecipe(y ~ ., data = df) %>% prep()"]},
    "r-m1-l42": {"data_table": table(["Package", "Purpose"], [
        ["randomForest / xgboost", "Fit ensemble tree-based models for classification and regression"],
    ]), "formulae": ["library(randomForest)\nfit <- randomForest(y ~ ., data = df)"]},
    "r-m1-l43": {"data_table": table(["Package", "Purpose"], [
        ["rsample", "Creates cross-validation and resampling splits for model evaluation"],
    ]), "formulae": ["library(rsample)\nfolds <- vfold_cv(df, v = 5)"]},
    "r-m1-l44": {"data_table": table(["Package", "Purpose"], [
        ["tune", "Systematically searches hyperparameter combinations to optimize model performance"],
    ]), "formulae": ["library(tune)\ntune_grid(wf, resamples = folds)"]},
    "r-m1-l45": {"data_table": table(["Term", "Meaning"], [
        ["Propensity score matching", "Pairs treated and untreated units with similar likelihood of treatment"],
    ]), "formulae": ["library(MatchIt)\nm <- matchit(treat ~ x1 + x2, data = df)"]},
    "r-m1-l46": {"data_table": table(["Term", "Meaning"], [
        ["Instrumental variables", "Uses a variable correlated with treatment but not the outcome to estimate a causal effect"],
    ]), "formulae": ["library(AER)\nivreg(y ~ x | z, data = df)"]},
    "r-m1-l47": {"data_table": table(["Term", "Meaning"], [
        ["Difference-in-differences", "Compares the change over time between a treated group and a control group"],
    ]), "formulae": ["lm(y ~ treat * post, data = df)"]},
    "r-m1-l48": {"data_table": table(["Term", "Meaning"], [
        ["Regression discontinuity", "Estimates a treatment effect by comparing units just above and below a cutoff"],
    ]), "formulae": ["library(rdrobust)\nrdrobust(y, x, c = 0)"]},
    "r-m1-l49": {"data_table": table(["Term", "Meaning"], [
        ["Bootstrapping", "Resamples data with replacement to estimate a statistic's sampling distribution"],
    ]), "formulae": ["library(boot)\nboot(df, statistic = function(d, i) mean(d[i]), R = 1000)"]},
    "r-m1-l50": {"data_table": table(["Term", "Meaning"], [
        ["Bayesian prior", "Encodes belief about a parameter before observing data"],
    ]), "formulae": ["library(brms)\nbrm(y ~ x, prior = prior(normal(0, 1), class = 'b'))"]},
    "r-m1-l51": {"data_table": table(["Term", "Meaning"], [
        ["Approximate Bayesian Computation", "Estimates a posterior when the likelihood is intractable, via simulation"],
    ]), "formulae": ["library(EasyABC)"]},
    "r-m1-l52": {"data_table": table(["Package", "Purpose"], [
        ["metafor", "Conducts meta-analyses combining effect sizes across studies"],
    ]), "formulae": ["library(metafor)\nrma(yi, vi, data = df)"]},
    "r-m1-l53": {"data_table": table(["Package", "Purpose"], [
        ["mice", "Performs multiple imputation to handle missing data"],
    ]), "formulae": ["library(mice)\nimp <- mice(df)"]},
    "r-m1-l54": {"data_table": table(["Term", "Meaning"], [
        ["Robust statistics", "Methods less sensitive to outliers than classical estimators like the mean"],
    ]), "formulae": ["library(MASS)\nrlm(y ~ x, data = df)"]},
    "r-m1-l55": {"data_table": table(["Term", "Meaning"], [
        ["Nonparametric method", "Makes fewer assumptions about a data's underlying distribution"],
    ]), "formulae": ["wilcox.test(x, y)"]},
    "r-m1-l56": {"data_table": table(["Package", "Purpose"], [
        ["quantreg", "Models specific percentiles of the response variable, not just the mean"],
    ]), "formulae": ["library(quantreg)\nrq(y ~ x, tau = 0.5, data = df)"]},
    "r-m1-l57": {"data_table": table(["Term", "Meaning"], [
        ["GLMM diagnostics", "Checks residuals and convergence to validate a generalized linear mixed model"],
    ]), "formulae": ["library(DHARMa)\nsimulateResiduals(fit)"]},
    "r-m1-l58": {"data_table": table(["Term", "Meaning"], [
        ["Simulation study", "Generates synthetic data under known conditions to test a statistical method's performance"],
    ]), "formulae": ["replicate(1000, mean(rnorm(30)))"]},
    "r-m1-l59": {"data_table": table(["Package", "Purpose"], [
        ["targets", "Manages reproducible analysis pipelines, re-running only outdated steps"],
    ]), "formulae": ["library(targets)\ntar_make()"]},
    "r-m1-l60": {"data_table": table(["Tool", "Purpose"], [
        ["R Markdown / Quarto", "Combine narrative text, code, and output into one reproducible document"],
    ]), "formulae": ["quarto::quarto_render('report.qmd')"]},
    "r-m1-l61": {"data_table": table(["Term", "Meaning"], [
        ["Parameterized report", "Generates multiple report variants by passing different input parameters"],
    ]), "formulae": ["rmarkdown::render('report.Rmd', params = list(region = 'US'))"]},
    "r-m1-l62": {"data_table": table(["Package", "Purpose"], [
        ["pkgdown", "Builds a documentation website automatically from an R package"],
    ]), "formulae": ["pkgdown::build_site()"]},
    "r-m1-l63": {"data_table": table(["Term", "Meaning"], [
        ["Continuous deployment for R packages", "Automatically publishes a package after passing checks"],
    ]), "formulae": ["# GitHub Action triggers on tag push"]},
    "r-m1-l64": {"data_table": table(["Feature", "Purpose"], [
        ["Rcpp sugar", "Provides R-like vectorized syntax within C++ code"],
    ]), "formulae": ["Rcpp::cppFunction('NumericVector sq(NumericVector x) { return x * x; }')"]},
    "r-m1-l65": {"data_table": table(["Package", "Purpose"], [
        ["reticulate", "Calls Python code and libraries directly from R"],
    ]), "formulae": ["library(reticulate)\nnp <- import('numpy')"]},
    "r-m1-l66": {"data_table": table(["Package", "Purpose"], [
        ["DBI", "A standard interface for R to connect to and query relational databases"],
    ]), "formulae": ["library(DBI)\ncon <- dbConnect(RSQLite::SQLite(), 'db.sqlite')"]},
    "r-m1-l67": {"data_table": table(["Package", "Purpose"], [
        ["sparklyr", "Connects R to Apache Spark for big data processing"],
    ]), "formulae": ["library(sparklyr)\nsc <- spark_connect(master = 'local')"]},
    "r-m1-l68": {"data_table": table(["Package", "Purpose"], [
        ["future / furrr", "Run R computations in parallel using a consistent, backend-agnostic API"],
    ]), "formulae": ["library(furrr)\nplan(multisession)\nfuture_map(1:10, ~ .x^2)"]},
    "r-m1-l69": {"data_table": table(["Term", "Meaning"], [
        ["GPU computing in R", "Offloads numerically intensive computation to the graphics card"],
    ]), "formulae": ["library(gpuR)"]},
    "r-m1-l70": {"data_table": table(["Term", "Meaning"], [
        ["Nested JSON handling", "Flattens deeply nested JSON structures into tidy data frames"],
    ]), "formulae": ["library(jsonlite)\nfromJSON('{\"a\": [1,2,3]}')"]},
    "r-m1-l71": {"data_table": table(["Package", "Purpose"], [
        ["rvest / httr2", "Scrape web pages and call HTTP APIs from R"],
    ]), "formulae": ["library(rvest)\nread_html('https://example.com') %>% html_nodes('p')"]},
    "r-m1-l72": {"data_table": table(["Term", "Meaning"], [
        ["Testing statistical correctness", "Verifies a package's statistical output against known analytical results"],
    ]), "formulae": ["expect_equal(mean(1:10), 5.5)"]},
    "r-m1-l73": {"data_table": table(["Term", "Meaning"], [
        ["Custom condition", "A structured, typed signal for errors/warnings beyond base R's defaults"],
    ]), "formulae": ["rlang::abort('custom_error', message = 'Something failed')"]},
    "r-m1-l74": {"data_table": table(["Term", "Meaning"], [
        ["Custom operator", "Defines a new infix operator using R's %op% syntax"],
    ]), "formulae": ["`%+%` <- function(a, b) paste0(a, b)\n'foo' %+% 'bar'"]},
    "r-m1-l75": {"data_table": table(["Term", "Meaning"], [
        ["R6 class design", "Uses reference-semantics classes to model complex, stateful systems"],
    ]), "formulae": ["library(R6)\nCounter <- R6Class('Counter', public = list(n = 0, add = function() self$n <- self$n + 1))"]},
    "r-m1-l76": {"data_table": table(["Term", "Meaning"], [
        ["Functional reactive programming", "Models values that automatically update in response to changing inputs"],
    ]), "formulae": ["library(shiny)\nreactive({ input$x * 2 })"]},
    "r-m1-l77": {"data_table": table(["Term", "Meaning"], [
        ["Programming with dplyr columns", "Passes column names as arguments using tidy evaluation"],
    ]), "formulae": ["library(dplyr)\nf <- function(df, col) df %>% summarise(m = mean({{ col }}))"]},
    "r-m1-l78": {"data_table": table(["Package", "Purpose"], [
        ["purrr", "Provides functional iteration tools (map, reduce) as tidyverse alternatives to loops"],
    ]), "formulae": ["library(purrr)\nmap_dbl(1:5, ~ .x^2)"]},
    "r-m1-l79": {"data_table": table(["Term", "Meaning"], [
        ["Time series cross-validation", "Splits data respecting temporal order to avoid leaking future information"],
    ]), "formulae": ["library(rsample)\nrolling_origin(df)"]},
    "r-m1-l80": {"data_table": table(["Package", "Purpose"], [
        ["gganimate", "Adds animation over time to ggplot2 visualizations"],
    ]), "formulae": ["library(gganimate)\nggplot(df, aes(x, y)) + geom_point() + transition_time(year)"]},
    "r-m1-l81": {"data_table": table(["Package", "Purpose"], [
        ["rgl / plotly", "Create interactive 3D visualizations in R"],
    ]), "formulae": ["library(plotly)\nplot_ly(df, x=~x, y=~y, z=~z, type='scatter3d')"]},
    "r-m1-l82": {"data_table": table(["Term", "Meaning"], [
        ["Bioconductor", "An R ecosystem of packages specialized for genomics and bioinformatics"],
    ]), "formulae": ["BiocManager::install('DESeq2')"]},
    "r-m1-l83": {"data_table": table(["Term", "Meaning"], [
        ["Outbreak modeling", "Uses compartmental or statistical models to simulate disease spread"],
    ]), "formulae": ["library(EpiModel)"]},
    "r-m1-l84": {"data_table": table(["Package", "Purpose"], [
        ["plm", "Fits panel data (fixed/random effects) econometric models"],
    ]), "formulae": ["library(plm)\nplm(y ~ x, data = df, model = 'within')"]},
    "r-m1-l85": {"data_table": table(["Package", "Purpose"], [
        ["PortfolioAnalytics", "Optimizes investment portfolios under risk and return constraints"],
    ]), "formulae": ["library(PortfolioAnalytics)"]},
    "r-m1-l86": {"data_table": table(["Term", "Meaning"], [
        ["Item response theory", "Models the relationship between a test-taker's ability and their responses to items"],
    ]), "formulae": ["library(mirt)\nmirt(df, 1)"]},
    "r-m1-l87": {"data_table": table(["Term", "Meaning"], [
        ["Adaptive trial simulation", "Simulates clinical trials that adjust design based on interim results"],
    ]), "formulae": ["library(rpact)"]},
    "r-m1-l88": {"data_table": table(["Term", "Meaning"], [
        ["Collaborative R workflows", "Coordinates version control and branching for teams working on shared R code"],
    ]), "formulae": ["usethis::pr_init('feature-branch')"]},
    "r-m1-l89": {"data_table": table(["Package", "Purpose"], [
        ["renv", "Manages project-specific, reproducible R package dependency environments"],
    ]), "formulae": ["renv::init()\nrenv::snapshot()"]},
    "r-m1-l90": {"data_table": table(["Term", "Meaning"], [
        ["Domain-specific language in R", "Uses R's metaprogramming to build a small custom syntax for a specific task"],
    ]), "formulae": ["library(rlang)\nquo(x + y)"]},
    "r-m1-l91": {"data_table": table(["Term", "Meaning"], [
        ["Retry logic", "Automatically re-attempts a failed operation with backoff before giving up"],
    ]), "formulae": ["library(purrr)\ninsistently(fetch_data)()"]},
    "r-m1-l92": {"data_table": table(["Term", "Meaning"], [
        ["Sparse matrix", "Stores only non-zero values to efficiently represent large, mostly-empty matrices"],
    ]), "formulae": ["library(Matrix)\nsparseMatrix(i = 1, j = 1, x = 1)"]},
    "r-m1-l93": {"data_table": table(["Term", "Meaning"], [
        ["Reproducible seeds", "Fixes a random number generator's state so results are exactly repeatable"],
    ]), "formulae": ["set.seed(123)\nrnorm(5)"]},
    "r-m1-l94": {"data_table": table(["Method", "Purpose"], [
        ["SHAP / LIME (R)", "Explain individual predictions from a machine learning model in R"],
    ]), "formulae": ["library(DALEX)\nexplain(model, data = df)"]},
    "r-m1-l95": {"data_table": table(["Term", "Meaning"], [
        ["Loss reserving model", "Estimates future insurance claim payments from historical claims data"],
    ]), "formulae": ["library(ChainLadder)\nMackChainLadder(triangle)"]},
    "r-m1-l96": {"data_table": table(["Package", "Purpose"], [
        ["terra", "Processes and analyzes raster (grid-based) remote sensing data"],
    ]), "formulae": ["library(terra)\nr <- rast('image.tif')"]},
    "r-m1-l97": {"data_table": table(["Term", "Meaning"], [
        ["Survey weight calibration", "Adjusts sample weights so survey estimates match known population totals"],
    ]), "formulae": ["library(survey)\ncalibrate(design, formula, population)"]},
    "r-m1-l98": {"data_table": table(["Package", "Purpose"], [
        ["lavaan", "Fits structural equation models relating latent and observed variables"],
    ]), "formulae": ["library(lavaan)\nsem('y ~ x', data = df)"]},
    "r-m1-l99": {"data_table": table(["Package", "Purpose"], [
        ["mapdeck", "Builds GPU-accelerated interactive maps in R using deck.gl"],
    ]), "formulae": ["library(mapdeck)\nmapdeck() %>% add_scatterplot(data = df)"]},
    "r-m1-l100": {"data_table": table(["Package", "Purpose"], [
        ["dismo", "Fits species distribution models predicting where a species can live"],
    ]), "formulae": ["library(dismo)\nmaxent(env_vars, occurrences)"]},
}

for worked_n in range(101, 121):
    base_n = worked_n - 100
    base_key = f"r-m1-l{base_n}"
    worked_key = f"r-m1-l{worked_n}"
    if base_n == 3:
        CHARTS[worked_key] = {"data_table": dict(_L3_SOURCE)}
    elif base_key in CHARTS:
        fields = {"data_table": dict(CHARTS[base_key]["data_table"])}
        if "formulae" in CHARTS[base_key]:
            fields["formulae"] = list(CHARTS[base_key]["formulae"])
        CHARTS[worked_key] = fields


def main() -> None:
    data = json.loads(SYLLABUS_PATH.read_text(encoding="utf-8"))
    lessons = data["subjects"]["R"]["lessons"]
    by_id = {l["id"]: l for l in lessons}

    missing = [lid for lid in CHARTS if lid not in by_id]
    if missing:
        raise SystemExit(f"Lesson ids not found in level_m1.json R: {missing}")

    updated = 0
    for lid, fields in CHARTS.items():
        lesson = by_id[lid]
        for key, value in fields.items():
            if key not in lesson:
                lesson[key] = value
                updated += 1

    SYLLABUS_PATH.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")
    print(f"Added {updated} fields across {len(CHARTS)} M1 R lessons (completing 120/120).")


if __name__ == "__main__":
    main()
