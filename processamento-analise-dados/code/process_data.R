library(readr)
library(tidyverse)
library(magrittr)

file_name <- "ccjc_reuniao-16-04-2019_10h.csv"
previdencia <- read_csv(paste0("data/build-data/", file_name))

process_previdencia <- previdencia %>% 
  mutate(partido_autor = ifelse(partido == "B", "PcdoB", partido)) %>% 
  select(data,
         autor,
         partido = partido_autor,
         uf,
         discurso)

write_csv(process_previdencia, paste0("data/process-data/", file_name))
