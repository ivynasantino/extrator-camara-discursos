library(readr)
library(magrittr)
library(tidyverse)

file_name <- "previdencia_07-08-17h"

previdencia <- read.csv(paste0("../raspagem-tratamento-dados/data/process-texts/", file_name, "-PT.txt"), sep = "|")

previdencia <- previdencia %>%
  mutate(data = "07/08/2019",
         id_sessao = 210)

write_csv(previdencia, paste0("data/", file_name, ".csv"))
