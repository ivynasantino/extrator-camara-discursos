library(readr)
library(tidyverse)
library(magrittr)

file_name <- "previdencia_09-07-20h.csv"
previdencia <- read_csv(paste0("data/build-data/", file_name))

process_previdencia <- previdencia %>% 
  mutate(partido_autor = ifelse(partido == "B", "PcdoB", partido)) %>% 
  select(id_sessao,
         data,
         autor,
         partido = partido_autor,
         uf,
         discurso)

write_csv(process_previdencia, paste0("data/process-data/", file_name))
