library(readr)
library(magrittr)
library(tidyverse)

file_name <- "ccjc_reuniao-16-04-2019_10h"
previdencia <- read.csv(paste0("../raspagem-tratamento-dados/data/process-texts/", file_name, "-PT.txt"), sep = "|")

previdencia <- previdencia %>%
  mutate(data = "10/04/2019")

write_csv(previdencia, paste0("data/build-data/", file_name, ".csv"))
