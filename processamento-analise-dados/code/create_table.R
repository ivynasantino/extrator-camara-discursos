library(readr)
library(magrittr)
library(tidyverse)

export_path <- "previdencia_10-07-16h"
name_txt <- "previdencia_10-7-16h"

previdencia <- read.csv("../raspagem-tratamento-dados/data/previdencia_10-7-16h.txt", sep = ";")

previdencia <- previdencia %>% 
  mutate(data = "10/07/2019",
         id_sessao = 191)

write_csv(previdencia, paste0("data/", export_path, ".csv"))
