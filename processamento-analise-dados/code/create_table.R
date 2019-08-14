library(readr)
library(magrittr)
library(tidyverse)

export_path <- "previdencia_06-08-21h"
name_txt <- "previdencia_06-08-21h"

previdencia <- read.csv(paste0("../raspagem-tratamento-dados/data/", name_txt, ".txt"), sep = "|")

previdencia <- previdencia %>% 
  mutate(data = "06/08/2019",
         id_sessao = 207)

write_csv(previdencia, paste0("data/", export_path, ".csv"))
